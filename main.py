import sys
import requests  # 添加 HTTP 请求库
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QPoint, QTimer,QFile,QTextStream
from remote_control import Ui_Form
from joystick import JoystickWidget

SEND_TO_SERVER = False
class RemoteControlWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # 设置UI
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.MAX_TRANSLATE_SPEED = 1.5
        self.MAX_ROTATE_SPEED = 0.769
        # 设置窗口标题
        self.setWindowTitle("XXX机器人遥控系统")
        
        # 滑块列表
        self.sliders = [
            self.ui.s0, self.ui.s1, self.ui.s2,
            self.ui.s3, self.ui.s4, self.ui.s5, self.ui.s6
        ]

        # 数字输入框列表
        self.spin_boxes = [
            self.ui.sb_0, self.ui.sb1, self.ui.sb2,
            self.ui.sb3, self.ui.sb4, self.ui.sb5, self.ui.sb6
        ]
        
        # HTTP 服务器配置
        self.api_base_url = "http://127.0.0.1:5000/api"  # 服务器地址
        
        # 初始化摇杆控件
        self.init_joysticks()
        
        # 连接滑块和数字输入框的信号
        self.connect_servo_controls()
        
        # 设置初始值
        self.set_initial_values()
        
        # 初始化摇杆状态
        self.translate_x = 0
        self.translate_y = 0
        self.rotate_x = 0
        self.rotate_z = 0
        
        # 创建定时器，定期发送控制信号
        self.send_timer = QTimer(self)
        self.send_timer.timeout.connect(self.send_control_data)
        self.send_timer.start(100)  # 每100毫秒发送一次 (10Hz)
        self.robot_speed_changed = False
        
    def init_joysticks(self):
        """初始化并添加摇杆控件"""
        # 创建平移摇杆
        self.translate_joystick = JoystickWidget(self.ui.translate_joy)
        # 设置摇杆位置和大小 - 直接使用父容器的大小
        self.translate_joystick.setGeometry(0, 0, 
                                           self.ui.translate_joy.width(), 
                                           self.ui.translate_joy.height())
        self.translate_joystick.setWindowTitle("平移控制")
        self.translate_joystick.set_keyboard_control_enabled(True)
        # 创建旋转摇杆
        self.rotate_joystick = JoystickWidget(self.ui.rotate_joy)
        # 设置摇杆位置和大小 - 直接使用父容器的大小
        self.rotate_joystick.setGeometry(0, 0, 
                                        self.ui.rotate_joy.width(), 
                                        self.ui.rotate_joy.height())
        self.rotate_joystick.setWindowTitle("旋转控制")
        
        # 连接摇杆位置变化信号
        self.translate_joystick.positionChanged.connect(self.on_translate_joystick_moved)
        self.rotate_joystick.positionChanged.connect(self.on_rotate_joystick_moved)
        # 最大速度改变信号
        self.ui.max_trans_speed_sb.valueChanged.connect(self.on_trans_speed_changed)
        self.ui.max_rota_speed_sb.valueChanged.connect(self.on_rota_speed_changed)
    
    def connect_servo_controls(self):
        """连接舵机控制滑块和数字输入框"""
        # 连接滑块和数字输入框
        for i, (slider, spin_box) in enumerate(zip(self.sliders, self.spin_boxes)):
            slider.setRange(0, 270)
            spin_box.setRange(0.0, 270.0)
            spin_box.setDecimals(1)
            
            # 滑块 -> 数字框
            slider.valueChanged.connect(lambda value, sb=spin_box: sb.setValue(value))
            
            # 数字框 -> 滑块
            spin_box.valueChanged.connect(lambda value, s=slider: s.setValue(int(value)))
            
            # 滑块值变化时更新舵机角度
            slider.valueChanged.connect(
                lambda value, idx=i: self.on_servo_angle_changed(idx, value)
            )
        self.sliders[6].setRange(0,180)
        self.spin_boxes[6].setRange(0,180)
    
    def on_trans_speed_changed(self, value):
        """平移速度改变事件处理"""
        self.MAX_TRANSLATE_SPEED = value

    def on_rota_speed_changed(self, value):
        """旋转速度改变事件处理"""
        self.MAX_ROTATE_SPEED = value
    
    def set_initial_values(self):
        """设置初始值"""
        # 设置摇杆初始位置 - 使用父容器的中心点
        self.translate_joystick.small_circle_xy = QPoint(
            self.ui.translate_joy.width() // 2,
            self.ui.translate_joy.height() // 2
        )
        self.translate_joystick.big_circle_xy = QPoint(
            self.ui.translate_joy.width() // 2,
            self.ui.translate_joy.height() // 2
        )
        
        self.rotate_joystick.small_circle_xy = QPoint(
            self.ui.rotate_joy.width() // 2,
            self.ui.rotate_joy.height() // 2
        )
        self.rotate_joystick.big_circle_xy = QPoint(
            self.ui.rotate_joy.width() // 2,
            self.ui.rotate_joy.height() // 2
        )
        
        # 设置舵机初始角度
        initial_angles = [135, 135, 135, 135, 135, 135, 90]
        for i, angle in enumerate(initial_angles):
            # 使用列表索引访问滑块
            self.sliders[i].setValue(angle)
            self.spin_boxes[i].setValue(float(angle))
        #设置最大速度
        self.ui.max_trans_speed_sb.setRange(0,1.5)
        self.ui.max_trans_speed_sb.setSingleStep(0.1)
        self.ui.max_trans_speed_sb.setDecimals(3)#2位小数
        self.ui.max_trans_speed_sb.setValue(self.MAX_TRANSLATE_SPEED)
        self.ui.max_rota_speed_sb.setSingleStep(0.1)
        self.ui.max_rota_speed_sb.setRange(0,0.769)
        self.ui.max_rota_speed_sb.setDecimals(3)#2位小数

        self.ui.max_rota_speed_sb.setValue(self.MAX_ROTATE_SPEED)

    def on_translate_joystick_moved(self, x, y):
        """平移摇杆移动事件处理"""
        self.translate_x = round(x / 90 * self.MAX_TRANSLATE_SPEED,3)
        self.translate_y = round(y / 90 * self.MAX_TRANSLATE_SPEED,3)
        #-max_translate_speed ~ max_translate_speed  -90~90
        #scrall_factor = /90 * max_translate_speed
        print(f"平移摇杆：x={self.translate_x:.3f},y={self.translate_y:.3f}")
        # 更新状态显示
        self.ui.tranlate_c_lb.setText(f"平移控制: X={self.translate_x:.2f}, Y={self.translate_y:.2f}")
    
    def on_rotate_joystick_moved(self, x, y):
        """旋转摇杆移动事件处理"""
        # 应用速度缩放并限制小数点范围
        self.rotate_x = round(x / 90 * self.MAX_ROTATE_SPEED, 3)  # 保留3位小数
        self.rotate_z = round(y / 90 * self.MAX_ROTATE_SPEED, 3)  # 保留3位小数
        
        # 限制在合理范围内
        self.rotate_x = max(min(self.rotate_x, self.MAX_ROTATE_SPEED), -self.MAX_ROTATE_SPEED)
        self.rotate_z = max(min(self.rotate_z, self.MAX_ROTATE_SPEED), -self.MAX_ROTATE_SPEED)
        print(f"旋转摇杆：x={self.rotate_x:.3f},y={self.rotate_z:.3f}")
        # 更新状态显示，格式化输出
        self.ui.rotate_c_lb.setText(f"旋转控制:Z={self.rotate_z:.3f} rad/s")
    
    def on_servo_angle_changed(self, servo_id, angle):
        """舵机角度变化事件处理"""
        # 这里可以添加舵机控制逻辑
        print(f"舵机 {servo_id} 角度设置为: {angle}°")
        
        # 更新状态显示 - 使用主窗口的状态栏
        self.statusBar().showMessage(f"舵机 {servo_id} 角度设置为: {angle}°")
        
        # 发送舵机更新
        if SEND_TO_SERVER:
            self.send_servo_update(servo_id, angle)
    
    def send_control_data(self):
        """定期发送控制数据到服务器"""
        # 检查是否有数据变化
        if SEND_TO_SERVER:
            if self.translate_x != 0 or self.translate_y != 0 or self.rotate_x != 0 or self.rotate_z != 0:
                self.robot_speed_changed = True
                # 准备数据
                data = {
                    "translate": {
                        "x": self.translate_x,
                        "y": self.translate_y
                    },
                    "rotate": {
                        # 旋转只管z轴，正为左转，负为右转
                        "z": self.rotate_z
                    }
                }
                
                try:
                    # 发送HTTP请求
                    response = requests.post(
                        f"{self.api_base_url}/control",
                        json=data,
                        timeout=0.5  # 超时时间0.5秒
                    )
                    
                    # 检查响应
                    if response.status_code == 200:
                        self.statusBar().showMessage("控制信号发送成功")
                    else:
                        self.statusBar().showMessage(f"控制信号发送失败: {response.status_code}")
                except Exception as e:
                    self.statusBar().showMessage(f"发送错误: {str(e)}")
            else:
                if self.robot_speed_changed:
                    # 准备数据
                    data = {
                        "translate": {
                            "x": 0,
                            "y": 0
                        },
                        "rotate": {
                            # 旋转只管z轴，正为左转，负为右转
                            "z": 0
                        }
                    }
                    
                    try:
                        # 发送HTTP请求
                        response = requests.post(
                            f"{self.api_base_url}/control",
                            json=data,
                            timeout=0.5  # 超时时间0.5秒
                        )
                        
                        # 检查响应
                        if response.status_code == 200:
                            self.statusBar().showMessage("零速控制信号发送成功")
                        else:
                            self.statusBar().showMessage(f"零速控制信号发送失败: {response.status_code}")
                    except Exception as e:
                        self.statusBar().showMessage(f"发送错误: {str(e)}")
                    self.robot_speed_changed = False
                
    def send_servo_update(self, servo_id, angle):
        """发送舵机更新到服务器"""
        data = {
            "servo_id": servo_id,
            "angle": angle
        }
        
        try:
            # 发送HTTP请求
            response = requests.post(
                f"{self.api_base_url}/servo",
                json=data,
                timeout=0.5  # 超时时间0.5秒
            )
            
            # 检查响应
            if response.status_code == 200:
                print(f"舵机 {servo_id} 更新发送成功")
            else:
                print(f"舵机 {servo_id} 更新发送失败: {response.status_code}")
        except Exception as e:
            print(f"舵机更新发送错误: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # # 加载QSS样式表
    # style_file = QFile("stylesheet.qss")
    # if style_file.open(QFile.ReadOnly | QFile.Text):
    #     stream = QTextStream(style_file)
    #     app.setStyleSheet(stream.readAll())
    #     style_file.close()
    #     print("QSS样式表加载成功")
    # else:
    #     print("无法加载QSS样式表")
    # 创建主窗口
    window = RemoteControlWindow()
    window.show()
    
    sys.exit(app.exec())
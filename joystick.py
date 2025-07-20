import sys
import math
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import Qt, QPoint, Signal
from PySide6.QtGui import QPainter, QPixmap, QMouseEvent, QPaintEvent, QKeyEvent

# 常量定义
SMALL_CIRCLE_RADIUS = 30  # 小圆半径
BIG_CIRCLE_RADIUS = 90    # 大圆半径
KEY_CONTROL_RADIUS = 60    #键盘控制大小
class JoystickWidget(QWidget):
    positionChanged = Signal(int, int)  # 位置变化信号
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()
        
    def init_ui(self):
        # 设置焦点策略，使窗口可以接收键盘事件
        self.setFocusPolicy(Qt.StrongFocus)
        
        # 设置大圆圆心位置
        self.small_circle_xy = QPoint(self.width() // 2, self.height() // 2)
        # 设置小圆圆心位置，与大圆相同
        self.big_circle_xy = QPoint(self.small_circle_xy.x(), self.small_circle_xy.y())
        
        # 鼠标点击标志初始化
        self.mouse_press_flag = False
        self.map_remov_old = QPoint(0, 0)
        
        # 键盘控制相关
        self.keyboard_control_enabled = False
        self.key_pressed = {
            Qt.Key_I: False,  # 上
            Qt.Key_K: False,  # 下
            Qt.Key_J: False,  # 左
            Qt.Key_L: False   # 右
        }
        
        # 加载图片资源
        self.big_circle_pixmap = QPixmap("./image/max.png")
        self.small_circle_pixmap = QPixmap("./image/min.png")
        
        # 检查图片是否加载成功
        if self.big_circle_pixmap.isNull():
            print("警告: 大圆图片加载失败")
        if self.small_circle_pixmap.isNull():
            print("警告: 小圆图片加载失败")
    
    def set_keyboard_control_enabled(self, enabled: bool):
        """设置键盘控制是否启用"""
        self.keyboard_control_enabled = enabled
        if not enabled:
            # 禁用时重置所有按键状态
            for key in self.key_pressed:
                self.key_pressed[key] = False
            self._reset_joystick_position()
    
    def resizeEvent(self, event):
        """窗口大小变化时重新计算中心点"""
        self.small_circle_xy = QPoint(self.width() // 2, self.height() // 2)
        self.big_circle_xy = QPoint(self.small_circle_xy.x(), self.small_circle_xy.y())
        self.update()
        
    def paintEvent(self, event: QPaintEvent):
        painter = QPainter(self)
        # 开启抗锯齿
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.setRenderHint(QPainter.SmoothPixmapTransform, True)
        
        # 绘制摇杆中的大圆
        if not self.big_circle_pixmap.isNull():
            painter.drawPixmap(
                self.small_circle_xy.x() - BIG_CIRCLE_RADIUS,
                self.small_circle_xy.y() - BIG_CIRCLE_RADIUS,
                BIG_CIRCLE_RADIUS * 2,
                BIG_CIRCLE_RADIUS * 2,
                self.big_circle_pixmap
            )
        
        # 绘制摇杆中的小圆
        if not self.small_circle_pixmap.isNull():
            painter.drawPixmap(
                self.big_circle_xy.x() - SMALL_CIRCLE_RADIUS,
                self.big_circle_xy.y() - SMALL_CIRCLE_RADIUS,
                SMALL_CIRCLE_RADIUS * 2,
                SMALL_CIRCLE_RADIUS * 2,
                self.small_circle_pixmap
            )
    
    def mouseMoveEvent(self, event: QMouseEvent):
        rocker_xy = event.position().toPoint()
        
        if self.mouse_press_flag:
            # 计算鼠标位置与大圆中心的距离平方
            dx = rocker_xy.x() - self.small_circle_xy.x()
            dy = rocker_xy.y() - self.small_circle_xy.y()
            distance_squared = dx * dx + dy * dy
            
            max_radius = BIG_CIRCLE_RADIUS
            if distance_squared > max_radius * max_radius:
                # 计算角度
                angle = math.atan2(abs(dy), abs(dx))
                
                # 计算边界点坐标
                x = int(max_radius * math.cos(angle))
                y = int(max_radius * math.sin(angle))
                
                # 根据象限调整坐标
                if dx >= 0 and dy >= 0:  # 第一象限 (右下)
                    self.big_circle_xy.setX(x + self.small_circle_xy.x())
                    self.big_circle_xy.setY(y + self.small_circle_xy.y())
                    # 转换为右手坐标系: 向后(X负), 向右(Y负)
                    joy_x = -y
                    joy_y = -x
                elif dx < 0 and dy >= 0:  # 第二象限 (左下)
                    self.big_circle_xy.setX(-x + self.small_circle_xy.x())
                    self.big_circle_xy.setY(y + self.small_circle_xy.y())
                    # 转换为右手坐标系: 向后(X负), 向左(Y正)
                    joy_x = -y
                    joy_y = x
                elif dx < 0 and dy < 0:  # 第三象限 (左上)
                    self.big_circle_xy.setX(-x + self.small_circle_xy.x())
                    self.big_circle_xy.setY(-y + self.small_circle_xy.y())
                    # 转换为右手坐标系: 向前(X正), 向左(Y正)
                    joy_x = y
                    joy_y = x
                elif dx >= 0 and dy < 0:  # 第四象限 (右上)
                    self.big_circle_xy.setX(x + self.small_circle_xy.x())
                    self.big_circle_xy.setY(-y + self.small_circle_xy.y())
                    # 转换为右手坐标系: 向前(X正), 向右(Y负)
                    joy_x = y
                    joy_y = -x
            else:
                # 鼠标在大圆内部，直接跟随鼠标
                self.big_circle_xy = rocker_xy
                # 转换为右手坐标系: 
                # 前-后: 向上为X正 (dy为负时X正), 向下为X负 (dy为正时X负)
                # 左-右: 向左为Y正 (dx为负时Y正), 向右为Y负 (dx为正时Y负)
                joy_x = -dy
                joy_y = -dx
            
            # 发出位置变化信号 (右手坐标系)
            self.positionChanged.emit(joy_x, joy_y)
            
            # 请求重绘
            self.update()
            
            # 保存当前鼠标位置
            self.map_remov_old = rocker_xy
    
    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            rocker_xy = event.position().toPoint()
            
            # 计算与大圆中心的距离平方
            dx = rocker_xy.x() - self.small_circle_xy.x()
            dy = rocker_xy.y() - self.small_circle_xy.y()
            distance_squared = dx * dx + dy * dy
            
            max_radius = BIG_CIRCLE_RADIUS
            # 检查是否在大圆内
            if distance_squared <= max_radius * max_radius:
                self.mouse_press_flag = True
                # 立即更新位置
                self.mouseMoveEvent(event)
            else:
                self.map_remov_old = rocker_xy
    
    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton and self.mouse_press_flag:
            # 重置状态
            self.mouse_press_flag = False
            
            # 小圆回归中心位置
            self.big_circle_xy = QPoint(self.small_circle_xy.x(), self.small_circle_xy.y())
            
            # 发出归零信号 (右手坐标系)
            self.positionChanged.emit(0, 0)
            
            # 请求重绘
            self.update()
            
    def keyPressEvent(self, event: QKeyEvent):
        """键盘按下事件处理"""
        if not self.keyboard_control_enabled:
            return
            
        key = event.key()
        if key in self.key_pressed:
            self.key_pressed[key] = True
            self._update_joystick_from_keys()
            
    def keyReleaseEvent(self, event: QKeyEvent):
        """键盘释放事件处理"""
        if not self.keyboard_control_enabled:
            return
            
        key = event.key()
        if key in self.key_pressed:
            self.key_pressed[key] = False
            self._update_joystick_from_keys()
            
    def _update_joystick_from_keys(self):
        """根据当前按下的键盘按键更新摇杆位置"""
        # 计算X和Y方向的分量
        x = 0
        y = 0
        
        # 上/下方向 (X轴)
        if self.key_pressed[Qt.Key_I]:  # I键 - 上
            x += KEY_CONTROL_RADIUS
        if self.key_pressed[Qt.Key_K]:  # K键 - 下
            x -= KEY_CONTROL_RADIUS
            
        # 左/右方向 (Y轴)
        if self.key_pressed[Qt.Key_J]:  # J键 - 左
            y += KEY_CONTROL_RADIUS
        if self.key_pressed[Qt.Key_L]:  # L键 - 右
            y -= KEY_CONTROL_RADIUS
            
        # 如果没有按键按下，则重置位置
        if x == 0 and y == 0:
            self._reset_joystick_position()
            return
            
        # 计算方向向量 (对角线长度为半径的√2/2倍，即45度方向)
        vec = int(KEY_CONTROL_RADIUS * 0.7071)  # cos(45°) ≈ sin(45°) ≈ 0.7071
        
        # 根据按键组合确定最终位置
        if x > 0:  # 向上
            if y > 0:  # 左上
                self.big_circle_xy = QPoint(
                    self.small_circle_xy.x() - vec,
                    self.small_circle_xy.y() - vec
                )
                # 发射信号: 前(X正), 左(Y正)
                self.positionChanged.emit(vec, vec)
            elif y < 0:  # 右上
                self.big_circle_xy = QPoint(
                    self.small_circle_xy.x() + vec,
                    self.small_circle_xy.y() - vec
                )
                # 发射信号: 前(X正), 右(Y负)
                self.positionChanged.emit(vec, -vec)
            else:  # 纯上
                self.big_circle_xy = QPoint(
                    self.small_circle_xy.x(),
                    self.small_circle_xy.y() - KEY_CONTROL_RADIUS
                )
                # 发射信号: 前(X正), 无左右
                self.positionChanged.emit(KEY_CONTROL_RADIUS, 0)
                
        elif x < 0:  # 向下
            if y > 0:  # 左下
                self.big_circle_xy = QPoint(
                    self.small_circle_xy.x() - vec,
                    self.small_circle_xy.y() + vec
                )
                # 发射信号: 后(X负), 左(Y正)
                self.positionChanged.emit(-vec, vec)
            elif y < 0:  # 右下
                self.big_circle_xy = QPoint(
                    self.small_circle_xy.x() + vec,
                    self.small_circle_xy.y() + vec
                )
                # 发射信号: 后(X负), 右(Y负)
                self.positionChanged.emit(-vec, -vec)
            else:  # 纯下
                self.big_circle_xy = QPoint(
                    self.small_circle_xy.x(),
                    self.small_circle_xy.y() + KEY_CONTROL_RADIUS
                )
                # 发射信号: 后(X负), 无左右
                self.positionChanged.emit(-KEY_CONTROL_RADIUS, 0)
                
        else:  # 无上下，只有左右
            if y > 0:  # 纯左
                self.big_circle_xy = QPoint(
                    self.small_circle_xy.x() - KEY_CONTROL_RADIUS,
                    self.small_circle_xy.y()
                )
                # 发射信号: 无前后, 左(Y正)
                self.positionChanged.emit(0, KEY_CONTROL_RADIUS)
            elif y < 0:  # 纯右
                self.big_circle_xy = QPoint(
                    self.small_circle_xy.x() + KEY_CONTROL_RADIUS,
                    self.small_circle_xy.y()
                )
                # 发射信号: 无前后, 右(Y负)
                self.positionChanged.emit(0, -KEY_CONTROL_RADIUS)
            
        # 请求重绘
        self.update()
        
    def _reset_joystick_position(self):
        """重置摇杆位置到中心"""
        self.big_circle_xy = QPoint(self.small_circle_xy.x(), self.small_circle_xy.y())
        self.positionChanged.emit(0, 0)
        self.update()
from flask import Flask, request, jsonify
import time

app = Flask(__name__)


@app.route('/api/control', methods=['POST'])
def handle_control():
    data = request.json

    # 获取控制数据
    translate = data.get('translate', {})
    rotate = data.get('rotate', {})
    
    # 在这里处理控制数据（示例：打印到控制台）
    print(f"平移控制: X={translate.get('x', 0)}, Y={translate.get('y', 0)}")
    print(f"旋转控制: X={rotate.get('x', 0)}, Y={rotate.get('y', 0)}")
    
    # 可以在这里将控制数据转发给机器人或其他人
    
    return jsonify({"status": "success"})

@app.route('/api/servo', methods=['POST'])
def handle_servo():
    data = request.json
    # 获取舵机数据
    servo_id = data.get('servo_id')
    angle = data.get('angle')
    
    # 在这里处理舵机数据（示例：打印到控制台）
    print(f"舵机 {servo_id} 角度更新: {angle}°")
    
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
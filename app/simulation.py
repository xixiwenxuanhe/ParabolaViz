import numpy as np
import math

def calculate_projectile(initial_velocity, initial_height=10.0, gravity=9.8, masses=None):
    """
    计算平抛运动的轨迹
    
    参数:
    - initial_velocity: 初始速度 (m/s)
    - initial_height: 初始高度 (m)，默认为10米
    - gravity: 重力加速度 (m/s^2)
    - masses: 质量类别列表 ['small', 'medium', 'large']
    
    返回:
    - 包含不同质量物体轨迹的字典
    """
    if masses is None:
        masses = ['small', 'medium', 'large']
    
    # 定义不同质量物体的空气阻力系数
    drag_coefficients = {
        'small': 0.05,
        'medium': 0.03,
        'large': 0.01
    }
    
    # 时间步长
    dt = 0.1
    
    results = {}
    
    for mass in masses:
        drag = drag_coefficients[mass]
        
        # 初始条件
        x, y = 0.0, initial_height
        vx, vy = initial_velocity, 0.0
        
        trajectory = {'x': [x], 'y': [y], 'time': [0]}
        t = 0
        
        # 模拟直到物体落地
        while y > 0:
            # 更新位置和速度
            x += vx * dt
            y += vy * dt
            
            # 应用重力和空气阻力
            vx = vx * (1 - drag * dt)
            vy = vy - gravity * dt
            
            t += dt
            
            # 记录轨迹
            trajectory['x'].append(x)
            trajectory['y'].append(y)
            trajectory['time'].append(t)
        
        results[mass] = trajectory
    
    return results

def calculate_oblique(initial_velocity, angle, gravity=9.8, masses=None):
    """
    计算斜抛运动的轨迹
    
    参数:
    - initial_velocity: 初始速度 (m/s)
    - angle: 发射角度 (度)
    - gravity: 重力加速度 (m/s^2)
    - masses: 质量类别列表 ['small', 'medium', 'large']
    
    返回:
    - 包含不同质量物体轨迹的字典
    """
    if masses is None:
        masses = ['small', 'medium', 'large']
    
    # 定义不同质量物体的空气阻力系数
    drag_coefficients = {
        'small': 0.05,
        'medium': 0.03,
        'large': 0.01
    }
    
    # 初始高度（假设从地面开始）
    initial_height = 0.0
    
    # 角度转换为弧度
    angle_rad = math.radians(angle)
    
    # 初始速度分量
    vx0 = initial_velocity * math.cos(angle_rad)
    vy0 = initial_velocity * math.sin(angle_rad)
    
    # 时间步长
    dt = 0.1
    
    results = {}
    
    for mass in masses:
        drag = drag_coefficients[mass]
        
        # 初始条件
        x, y = 0.0, initial_height
        vx, vy = vx0, vy0
        
        trajectory = {'x': [x], 'y': [y], 'time': [0]}
        t = 0
        
        # 模拟直到物体落地（当y变回0）
        while True:
            # 更新位置和速度
            x += vx * dt
            y += vy * dt
            
            # 应用重力和空气阻力
            vx = vx * (1 - drag * dt)
            vy = vy - gravity * dt
            
            t += dt
            
            # 记录轨迹
            trajectory['x'].append(x)
            trajectory['y'].append(y)
            trajectory['time'].append(t)
            
            # 如果物体落地且向下运动，则停止
            if y <= 0 and vy < 0:
                # 修正最后一点为y=0
                trajectory['x'][-1] = x - vx * (y / vy)
                trajectory['y'][-1] = 0
                break
        
        results[mass] = trajectory
    
    return results 
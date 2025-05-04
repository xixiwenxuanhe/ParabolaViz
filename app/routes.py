from flask import render_template, request, jsonify
from app import app
from app.simulation import calculate_projectile, calculate_oblique

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projectile')
def projectile():
    return render_template('projectile.html')

@app.route('/oblique')
def oblique():
    return render_template('oblique.html')

@app.route('/api/projectile', methods=['POST'])
def api_projectile():
    data = request.json
    initial_velocity = float(data.get('initial_velocity', 10))
    initial_height = float(data.get('initial_height', 10))  # 获取初始高度，默认为10米
    
    # 计算地球重力下的结果
    earth_results = calculate_projectile(initial_velocity, initial_height=initial_height, gravity=9.8, 
                                       masses=['small', 'medium', 'large'])
    
    # 计算月球重力下的结果
    moon_results = calculate_projectile(initial_velocity, initial_height=initial_height, gravity=1.62, 
                                      masses=['small', 'medium', 'large'])
    
    return jsonify({
        'earth': earth_results,
        'moon': moon_results
    })

@app.route('/api/oblique', methods=['POST'])
def api_oblique():
    data = request.json
    initial_velocity = float(data.get('initial_velocity', 10))
    angle = float(data.get('angle', 45))
    
    # 计算地球重力下的结果
    earth_results = calculate_oblique(initial_velocity, angle, gravity=9.8, 
                                     masses=['small', 'medium', 'large'])
    
    # 计算月球重力下的结果
    moon_results = calculate_oblique(initial_velocity, angle, gravity=1.62, 
                                    masses=['small', 'medium', 'large'])
    
    return jsonify({
        'earth': earth_results,
        'moon': moon_results
    }) 
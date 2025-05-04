# 🚀 物理运动仿真项目

该项目是一个基于Flask的Web应用，用于模拟平抛运动和斜抛运动的物理过程。它允许用户调整各种参数，如初始速度和发射角度，然后观察不同质量的物体在地球和月球重力环境下的运动轨迹。

🌐 **在线演示**：[https://parabolaviz.onrender.com/](https://parabolaviz.onrender.com/)

## ✨ 功能特点

- **🎯 平抛运动模拟**：模拟物体从高处以水平初速度抛出的运动
- **↗️ 斜抛运动模拟**：模拟物体以特定角度和初速度抛出的运动
- **🎚️ 参数调整**：用户可以调整初始速度和发射角度
- **🌍🌑 多环境对比**：同时展示地球重力和月球重力环境下的运动差异
- **⚖️ 质量影响**：呈现不同质量物体（考虑空气阻力）的运动轨迹差异
- **📊 实时图表展示**：使用Chart.js绘制直观的运动轨迹图表

## 🛠️ 技术栈

- **🐍 后端**：Flask (Python)
- **🖥️ 前端**：HTML, CSS, JavaScript
- **📈 可视化**：Chart.js
- **🎨 样式框架**：Bootstrap 5

## 🚀 如何运行

1. 确保安装了Python 3.6+
2. 安装依赖包：
   ```
   pip install -r requirements.txt
   ```
3. 运行应用：
   ```
   python run.py
   ```
4. 在浏览器中访问 `http://127.0.0.1:5000/`

## 📂 项目结构

```
physics_simulation/
│
├── app/
│   ├── __init__.py           # Flask应用初始化
│   ├── routes.py             # 路由定义
│   ├── simulation.py         # 物理仿真计算逻辑
│   ├── templates/            # HTML模板
│   │   ├── index.html        # 主页
│   │   ├── projectile.html   # 平抛运动页面
│   │   ├── oblique.html      # 斜抛运动页面
│   │   └── layout.html       # 布局模板
│   │
│   └── static/               # 静态文件
│       ├── css/
│       │   └── style.css     # 自定义样式
│       ├── js/
│       │   └── simulation.js # 仿真前端逻辑
│       └── images/           # 图像资源
│
├── requirements.txt          # 项目依赖
├── run.py                    # 启动脚本
└── README.md                 # 项目说明
```

## 📚 物理原理

- **➡️ 平抛运动**：物体在水平方向具有初速度，在竖直方向受重力作用做自由落体运动
- **↗️ 斜抛运动**：物体在水平和竖直方向都具有初速度分量，同时受重力作用
- **💨 空气阻力**：阻力与速度成正比，质量越小，受空气阻力影响越大
- **🌍🌑 重力环境**：地球重力加速度约为9.8 m/s²，月球重力加速度约为1.62 m/s²

## 🌐 部署

本项目已部署在Render平台上：
- 演示地址：[https://parabolaviz.onrender.com/](https://parabolaviz.onrender.com/)
- 通过Render的免费托管服务实现自动部署
- 任何推送到主分支的更改都会自动触发新的部署 
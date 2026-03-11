# BUPTravel
北京邮电大学旅行系统
# BUPTravel
![GitHub stars](https://img.shields.io/github/stars/BUPT-OpenSource/BUPTravel?style=flat-square)
![GitHub forks](https://img.shields.io/github/forks/BUPT-OpenSource/BUPTravel?style=flat-square)
![GitHub license](https://img.shields.io/github/license/BUPT-OpenSource/BUPTravel?style=flat-square)
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue?style=flat-square)

北京邮电大学出行服务工具，一站式解决校内师生出行规划、通勤查询、校园周边交通等核心需求。

## 项目描述
BUPTravel 是面向北京邮电大学全体师生的开源出行辅助工具，旨在整合校园周边公共交通、共享单车、校园班车、节假日出行攻略等信息，通过简洁的交互和自动化的信息聚合，解决师生出行前的信息碎片化、规划效率低等问题。项目支持自定义出行偏好、实时交通状态查询，并提供轻量化的离线数据支持，适配校园网络环境。

## 核心功能亮点
- 🚇 **通勤路线规划**：基于起点/终点自动生成最优公共交通/骑行/步行路线，适配北邮各校区
- 📱 **校内美食推荐**：推荐校内各个食堂出的美食，支持关键字查询
- 🎫 **出行攻略聚合**：整理节假日返校/离校、周边商圈/医院等场景化出行规划
- ⚡ **轻量化设计**：无冗余依赖，启动速度快，支持命令行/简易Web界面两种使用方式

## 安装步骤
### 前置条件
- Python 3.8+
- pip 20.0+

### 安装方式
1. 克隆仓库
```bash
git clone https://github.com/BUPT-OpenSource/BUPTravel.git
cd BUPTravel
```

2. 安装依赖
```bash
pip install -r requirements.txt
```

3. （可选）安装为系统命令
```bash
pip install .
```

## 快速入门
### 基础使用（命令行）
```python
# 导入核心模块
from buptravel import BusQuery, RoutePlanner

# 查询校园班车（西土城校区→沙河校区）
bus_query = BusQuery()
shuttle_info = bus_query.get_shuttle("西土城", "沙河")
print("班车信息：", shuttle_info)

# 规划通勤路线（沙河校区→五道口）
route_planner = RoutePlanner()
best_route = route_planner.get_best_route("沙河校区", "五道口", mode="public")
print("最优路线：", best_route)
```

### 启动简易Web界面
```bash
python run_web.py
# 访问 http://localhost:8080 即可使用可视化界面
```

## 贡献指南
我们欢迎所有形式的贡献，包括但不限于代码提交、Bug报告、功能建议、文档完善。

### 贡献步骤
1. Fork 本仓库到个人账号
2. 创建特性分支（`git checkout -b feature/your-feature`）
3. 提交代码修改（`git commit -m "feat: add your feature"`）
4. 推送到远程分支（`git push origin feature/your-feature`）
5. 提交 Pull Request 到主仓库 `main` 分支

### 代码规范
- 遵循 PEP 8 编码规范（Python）
- 提交信息遵循 [Conventional Commits](https://www.conventionalcommits.org/) 规范
- 新增功能需补充对应的单元测试

## 许可证信息
本项目采用 [MIT License](LICENSE) 开源许可证，允许自由使用、修改、分发，商业使用也无需额外授权。详情请查看 LICENSE 文件。
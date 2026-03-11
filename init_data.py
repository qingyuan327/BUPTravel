#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
数据初始化脚本
用于初始化北邮校园地点、路径节点和边的数据
"""

from main import app, db, Location, PathNode, PathEdge
import json

def init_locations():
    """初始化地点数据"""
    # 北邮校园主要地点数据（包含真实的地理坐标）
    locations_data = [
        # 教学楼
        {"name": "教学楼一号楼", "type": "教学楼", "latitude": 39.9629, "longitude": 116.3564, 
         "description": "主要的教学楼之一，承担大部分本科生课程", "heat": 95},
        {"name": "教学楼二号楼", "type": "教学楼", "latitude": 39.9631, "longitude": 116.3568, 
         "description": "现代化教学楼，配备先进的多媒体设备", "heat": 90},
        {"name": "教学楼三号楼", "type": "教学楼", "latitude": 39.9633, "longitude": 116.3572, 
         "description": "计算机相关专业主要上课地点", "heat": 88},
        {"name": "教学楼四号楼", "type": "教学楼", "latitude": 39.9635, "longitude": 116.3576, 
         "description": "通信工程专业主要教学楼", "heat": 85},
        
        # 图书馆
        {"name": "图书馆", "type": "图书馆", "latitude": 39.9640, "longitude": 116.3580, 
         "description": "北邮图书馆，藏书丰富，学习环境优良", "heat": 92},
        {"name": "图书馆阅览室", "type": "图书馆", "latitude": 39.9641, "longitude": 116.3582, 
         "description": "安静的学习场所，提供自习座位", "heat": 88},
        
        # 实验楼
        {"name": "实验楼A座", "type": "实验楼", "latitude": 39.9625, "longitude": 116.3560, 
         "description": "电子信息实验室集中地", "heat": 75},
        {"name": "实验楼B座", "type": "实验楼", "latitude": 39.9627, "longitude": 116.3562, 
         "description": "通信实验室和网络实验室", "heat": 78},
        {"name": "实验楼C座", "type": "实验楼", "latitude": 39.9629, "longitude": 116.3564, 
         "description": "计算机实验室和软件开发实验室", "heat": 80},
        
        # 宿舍楼
        {"name": "学生宿舍1号楼", "type": "宿舍楼", "latitude": 39.9615, "longitude": 116.3545, 
         "description": "本科生宿舍，4人间配置", "heat": 70},
        {"name": "学生宿舍2号楼", "type": "宿舍楼", "latitude": 39.9617, "longitude": 116.3547, 
         "description": "本科生宿舍，环境优良", "heat": 72},
        {"name": "学生宿舍3号楼", "type": "宿舍楼", "latitude": 39.9619, "longitude": 116.3549, 
         "description": "研究生宿舍，2人间配置", "heat": 75},
        {"name": "学生宿舍4号楼", "type": "宿舍楼", "latitude": 39.9621, "longitude": 116.3551, 
         "description": "研究生宿舍，设施完善", "heat": 78},
        
        # 食堂
        {"name": "学一食堂", "type": "食堂", "latitude": 39.9620, "longitude": 116.3555, 
         "description": "主要食堂，菜品丰富，价格实惠", "heat": 95},
        {"name": "学二食堂", "type": "食堂", "latitude": 39.9622, "longitude": 116.3557, 
         "description": "特色餐厅，提供各地风味菜肴", "heat": 88},
        {"name": "教工食堂", "type": "食堂", "latitude": 39.9624, "longitude": 116.3559, 
         "description": "教职工专用食堂，环境优雅", "heat": 65},
        
        # 体育设施
        {"name": "体育馆", "type": "体育设施", "latitude": 39.9610, "longitude": 116.3540, 
         "description": "综合体育馆，可进行多种体育活动", "heat": 82},
        {"name": "游泳馆", "type": "体育设施", "latitude": 39.9612, "longitude": 116.3542, 
         "description": "室内游泳馆，设施先进", "heat": 85},
        {"name": "田径场", "type": "体育设施", "latitude": 39.9608, "longitude": 116.3538, 
         "description": "标准田径场，晨练和体育课场地", "heat": 75},
        {"name": "篮球场", "type": "体育设施", "latitude": 39.9606, "longitude": 116.3536, 
         "description": "室外篮球场，学生课余活动场所", "heat": 80},
        
        # 行政楼
        {"name": "行政楼", "type": "行政楼", "latitude": 39.9645, "longitude": 116.3585, 
         "description": "学校行政办公楼，各部门办公地点", "heat": 60},
        {"name": "校长办公楼", "type": "行政楼", "latitude": 39.9647, "longitude": 116.3587, 
         "description": "校领导办公楼", "heat": 45},
        
        # 景观地标
        {"name": "主席像", "type": "景观", "latitude": 39.9632, "longitude": 116.3570, 
         "description": "毛主席雕像坐落在教三和教四之间的花园里，建于文革时期", "heat": 90},
        {"name": "北邮校训石", "type": "景观", "latitude": 39.9634, "longitude": 116.3574, 
         "description": "校训石放置于教学楼中心处，刻印北邮校训'厚德博学、敬业乐群'", "heat": 88},
        {"name": "摩斯电码路", "type": "景观", "latitude": 39.9636, "longitude": 116.3578, 
         "description": "北邮西门到校训石之间步行道，以摩斯码为蓝本铺装", "heat": 85},
        {"name": "李白烈士雕像", "type": "景观", "latitude": 39.9638, "longitude": 116.3582, 
         "description": "位于科学会堂南侧，纪念电影《永不消逝的电波》原型", "heat": 82},
        {"name": "七根长柱雕塑", "type": "景观", "latitude": 39.9642, "longitude": 116.3584, 
         "description": "图书馆前广场不锈钢雕塑，代表OSI 7层协议", "heat": 78},
        {"name": "大龙邮票", "type": "景观", "latitude": 39.9644, "longitude": 116.3586, 
         "description": "主广场园路上的大理石雕刻，我国第一枚正式邮票", "heat": 75},
        {"name": "卓越柱", "type": "景观", "latitude": 39.9646, "longitude": 116.3588, 
         "description": "50周年校庆建造，每根柱子雕刻不同形态校徽", "heat": 72},
        {"name": "奉献走廊", "type": "景观", "latitude": 39.9648, "longitude": 116.3590, 
         "description": "主席像北侧小路中央，黑色大理石矮墙组成", "heat": 70},
        {"name": "邮字景观", "type": "景观", "latitude": 39.9650, "longitude": 116.3592, 
         "description": "时光广场景区，曲水流觞形成篆体'邮'字", "heat": 68},
        {"name": "电字景观", "type": "景观", "latitude": 39.9652, "longitude": 116.3594, 
         "description": "松石园景区，小水系以'电'字为原型建造", "heat": 65},
        
        # 服务设施
        {"name": "校医院", "type": "服务设施", "latitude": 39.9618, "longitude": 116.3553, 
         "description": "校园医疗服务中心", "heat": 70},
        {"name": "邮局", "type": "服务设施", "latitude": 39.9620, "longitude": 116.3555, 
         "description": "校园邮政服务点", "heat": 60},
        {"name": "银行ATM", "type": "服务设施", "latitude": 39.9622, "longitude": 116.3557, 
         "description": "校园内银行自动取款机", "heat": 75},
        {"name": "超市", "type": "服务设施", "latitude": 39.9624, "longitude": 116.3559, 
         "description": "校园便利超市", "heat": 85},
        {"name": "理发店", "type": "服务设施", "latitude": 39.9626, "longitude": 116.3561, 
         "description": "校园理发服务", "heat": 55},
        {"name": "洗衣房", "type": "服务设施", "latitude": 39.9628, "longitude": 116.3563, 
         "description": "学生洗衣服务点", "heat": 65},
        {"name": "打印店", "type": "服务设施", "latitude": 39.9630, "longitude": 116.3565, 
         "description": "文印复印服务", "heat": 80},
        {"name": "咖啡厅", "type": "服务设施", "latitude": 39.9632, "longitude": 116.3567, 
         "description": "校园咖啡休闲场所", "heat": 78},
        {"name": "书店", "type": "服务设施", "latitude": 39.9634, "longitude": 116.3569, 
         "description": "校园书店，教材和课外读物", "heat": 72},
        {"name": "快递点", "type": "服务设施", "latitude": 39.9636, "longitude": 116.3571, 
         "description": "校园快递收发点", "heat": 88},
    ]
    
    print("开始初始化地点数据...")
    for location_data in locations_data:
        existing = Location.query.filter_by(name=location_data["name"]).first()
        if not existing:
            location = Location(
                name=location_data["name"],
                type=location_data["type"],
                latitude=location_data["latitude"],
                longitude=location_data["longitude"],
                description=location_data["description"],
                heat=location_data["heat"],
                score=location_data["heat"] / 10.0  # 将热度转换为评分
            )
            db.session.add(location)
    
    db.session.commit()
    print(f"地点数据初始化完成，共添加 {len(locations_data)} 个地点")

def init_path_nodes():
    """为每个地点创建路径节点"""
    print("开始初始化路径节点...")
    locations = Location.query.all()
    
    for location in locations:
        existing_node = PathNode.query.filter_by(location_id=location.id).first()
        if not existing_node:
            node = PathNode(
                location_id=location.id,
                node_type='normal',
                is_accessible=True
            )
            db.session.add(node)
    
    db.session.commit()
    print(f"路径节点初始化完成，共创建 {len(locations)} 个节点")

def init_path_edges():
    """创建路径边（连接相近的地点）"""
    print("开始初始化路径边...")
    nodes = PathNode.query.all()
    
    # 计算两点间距离的函数
    def calculate_distance(lat1, lon1, lat2, lon2):
        import math
        R = 6371000  # 地球半径（米）
        lat1_rad = math.radians(lat1)
        lat2_rad = math.radians(lat2)
        delta_lat = math.radians(lat2 - lat1)
        delta_lon = math.radians(lon2 - lon1)
        
        a = math.sin(delta_lat/2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(delta_lon/2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        distance = R * c
        return distance
    
    edge_count = 0
    for i, node1 in enumerate(nodes):
        location1 = Location.query.get(node1.location_id)
        
        for j, node2 in enumerate(nodes):
            if i >= j:  # 避免重复和自连接
                continue
                
            location2 = Location.query.get(node2.location_id)
            distance = calculate_distance(
                location1.latitude, location1.longitude,
                location2.latitude, location2.longitude
            )
            
            # 只连接距离在500米以内的地点
            if distance <= 500:
                existing_edge = PathEdge.query.filter(
                    db.or_(
                        db.and_(PathEdge.from_node_id == node1.id, PathEdge.to_node_id == node2.id),
                        db.and_(PathEdge.from_node_id == node2.id, PathEdge.to_node_id == node1.id)
                    )
                ).first()
                
                if not existing_edge:
                    # 计算步行时间（假设步行速度为5km/h）
                    walk_time = (distance / 1000) * 12  # 分钟
                    bike_time = walk_time * 0.3  # 骑行时间约为步行的30%
                    bus_time = walk_time * 1.5   # 公交时间约为步行的150%（包含等车时间）
                    
                    edge = PathEdge(
                        from_node_id=node1.id,
                        to_node_id=node2.id,
                        distance=distance,
                        travel_time_walk=walk_time,
                        travel_time_bike=bike_time,
                        travel_time_bus=bus_time,
                        path_type='walkway',
                        is_bidirectional=True
                    )
                    db.session.add(edge)
                    edge_count += 1
    
    db.session.commit()
    print(f"路径边初始化完成，共创建 {edge_count} 条边")

def main():
    """主函数"""
    with app.app_context():
        print("开始数据初始化...")
        
        # 创建所有表
        db.create_all()
        
        # 初始化数据
        init_locations()
        init_path_nodes()
        init_path_edges()
        
        print("数据初始化完成！")
        
        # 输出统计信息
        location_count = Location.query.count()
        node_count = PathNode.query.count()
        edge_count = PathEdge.query.count()
        
        print(f"统计信息：")
        print(f"- 地点数量: {location_count}")
        print(f"- 路径节点数量: {node_count}")
        print(f"- 路径边数量: {edge_count}")

if __name__ == '__main__':
    main()

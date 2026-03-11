#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
创建测试用户并测试API
"""

from main import app, db, LoginUser
from werkzeug.security import generate_password_hash

def create_test_user():
    """创建测试用户"""
    with app.app_context():
        # 检查是否已存在测试用户
        existing_user = LoginUser.query.filter_by(username='testuser').first()
        if existing_user:
            print("测试用户已存在")
            return
        
        # 创建新的测试用户
        test_user = LoginUser(
            username='testuser',
            password=generate_password_hash('123456'),
            email='test@example.com'
        )
        
        db.session.add(test_user)
        db.session.commit()
        print("测试用户创建成功: testuser / 123456")

def test_locations_count():
    """测试地点数量"""
    with app.app_context():
        from main import Location
        locations = Location.query.all()
        print(f"数据库中共有 {len(locations)} 个地点")
        
        # 按类型统计
        types = {}
        for location in locations:
            if location.type in types:
                types[location.type] += 1
            else:
                types[location.type] = 1
        
        print("地点类型统计:")
        for type_name, count in types.items():
            print(f"  {type_name}: {count} 个")

if __name__ == '__main__':
    print("创建测试用户...")
    create_test_user()
    print("\n统计地点数据...")
    test_locations_count()

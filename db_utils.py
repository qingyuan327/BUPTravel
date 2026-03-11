import pymysql
import logging

# 数据库配置
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'mahaijuan0511',
    'database': 'demo01',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}

def con_my_sql():
    """创建数据库连接并返回游标"""
    try:
        connection = pymysql.connect(**DB_CONFIG)
        cursor = connection.cursor()
        return cursor
    except Exception as e:
        logging.error(f"数据库连接失败: {e}")
        return None

def con_my_sql_with_params(sql, params=None):
    """执行带参数的SQL查询"""
    try:
        connection = pymysql.connect(**DB_CONFIG)
        cursor = connection.cursor()
        
        if params:
            cursor.execute(sql, params)
        else:
            cursor.execute(sql)
            
        return cursor
    except Exception as e:
        logging.error(f"数据库查询失败: {e}")
        return None

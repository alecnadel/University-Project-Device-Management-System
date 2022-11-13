from db.db_helper import get_cursor


def get_popular_devices():
    """Get data from database about which devices are most popular
    over the last month"""
    cursor = get_cursor()
    cursor.execute(
        'SELECT Device_name, COUNT(*) AS counts FROM usersdevices WHERE Start_Date > NOW() - INTERVAL 1 MONTH GROUP BY Device_name ORDER BY counts DESC;')
    return cursor.fetchall()

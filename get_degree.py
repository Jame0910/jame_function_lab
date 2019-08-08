from math import radians, sin, cos, degrees, atan2, atan, acos, tan

def get_degree(lon_a, lat_a, lon_b, lat_b):
    '''
    获取两个经纬度点的方向角，正北为基准
    Args:
        point p1(latA, lonA)
        point p2(latB, lonB)
    Returns:
        bearing between the two GPS points,
        default: the basis of heading direction is north
    '''
    
    rad_lat_a = radians(lat_a)
    rad_lon_a = radians(lon_a)
    rad_lat_b = radians(lat_b)
    rad_lon_b = radians(lon_b)
    d_lon = rad_lon_b - rad_lon_a
    y = sin(d_lon) * cos(rad_lat_b)
    x = cos(rad_lat_a) * sin(rad_lat_b) - sin(rad_lat_a) * cos(rad_lat_b) * cos(d_lon)
    brng = degrees(atan2(y, x))
    brng = (brng + 360) % 360
    return brng 
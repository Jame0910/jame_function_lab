from math import radians, sin, cos, degrees, atan2, atan, acos, tan


def get_distance(lon_a, lat_a, lon_b, lat_b):
    '''
    获取两个经纬度点的距离(meter)
    '''

    ra = 6378140  # radius of equator: meter
    rb = 6356755  # radius of polar: meter
    flatten = (ra - rb) / ra  # Partial rate of the earth
    # change angle to radians
    rad_lat_a = radians(lat_a)
    rad_lon_a = radians(lon_a)
    rad_lat_b = radians(lat_b)
    rad_lon_b = radians(lon_b)
    
    pa = atan(rb / ra * tan(rad_lat_a))
    pb = atan(rb / ra * tan(rad_lat_b))
    x = acos(sin(pa) * sin(pb) + cos(pa) * cos(pb) * cos(rad_lon_a - rad_lon_b))
    if x == 0:
        return x
    c1 = (sin(x) - x) * (sin(pa) + sin(pb))**2 / cos(x / 2)**2
    c2 = (sin(x) + x) * (sin(pa) - sin(pb))**2 / sin(x / 2)**2
    dr = flatten / 8 * (c1 - c2)
    distance = ra * (x + dr)
    return distance
def get_key(target_dict, value):
    '''
    输入value，输出字典对应的key
    '''
    # a = {'a':1, 'b':2}
    return [k for k, v in target_dict.items() if v == value]
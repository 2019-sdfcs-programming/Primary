def calc(d):
    if d['__init__'] != 'calc':
        raise NoRequiredData

    if d['__type__'] == 'svt' or d['__type__'] == 'fma' or d['__type__'] == 'pmv' or d['__type__'] == 'ift':
        # [s, v, t] [f, m, a] [p, m, v] [i, f, t] 순서대로
        if d['__requ__'] == 's' or d['__requ__'] == 'f' or d['__requ__'] == 'p' or d['__requ__'] == 'i':
            calced = d['data'][0] * d['data'][1]
        elif d['__requ__'] == 'v' or d['__requ__'] == 'm' or d['__requ__'] == 'm' or d['__requ__'] == 'f':
            calced = d['data'][0] / d['data'][1]
        elif d['__requ__'] == 't' or d['__requ__'] == 'a' or d['__requ__'] == 'v' or d['__requ__'] == 't':
            calced = d['data'][0] / d['data'][1]
        else:
            raise NoRequiredData
    
    result = {
        '__init__' : 'calced',
        '__type__' : d['__type__'],
        'received' : d['data'],
        'result' : calced
    }
    return result

if __name__ == '__main__':
    print(calc(dtemplate))
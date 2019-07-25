def delbtn(str_):
    str_r = ''
    for i in range(len(str_)-1):
        str_r += str_[i]
    return str_r

def chkif(if_, obj):
    # if_ = ['f', 't'], obj = index
    print(if_)
    print(obj)
    stack = 0
    for i in if_:
        if i in obj:
            stack += 1
    print('stack = {}'.format(stack))
    if stack == len(if_):
        return True
    else:
        return False

def wrapper(variables, target):
    for j in variables:
        if j['var'] == target:
            return j['obj'].value

if __name__ == '__main__':
    print(delbtn('string'))
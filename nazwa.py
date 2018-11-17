
def f1(a, b=0):
    return a*a + b


def f2(parms):
    if parms == 'ala':
        return  parms[0]
    elif parms == [1,2,3]:
        return  parms[0]
    elif parms == []:
        return 'BUUUUM'

def f4(name, name2=''):
    if name2=='':
        return name+' ma kota '
    else:
        return name+' ma kota i ' + name2

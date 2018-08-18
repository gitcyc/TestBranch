def add(*args):
    l = len(args)
    result = 0
    for i in range(l):
        if hasattr(args[i],'index'):
            for j in range(len(args[i])):
                result += args[i][j]
        else:
            result += args[i]
    return result
print(add(1,2,[3,4]))

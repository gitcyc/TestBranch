def add(args):
    l = len(args)
    result = 0
    for i in range(l):
        result += args[i]
    return result
print(add([1,2,3,4]))

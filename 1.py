arr = '111111111110000000000000000'


def task(array):
    array = [x for x in array]
    return array.index('0')


print(task(arr))

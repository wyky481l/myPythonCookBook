def q(arg1, arg2, arg3, arg4):
    print(arg1, arg2, arg3, arg4)


tu = (1, 2, 3, 4)
du = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

q(*tu)

a = {'name': 'w', 'number': '22', 'price': '10'}
print('a_value', *a)


my_dict = {'tuple': (2, 'test', 8, 3.2, [1, 5, 7]),
           'list': [45, 87, 26, 34, 12, ['лето', 'жара']],
           'dict': {'1': 'январь', '2': 'февраль', '3': 'март', '4': 'апрель', '5': 'май'},
           'set': {2, 58, 12, 48, 75}}

print(my_dict['tuple'][-1])
my_dict['list'].append(83)
my_dict['list'].pop(1)
my_dict['dict'][('i am a tuple',)] = '1'
del my_dict['dict']['5']
my_dict['set'].add(25)
my_dict['set'].remove(75)
print(my_dict)

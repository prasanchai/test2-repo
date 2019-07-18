import os
import sys
# from sys import executable
from os import rename


print(sys.version)
print(sys.executable)

dict = {'a': 18, 'b': 40, 'c': '20'}
# print(dict['b'])

dict2 = dict.copy()
# print(dict2)

dict2.update({'d': 15})
# print(dict2)

del dict2['b']
# print(dict2)

# print(dict)
# print(dict2)
# print('student name: %s' % list(dict2))
#

for key in dict.keys():
    if key in dict2.keys():
        print('true')
    else:
        print('false')

for key in list(dict.keys()):
    # print(key)
    if key in list(dict.keys()):
        print('true')
    else:
        print('false')

for key, value in dict.items():
    print("User Name:%s Age:%s" % (key, value))

import sys
print(dir())
a = 1
b = 'abracadabra'
c = 17.1
print(dir())

for i in dir(sys):
    print(i, end = ' ')

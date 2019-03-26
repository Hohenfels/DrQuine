# c bi1 piton
str = "# c bi1 piton%cstr = %c%s%c%cbuffer = str %% (10, 34, str, 34, 10, 10, 10)%cfile = open('Grace_kid.py', 'w')%cfile.write(buffer)"
buffer = str % (10, 34, str, 34, 10, 10, 10)
file = open('Grace_kid.py', 'w')
file.write(buffer)
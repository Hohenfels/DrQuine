import os
import sys
i = 5
if sys.argv[0] == 'Sully.py':
    i += 1
if i > 0:
    filename = 'Sully_{}.py'.format(i - 1)
    str = "import os%cimport sys%ci = %d%cif sys.argv[0] == 'Sully.py':%c    i += 1%cif i > 0:%c    filename = 'Sully_%c%c.py'.format(i - 1)%c    str = %c%s%c%c    buffer = str %% (10, 10, i - 1, 10, 10, 10, 10, 123, 125, 10, 34, str, 34, 10, 10, 10, 10, 10, 10)%c    file = open(filename, 'w')%c    file.write(buffer)%c    file.write(buffer)%c    file.close()%c    os.system('/usr/bin/python ' + filename)"
    buffer = str % (10, 10, i - 1, 10, 10, 10, 10, 123, 125, 10, 34, str, 34, 10, 10, 10, 10, 10, 10)
    file = open(filename, 'w')
    file.write(buffer)
    file.close()
    os.system('/usr/bin/python ' + filename)

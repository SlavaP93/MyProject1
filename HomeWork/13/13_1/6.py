import os
from os.path import join, getsize
num = os.path.abspath('C:/')
print(num)
for root, dirs, files in os.walk(num):
    print(root, "consumes", end=" ")
    print(sum(getsize(join(root, name)) for name in files), end=" ")
    print("bytes in", len(files), "non-directory files")
    if 'CVS' in dirs:
        dirs.remove('CVS')  # don't visit CVS directories
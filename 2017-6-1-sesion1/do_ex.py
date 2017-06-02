import os

rootdir = '../data_01/'
for parent, dirnames, filenames in os.walk(rootdir):
    for filename in filenames:
        path = os.path.join(parent,filename)
        print path
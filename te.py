import numpy as np


import argparse
import os


def parse_inputs():
    parser = argparse.ArgumentParser(description='Test different nets with 3D data.')
  
    parser.add_argument('-mn', '--model_name', dest='model_name', type=str, default='dense24')
    parser.add_argument('-r', '--root', dest='root', type=str, default='/home/lchen63/project/spie/Jan3')
    parser.add_argument('-i', '--inx', dest='inx', type=int, default=1)

    return vars(parser.parse_args())


options = parse_inputs()
model_name = options['model_name']
root = options['root']
inx = options['inx']
txt  = root + '/test.txt'
name  = []
with open(txt) as f:
	for line in f:
	    name.append(line[:-1])
dice_whole =  np.load( root +'/' +   model_name + '_dice_whole.npy')
dice_core = np.expand_dims(np.load( root + '/' + model_name + '_dice_core.npy')[:,1],axis = 1)
dice_et = np.expand_dims(np.load(root + '/' +  model_name + '_dice_enhance.npy')[:,1],axis = 1)
b = np.concatenate((dice_whole, dice_core,dice_et), axis=1)





# b = np.load(root + '/' + model_name)




c =  b[b[:,inx].argsort()]

print (c[18:])
print (c[18:].mean(axis=0))
print ('================================================')



print name 
print len(name)
print b[:,inx].argsort()
print len(b[:,inx].argsort())
new  = [ name[i] for i in b[:,inx].argsort()]

# new = name[b[:,inx].argsort()]

for i in range(len(new)):
	print new[i]


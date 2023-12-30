import numpy as np
import pprint 

def calculate(a):
    a = np.array(a).reshape(3,3)
    d = {
        'mean':[[a[:,0].mean(),a[:,1].mean(),a[:,2].mean()],[a[0].mean(),a[1].mean(),a[2].mean()],a.flatten().mean()],
        'variance':[[a[:,0].var(),a[:,1].var(),a[:,2].var()],[a[0].var(),a[1].var(),a[2].var()],a.flatten().var()],
        'standard deviation':[[a[:,0].std(),a[:,1].std(),a[:,2].std()],[a[0].std(),a[1].std(),a[2].std()],a.flatten().std()],
        'max':[[a[:,0].max(),a[:,1].max(),a[:,2].max()],[a[0].max(),a[1].max(),a[2].max()],a.flatten().max()],
        'min':[[a[:,0].min(),a[:,1].min(),a[:,2].min()],[a[0].min(),a[1].min(),a[2].min()],a.flatten().min()],
        'sum':[[a[:,0].sum(),a[:,1].sum(),a[:,2].sum()],[a[0].sum(),a[1].sum(),a[2].sum()],a.flatten().sum()]
    }
    return d


input1 = input('Enter the list of numbers(9_digits_):')
a = map(int,input1.split(','))
l = list()
for i in  a:
    l.append(i)
try:
    b = calculate(l)
    pprint.pprint(b)
except ValueError:
    print('List must contain nine numers')
#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'John AHUT'
#=======================================================================================================================
import numpy as np
#=======================================================================================================================
def f_consistency(x,n):
    RI=[0,0,0.58,0.9,1.12,1.24,1.32,1.41,1.45,1.49,1.51]
    ci=(x-n)/(n-1)
    ri=RI[n-1]
    CR=ci/ri
    if CR<0.1:
        print('=======================通过一致性检验！===========================')
    else:
        print('=======================警告：一致性未通过！！！===================')
    return CR

def f_consis(X):
    r,c=X.shape
    values,vectors=np.linalg.eig(X)
    max_value=values[0].real
    max_vector=vectors[:,0]
    sum=0
    for i in range(r):
        sum=sum+max_vector[i]
    max_weights=(max_vector/sum).real
    test_value=f_consistency(max_value,r)
    #return max_value,max_weights,test_value
    print('特征值：',max_value)
    print('权重：',max_weights)
    print('CR:',test_value)
## -------------------------------------------------------------------------------------------------------------------
#X=np.array([[1,2,6],[0.5,1,4],[1/6,1/4,1]])
#=np.array([[1,0.5,4,3,3],[2,1,7,5,5],[1/4,1/7,1,0.5,1/3],[1/3,1/5,2,1,1],[1/3,1/5,3,1,1]])
#Z=np.array([[1,2,5],[0.5,1,2],[0.2,0.5,1]])
#a,b,c=f_consis(Y)
#print('特征值：',a)
#print('权重：',b)
#print('CR:',c)

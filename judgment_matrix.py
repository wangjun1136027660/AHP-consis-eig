#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'John AHUT'
## ========================================
import numpy as np
def f_judgment(labels):
    print('-----------------------打分说明------------------------')
    print('1:前者与后者同等重要')
    print('3:前者对于后者稍微重要')
    print('5:前者对于后者明显重要')
    print('7:前者对于后者极其重要')
    print('9:前者对于后者强烈重要')
    print('2、4、6、8:表示上述相邻判断的中间值')
    print('=======================================================')
    a=len(labels)
    j_mat=np.ones([a,a])
    for i in range(a):
        for j in range(a-i):
            print('请输入（请输入整数或者小数）——> %s比%s相比：'%(labels[i],labels[j+i]))
            j_mat[i,j+i]=input()
    U = np.triu(j_mat,1)
    ds_j_mat=1/j_mat
    #对倒矩阵，取上三角
    dj_ds=np.triu(ds_j_mat)  # np.triu()中参数的特殊意义
    x = dj_ds.T
    x=x+U
    return x

## ---------------------------------------------------------------------------------------------------------------------
#labels=['外观','质量','价格']
#f_judgment(labels)

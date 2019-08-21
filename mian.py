# judgment-matrix模块  consis-eig模块 共同操作，输出一个 判断矩阵 并将它  最大特征值 与 特征向量 输出。
from judgment_matrix import f_judgment
import consis_eig
n=input('请输入字段数:')
names=[]
for i in range(int(n)):
    print('请输入第%d个字段：'%(i+1))
    y=input()
    names.append(y)
x=f_judgment(names)
consis_eig.f_consis(x)

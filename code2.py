# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 17:40:39 2021

@author: hello python
"""

 # 使用递归编写一个 power() 函数模拟内建函数 pow()，即 power(x, y) 为计算并返回 x 的 y 次幂的值。
def power(x, y):
    if y:
        return x*power(x,y-1)
    else:
        return 1

    
power(4,6)   
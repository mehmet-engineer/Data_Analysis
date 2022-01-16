import pandas as pd
import numpy as np

pd_series = pd.Series([10,20,30,40], ['a','b','c','d'])
#result = pd_series.ndim   --> 1
#result = pd_series.shape  --> (4,)
#result = pd_series.sum()  --> 100
#result = pd_series.max()  --> 40
#result = pd_series.min()  --> 10

result1 = pd_series + pd_series  #20,40,60,80
result2 = pd_series + 10         #20,30,40,50

#numpy ve pandas kardeş paketlerdir, birbiriyle uyumludur.
pd_series = pd.Series([1,2,3,4])
result_1 = np.power(pd_series, 2)
result_2 = np.sqrt(pd_series)

pd_series = pd.Series([10,20,30,40])
query1 = pd_series >= 20
query2 = pd_series %2 == 0
sonuç = pd_series[query1]  #süzülmüş, sorguya göre istenilen değerler
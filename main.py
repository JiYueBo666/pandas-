import  pandas as pd

#这四个参数比较重要
data_S=pd.Series([1,2,3],dtype=int,name='test')

#print(data)

#Series索引
'''
带'i'的表示用标号（intger）索引

1.用index直接索引
2.用iloc标号索引
3.用loc【index】索引
'''
#print(data['a'])
#print(data.iloc[1])
#print(data.loc['b'])


'''
切片
标号索引 iloc[n1:n2] 左闭右开
标签索引 loc【index1,index2】，左闭右闭

'''

#print(data.iloc[1:2])
#print(data.loc['b':'c'])

'''
获取属性
'''

# print(data.name)
# print(data.values)#np数组
# print(type(data.values))
# print(data.index)
# print(data.dtype)
# print(data.shape)#获取形状
# print(data.ndim)#获取维度
# print(data.size)#获取元素个数


'''
创建dataframe，这里Series的name要和dataframe的columns一致

指定列数据
'''
# print(data_S)
# data_S=pd.Series([1,2,3],dtype=int,name='python')
# data=pd.DataFrame(data_S,columns=['python'])
# print(data)

data={
    'a':[1,2],
    'b':[3,4],
    'c':[5,6]
}

dataframe=pd.DataFrame(data,index=['a','b'])
print(dataframe)
print(dataframe.index)



# 字典的创建删除修改
dict1 = {'jack': 4098, 'sape': 4139,'yellow':8466}
# # dict2 = dict([('jack',4098),('sape',4139),('yellow',8466)])
# # dict3 = dict(jack=4098,sape=4139,yellow=8466)
# # dict4 = {i:chr(65+i) for i in range(4)}
# # dict5 = {(k,v):k+v for k in range(2) for v in range(3)}
# # dict1['jack'] = 4299
# # dict1['rose'] = 4300
# # print(dir(dict1))
# 字典的方法--拷贝
# dict1 = {'jack': [4098,4100], 'sape': 4139,'yellow':8466}
# dic1 = dict1        #引用对象
# dic2 = dict1.copy() #浅拷贝
# dict1['jack'] = [4399,3300]
# # dict1['red'] = 3200
# print(dic1)
# print(dic2)
#字典的方法--fromkeys
print(dict1.pop('jack',4100))
print(dict1)
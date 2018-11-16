# 字典, index - value
tel = {'Justin':12334, 'Ivy':33333}
tel['Johny']='8888888'
print("tel =")
print(tel)
# {'Justin': 12334, 'Ivy': 33333, 'Johny': '8888888'}
print(tel.keys())
# dict_keys(['Justin', 'Ivy', 'Johny'])
print(list(tel.keys()))
# ['Justin', 'Ivy', 'Johny']
print(len(tel))
# 3

for t in tel:
    print(t)
'''
Justin
Ivy
Johny
'''

name = list(tel.keys())
print('name =')

print(name)
# ['Justin', 'Ivy', 'Johny']
print(name[0])
# Justin

print('Justin' in tel)
# True
print('Peter' in tel)
# False

# 串列
print('-----------------------')
fruits=['orange', 'banana', 'apple', 'kiwi']
print(fruits.count('banana'))
# 1
print(fruits.index('banana'))
# 1
print(fruits[1])
# banana
fruits.append('apple')
print(fruits)

# set 集合
st1 = set()
st2 = set([1,2,3,4])
st3 = set(['a','b','c','d'])
st4 = set(['a','c','e',1])
st5 = st3.union(st2)
st6 = list(st5)
print('st2 =')
print(st2)
# {1, 2, 3, 4}
print('st3 =')
print(st3)
# {'a', 'd', 'c', 'b'}

print('st4 =')
print(st4)
# {'a', 1, 'c', 'e'}

print('st6 =')
print(st6)
# [1, 2, 'b', 3, 4, 'c', 'a', 'd']

print(st6[3])
# 4

print('union')
print(st3.union(st2))
# {1, 2, 3, 'c', 'b', 4, 'a', 'd'}

print('intersection')
print(st3.intersection(st4))
# {'a', 'c'}

print('difference')
print(st3.difference(st4))
# {'d', 'b'}


#print(st2[0])
# TypeError: 'set' object does not support indexing

print(list(st2))
# [1, 2, 3, 4]
print(list(st2)[1])
# 2

words='abcdefghijklmnopqrstuvwxyz'
print(words[0])
# a
print(words[-2])
# y
print(words[0:2])
# ab
print(words[0:26:2])
# acegikmoqsuwy

name='Peter'
print(name.replace('P','p'))
# peter

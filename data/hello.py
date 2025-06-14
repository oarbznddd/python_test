a = [20,40]
a.append(80)
print(a)    #结果：[20, 40, 80]

a = [20,40]
print(id(a))
a = a+[50]
print(id(a))  #两次地址不一样，创建了新的对象

a = [20,40]
print(id(a))
b = [50,60]
a.extend(b)   #原对象修改
print(id(a))
a = a+b     #产生新对象
print(id(a))

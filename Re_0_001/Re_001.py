'''
什么事 函数  ：组织好的 可重复使用的 实现单一或者关联功能的代码段
作用：  提高应用的模块性  提高代码重复使用性
格式：
def 函数名（【参数】）
    # 函数说明
    要封装的代码
'''
# 1、、、、、、、、、、、、、、、、、、、、、、、、、、  举例子
'''
# def Pname():   # 当前函数没有放参数
#     #获取姓名
#     print("大家好我是小米")


# Pname() # 调用函数
# pri = Pname  # 将函数名赋值给另一个变量 ，取别名
# pri()

# def getNum():  # 定义
#     print('100')
# getNum()  # 调用

'''


# 2、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、  函数的参数
'''
# def Pname(userName):  # 形参  自定义
#     print('Hello  %s' %userName)
# Pname('刘德华')   # 实参

# 必备参数
# def getInfo(name,age):
#     print('wojiao %s  jinnian %s' %(name,age))
# getInfo('liudehua',19)  # 第一个实参 对应第一个形参  以此类推   且 形参 有两个 实参也要有两个

#关键字参数
# def getInfo(name,age):
#     print('wojiao %s  jinnian %s' %(name,age))
# getInfo(age = 19, name = 'liudehua')  # 给实参加上关键字  可以一一对应 形参

# 参数的默认值
# def getInfo(name,age = 19):  # 默认值参数 在申明函数时  给定
#     print('wojiao %s  jinnian %s' %(name,age))
# getInfo('liudehua')  # 有默认值形参 不传递
# getInfo('liudehua',20)  # 传递有默认值的 实参 会覆盖
'''
# 不定长参数
def getInfo(name,age,*args,**args2):   # *args  接收所有；未命名的参数（不带 ）   **args2 带关键字
    print('wojiao %s  jinnian %s' %(name,age))
    print(args)  # args  是一个元组
    print(args2)  # 字典数据类型
getInfo('liudehua',19,'a','b',add = 20)



# 3、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、
'''

'''

# 3、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、
'''

'''

# 3、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、
'''

'''

















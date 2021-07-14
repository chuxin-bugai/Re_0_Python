import numpy as np
import matplotlib.pyplot as plt
# 导入线性回归模型
from sklearn.linear_model import LinearRegression
# 数据集 生成
from sklearn.datasets import make_regression

'''
# 令x 为 -5到5之间 元素为 100 的等差数列
x = np.linspace(-5, 5, 100)
# 输入直线方程
y = 0.5*x + 3
plt.plot(x, y, c='orange')
plt.title('Straight Line')
plt.show()

''' # 线性模型的基本 概念

'''

X = [[1],[4]] # 两个点的 横坐标
y = [3,5]  # 两个点的 纵坐标
# 拟合 两个点
lr = LinearRegression().fit(X, y)
# 画出 两个点 和直线的 图形
z = np.linspace(0, 5,20)
plt.scatter(X, y, s=80)
plt.plot(z, lr.predict(z.reshape(-1, 1)), c='k')
plt.title('Straight Line')
print('y = {:.3f}'.format(lr.coef_[0]),'x','+ {:.3f}'.format(lr.intercept_))
plt.show()

# 假设三个点
X = [[1],[4],[3]] # 两个点的 横坐标
y = [3,5,3]  # 两个点的 纵坐标
# 拟合 两个点
lr = LinearRegression().fit(X, y)
# 画出 两个点 和直线的 图形
z = np.linspace(0, 5,20)
plt.scatter(X, y, s=80)
plt.plot(z, lr.predict(z.reshape(-1, 1)), c='k')
plt.title('Straight Line')
print('y = {:.3f}'.format(lr.coef_[0]),'x','+ {:.3f}'.format(lr.intercept_))
plt.show()

'''  # 两点确定一个支线











































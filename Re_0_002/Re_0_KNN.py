import numpy as np
# k最邻近算法 使用
from sklearn.datasets import make_blobs
from sklearn.datasets import make_regression
from sklearn.datasets import load_wine
# 导入 KNN 分类 工具
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import KNeighborsRegressor
# 导入 画图
import matplotlib.pyplot as plt
# 导入 数据集 拆分 工具
from sklearn.model_selection import train_test_split

'''
# 生成 样本数为200  分类为2 的数据集
data = make_blobs(n_samples=200,centers=2,random_state=8)
X, y = data
# 数据集 可视化
# plt.scatter(X[:,0],X[:,1],c=y,cmap=plt.cm.spring,edgecolors='k')
# plt.show()

clf = KNeighborsClassifier()
clf.fit(X,y)

# 下列代码 用于画图    (后续弄懂 代码  原理)
x_min, x_max = X[:,0].min() - 1, X[:,0].max() + 1
y_min, y_max = X[:,1].min() - 1, X[:,1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, .02),
                     np.arange(y_min, y_max, .02))
Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.pcolormesh(xx, yy, Z, cmap=plt.cm.Pastel1)
plt.scatter(X[:,0],X[:,1],c=y,cmap=plt.cm.spring,edgecolors='k')
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.title('Classifiler:KNN')
plt.scatter(6.75, 4.82, marker='*', c='red', s=200)
plt.show()
# 新点的分配
print(clf.predict([[6.75, 4.82]]))

'''     # 简单的 KNN

'''
data2 = make_blobs(n_samples=500, centers=5, random_state=8)
X2, y2 = data2

plt.scatter(X2[:,0],X2[:,1], c=y2, cmap=plt.cm.spring, edgecolors='k')



clf = KNeighborsClassifier()
clf.fit(X2, y2)

x_min, x_max = X2[:,0].min() - 1, X2[:,0].max() + 1
y_min, y_max = X2[:,1].min() - 1, X2[:,1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, .02),
                     np.arange(y_min, y_max, .02))
Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.pcolormesh(xx, yy, Z, cmap=plt.cm.Pastel1)
plt.scatter(X2[:,0],X2[:,1],c=y2,cmap=plt.cm.spring,edgecolors='k')
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.title('Classifiler:KNN')
# plt.show()

print('模型正确率:{:.2f}'.format((clf.score(X2, y2))))
'''     # 多元的分类任务

'''

# 特征为1  噪音为50 的数据集
X, y = make_regression(n_features=1, n_informative=1, noise=50, random_state=8)

plt.scatter(X, y, c='orange', edgecolors='k')

reg = KNeighborsRegressor()
reg.fit(X, y)

Z = np.linspace(-3, 3, 200).reshape(-1, 1)
plt.scatter(X, y, c='orange', edgecolors='k')
plt.plot(Z, reg.predict(Z), c='k', linewidth=3)
plt.title('KNN Regressor')
print('模型准确率：{:.2f}'.format(reg.score(X, y)))


# 进行优化

reg2 = KNeighborsRegressor(n_neighbors=2)  # 默认为 5
reg2.fit(X, y)

plt.scatter(X, y, c='orange', edgecolors='k')
plt.plot(Z, reg2.predict(Z), c='k', linewidth=3)
plt.title('KNN Regressor : n_neighbors = 2')
plt.show()
print('模型准确率：{:.2f}'.format(reg2.score(X, y)))
'''           # KNN 回归分析


'''

''' # KNN 实战--酒的分类

wine_dataset = load_wine()
# print('红酒数据集中的键 ： \n {}'.format(wine_dataset.keys()))
# print('数据概况 ： {}'.format(wine_dataset['data'].shape))
# print(wine_dataset['DESCR'])

# 拆分 数据集为 训练和测试数据集
X_train, X_test, y_train, y_test = train_test_split(wine_dataset['data'], wine_dataset['target'], random_state=0)

# 打印 训练 数据集 的向量形态
print('X_train shape : {}'.format(X_train.shape))
# 打印 测试 数据集 的向量形态
print('X_test shape : {}'.format(X_test.shape))
# 打印 训练 数据集 的目标形态
print('y_train shape : {}'.format(y_train.shape))
# 打印 测试 数据集 的目标形态
print('y_test shape : {}'.format(y_test.shape))

knn = KNeighborsClassifier(n_neighbors = 1)

# 使用 KNN 进行数据的 拟合
knn.fit(X_train, y_train)
print(knn)

print('测试数据集得分 : {:.2f}'.format(knn.score(X_test, y_test)))

# 输入 新的 数据点
X_new = np.array([[13.2,2.77,2.51,18.5,96.6,1.04,2.55,0.57,1.47,6.2,1.05,3.33,820]])

# 使用。predict 进行 预测
prediction = knn.predict(X_new)
print('预测新红酒的分类 : {}'.format(wine_dataset['target_names'][prediction]))





















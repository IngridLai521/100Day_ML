## mayavi 初嘗試

## 1. 給定座標，將多個平面連起

from mayavi import mlab
x = [[0,1,2,1,0],[0,1,2,1,0]]
y = [[1,0,1,2,1],[1,0,1,2,1]]
z = [[1,1,1,1,1],[2,2,2,2,2]]
s = mlab.mesh(x,y,z)
mlab.show()

## 2. 解方程式示意圖

import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-5, 5, 100)
# 給定x為-5到5間的等差數列(-5到5間有100個數)
y1 = -x + 6
y2 = x + 4
# 定義y1、y2
fig, ax = plt.subplots(figsize = (12, 7))
# 創建一個12*7的畫布和一個axes
ax.scatter(1, 5, s = 200, zorder=5, color = 'r', alpha = .8)
# 設定標點(解)格式，zorder為繪圖次序，alpha為透度
ax.plot(x, y1, x, y2, lw = 3)
# 繪製兩條線
ax.plot([1, 1], [0, 5], ls = '--', color = 'b', alpha = .5)
ax.plot([-5, 1], [5, 5], ls = '--', color = 'b', alpha = .5)
# 繪製標點的輔助線，為(1,0)到(1,5)以及(-5,5)到(1,5)之虛線
ax.set_xlim([-5, 5])
ax.set_ylim([0, 12])
# 設定x、y的座標軸範圍
s = '$(1,5)$'
# 給定s為(1,5)
ax.text(1, 5.5, s, fontsize = 20)
# 在圖上加上s(文字)
ax.set_title('Solution of $x+y=6$, $x-y=-4$', size = 22)
# 加上標題
ax.grid()
# 加上網格
plt.show()

## 3. 標出點點

import matplotlib.pyplot as plt
# 召換補師!!
import numpy as np
# 召喚戰神!!
x, y = np.arange(-3, 4, 1), np.arange(-3, 4, 1)
# 上面arange(-3, 4, 1) 指-3到3中間隔1的每個數字
X, Y = np.meshgrid(x, y)
# 形成x-y座標(矩陣)
fig, ax = plt.subplots(figsize = (12, 12))
# 設定畫布和一個axes，畫布大小為12*12
ax.scatter(X, Y, s = 100, color = 'red', zorder = 3)
# 設定標點格式
ax.axis([-5, 5, -5, 5])
# 設定x、y座標軸範圍
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')
# 默認座標軸有4個(上下左右)，讓縱橫各一以0為軸，剩下的消失
plt.show()
# magic time (NoN!!

## 4. Matplotlib三維標點

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
x, y = np.arange(-3, 4, 1), np.arange(-3, 4, 1)
X, Y = np.meshgrid(x, y)
# 給定X、Y
Z = X+Y
# 定義Z
fig = plt.figure(figsize = (7, 5))
# 建立7*5畫布
ax = fig.add_subplot(111, projection = '3d')
# 建立一個3D投影的子圖，111指畫布分割1行1列，影象畫在左到右、上到下的第1塊
ax.scatter(X, Y, Z, s = 100)
# 設定標點格式
plt.show()

## 5. Matplotlib三維平面

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
x, y = np.arange(-3, 4, 1), np.arange(-3, 4, 1)
X, Y = np.meshgrid(x, y)
# 給定X、Y
Z = X+Y
# 定義Z
fig = plt.figure(figsize = (7, 5))
# 建立7*5畫布
ax = fig.add_subplot(111, projection = '3d')
# 建立一個3D子圖
ax.plot_surface(X, Y, Z, cmap ='spring')
# 以給定標點(取樣點)建構曲面(此處為平面)，cmap為顏色指定
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.set_zlabel('z-axis')
# 設定座標軸標題
ax.set_title('$z=x+y$', size = 18)
# 設定axes標題
plt.show()

## 6. Matplotlib三元一次方程式圖解

# x1-2*x2+x3 = 0
# 2*x2-8*x3 = 8
# -4x1+5*x2+9*x3 = -9

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
x1 = np.linspace(25, 35, 20)
x2 = np.linspace(10, 20, 20)
# 給定x1、x2 (等差數列)
X1, X2 = np.meshgrid(x1, x2)
# 定義X1、X2，建立座標(矩陣)
fig = plt.figure(figsize = (7, 5))
# 建立7*5畫布
ax = fig.add_subplot(111, projection = '3d')
# 建立一個3D子圖
X3 = 2*X2 - X1
ax.plot_surface(X1, X2, X3, cmap ='viridis', alpha = 1)
X3 = .25*X2 - 1
ax.plot_surface(X1, X2, X3, cmap ='summer', alpha = 1)
X3 = -5/9*X2 + 4/9*X1 - 1
ax.plot_surface(X1, X2, X3, cmap ='spring', alpha = 1)
# 依據方程式分別定義X3，並建構曲面
ax.scatter(29, 16, 3, s = 100, color = 'black')
# 設定標點(解)
plt.show()

# [註] 教程原話
# The problem is that Matplotlib is not truly for drawing complicated
# 3D graphics, and it renders merely fake 3D graphs.

## 7. Mayavi三元一次圖解

from mayavi import mlab
import numpy as np
X1, X2 = np.mgrid[-10:10:21*1j, -5:10:21*1j]
# 給定X1、X2，X1為-10到10的數，21*1j為步長21點，參數越大越精細
# (中止數--實數表間隔不包尾數，虛數表點數包尾)
X3 = 6 - X1 - X2
mlab.mesh(X1, X2, X3,colormap="spring")
X3 = 3 - 2*X1 + X2
mlab.mesh(X1, X2, X3,colormap="winter")
X3 = 3*X1 + 2*X2 -4
mlab.mesh(X1, X2, X3,colormap="summer")
# 繪製三個曲面(平面)
mlab.axes()
# 增加座標軸
mlab.outline()
# 增加外框的線
mlab.points3d(1, 2, 3, color = (0.8, 0.2, 0.2))
# 設定標點格式，(1, 2, 3)為方程組解
mlab.title('A System of Linear Equations')
# 增加標題
plt.show()

## 8. 畫向量

import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots(figsize=(8, 8))
vec = np.array([[0, 0, 4, 7], [0, 0, 8, 6]])
X, Y, U, V = zip(*vec)
# 建立X, Y, U, V座標
ax.quiver(X, Y, U, V, angles='xy', scale_units='xy', scale=1, color = 'red', alpha = .6)
# 畫箭頭，angles為由(X,Y)到(X+U,Y+V)
ax.set_xlim([0, 10])
ax.set_ylim([0, 10])
# 設定座標軸範圍
ax.set_xlabel('x-axis', fontsize =16)
ax.set_ylabel('y-axis', fontsize =16)
# 設定座標軸標題
ax.grid()
ax.text(4, 7, '$(4, 7)$', fontsize = 16)
ax.text(8, 6, '$(8, 6)$', fontsize = 16)
# 加上文字
ax.plot([4, 4], [0, 7], c = 'b', lw = 2)
ax.plot([0, 4], [0, 0], c= 'b', lw = 2)
ax.plot([8, 0], [0, 0], c = 'b', lw = 2)
ax.plot([8, 8], [0,6], c= 'b', lw = 2)
# 畫兩個向量的X軸和Y軸輔助線
ax.text(1.7, 3.8, '$\sqrt{4^2+7^2}$', fontsize = 16, rotation = np.arctan(7/4)*180/np.pi)
ax.text(5, 4.1, '$\sqrt{8^2+6^2}$', fontsize = 16, rotation = np.arctan(6/8)*180/np.pi )
# 加上文字，文字旋轉角度與向量相同
plt.show()

## 9. 求範數

import numpy as np
a = np.array([4, 7])
b = np.array([8, 6])
a_norm = np.linalg.norm(a)
b_norm = np.linalg.norm(b)
print('Norm of a and b are {0:.4f}, {1} respectively.'.format(a_norm, b_norm))

## 10. 畫三維向量

import matplotlib.pyplot as plt
import numpy as np
vec = np.array([[0, 0, 0, 1, 1, 1], 
                [0, 0, 0, -2, 2, 5], 
                [0, 0, 0, 3, -2, 1]])
X, Y, Z, U, V, W = zip(*vec)
fig, ax = plt.subplots(figsize = (8, 8))
ax = fig.gca(projection='3d')
ax.quiver(X, Y, Z, U, V, W, length=1, normalize=False, color = 'red', alpha = .6,
          arrow_length_ratio = .18, pivot = 'tail', linestyles = 'solid',linewidths = 3)
# 畫三條三維向量
ax.grid()
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
ax.set_zlim([0, 5])
# 設定座標軸範圍
ax.text(1, 1, 1, '$(1, 1, 1)$')
ax.text(-2, 2, 5, '$(-2, 2, 5)$')
ax.text(3, -2, 1, '$(3, -2, 1)$')
ax.text(0, 0, 0, '$(0, 0, 0)$')
# 加上文字(座標)
point1 = [1, 1, 1]
point2 = [1, 1, 0]
vec1 = np.array([point1, point2])
X, Y, Z = zip(*vec1)
ax.plot(X, Y, Z, lw = 2, color = 'b', alpha = 0.7)
point1 = [0, 0, 0]
point2 = [1, 1, 0]
vec1 = np.array([point1, point2])
X, Y, Z = zip(*vec1)
ax.plot(X, Y, Z, lw = 2, color = 'b', alpha = 0.7)
point1 = [3, -2, 1]
point2 = [3, -2, 0]
vec1 = np.array([point1, point2])
X, Y, Z = zip(*vec1)
ax.plot(X, Y, Z, lw = 2, color = 'b', alpha = 0.7)
point1 = [0, 0, 0]
point2 = [3, -2, 0]
vec1 = np.array([point1, point2])
X, Y, Z = zip(*vec1)
ax.plot(X, Y, Z, lw = 2, color = 'b', alpha = 0.7)
point1 = [-2, 2, 5]
point2 = [-2, 2, 0]
vec1 = np.array([point1, point2])
X, Y, Z = zip(*vec1)
ax.plot(X, Y, Z, lw = 2, color = 'b', alpha = 0.7)
point1 = [0, 0, 0]
point2 = [-2, 2, 0]
vec1 = np.array([point1, point2])
X, Y, Z = zip(*vec1)
ax.plot(X, Y, Z, lw = 2, color = 'b', alpha = 0.7)
# 畫輔助線
plt.show()

# 上面繪製輔助線部分也可以改用for
# 此段代碼不完整

ax.text(1, 1, 1, '$(1, 1, 1)$')
ax.text(-2, 2, 5, '$(-2, 2, 5)$')
ax.text(3, -2, 1, '$(3, -2, 1)$')
ax.text(0, 0, 0, '$(0, 0, 0)$')

points = np.array([[[1, 1, 1], [1, 1, 0]], 
                  [[0, 0, 0], [1, 1, 0]], 
                  [[3, -2, 1],[3, -2, 0]],
                  [[0, 0, 0],[3, -2, 0]],
                  [[-2, 2, 5],[-2, 2, 0]],
                  [[0, 0, 0],[-2, 2, 0]]])

for i in range(points.shape[0]): # loop through the 3rd axis
    X, Y, Z = zip(*points[i,:,:])
    ax.plot(X,Y,Z,lw = 2, color = 'b', alpha = 0.7)
ax.grid()

## 11. 平面線性組合

import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots(figsize=(8, 8))
vec = np.array([[[0,0,4,2]],
                 [[0,0,-2,2]],
                 [[0,0,2,10]],
                 [[0,0,8,4]], 
                 [[0,0,-6,6]]])
colors = ['b','b','r','b','b']
for i in range(vec.shape[0]):
    X,Y,U,V = zip(*vec[i,:,:])
    ax.quiver(X, Y, U, V, angles='xy', scale_units='xy', color = colors[i], scale=1, alpha = .6)
    ax.text(x = vec[i,0,2], y = vec[i,0,3], s = '(%.0d, %.0d)' %(vec[i,0,2],vec[i,0,3]), fontsize = 16)
points12 = np.array([[8,4],[2,10]])
ax.plot(points12[:,0], points12[:,1], c = 'b', lw = 3.5,alpha =0.5, ls = '--')
points34 = np.array([[-6, 6],[2,10]])
ax.plot(points34[:,0], points34[:,1], c = 'b', lw = 3.5,alpha =0.5, ls = '--')
ax.set_xlim([-10, 10])
ax.set_ylim([0, 10.5])
ax.set_xlabel('x-axis', fontsize =16)
ax.set_ylabel('y-axis', fontsize =16)
ax.grid()
# 畫輔助線(basis)
a = np.arange(-11, 20, 1)
x = np.arange(-11, 20, 1)
for i in a:    
    y1 = i + .5*x
    ax.plot(x, y1, ls = '--', color = 'pink', lw = 2)
    y2 = i - x
    ax.plot(x, y2, ls = '--', color = 'pink', lw = 2)    
ax.set_title('Linear Combination of Two Vectors in $\mathbf{R}^2$', size = 22, x =0.5, y = 1.01)
plt.show()















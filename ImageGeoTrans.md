# 图像的几何变换

---

## 仿射变换

仿射变换类型有：平移、缩放、旋转

仿射变换矩阵：

<img src="http://latex.codecogs.com/gif.latex?A=\left\{\begin{matrix}a_{11} & a_{12} & a_{13} \\a_{21} & a_{22} & a_{23} \\0 & 0 & 1\end{matrix}\right\}" />


### 平移

平移是最简单的仿射变换，假设将空间坐标$(x,y)$，先沿x轴正方向平移200，再沿y轴正方向平移300，平移后的坐标为$(\widetilde x,\widetilde y)=(x+200,y+300)$

将假设一般化，假设任意空间坐标$(x,y)$先沿x轴平移$t_{x}$，再沿y轴平移$t_{y}$，则最后得到的坐标为$(\widetilde x,\widetilde y)=(x+t_{x},y+t_{y})$。

用矩阵形式来表示该平移变换过程如下：

<img src="http://latex.codecogs.com/gif.latex?\left\{\begin{matrix}\widetilde x \\\widetilde y \\1\end{matrix}\right\}=\left\{\begin{matrix}1 & 0 & t_{x} \\0 & 1 & t_{y} \\0 & 0 & 1\end{matrix}\right\}\left\{\begin{matrix}x \\y \\1\end{matrix}\right\}" />

其中，若$t_{x}>0$，则表示沿x轴正方向移动；若$t_{x}<0$，则表示沿x轴负方向移动。$t_{y}$与之类似。

### 放大和缩小


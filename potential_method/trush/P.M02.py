# http://denshi.blog.jp/robotics/python/vector_field_obstacle_avoidance
# 障害物との衝突を回避するベクトル場
# 経路を進む速度場を計算し, その後グラフに描く

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from numpy import*


# 障害物を回避する速度場の計算
def vector_obst(X,Xr,a=1,b=1,c=1):
    V = 0.0
    # ユークリッド距離の計算
    for i in range(Xr.shape[0]):
        R = Xr[i]-X
        r = np.linalg.norm(R)
        V += -(R/r)*c/(1+exp(a*r-b))
    return V

# メイン


# グラフの設定
fig = plt.figure()
ax = fig.add_subplot(111,aspect="equal")
ax.set_xticks(np.arange(-3,4))  # x軸の範囲
ax.tick_params(labelsize=15)    # 軸のフォントサイズ
plt.rcParams["font.family"] = "Times New Roman"
plt.xlabel("$x$ $[m]$",fontsize=20,fontname="Times New Roman")
plt.ylabel("$y$ $[m]$",fontsize=20,fontname="Times New Roman")
plt.xlim([-3,3])
plt.ylim([0,6])
plt.grid()

# 位置情報を取得
Xr = np.loadtxt("obstacle.txt")
# ファイルの中身が一行しか無いときの処理
if Xr.ndim == 1:
    Xr = Xr.reshape((1,3))
# x,y軸の範囲と間隔
X = np.linspace(-3,3,20)
Y = np.linspace(0,6,20)

# 障害物を描画
for i in range(2) :
    rect = matplotlib.patches.Rectangle((Xr.T[0][i]-0.25,Xr.T[1][i]-0.25),0.5,0.5,color="#333333")
    ax.add_patch(rect)
    # テキストを挿入
    plt.text(Xr.T[0][i]-0.25,Xr.T[1][i]-0.1,"ob"+str(i+1),fontsize=15,color="#FFFFFF")

# 速度場の計算と描画
for x in X:
    for y in Y:
        vx,vy,vz = vector_obst((x,y,0),Xr)
        plt.quiver(x,y,vx,vy,angles="xy",headwidth=3,scale=10,color="#555555")
# グラフの表示
plt.show()

# if __name__ == '__main__':
#     main()
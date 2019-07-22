# http://denshi.blog.jp/robotics/python/vector_field

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from numpy import*

# 経路を進む速度場の計算
def vector_route(X,Xi):

    # ユークリッド距離格納用の変数
    r = np.empty([Xi.shape[0],1])

    # ユークリッド距離の計算
    for i in range(Xi.shape[0]):
        R = X-Xi[i]
        r[i] = np.linalg.norm(R)

    # ユークリッド距離が最小の要素番号を取得
    min_i = np.argmin(r)

    # 速度ベクトルを計算
    if min_i == Xi.shape[0]-1:
        V = Xi[min_i] - X
        return V
    else:
        V = Xi[min_i+1] - X
        return V

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
def main():
    # グラフの設定
    fig = plt.figure()
    ax = fig.add_subplot(111,aspect="equal")
    ax.set_xticks(np.arange(-2,3))  # x軸の範囲
    ax.tick_params(labelsize=20)    # 軸のフォントサイズ
    plt.rcParams["font.family"] = "Times New Roman"
    plt.xlabel("$x$ $[m]$",fontsize=30,fontname="Times New Roman")
    plt.ylabel("$y$ $[m]$",fontsize=30,fontname="Times New Roman")
    plt.xlim([-2,2])
    plt.ylim([0,6])
    plt.grid()

    # 経路の位置情報を取得
    Xi = np.loadtxt("route.txt")
    Xr = np.loadtxt("obstacle.txt")
    # ファイルの中身が一行しか無いときの処理
    if Xi.ndim == 1:
        Xi = Xi.reshape((1,3))
    if Xr.ndim == 1:
        Xr = Xr.reshape((1,3))

    # x,y軸の範囲と間隔
    X = np.linspace(-3,3,15)
    Y = np.linspace(0,6,15)

    # 障害物を描画
    for i in range(2) :
        rect = matplotlib.patches.Rectangle((Xr.T[0][i]-0.5,Xr.T[1][i]-0.5),1.0,1.0,color="#333333")
        ax.add_patch(rect)
        # テキストを挿入
        plt.text(Xr.T[0][i]-0.4,Xr.T[1][i]-0.1,"Obst"+str(i+1),fontsize=30,color="#FFFFFF")

    # 経路の描画
    plt.plot(Xi.T[0],Xi.T[1],"r-o",linewidth=3,alpha=0.7)
    plt.text(0.2,0.1,"Start",fontsize=30,color="#BB0000")
    plt.text(0,5.3,"Goal",fontsize=30,color="#BB0000")

    # 速度場の計算と描画
    for x in X:
        for y in Y:
            vx,vy,vz = vector_route((x,y,0),Xi)+vector_obst((x,y,0),Xr)
            plt.quiver(x,y,vx,vy,angles="xy",headwidth=3,scale=10,color="#555555")

    # グラフの表示
    plt.show()

if __name__ == '__main__':
    main()
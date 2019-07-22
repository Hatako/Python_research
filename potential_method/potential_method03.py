# http://denshi.blog.jp/robotics/python/vector_field_path

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
    # ファイルの中身が一行しか無いときの処理
    if Xi.ndim == 1:
        Xi = Xi.reshape((1,3))

    # x,y軸の範囲と間隔
    X = np.linspace(-3,3,15)
    Y = np.linspace(0,6,15)

    # 経路の描画
    plt.plot(Xi.T[0],Xi.T[1],"r-o",linewidth=3,alpha=0.7)
    plt.text(0.2,0.1,"Start",fontsize=30,color="#BB0000")
    plt.text(0,5.3,"Goal",fontsize=30,color="#BB0000")
    # 速度場の計算と描画
    for x in X:
        for y in Y:
            vx,vy,vz = vector_route((x,y,0),Xi)
            plt.quiver(x,y,vx,vy,angles="xy",headwidth=3,scale=10,color="#555555")

    # グラフの表示
    plt.show()

if __name__ == '__main__':
    main()
# http://denshi.blog.jp/robotics/python/potential_field_kim
# ポテンシャル法を用いて, ポテンシャル関数を作成しグラフを描写するプログラム


#三次元グラフではなくまずはデカルト座標空間にポテンシャル関数の値f(x, y)を表示させる

import numpy as np
import matplotlib
#matplotlib.use('Agg') # -----(1)
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

def plot3d(U,xm,ym):
    # グラフ表示の設定
    fig = plt.figure(facecolor="white")
    ax = fig.add_subplot(111, projection="3d") #111は1行目1列目1番目
    ax.tick_params(labelsize=8, colors='r')    # 軸のフォントサイズ
    ax.set_xlabel("$x$", fontsize=12, fontname="Times New Roman")
    ax.set_ylabel("$y$", fontsize=12, fontname="Times New Roman")
    ax.set_zlabel("$U(x,y)$", fontsize=12, fontname="Times New Roman")
    surf = ax.plot_surface(xm, ym, U, rstride=1, cstride=1,linewidth=1, antialiased=True, cmap=cm.jet)
    plt.show()


def main():
    # ポテンシャル場を求める範囲
    x = np.arange(-10, 10, 0.1)
    y = np.arange(0, 20, 0.1)
    xm, ym = np.meshgrid(x, y)

    # 障害物と壁の座標を取得
    o = np.loadtxt("obstacle.txt", delimiter=",")

    # ポテンシャル関数のパラメータ
    Uo, Ug = 0, 0    # ポテンシャルの初期化
    lo, lg = 1, 2   # パラメータ1(形状)
    co, cg =1, 3    # パラメータ2(重み)
    # 目標のポテンシャルを計算
    xg, yg = 4, 16          # 目標地の座標
    Ug = cg*(1-np.exp(-((xg-xm)**2+(yg-ym)**2)/lg**2))
    # 障害物のポテンシャルを計算
    for i in range(o.shape[0]):
        Uo += co*np.exp(-((o[i][0]-xm)**2+(o[i][1]-ym)**2)/lo**2)
    # 各ポテンシャルの重ねあわせ
    U = (Uo/cg + 1)*Ug

    # グラフの描画
    plot3d(U,xm,ym)
    plt.savefig('figure.png')  # -----(2)


if __name__ == '__main__':
    main()

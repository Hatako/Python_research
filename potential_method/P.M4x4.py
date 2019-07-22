"""
matplotlibを用いてグリッドを持つグラフを作成し,
目標地点と障害物座標から計算されたポテンシャル関数を挿入

行列の座標とnumpy上での座標の関係を見直してきちんとグラフを表示できるようにした
探索の順序を表示することができた
まだ障害物にぶつかるので, ぶつからないようにパラメータをいじる事が出来るようにする
"""
import numpy as np
import matplotlib.pyplot as plt

# ポテンシャル場を求める範囲
RANGE = 5
x = np.arange(0, RANGE, 1)
y = np.arange(0, RANGE, 1)
ym, xm = np.meshgrid(x, y) #x, yではなく行, 列で

# 障害物と壁の座標を取得しndarrayに収納
o = np.loadtxt("obstacle.txt", delimiter=",")

# ポテンシャル関数のパラメータ
Uo, Ug = 0, 0    # ポテンシャルの初期化
lo, lg = 3, 3   # パラメータ1
co, cg =2, 2    # パラメータ2
xg, yg = 3, 3          # 目標地の座標

Ug = cg*(1-np.exp(-((xg-xm)**2+(yg-ym)**2)/lg**2))  # 目標のポテンシャルを計算

# 障害物のポテンシャルを計算(障害物の個数分)
obstacle_size = int(o.size/2)
if obstacle_size == 1:
    Uo += co * np.exp(-((o[0] - xm) ** 2 + (o[1] - ym) ** 2) / lo ** 2)
else:
    for i in range(obstacle_size):
       Uo += co*np.exp(-((o[i][0]-xm)**2+(o[i][1]-ym)**2)/lo**2)

# 各ポテンシャルの重ねあわせ
#U = (Uo/cg + 1)*Ug
U=Uo+Ug
U = np.round(U, decimals=2)
print(U)

####################################################

# matplotlibでグリッド付きグラフを作成, 行列の数値も挿入
# 次にそれぞれのポテンシャル関数を作成して挿入

plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = False  # x軸下ラベル無効
plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = True         # x軸上ラベル有効

plt.figure(figsize=(5, 5))
ax = plt.subplot(1, 1, 1)
ax.set_xlim([0,RANGE])
ax.set_ylim([RANGE,0]) # y軸を反転させる

ticks=np.linspace(0, RANGE, RANGE+1)
ax.set_xticks(ticks, minor=False)
ax.set_yticks(ticks, minor=False)
ax.grid()


for i in range(RANGE): #ポテンシャル関数の値, 行列のインデックスをグリッドに挿入
    for j in range(RANGE):
        plt.text(j + 0.8, i + 0.9, str(i)+str(j), fontsize=10)
        plt.text(j + 0.2, i + 0.6, U[i][j], fontsize=20)


# スタート位置座標
plt.text(0.25, 0.2, "start!",fontsize=15, color="blue")

# 障害物座標
if obstacle_size == 1:
    plt.text(o[1] + 0.1, o[0] + 0.2, "obstacle", fontsize=14)
else:
    for k in range(obstacle_size):
        plt.text(o[k][1]+0.1, o[k][0]+0.2, "obstacle",fontsize=14)

# 目標座標
plt.text(xg+0.3, yg+0.2, "goal",fontsize=15, color="red")
plt.xlabel("potential function")


# 経路選択
# スタート地点
# スタート地点に戻ることは無いので0で埋める

ROUTE=[]
location=[0,0]
plt.text(location[1] + 0.32, location[0] + 0.9, "●", fontsize=25, color="red")
plt.text(location[1] + 0.4, location[0] + 0.9, "1", fontsize=15, color="black")
U[0][0]=100
ROUTE.append(location)


# ポテンシャル関数の周りに無限大(ここでは100)を埋める
# これは壁を仮定しているのと経路選択の際に現在地を中心とした周囲3x3マスを選択するときにも便利

new_U = np.insert(U, 0, 100, axis=0)
new_U = np.insert(new_U, RANGE + 1, 100, axis=0)
new_U = np.insert(new_U, 0, 100, axis=1)
new_U = np.insert(new_U, RANGE + 1, 100, axis=1)


# 赤丸が戻ってしまうので修正
# ポテンシャル関数を, 現在位置基準で3x3にスライス
# スライスした3x3関数に対して, 全体の数字を中央の数値で引く操作を行う
# 3x3マスの中で最小の値をもつインデックスを返す

l=2
while True:
    print(location)
    slice=new_U[location[0]:location[0]+3,location[1]:location[1]+3]
    np.set_printoptions(suppress=True)
    min_coodinate = list(np.unravel_index(np.argmin(slice), slice.shape))

    # 1ステップ終了後の位置を赤丸でグラフ上に描く
    def python_list_add(in1, in2):
        wrk = np.array(in1) + np.array(in2)-1
        return wrk.tolist()

    next_location = python_list_add(location, min_coodinate)
    new_U[next_location [0]+1][next_location [1]+1]=100 # 既に通ったところを100で埋める
    ROUTE.append(next_location)
    location = next_location
    plt.text(location[1] + 0.32, location[0] + 0.9, "●", fontsize=25, color="red")
    plt.text(location[1] + 0.4, location[0] + 0.9, str(l), fontsize=15, color="black")
    l+=1
    if location[0] == xg and location[1] == yg:
        break

plt.savefig('potential_method4x4.png')
plt.show()

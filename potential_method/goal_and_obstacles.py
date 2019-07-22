# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

# goalの座標
x_goal = np.linspace(4, 1, 1)
y_goal = x_goal + 12

# obstacleの座標
x_obstacle = np.array([-1, -1, -4])
y_obstacle = np.array([3, 10, 6])

# 点プロット
plt.plot(x_goal, y_goal, "bo",lw=2, alpha=0.7, ms=5,label="Goal", color='black')
plt.plot(x_obstacle, y_obstacle, "bo",lw=2, alpha=0.7, ms=5,label="Obstacles", color='red')

# グラフ設定
plt.rcParams['font.family'] = 'Times New Roman' # 全体のフォント
plt.rcParams['font.size'] = 20                  # フォントサイズ
plt.rcParams['axes.linewidth'] = 1.0    # 軸の太さ 
plt.legend(loc=2,fontsize=20)           # 凡例の表示（2：位置は第二象限）
plt.title('Goal and Obstacles', fontsize=20)   # グラフタイトル
plt.xlabel('x', fontsize=20)            # x軸ラベル
plt.ylabel('y', fontsize=20)            # y軸ラベル
plt.xlim([-10, 10])                       # x軸範囲
plt.ylim([0, 20])                       # y軸範囲
plt.tick_params(labelsize = 10)         # 軸ラベルの目盛りサイズ
plt.xticks(np.arange(-10, 11, 2.0))   # x軸の目盛りを引く場所を指定（無ければ自動で決まる）
plt.yticks(np.arange(0, 21, 2.0))   # y軸の目盛りを引く場所を指定（無ければ自動で決まる）
#plt.axis('scaled')                      # x, y軸のスケールを均等
plt.tight_layout()                      # ラベルがきれいに収まるよう表示
plt.grid()                              # グリッドの表示
plt.show()                              # グラフ表示
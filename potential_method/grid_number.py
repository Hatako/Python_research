# matplotlibを用いてgrid付きの二次元グラフを作成, その後それぞれの行列の数値を挿入
# とりあえず4X4行列


import matplotlib.pyplot as plt
import numpy as np

RANGE = 4

x = np.linspace(0, RANGE)
y = np.linspace(0, RANGE)
fig = plt.figure(figsize=(RANGE, RANGE))

ax = fig.add_subplot(1, 1, 1)
ax.set_xticks(np.linspace(0, RANGE, RANGE+1))
ax.set_xticks(np.linspace(0, RANGE, RANGE+1), minor=True)
ax.set_yticks(np.linspace(0, RANGE, RANGE+1))
ax.set_yticks(np.linspace(0, RANGE, RANGE+1), minor=True)
ax.grid()
for i in range(RANGE):
    for j in range(RANGE):
        plt.text(0.2+j,0.3+i,"U"+str(i)+str(j),fontsize=20)
plt.show()
plt.savefig('figure_number.png')
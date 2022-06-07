import numpy as np
import matplotlib.pyplot as plt
from timeit import default_timer as timer
from tabulate import tabulate

from binary_search_tree import BST
from red_black_tree import RBT

start_test = timer()

# TEST 2: confronto altezza abr e rbt caso pessimo

bst_testee = BST()
rbt_testee = RBT()

x = np.linspace(0, 10_000, 10, dtype=np.int32)
h_bst = np.array(x)
h_rbt = []
step = 0
for i in range(0, 10_001):
    if i == x[step]:
        bst_testee.insert(i)
        rbt_testee.insert(i)
        h_rbt.append(rbt_testee.get_height())
        step += 1
    else:
        bst_testee.insert(i)
        rbt_testee.insert(i)

fig, ax = plt.subplots()

x_axes = np.linspace(0, 100, 10_000)
h_rbt = np.array(h_rbt)

ax.plot(x, h_bst, label='Altezza bst')
ax.plot(x, h_rbt, label='Altezza rbt')
ax.plot(x_axes, np.log2(x_axes), ':', label='lg n')
ax.set_xlabel('n')
ax.legend()

plt.xlim([-5, 100])
plt.ylim([-5, 100])

fig2, ax2 = plt.subplots()
ax2.plot(x, h_bst, label='Altezza bst')
ax2.plot(x, h_rbt, label='Altezza rbt')
ax2.plot(x_axes, np.log2(x_axes), ':', label='lg n')
ax2.set_xlabel('n')
ax2.legend()

ratio = np.around((h_rbt[1:499:15]) / np.log2(h_bst[1:499:15]), 3)
datas2 = np.stack((h_bst[1:499:15], h_rbt[1:499:15], np.around(np.log2(h_bst[1:499:15]), 3), ratio), axis=1)
f = open('test_data/test2_table.txt', 'w')
table2_headers = ['Altezza ABR = n', 'Altezza ARN', 'lg n', 'Altezza ARN / lg n']
f.write(tabulate(datas2, headers=table2_headers, tablefmt='latex_booktabs'))
f.close()

end_test = timer()
print(str(end_test - start_test) + "s")

plt.show()

import numpy as np
import matplotlib.pyplot as plt
from timeit import default_timer as timer
from tabulate import tabulate
from random import randint

from binary_search_tree import BST
from red_black_tree import RBT

start_test = timer()

# TEST 3: confronto altezza abr e rbt caso medio

bst_testee = BST()
rbt_testee = RBT()

xmax = 10000
x = np.linspace(0, xmax, 10000, dtype=np.int32)
h_bst = []
h_rbt = []
step = 0
for i in range(0, xmax + 1):
    new_element = randint(0, xmax)
    if i == x[step]:
        bst_testee.insert(new_element)
        rbt_testee.insert(new_element)
        h_rbt.append(rbt_testee.get_height())
        h_bst.append(bst_testee.get_height())
        step += 1
    else:
        bst_testee.insert(new_element)
        rbt_testee.insert(new_element)

fig, ax = plt.subplots()

x_axes = np.linspace(0, xmax, 100)
h_rbt = np.array(h_rbt)
h_bst = np.array(h_bst)

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

ratio_rbt = np.around((h_rbt[1:499:15]) / np.log2(h_bst[1:499:15]), 3)
ratio_bst = np.around((h_bst[1:499:15]) / np.log2(h_bst[1:499:15]), 3)
data = np.stack((h_bst[1:499:15], h_rbt[1:499:15], np.around(np.log2(h_bst[1:499:15]), 3), ratio_rbt, ratio_bst), axis=1)
f = open('test_data/test3_table.txt', 'w')
table3_headers = ['Altezza ABR = n', 'Altezza ARN', 'lg n', 'Altezza ARN / lg n', 'Altezza RBT / lg n']
f.write(tabulate(data, headers=table3_headers, tablefmt='latex_booktabs'))
f.close()

end_test = timer()
print(str(end_test - start_test) + "s")

plt.show()


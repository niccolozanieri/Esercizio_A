import numpy as np
import matplotlib.pyplot as plt
from timeit import default_timer as timer
from tabulate import tabulate

from binary_search_tree import BST

start_test = timer()

# TEST 1

bst_testee = BST()

x = np.linspace(0, 10_000, 500, dtype=np.int32)
h = np.zeros(500)
y_ins = np.zeros(500)
y_search = np.zeros(500)
y_del = np.zeros(500)
for j in range(0, 3):
    y_ins_tmp = []
    y_search_tmp = []
    y_del_tmp = []
    step = 0
    for i in range(0, 10_001):
        if i == x[step]:
            start_ins = timer()
            bst_testee.insert(i)
            end_ins = timer()

            start_search = timer()
            bst_testee.search(i)
            end_search = timer()

            y_ins_tmp.append((end_ins - start_ins) * 10e5)
            y_search_tmp.append((end_search - start_search) * 10e5)
            h[step] = x[step]
            step += 1
        else:
            bst_testee.insert(i)

    step = 0
    for i in range(0, 10_001):
        z = bst_testee.get_min()
        if i == x[step]:
            start_del = timer()
            bst_testee.delete(z)
            end_del = timer()
            y_del_tmp.append((end_del - start_del) * 10e5)
            step += 1
        else:
            bst_testee.delete(z)

    y_ins += np.array(y_ins_tmp)
    y_search += np.array(y_search_tmp)
    y_del += np.array(y_del_tmp)


y_ins = np.around(y_ins / 3, 3)
y_search = np.around(y_search / 3, 3)
y_del = np.fliplr(np.around(y_del / 3, 3))

fig, ax = plt.subplots()

ax.plot(x, y_ins, label='Inserimento')
ax.plot(x, y_search, label='Ricerca')
ax.plot(x, y_del, label='Cancellazione')
ax.plot(x, np.array(h), ':', label='Altezza')
ax.set_xlabel("# Nodi")
ax.set_ylabel('Tempo(1x10^-5 s)')
ax.legend()

y_ins = np.around(y_ins / 100, 3)
y_search = np.around(y_search / 100, 3)
y_del = np.around(y_del / 100, 3)
datas1 = np.stack((x[0:499:15], y_ins[0:499:15], y_search[0:499:15], y_del[0:499:15], h[0:499:15]), axis=1)
f = open('test_data/test1_table.txt', 'w')
f.write(tabulate(datas1, headers=['# Nodi', 'Inserimento', 'Ricerca', 'Cancellazione', 'Altezza'], tablefmt='latex_booktabs'))
f.close()

end_test = timer()
print(str(end_test - start_test) + "s")

plt.show()

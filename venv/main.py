import sys
from collections import Counter
#sys.stdout = open('AD.txt', 'w')
graf1 = [
    [1, 0.6, 4], [1, 0.4, 5],
    [2, 0.5, 5], [2, 0.5, 6],
    [3, 1, 6],
    [4, 0.6, 5], [4, 0.4, 8],
    [5, 1, 8],
    [6, 0.8, 7], [6, 0.2, 8],
    [7, 0.7, 8], [7, 0.3, 4],
    [8, 0.3, 6]
]

graf = [
    [1, 0.8, 7], [1, 0.2, 5],
    [2, 0.5, 4], [2, 0.5, 5],
    [3, 0.7, 4], [3, 0.3, 6],
    [4, 0.5, 6], [4, 0.5, 7],
    [5, 1, 7],
    [6, 0.9, 8], [6, 0.1, 4],
    [7, 0.6, 6], [7, 0.4, 8],
    [8,1,9]
]
print(' SIMULATE')

gen=[10,20,10]

output = Counter([graf[j][0] for j in range(len(graf))])
input = Counter([graf[j][2] for j in range(len(graf))])
start = list(set(output) - set(input))

i = 0
c = 0
f = True

while c != 3:
    if f == True:
        print('  GENERATE ' + str(gen[c]))
        c += 1
        f = False

    if input[graf[i][0]] < 2:
        print('  OUEUE QD' + str(graf[i][0]))
    else:
        print('LAB' + str(graf[i][0]) + ' OUEUE QD' + str(graf[i][0]))

    print('  SEIZE DD' + str(graf[i][0]) + '\n'
          '  DEPART QD' + str(graf[i][0]) + '\n'
          '  ADVANCE 1' + str(graf[i][0]) + '\n'
          '  RELEASE DD' + str(graf[i][0]))
    if output[graf[i][0]] > 1:
        print('  TRANSFER ' + str(graf[i + 1][1])
              + ',,LAB' + str(graf[i + 1][2]))


    if graf[i][0] == 8:
        print('  TERMINATE')
        f = True
        print(str(c) + '!!!!!!!!!!')
        i = [graf[j][0] for j in range(len(graf))].index(start[c])
    else:
        i = [graf[j][0] for j in range(len(graf))].index(graf[i][2])




print('  GENERATE 100\n'
      '  TERMINATE 1\n'
      '  START 1\n'
      ' END')
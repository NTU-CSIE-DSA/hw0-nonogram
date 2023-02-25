from random import randint, seed
from pprint import pprint

def genPlate(n, m):
    plate = [[ randint(0, 1) for _ in range(m) ] for _ in range(n)]
    return plate

def encodePlate(plate):
    n, m = len(plate), len(plate[0])

    res = []
    for i in range(n):
        row = []
        accu = 0
        for j in range(m):
            if plate[i][j] == 0 and accu != 0:
                row.append(accu)
                accu = 0
            elif plate[i][j] == 1:
                accu += 1

        if accu != 0:
            row.append(accu)
        res.append(row)

    for i in range(m):
        col = []
        accu = 0
        for j in range(n):
            if plate[j][i] == 0 and accu != 0:
                col.append(accu)
                accu = 0
            elif plate[j][i] == 1:
                accu += 1

        if accu != 0:
            col.append(accu)
        res.append(col)

    return res

subtask1 = 10
subtask2 = 10 + subtask1
subtask3 = 10 + subtask2
subtask4 = 30 + subtask3
seed(0xdeadbeef)

for i in range(subtask1):
    n, m = 1, randint(1, 5)
    p = genPlate(n, m)
    e = encodePlate(p)

    with open(f'./testdata/{i}.in', 'w') as f:
        f.write(f'{n} {m}\n')
        for r in e:
            f.write(f"{len(r)} ")
            f.write(" ".join(map(str, r)) + "\n")

    with open(f'./testdata/{i}.out', 'w') as f:
        for r in p:
            for c in r:
                f.write(['_', 'o'][c])
            f.write('\n')

for i in range(subtask1, subtask2):
    n, m = randint(1, 3), randint(1, 3)
    
    p = genPlate(n, m)
    e = encodePlate(p)

    with open(f'./testdata/{i}.in', 'w') as f:
        f.write(f'{n} {m}\n')
        for r in e:
            f.write(f"{len(r)} ")
            f.write(" ".join(map(str, r)) + "\n")

    with open(f'./testdata/{i}.out', 'w') as f:
        for r in p:
            for c in r:
                f.write(['_', 'o'][c])
            f.write('\n')

for i in range(subtask2, subtask3):
    n, m = 1, randint(3, 25)

    p = genPlate(n, m)
    e = encodePlate(p)

    with open(f'./testdata/{i}.in', 'w') as f:
        f.write(f'{n} {m}\n')
        for r in e:
            f.write(f"{len(r)} ")
            f.write(" ".join(map(str, r)) + "\n")

    with open(f'./testdata/{i}.out', 'w') as f:
        for r in p:
            for c in r:
                f.write(['_', 'o'][c])
            f.write('\n')

for i in range(subtask3, subtask4):
    n, m = randint(1, 25), randint(1, 25)
    while n * m > 25 or n * m < 5:
        n, m = randint(1, 25), randint(1, 25)

    p = genPlate(n, m)
    e = encodePlate(p)

    with open(f'./testdata/{i}.in', 'w') as f:
        f.write(f'{n} {m}\n')
        for r in e:
            f.write(f"{len(r)} ")
            f.write(" ".join(map(str, r)) + "\n")

    with open(f'./testdata/{i}.out', 'w') as f:
        for r in p:
            for c in r:
                f.write(['_', 'o'][c])
            f.write('\n')

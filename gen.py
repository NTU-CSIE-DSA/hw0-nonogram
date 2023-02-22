from random import randint
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

for i in range(50):
    n, m = randint(1, 5), randint(1, 5)
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

for i in range(50, 70):
    n, m = randint(1, 25), randint(1, 25)
    while n * m > 25:
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

for i in range(70, 100):
    n, m = randint(1, 25), randint(1, 25)
    while n * m > 25 or n * m < 20:
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

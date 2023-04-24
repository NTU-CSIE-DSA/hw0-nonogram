### DSA 2023 HW0 - Nonogram

```bash
# gen testdata

mkdir ./testdata
python3 gen.py
```

Official Solution with comment can be found [here](./sol2.c)

We implement the Nonogram solver with the following pseudo code

```pseudocode
def solve(plate, n, m, i):  // plate is n*m
  if i == n:
    return check_the_whole_plate()
  if not check_all_column: return false
  for every possible way of row(i):
    fillrow(i)
  if not check_row(i): return false
  return solve(plate, n, m, next(i))
```


#include <stdbool.h>
#include <stdio.h>

bool solve(int n, int m, char plate[25][25], int rowCnt[25], int row[25][13],
           int colCnt[25], int col[25][13], int r) {
  if (r == n) {
    // check each colsx
    for (int c = 0; c < m; c++) {
      bool colLegal = true;
      // status of current block
      int cCnt = 0, cLen[13], accu = 0;
      for (int k = 0; k < n; k++) {
        if (plate[k][c] == 'o') {
          accu++;
        } else if (accu != 0) {
          cLen[cCnt++] = accu;
          accu = 0;
        }
      }
      if (accu != 0) {
        // record how many we filled in each block
        cLen[cCnt++] = accu;
        accu = 0;
      }

      // not legal -> prune
      if (cCnt != colCnt[c]) colLegal = false;
      for (int k = 0; k < cCnt; k++) {
        if (cLen[k] != col[c][k]) colLegal = false;
      }

      if (!colLegal) return false;
    }

    return true;
  }

  // enumerate the r-th row
  // fill with every possible way
  for (int i = 0; i < (1 << m); i++) {
    bool rowLegal = true;

    int rCnt = 0, rLen[13], accu = 0;
    for (int k = 0; k < m; k++) {
      // fill in the plate
      plate[r][k] = "_o"[(i >> k) & 1];
      if (plate[r][k] == 'o') {
        accu++;
      } else if (accu != 0) {
        rLen[rCnt++] = accu;
        accu = 0;
      }
    }
    if (accu != 0) {
      rLen[rCnt++] = accu;
      accu = 0;
    }

    // same as colLegal -> prune
    if (rCnt != rowCnt[r]) rowLegal = false;
    for (int k = 0; k < rCnt; k++) {
      if (rLen[k] != row[r][k]) rowLegal = false;
    }

    if (!rowLegal) continue;

    // do it recursively
    if (solve(n, m, plate, rowCnt, row, colCnt, col, r + 1)) return true;
  }

  return false;
}

int main() {
  // reading input
  int n, m;
  int rowCnt[25], row[25][13]; // number of blocks in one row
  int colCnt[25], col[25][13]; // number of blocks in one col

  scanf("%d %d", &n, &m);

  for (int i = 0; i < n; i++) {
    scanf("%d", &rowCnt[i]);
    for (int j = 0; j < rowCnt[i]; j++) scanf("%d", &row[i][j]);
  }

  for (int i = 0; i < m; i++) {
    scanf("%d", &colCnt[i]);
    for (int j = 0; j < colCnt[i]; j++) scanf("%d", &col[i][j]);
  }

  char plate[25][25] = {};

  if (n > m) {
    solve(n, m, plate, rowCnt, row, colCnt, col, 0);

    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) printf("%c", plate[i][j]);
      printf("\n");
    }
  } else {
    solve(m, n, plate, colCnt, col, rowCnt, row, 0);

    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) printf("%c", plate[j][i]);
      printf("\n");
    }
  }

  return 0;
}

#include "testlib.h"
#include <vector>
using namespace std;

vector< vector<int> > encode(char plate[25][25], int n, int m){
	vector< vector<int> > res;

	for(int i = 0; i < n; i++){
		vector<int> row;
		int accu = 0;
		for(int j = 0; j < m; j++){
			if(plate[i][j] == '_' && accu != 0){
				row.push_back(accu);
				accu = 0;
			}else if (plate[i][j] == 'o'){
				accu ++;
			}
		}

		if (accu != 0)
			row.push_back(accu);
		res.push_back(row);
	}

	for(int i = 0; i < m; i++){
		vector<int> row;
		int accu = 0;
		for(int j = 0; j < n; j++){
			if(plate[j][i] == '_' && accu != 0){
				row.push_back(accu);
				accu = 0;
			}else if (plate[j][i] == 'o'){
				accu ++;
			}
		}

		if (accu != 0)
			row.push_back(accu);
		res.push_back(row);
	}

	return res;
}

int main(int argc, char *argv[]){
	setName("checker for nonogram");
	registerTestlibCmd(argc, argv);

	int n = inf.readInt(), m = inf.readInt();
	inf.readEoln();
	char plate[25][25];

	for(int i = 0; i < n; i++){
		for(int j = 0; j < m; j++)
			plate[i][j] = ouf.readChar();
		ouf.readEoln();
	}


	vector< vector<int> > ans;
	for(int i = 0; i < m + n; i++){
		vector<int> row;
		int len = inf.readInt();
		inf.readSpace();
		for(int j = 0; j < len; j++)
			row.push_back(inf.readInt());
		inf.readEoln();
		ans.push_back(row);
	}


	if (encode(plate, n, m) != ans)
		quitf(_wa, "invalid solution");

	quitf(_ok, "valid solution");
}

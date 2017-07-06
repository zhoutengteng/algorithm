#include <iostream>
#include <memory>
using namespace std;


int match[5] = {0,0,0,0,0};
int line[5][5] = {{0,0,0,0,0},
                  {0,1,1,0,0},
                  {0,0,1,1,0},
                  {0,1,1,0,0},
                  {0,0,0,1,0}};

bool find(int boyId, int beginGirl) {
    for (int girlId = beginGirl; girlId <= 4; girlId++) {
        if (line[boyId][girlId]) {
            if (match[girlId] == 0 || find(match[girlId], beginGirl+1)) {
                match[girlId] = boyId;
                return true;
            } 
        } 
    }
    return false;
}


int main() {
    int all = 0;
    for (int i = 1; i <= 4; i++) {
        if (find(i, 1)) all+=1; 
    }
    for (int i = 0; i < all; i++) {
        printf("girl %d---- boy %d\n",i+1, match[i+1]);
    }


}
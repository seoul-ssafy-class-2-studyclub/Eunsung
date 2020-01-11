#include <stdio.h>

long long waters[200005] = {0, };

struct City {
    int parent;
    int depth;

    City() {};
    City(int p, int d): parent(p), depth(d) {};
} DS[200005];

void init(int N) {
    for (int n = 1; n <= N; n++) {
        DS[n] = City(n, 1);
    }
}

void input(int N) {

    int p, c;
    for (int i = 0; i < N; i++) {
        scanf("%d %d", &p, &c);
        DS[c] = City(p, DS[p].depth + 1);
    }
}

int main() {
    return 0;
}
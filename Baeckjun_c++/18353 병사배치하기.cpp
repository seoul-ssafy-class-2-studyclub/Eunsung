#include <stdio.h>
#define MN 2005

int N;
int scores[MN], DP[MN];

void init() {
    scanf("%d", &N);
    int score;
    for (int i = 0; i < N; i++) {
        scanf("%d", &score);
        scores[i] = score;
        DP[i] = 1;
    }
}

int main() {

    init();
    int max_dp = 1;
    for (int now = 0; now < N; now++) {
        for (int before = 0; before < now; before++) {
            if (scores[before] > scores[now]) {
                DP[now] = (DP[before] + 1) > DP[now] ? DP[before] + 1 : DP[now];
            }
        }
        // printf("%d " , DP[now]);
        if (DP[now] > max_dp) max_dp = DP[now];
    }

    printf("%d", N - max_dp);   

    return 0;
}
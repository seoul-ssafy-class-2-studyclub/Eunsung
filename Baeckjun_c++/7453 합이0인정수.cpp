#include <stdio.h>

int N, A[4005], B[4005], C[4005], D[4005];

int main() {

    scanf("%d", &N);
    int answer = 0;
    int tmp;
    for (int i = 0; i < N; i++) {
        scanf("%d %d %d %d", &A[i], &B[i], &C[i], &D[i])
    }

    printf("%d", answer);

    return 0;
}
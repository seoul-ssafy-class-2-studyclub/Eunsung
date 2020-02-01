#include <stdio.h>
#define MM 1000005
int N, M;

struct Now{
    int y, x;
    int d;
    int c;

    Now() {};
    Now(int y, int x, int d, int c) : y(y), x(x), d(d), c(c) {};

} heap[MM];

int heapN = 0;

void push(Now n) {
    heap[++heapN] = n;
    int idx = heapN;

    while (idx > 1) {
        if (heap[idx].c > heap[idx / 2].c) {
            Now temp = heap[idx];
            heap[idx] = heap[idx / 2];
            heap[idx / 2] = temp;
            idx /= 2;
        }
        else break;
    }
}

Now pop() {
    Now result = heap[1];
    heap[1] = heap[heapN--];

    int parent = 1;
    while (parent * 2 <= heapN) {
        int child = 2 * parent;
        int target = child;
        if (heap[child].c < heap[child + 1].c && child + 1 <= heapN ) target = child + 1;

        if (heap[target].c > heap[parent].c) {
            Now temp = heap[target];
            heap[target] = heap[parent];
            heap[parent] = temp;
            parent *= target;
        }
        else break;
    }
    return result;
}

int dys[3] = {0, 0, 1};
int dxs[3] = {1, -1, 0};
int board[1005][1005];
int visited[1005][1005];

int main() {

    scanf("%d %d", &N, &M);
    int val;
    for (int n = 0; n < N; n++) {
        for (int m = 0; m < M; m++) {
            scanf("%d", &val);
            board[n][m] = val;
        }
    }
    push(Now(0,0,-2,board[0][0]));
    int max_c = 0;
    while (heapN > 0) {
        Now now = pop();
        // if (visited[now.y][now.x] > now.c && now.y != N - 1 && now.x != M - 1) continue;
        // else visited[now.y][now.x] = now.c;
        if (now.y + 1 == N && now.x + 1 == M) {
            // printf("%d", now.c);
            printf("%d, %d, %d \n", now.y, now.x, now.c);
            if (max_c < now.c) {max_c = now.c;}
        }

        for (int now_d = 0; now_d < 3; now_d ++) {
            bool out = now.x + dxs[now_d] >= M || now.x + dxs[now_d] < 0 || now.y + dys[now_d] >= N;
            if (now_d + now.d == 1 || out) continue;
            // printf("%d, %d, %d, %d \n", now.y, now.x, now.c, now_d);
            push(Now(now.y + dys[now_d], now.x + dxs[now_d], now_d, now.c + board[now.y + dys[now_d]][now.x + dxs[now_d]]));
        }
    }
    printf("%d", max_c);
    return 0;
}
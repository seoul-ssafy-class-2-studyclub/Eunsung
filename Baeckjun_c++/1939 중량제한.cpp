#include <stdio.h>
#define MI 200005

int N, M;

struct Route {
    int e;
    Route *next;
    int c;

    Route() {};
    Route(int e, Route *next, int c) : e(e), next(next), c(c) {};

} con[MI];

Route *mem[MI];

struct Info {
    int e, max_c;
    Info() {};
    Info(int e, int max_c): e(e), max_c(max_c) {};
} heap[MI];

int heapN;

void init() {
    heapN = 0;
    for (int i=0; i< MI; i++) {mem[i] = nullptr;}
    scanf("%d %d", &N, &M);
    int a,b,c;
    for (int m = 0; m < M; m++) {
        scanf("%d %d %d", &a, &b, &c);

        con[2 * m] = Route(b, mem[a], c);
        mem[a] = &con[2 * m];
        con[2 * m + 1] = Route(a, mem[a], c);
        mem[b] = &con[2 * m + 1];

    }
}

void push(Info n) {
    heap[++heapN] = n;
    int idx = heapN;
    while (idx > 1) {
        if (heap[idx].max_c < heap[idx / 2].max_c){
            Info temp = heap[idx];
            heap[idx] = heap[idx / 2];
            heap[idx / 2] = temp;
            idx /= 2;
        }
        else break;
    }
}

Info top() {
	if (heapN == 0) return Info();
	return heap[1];
}
void pop() {
	if (heapN == 0) return;

	heap[1] = heap[heapN];
	heapN--;

	int idx = 1;
	while (idx * 2 <= heapN) {
		int left = idx * 2;
		int right = left + 1;
		int target = 0;
		if (heap[left].max_c < heap[right].max_c || right > heapN)
			target = left;
		else
			target = right;

		if (heap[target].max_c < heap[idx].max_c) {
			Info temp = heap[idx];
			heap[idx] = heap[target];
			heap[target] = temp;
			idx = target;
		}
		else break;
	}
}

int main() {

    init();

    return 0;
}
#include <stdio.h>

int toMa[5005], GuntoMa[5005];

struct Route {
    int e;
    Route* next;
    int c;

    Route() {e= c = 0; next= nullptr;};
    Route(int e, Route* next, int c): e(e), next(next), c(c) {};
} con[20005];
Route* mem[5005];

struct Info {
    int e;
    long long c;
    Info() {}
    Info(int e, long long c): e(e), c(c) {};
} heap[20005];
int heapN;
bool visited[5005];
void init() {
    heapN = 0;
    for (int i = 0; i < 5005; i++) visited[i] = false;
}

void push(Info n) {
    heap[++heapN] = n;
    int idx = heapN;
    while (idx > 1) {
        if (heap[idx].c > heap[idx / 2].c){
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
		if (heap[left].c < heap[right].c || right > heapN)
			target = left;
		else
			target = right;

		if (heap[target].c < heap[idx].c) {
			Info temp = heap[idx];
			heap[idx] = heap[target];
			heap[target] = temp;
			idx = target;
		}
		else break;
	}
}
void dijk(int start, int arr[]) {
    init();
    push(Info(start, 0));

    while (heapN > 0) {
        Info info = top(); pop();
        // if (visited[info.e]) continue;
        // visited[info.e] = true;
        for (Route* edge = mem[info.e]; edge != nullptr; edge = edge -> next){
            
            if (arr[edge -> e] > info.c + edge -> c) {
                arr[edge -> e] = info.c + edge -> c;
                push(Info(edge -> e, arr[edge -> e]));
            }
        }
    }
}

int main() {

    int V, E, P;
    scanf("%d %d %d", &V, &E, &P);
    
    for (int v = 1; v <= V; v++) toMa[v] = 2e9, GuntoMa[v] = 2e9, mem[v] = nullptr;
    int a, b, c;
    for (int e = 0; e < E; e++) {
        scanf("%d %d %d", &a, &b, &c);
        con[2 * e] = Route(b, mem[a], c);
        mem[a] = &con[2 * e];
        // printf("%d", con[2*e].e);
        con[2 * e + 1] = Route(a, mem[b], c);
        mem[b] = &con[2 * e + 1];
    }

    dijk(1, toMa);
    dijk(P, GuntoMa);

    if (toMa[V] == (GuntoMa[V] + toMa[P])) printf("SAVE HIM");
    else printf("GOOD BYE");
    // printf("%d")
    return 0;
}
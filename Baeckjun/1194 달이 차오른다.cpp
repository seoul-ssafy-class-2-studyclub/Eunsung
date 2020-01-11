#include <stdio.h>
#include <iostream>
using namespace std;

bool visited[50][50];
char board[50][50];
int status;

struct Node{
    int y;
    int x;
    int status;
    int cnt;

    Node() {};
    Node(int y, int x, int status, int cnt): y(y), x(x), status(status), cnt(cnt) {};
} queue[160005], save[160005];
int head, tail, save_idx = 0;
int dys[4] = {-1, 1, 0, 0};
int dxs[4] = {0, 0, -1, 1};
int idx;
void init() {
    for (int y = 0; y < 50; y++) {
        for (int x = 0; x < 50; x++){
            visited[y][x] = false;
        }
    }
    head = 1;
    tail = 0;
}

void push(Node n) {
    queue[++tail] = n;
}

Node pop() {
    if (head > tail) return Node();
    return queue[head++];
}

int main() {
    int N, M;
    cin >> N >> M;

    for (int y = 0; y < N; y++) {
        for (int x = 0; x < M; x++) {
            char c;
            cin >> c;
            board[y][x] = c;
            if (board[y][x] == '0') {
                save[save_idx++] = Node(y, x, 0, 0);
            }
        }
    }

    int now_idx = 0, ry, rx;
    int result = -1;
    bool flag = false;
    while (now_idx <= save_idx && now_idx < 160005) {
        init();
        push(save[now_idx++]);
        while (head <= tail) {
            Node now = pop();
            visited[now.y][now.x] = true;
            // cout << now.y <<now.x;
            if (board[now.y][now.x] == '1') {
                if (result == -1 || result > now.cnt) {
                    flag = true;
                    result = now.cnt;
                    // cout << 1111;
                }
                break;
            }
            for (int idx = 0; idx < 4; idx++) {
                ry = now.y + dys[idx];
                rx = now.x + dxs[idx];
                if (0 <= ry && ry < N && 0 <= rx && rx < M && !visited[ry][rx]){
                    // visited[ry][rx] = true;
                    if ('a' <= board[ry][rx] && board[ry][rx] <= 'z' && !(now.status & (1 << board[ry][rx] - 'a'))) {
                        // status += 1 << board[ry][rx] - 'a';
                        cout << now.status << '-' << '(' << now.y << ',' << now.x <<')'<<endl;
                        save[save_idx++] = Node(ry, rx, now.status | (1 << board[ry][rx] - 'a'), now.cnt + 1);
                    }
                    else if ('A' <= board[ry][rx] && board[ry][rx] <= 'Z') {
                        if (now.status & (1 << board[ry][rx] - 'A')) {
                            push(Node(ry, rx, now.status, now.cnt + 1));
                        };
                     }
                    else if (board[ry][rx] == '#') continue;
                    else {
                         push(Node(ry, rx, now.status, now.cnt + 1));
                     }
                }
            }
        }
    
    }
    cout << result;
}
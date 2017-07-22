#include <stdio.h>

int printArr();

int main() {
    int N;
    scanf("%d", &N);

    int x1[N],
        y1[N],
        x2[N],
        y2[N],
        g[N],
        grouplength[N],
        lastgroup = 1;

    for (int i = 0; i < N; i++) {
        scanf("%d %d %d %d", &x1[i], &y1[i], &x2[i], &y2[i]);
        g[i] = 0;
        grouplength[i] = 0;
        if (i == 0) {
            continue;
        }

        for (int j = 0; j < i; j++) {
            int c1 = x1[i] > x1[j] && x2[i] > x2[j],
                c2 = y1[i] > y1[j] && y2[i] > y2[j],
                c3 = x1[i] < x1[j] && x2[i] < x2[j],
                c4 = y1[i] < y1[j] && y2[i] < y2[j];
            
            if ((c1 || c3) && (c2 || c4)) {
                continue;
            }
            if (g[i] + g[j] == 0) {
                g[i] = lastgroup++;
                g[j] = g[i];
                continue;

            } else if (g[i] * g[j] == 0) {
                g[i] = g[i] + g[j];
                g[j] = g[i];
                continue;

            } else {
                for (int k = 0; k <= i; k++) {
                    if (g[k] == g[i]) {
                        g[k] = g[j];
                    }
                }
            }
        }
    }

    int maxg = 1;

    for (int i = 0; i < N; i++) {
        if (maxg < ++grouplength[g[i]])
            maxg = grouplength[g[i]];
    }

    printf("%d\n%d\n", --lastgroup, maxg);

    return 0;
}
#include <stdio.h>

typedef int bool;
#define true 1
#define false 0

int intersection(int x1, int y1, int x2, int y2, int X1, int Y1, int X2, int Y2) {
    int a = (y1 - y2) / (x1 - x2) == (Y1 - Y2) / (X1 - X2),
        b = (y1 - y2) * (X1 - X2),
        c = x1 - x2;

    if (a) {
        // 두 선분이 평행한 경우.
        return false;
    }

    double x = ( b * (x1 - X1) - c * (y1 - Y1) * (X1 - X2) ) / ( b - (Y1 - Y2) ),
        x_s = (double) x1,
        x_e = (double) x2;

    // 한 점에서 만나는 경우
    if (x_s <= x & x <= x_e)
        return true;

    // 평행하진 않지만 그냥 안 만나는 경우
    else
        return false;
}

int main() {
    int n;
    scanf("%d", &n);

    int line[n][4];
    // line[a][b]
    // b  0  1  2  3
    //    x1 y1 x2 y2

    for(int i = 0; i < n; i++) {
        scanf("%d %d %d %d", &line[i][0], &line[i][1], &line[i][2], &line[i][3]);
    }

    int groups = n;

    // y = ax + b

    for(int i = 0; i < n; i++) {
        for(int j = 0; j < i; j++) {
            bool isCollapse = intersection(line[i][0], line[i][1], line[i][2], line[i][3], line[j][0], line[j][1], line[j][2], line[j][3]);
            if (isCollapse) {
                groups--;
            }
        }
    }

    printf("%d", groups);
    return 0;
}
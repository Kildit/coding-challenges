def isIntersect(a, b):
    # 점 A는 점 B보다 왼쪽에, 점 C는 점 D보다 왼쪽에.
    if a[0] > a[2]:
        Ax = a[2]
        Ay = a[3]
        Bx = a[0]
        By = a[1]
    else:
        Ax = a[0]
        Ay = a[1]
        Bx = a[2]
        By = a[3]

    if b[0] > b[2]:
        Cx = b[2]
        Cy = b[3]
        Dx = b[0]
        Dy = b[1]
    else:
        Cx = b[0]
        Cy = b[1]
        Dx = b[2]
        Dy = b[3]

    # 평범한 두 선분
    if Ax != Bx and Cx != Dx and Ay != By and Cy != Dy:
        slopeAB = ( Ay - By ) / ( Ax - Bx )
        slopeCD = ( Cy - Dy ) / ( Cx - Dx )

        x = ( ( Cy - slopeCD * Cx ) - ( Ay - slopeAB * Ax ) ) / ( slopeAB - slopeCD )

        if Ax <= x <= Bx and Cx <= x <= Dx:
            return True

    # 평행한 두 선분
    if Ax == Bx and Cx == Dx:
        if Ax == Cx:
            return True
        else:
            return False

    elif Ay == By and Cy == Dy:
        if Ay == Cy:
            return True
        else:
            return False

    # 한 선분이 x축, y축에 평행한 경우
    for i in [0, 1]:
        if Ax == Bx or Ay == By:
            slopeCD = ( Cy - Dy ) / ( Cx - Dx )
            if Ax == Bx:
                if Ay > By:
                    return Ay >= ( slopeCD * (Ax - Cx) + Cy ) >= By
                else:
                    return Ay <= ( slopeCD * (Ax - Cx) + Cy ) <= By
            else:
                if Ax > Bx:
                    return Ax >= ( (Ay - Cy) / slopeCD + Cx ) >= Bx
                else:
                    return Ax <= ( (Ay - Cy) / slopeCD + Cx ) <= Bx
        
        ax = Ax
        ay = Ay
        bx = Bx
        by = By
        Ax = Cx
        Ay = Cy
        Bx = Dx
        By = Dy
        Cx = ax
        Cy = ay
        Dx = bx
        Dy = by

    # HARD CODING

    return False

def assignGroup(a, b):
    global group

    inGroup = []

    for i in range(0, len(group)):
        if b in group[i]:
            inGroup.append(i)

    if len(inGroup) != 0:
        joinGroup = []
        for i in inGroup:
            joinGroup = joinGroup + group[i]

        # 첫번째 공통 그룹으로 나머지 그룹을 join시킴.
        isFirstGroup = True
        # group이 pop될때마다 인덱스가 1씩 당겨지므로 j를 통해 타겟 인덱스 조정.
        j = 0
        for i in inGroup:
            if isFirstGroup:
                group[i] = group[i] + joinGroup
                isFirstGroup = False
                continue

            group.pop(obj=group[i - j])
            j += 1

    else:
        group = group + [[a, b]]

n = int( input() )
c = []
group = []

# 입력 받는 부분
for i in range(0, n):

    a = input().split(' ')
    for j in range(0, 4):
        a[j] = int(a[j])

    c.append(a)

# 본격
for i in range(0, n-1):
    for j in range(i+1, n):
        if isIntersect(c[i], c[j]):
            assignGroup(i, j)

print(group)
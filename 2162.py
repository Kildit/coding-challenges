# Global Variables
lines = []
groups = []


def main():
    N = int(input())

    i = 0
    while i < N:
        coordinate = [int(j) for j in input().split(' ')]
        item = {
            'x1': coordinate[0],
            'y1': coordinate[1],
            'x2': coordinate[2],
            'y2': coordinate[3],
            'group': None
        }
        lines.append(item)
        i += 1

    for i in range(0, N-1):
        for j in range(i+1, N):
            if intersect(lines[i], lines[j]):
                addGroup(i, j)
    
    # print length of groups
    print(len(groups))
    # find largest group
    print(findLargestGroup(groups))

    return

def intersect(l1, l2):
    cond1 = l1['x1'] > l2['x1'] and l1['x2'] > l2['x2']
    cond2 = l1['y1'] > l2['y1'] and l1['y2'] > l2['y2']
    cond3 = l1['x1'] < l2['x1'] and l1['x2'] < l2['x2']
    cond4 = l1['y1'] < l2['y1'] and l1['y2'] < l2['y2']

#   a and b or a and d or c and b or c and d
#   a * b + a * d + c * b + c * d
#   a * (b + d) + c * (b + d)
#   (a + c) * (b + d)

    if (cond1 or cond3) and (cond2 or cond4):
        return False
    
    return True

def addGroup(a, b):
    l1 = lines[a]
    l2 = lines[b]

    group = {}
    g_num = None

    cond1 = l1['group'] is None
    cond2 = l2['group'] is None

    # append new group
    if cond1 and cond2:
        g_num = len(groups)

        group = {a, b}
        groups.append(group)

    # append line to the other line's group
    elif cond1:
        g_num = l2['group']

        group = groups[g_num] | {a, b}

    elif cond2:
        g_num = l1['group']

        group = groups[g_num] | {a, b}

    # bind two groups into a group
    else:
        g1 = l1['group']
        g2 = l2['group']
        
        g_num = g1

        if not g1 is g2:
            group = groups[g1] | groups[g2]

            for i in list(groups[g2]):
                lines[i]['group'] = g1
            
            del groups[g2]

        else:
            group = groups[g1]

    lines[a]['group'] = g_num
    lines[b]['group'] = g_num
    
    groups[g_num] = group

    return

def findLargestGroup(groups):
    largest = 0

    for i in groups:
        largest = len(i) if len(i) > largest else largest

    return largest

main()
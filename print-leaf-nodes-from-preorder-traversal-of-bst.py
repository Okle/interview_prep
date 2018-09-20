# code

def findLeafs(pre):
    stack = list()
    i, j = 0, 1
    while j < len(pre):
        if pre[i] > pre[j]:
            stack.append(pre[i])
        else:
            leaf = False
            while stack:
                if pre[j] > stack[-1]:
                    stack.pop()
                    leaf = True
                else:
                    break
            if leaf:
                print(pre[i], end=' ')
        # print(stack)
        i = i + 1
        j = j + 1

    print(pre[i], end=' ')


string = "890 325 290 530 965 "
arr = list(map(int, string.split()))

findLeafs(arr)
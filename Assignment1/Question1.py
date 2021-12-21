# return the k-th largest element


def kth(A, k, l, r):
    if l == r:
        return A[l]
    # l = 0
    # r = n - 1
    mid = l + r // 2
    pivot = A[mid]  # 选取第一个元素作为pivot
    b = list()  # 记录比pivot小的元素
    c = list()  # 记录比pivot大的元素
    d = list()  # 记录排序一轮合并的数组
    for i in range(l, r):
        if A[i] < pivot:  # 比pivot小的元素放左边
            b.append(A[i])
        else:
            c.append(A[i])
    d.extend(b)
    d.append(pivot)
    d.extend(c)
    index = d.index(pivot)  # 获取pivot下标
    if k == index + 1:
        return pivot
    elif k <= index:  # 如果k小于index，证明目标元素在右边，对右半部分迭代
        c.insert(0, pivot)  # 把pivot元素插入到数组最前面
        kth(c, k, l, len(c))
    elif k > index:  # 如果k大于index，证明目标元素在左边，对左半部分迭代
        b.append(pivot)  # 把pivot元素插入到数组最后面
        kth(b, k, l, len(b))


# test
A = [8, 1, 15, 10, 4, 3, 2, 9, 7, 12, 5, 16, 14, 6, 13, 11]
print(kth(A, 7, 0, 16))

# Question:
# 如果pivot每次都选择A[0]，则递归无法终止
# 如果pivot = A[mid], mid = (l+r)//2, 仅能找出第7大的数字

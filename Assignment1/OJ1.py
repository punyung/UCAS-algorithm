# Fast Mod Exponentiation
# 首先实现快速幂
# Input：底数integer a, 幂为数组b
# Output： a^n的结果，其中n=数组b中的数提取出来合并

# 由于b为数组，先实现十进制转化二进制的算法,python 自带bin函数可以转化为二进制
def mybin(x):
    num = bin(x).replace("0b", "")
    return num


print(mybin(3))
print(mybin(5))
print(mybin(35))

# py读入数据
a = int(input()) # 输入整数
b = input() # 输入list



def FastExponentiation(a, b):
    # conquer
    c = 1337
    if b == 1:
        return a % c
    # divide & combine
    if b & 1 == 0:
        ans = FastExponentiation(a, b // 2) * FastExponentiation(a, b // 2) % c
    else:
        ans = FastExponentiation(a, b // 2) * FastExponentiation(a, b // 2) * a % c

    return ans


# 本地测试
print(FastExponentiation(222222222, 400))

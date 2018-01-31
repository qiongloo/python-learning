###递归函数

#用函数fact(n)表示，可以看出：fact(n) = n! = 1 x 2 x 3 x ... x (n-1) x n = (n-1)! x n = fact(n-1) x n
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

print(fact(5))
#print(fact(1000))

#尾递归
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

print(fact(5))
#print(fact(1000))


###############
## 练习
def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n - 1, a, c, b)  # 将a上的n-1个盘子借助c移动到b上
        move(1, a, b, c)  # 将a上剩余的1个盘子借助b移动到c上
        move(n - 1, b, a, c)  # 将b上的n-1个盘子借助a移动到c上

move(3, 'A','B','C')













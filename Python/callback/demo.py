from event import double, quadruple


# 中间函数
# 接受一个生成偶数的函数作为参数
# 返回一个奇数
def getOddNumber(k, get_even_number):
    return 1 + get_even_number(k)


# 起始函数，这里是程序的主函数
def main():
    k = 1
    # 当需要生成一个2k+1形式的奇数时
    i = getOddNumber(k, double)  # 登记回调函数
    print(i)
    # 当需要一个4k+1形式的奇数时
    i = getOddNumber(k, quadruple)
    print(i)
    # 当需要一个8k+1形式的奇数时
    i = getOddNumber(k, lambda x: x * 8)
    print(i)


if __name__ == "__main__":
    main()

'''
回调实际上有两种：阻塞式回调和延迟式回调。两者的区别在于：
 - 阻塞式回调里，回调函数的调用一定发生在起始函数返回之前 -> getOddNumber在main()作用域内
 - 延迟式回调里，回调函数的调用有可能是在起始函数返回之后;
'''

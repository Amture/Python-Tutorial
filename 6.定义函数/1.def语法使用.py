# def 定义函数
# 也就是说，这个是一个命令批量处理
#     比如

x = None
def number(a):
    print(a)
x=number(input("输入:"))
number(x)

#     运行这段程序的时候会输出x的数值
#     可以看得出来，我们定义了一个名为number的函数，他有一个参数为a，随后我们定义这个函数的意思是输出a的内容
#     随后我们定义一个变量为x，他的数值为10,然后我们调用这个新的函数number，命名他的参数为x，最终输出了x的数值
# 我们可以用它做很多事情
# 比如检查数值是否为数字而不是其他字符
#     eg.
def number_True(a):
    try:
        float(a)
    except TypeError:
        return False
    except ValueError:
        return False
    else:
        return True
x = None
x=number_True(input("输入:"))
#     这个可以检测输入的数值是否为数字而不是其他字符
#     如果输入的是a=x等或者其他字符
#     number_True会输出False
#     如果是数字则输出True
# 总而言之就是，def可以批量处理一些函数
# 这个def函数和windows中的批处理文件（.bat）极其相似，你可以相互理解的看

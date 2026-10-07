# try说的是：怎么让程序在出错的时候不崩溃，还能优雅地告诉你哪儿出问题了


#  为什么需要 try？ 
#
# 你写程序的时候，总有一些情况是你控制不了的：
# 
# 用户输入了字母，但你的代码等着数字
# 文件被删了，但你的代码要去读它
# 网络断了，但你的代码要连服务器
# 
# 这些情况，你没办法提前用 if 判断
# 因为你根本不知道会出现什么状况
# 
# 这时候就需要 try 来“兜底”


#  try 
# try 就是告诉 Python：
# “下面这几行代码，你试着跑一下。如果出错了，别崩溃，我有安排”
#
# 语法：
# try:
#     # 可能出现问题的代码
#     # 比如：用户输入、文件读写、类型转换


#  except 
# except 就是告诉 Python：
# “如果 try 里面出了某种错，你就执行这里的代码”
#
# 你可以指定捕获某一种错误：
# except ValueError:        # 值错误（比如把字母转数字）
# except TypeError:         # 类型错误（比如字符串和数字相加）
# except FileNotFoundError: # 文件找不到
#
# 你也可以所有错误一网打尽（不推荐，但新手可以先用）：
# except Exception as e:    # 把所有错误都抓进来，e 是错误信息


#  else 
# else 就是告诉 Python：
# “如果 try 里面一点错都没出，你就执行这里的代码”
# 
# 注意：只有 try 完全不出错，else 才会执行


#  finally 
# finally 就是告诉 Python：
# “不管 try 里面出没出错，最后都要执行这里的代码”
#
# 这是“无条件执行”的最后一块
# 通常用来做清理工作：关闭文件、关闭数据库连接、释放资源


#  完整示例 
# 下面这个例子展示 try-except-else-finally 完整结构


def test_try(a):
    try:
        # 尝试把 a 转成整数
        b = int(a)
        print("转换成功，b 是：", b)

    except ValueError:
        # 如果 a 是“abc”这种字母，int() 会报 ValueError
        print("出错啦！你输入的不是数字")

    else:
        # 如果上面的 int(a) 成功了，就会执行这里
        print("转换完全没问题，一切正常")

    finally:
        # 不管成不成功，最后都会执行这里
        print("===== 这次尝试结束了 =====")


# 测试一下
print("第1次测试：传入 123")
test_try(123)

print("\n第2次测试：传入 abc")
test_try("abc")


#  输出 
# 第1次测试：传入 123
# 转换成功，b 是： 123
# 转换完全没问题，一切正常
# ===== 这次尝试结束了 =====
#
# 第2次测试：传入 abc
# 出错啦！你输入的不是数字
# ===== 这次尝试结束了 =====


#  注意：finally 一定会执行 
#
# 哪怕你在 except 里面写了 return，finally 也会在 return 之前执行
# 哪怕程序出错了，finally 也会执行
#
# 这就是 finally 的“最后保障”作用


#  异常处理的执行流程 
#
# 正确情况：
# try → 全部顺利跑完 → else → finally → 结束
#
# 出错情况：
# try → 某行报错 → 跳到 except → 执行 except → finally → 结束
#
# 不管哪种情况，finally 都会跑


#  实战：文件读取 
# 这个是你之前写飞机档案程序的时候用到的
# 你要读 planes.txt，但这个文件可能不存在
# 不用 try 的话，文件不存在程序就直接崩了


def load_file():
    try:
        with open("planes.txt", "r", encoding="utf-8") as f:
            content = f.read()
            print("文件读取成功！内容：", content)

    except FileNotFoundError:
        print("文件不存在，我帮你创建一个空的")
        # 这里可以自动创建文件

    except Exception as e:
        print("出了其他错误：", e)

    else:
        print("读文件一切顺利")

    finally:
        print("本次文件读取尝试结束")


#  总结 
#
# try     ：放可能出错的代码
# except  ：放出错后要执行的代码（可以指定捕获哪种错误）
# else    ：放没出错时要执行的代码（可选）
# finally ：放不管出没出错最后都要执行的代码（可选）
#
# 你的代码不一定四个块都要写
# 但 try 和 except 是最基础的
# 只要会写 try-except，就能应付绝大多数情况了


# ============================================================
# 附录：常见报错类型（异常）大全
# 这些是你写代码最常遇到的报错
# ============================================================


#  1. SyntaxError（语法错误） 
# 这个是最常见的！就是你代码写错了格式
# 比如：if 后面忘了写冒号，括号没关，引号没配对
#
# 例子：
# if a == 1    ← 这里少了冒号
#     print(a)
# 报错：SyntaxError: expected ':'
#
# 这种错误 try 捕获不到，因为代码还没开始跑就已经错了


#  2. NameError（名字错误） 
# 你用的变量名没有定义过
# 比如你写了 print(a)，但前面没有 a = 1
#
# 例子：
# print(x)
# 报错：NameError: name 'x' is not defined


#  3. TypeError（类型错误） 
# 不同类型的值做了不该做的操作
# 比如：字符串和数字相加，或者在数字上调用方法
#
# 例子：
# "1" + 1
# 报错：TypeError: can only concatenate str (not "int") to str
#
# 例子：
# a = 123
# a.append(1)
# 报错：TypeError: 'int' object is not subscriptable


#  4. ValueError（值错误） 
# 值本身是对的，但不适合用在这里
# 比如：int("abc")，abc 是个字符串，但转不成数字
#
# 例子：
# int("abc")
# 报错：ValueError: invalid literal for int() with base 10: 'abc'


#  5. IndexError（索引错误） 
# 从列表或字符串里取一个不存在的下标
# 比如列表有3个元素，你取了第10个
#
# 例子：
# a = [1, 2, 3]
# print(a[10])
# 报错：IndexError: list index out of range


#  6. KeyError（键错误） 
# 从字典里取一个不存在的键
#
# 例子：
# d = {"name": "张三"}
# print(d["age"])
# 报错：KeyError: 'age'


#  7. AttributeError（属性错误） 
# 对象没有这个属性或方法
# 比如：你写 a.append(1)，但 a 是数字不是列表
#
# 例子：
# a = 123
# a.append(1)
# 报错：AttributeError: 'int' object has no attribute 'append'


#  8. FileNotFoundError（文件找不到） 
# 你要打开的文件不存在
#
# 例子：
# open("不存在的文件.txt", "r")
# 报错：FileNotFoundError: [Errno 2] No such file or directory: '不存在的文件.txt'


#  9. ZeroDivisionError（除以零） 
# 你做了除以0的运算
#
# 例子：
# a = 10 / 0
# 报错：ZeroDivisionError: division by zero


#  10. ImportError（导入错误） 
# import 一个不存在的模块
#
# 例子：
# import 不存在模块
# 报错：ModuleNotFoundError: No module named '不存在模块'


#  11. IndentationError（缩进错误） 
# 缩进不对
# Python 用缩进来区分代码块，缩进不对就会报错
#
# 例子：
# if a == 1:
# print(a)    ← 这里应该缩进，但没有
# 报错：IndentationError: expected an indented block


#  12. StopIteration（迭代停止） 
# 迭代器已经迭代完了，你又去取下一个
# 这个你用到迭代器的时候才需要关心，一般用 for 循环不会遇到


#  你怎么记这些报错？ 
#
# 不用背！因为：
# 1. 你遇到一次就记住了（报错信息会告诉你是什么类型）
# 2. 报错信息最下面一行会写清楚是什么类型
# 3. 你看一眼就知道是 SyntaxError 还是 TypeError
# 4. 你只需要知道“前面那个单词”就是你捕获的时候要写的
#
# 比如：
# except ValueError:     # 捕获值错误
# except TypeError:      # 捕获类型错误
# except Exception:      # 捕获所有错误（不推荐，但新手可以用）
# except Exception as e: # 捕获所有错误，并把错误信息存到 e 里


#  实战：捕获特定错误 

try:
    a = int(input("输入一个数字："))
    b = 10 / a
    print("结果是：", b)

except ValueError:
    print("你输入的不是数字！")

except ZeroDivisionError:
    print("不能除以0！")

except Exception as e:
    print("发生了其他错误：", e)

else:
    print("计算完成！")

finally:
    print("程序运行结束")

#
# 输入 abc → ValueError → 输出“你输入的不是数字！”
# 输入 0   → ZeroDivisionError → 输出“不能除以0！”
# 输入 5   → 一切正常 → 输出“结果是：2.0” → 输出“计算完成！”
# 不管怎样 → finally 都会输出“程序运行结束”
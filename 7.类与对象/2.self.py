# 你肯定发现了：每个函数里面都有 self
# 这一章专门讲：self 到底是啥？为什么必须写？


# 先写一个不在类里面的普通函数
def add(a, b):
    return a + b

print(add(3, 5))   # 输出 8，正常，没毛病


# 然后把这个函数搬进类里面
class Calc:
    def add(a, b):
        return a + b

# 调用一下
print(Calc.add(3, 5))

# 报错了！！！
# TypeError: add() takes 2 positional arguments but 3 were given
# 翻译：你这个 add 只能接收 2 个参数，但我塞了 3 个进来
# 为什么？？？
# 我在类外面的时候，传两个参数就是两个参数
# 怎么搬到类里面，就变成三个了？
#
# 因为：当你通过类名调用方法的时候
# Python 会悄悄把“类本身”作为第一个参数塞进去
# 所以实际传进去的是：(Calc, 3, 5)
# 3 个参数，但你的 add 只写了 (a, b) 两个位置
# 第三个参数没人接 → 报错


# 那怎么解决？
# 在第一个位置加一个参数，用来接住那个被塞进来的东西
class Calc:
    def add(self, a, b):   # 第一个位置留给被塞进来的东西
        return a + b

# 调用的时候
print(Calc.add(3, 5))   # 注意：这里依然只传了 3 和 5
                        # Python 会把 Calc 塞给 self
                        # 3 塞给 a，5 塞给 b
                        # 成功！

# 但如果我用对象调呢？
c = Calc()
print(c.add(3, 5))      # Python 把 c 塞给 self，一样能跑


# 那 self 这个名字能不能改成别的？
class Calc:
    def add(this, a, b):   # 改成 this
        return a + b

print(Calc.add(3, 5))   # 依然能跑！

# 为什么能改？因为 self 只是个名字
# 第一个参数的位置才是关键！
# 不管叫 self、this、me、A，它都是用来接“被塞进来的那个东西”的


# 好了，前面讲的是“通过类名调用”
# 那如果我先造个对象，再用对象调呢？
class Test:
    def show(a):         # 没写 self，只有一个参数 a
        print(a)
t = Test()
t.show(10)
# 报错！！！
# TypeError: show() takes 1 positional argument but 2 were given
# 同样的问题：Python 会把 t 塞进去，你的 show 只有 a 一个位置
# 塞了两个进来 → 报错


# 总结一下 self 的规矩：
#
# 1. 在 class 里面的普通方法，Python 会强制塞一个东西进来
#    这个东西就是：要么是对象本身，要么是类本身
#
# 2. 你必须留第一个参数位置来接住它
#    这个位置叫什么名字不重要（self/this/me/A 都行）
#    但位置必须留着，不能空
#
# 3. 如果你不写 self（只写 a, b），就会报错
#    因为 Python 塞了东西进来，但你没地方接


# 那问题来了：
# 如果我真的不需要这个被塞进来的东西，怎么办？
# 比如我就是做个加法，根本不需要对象本身的数据
#
# 解决办法：用 @staticmethod
class Calc:
    @staticmethod
    def add(a, b):      # 不用写 self 了！
        return a + b

print(Calc.add(3, 5))   # 输出 8，正常


# @staticmethod 干了什么？
# 它告诉 Python：“这个函数不需要那个被塞进来的东西，别塞”
# 所以 add 就只收到 3 和 5，两个参数，完美运行


# 再对比一下三种情况：

# 情况一：在类外面定义普通函数
def add(a, b):
    return a + b
# → 不塞任何东西，传几个就是几个


# 情况二：在类里面定义普通方法（没贴 @staticmethod）
class Calc:
    def add(self, a, b):   # 必须写 self
        return a + b
# → Python 会强塞东西进来，必须用 self 接住


# 情况三：在类里面定义静态方法（贴了 @staticmethod）
class Calc:
    @staticmethod
    def add(a, b):         # 不写 self
        return a + b
# → Python 不塞东西，干净利落


#  这一章总结 
# 1. self 不是 Python 故意恶心你的
#    是因为 Python 会悄悄往方法里塞东西
#    self 就是用来接住那个东西的
#
# 2. self 这个名字可以随便改
#    但第一个参数的位置必须留着
#
# 3. 如果你不想接那个东西
#    就用 @staticmethod 告诉 Python “别塞了”
# 你一定又要问了 这个@xxx是个什么东西
# 看就完了

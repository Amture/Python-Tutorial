# class 就是一张模具/图纸
# 你拿着这张图纸，就能造出一个个具体的东西

class Robot:

    def __init__(self, name):
        self.name = name
        self.power = 100

    def work(self):
        self.power -= 10
        print(f"{self.name} power : {self.power}%")

cleaner = Robot("aa")
cleaner.work()

# 这里会输出什么呢？
# 输出的是：aa power : 90%
# 一行行看
# 我们定义一个函数为__init__参数有self name
# 然后定义其他的下属参数，这个power也可以随便写，不一定非要写power，这里显示的是电量
# 然后下面这里的work的def定义这个robot有哪些东西可以使用

# 这里你应该要发问了
# __init__是写死的吗？
# self必须写吗？
# 1.__init__不一定要写，看情况，具体情况看第九个文件夹
# 2.self必须写，或者也可以不写，请先往下看




# 这次造个能接收两个参数的
class Amturester:

    def __init__(self, Am1, Am2):
    # __init__ 是写死的，不用管，照抄就行
    # 这里有两个参数：Am1 和 Am2
    # 你创建对象的时候传几个，这里就接几个
        self.Am1 = Am1
        self.Am2 = Am2
        self.power = 100
        # self 是造出来的那个具体东西本身
        # 后面的 Am1 和 Am2 才是你真正传进来的数据

    def Amture(self):
        self.power -= 1
        print(f"{self.Am1} power : {self.power}%")
        print(f"{self.Am2} power : {self.power}%")


x = Amturester('001', '002')
x.Amture()
# 造东西：传两个参数进去
# '001' 会被传给 Am1，'002' 会被传给 Am2



# 输出什么？
# 001 power : 99%
# 002 power : 99%

# 这里你可能会问：
# 如果我只传一个参数呢？
# 会报错，因为 __init__ 要两个，你只给一个
# Python 会告诉你：missing 1 required positional argument
# 意思是有一个参数的位置没有塞东西

# 如果传三个呢？
# 也会报错，因为你多给了
# Python 会告诉你：takes 2 positional arguments but 3 were given

# 所以：__init__ 有几个参数，你造对象的时候就得传几个
# 多一个少一个都不行
# 对def有不理解的往回看，看定义函数那里
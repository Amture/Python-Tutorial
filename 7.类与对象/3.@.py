# 上一章说完了 self，你知道了：
# Python 会强行往类里面的方法塞东西
# 你必须写 self 来接住

# 这一章讲：那我就不想接，怎么办？
# 用 @staticmethod


#  先看老问题 

class Calc:
    def add(a, b):        # 没写 self，没位置接
        return a + b

# Calc.add(3, 5)
# 报错：add() takes 2 positional arguments but 3 were given
# Python 强行塞了 Calc 进去，你没地方接


#  用 @staticmethod 解决 

class Calc:
    @staticmethod         # 贴了这个标签
    def add(a, b):        # 不用写 self 了！
        return a + b

print(Calc.add(3, 5))     # 输出 8

# @staticmethod 是啥意思？
# 它告诉 Python：“这个函数不需要对象，别塞东西进来”
# 就这么简单


#  那 @ 到底是啥？ 

# @ 是一个“标记”
# 你把它贴在函数头上，它就会改变这个函数的行为
#
# 具体来说：
# @ 后面的东西是一个“工具”
# Python 会把下面这个函数丢进这个工具里处理
# 然后把处理后的结果重新赋值给这个函数名

# 你写的是：
# @staticmethod
# def add(a, b):
#     return a + b

# Python 实际做的是：
# def add(a, b):
#     return a + b
# add = staticmethod(add)

# 看懂了吗？
# @staticmethod 就是：
# 1. 先正常定义这个函数
# 2. 把这个函数丢给 staticmethod 这个工具处理
# 3. 把处理后的结果重新赋值给 add

#  @ 可以用在什么地方？ 
# 最常见的有两种：
# 1. @staticmethod   → 告诉 Python：“不要塞对象进来”
# 2. @classmethod    → 告诉 Python：“不要塞对象，但要塞类本身”

# 对比三种方法
class Demo:
    # 1. 普通方法：需要 self，Python 会塞对象
    def normal(self, x):
        return x + 1

    # 2. 静态方法：不需要 self，Python 不塞东西
    @staticmethod
    def static_add(x, y):
        return x + y

    # 3. 类方法：需要 cls，Python 塞类本身
    @classmethod
    def class_info(cls):
        print(f"我是 {cls.__name__} 类")


# 测试一下
d = Demo()

print(d.normal(5))           # 6，正常
print(Demo.static_add(3, 4)) # 7，直接用类名调
print(d.static_add(3, 4))    # 7，用对象调也行，但不会塞 d

Demo.class_info()            # 输出：我是 Demo 类
d.class_info()               # 输出：我是 Demo 类（用对象调，塞的也是类）


#  @staticmethod 和 __init__ 有关系吗？ 

# 没有！！！完全没有！！！
# __init__ 管的是“创建对象时怎么存数据”
# @staticmethod 管的是“调用方法时塞不塞东西”

# 它们是两条平行线，谁也不影响谁

class Robot:
    def __init__(self, name):      # 存数据，必须写 self
        self.name = name

    @staticmethod
    def version():                 # 不需要数据，不写 self
        return "v1.0"

# __init__ 要 self，因为要往对象里存 name
# version 不要 self，因为只是返回一个版本号
# 各管各的，互不影响

#  那 @staticmethod 从哪来的？ 

# staticmethod 是 Python 自带的“内置工具”
# 跟 print()、len()、int() 一样，不需要 import
# 直接就能用

# 你还可以验证：
# import builtins
# print(dir(builtins))  # 里面就有 'staticmethod'


#  这一章总结 

# 1. @ 是一个标记，贴在函数头上
#    它告诉 Python：“下面这个函数，用 @ 后面的工具处理一下”

# 2. @staticmethod 是最常见的用法
#    意思是：“不要往这个函数里塞对象”

# 3. @ 的本质是“赋值替换”
#    @xxx def f(): pass
#    等价于：def f(): pass; f = xxx(f)

# 4. @staticmethod 和 __init__ 没有关系
#    __init__ 管创建，@staticmethod 管调用

# 5. @staticmethod 是 Python 自带的
#    不需要 import
# 那么就剩下最后一个问题了
# 那 Python 自带的装饰器（@xxx）有哪些？



# 装饰器名	             来自哪里	  作用
# @staticmethod	        内置	     告诉解释器：这个方法不需要对象
# @classmethod	        内置	     告诉解释器：这个方法需要的是类本身
# @property	            内置	     把方法变成属性访问（obj.name 而不是 obj.name()）
# @abstractmethod	    abc 模块	 声明这个方法是抽象的，子类必须重写

# @functools.wraps	    functools    保留被装饰函数的原名和文档
# @dataclass	        dataclasses	 自动生成 __init__、__repr__ 等
# @contextmanager	    contextlib   把函数变成 with 上下文管理器
# @asyncio.coroutine	asyncio	     声明这是一个协程（Python 3.4 旧写法）
# @lru_cache	        functools	 缓存函数返回值
# @total_ordering	    functools	 只要定义 __eq__ 和一个比较方法，自动补全其他比较
# @singledispatch	    functools	 单分派泛型函数（根据第一个参数类型走不同分支）

# 常用的其实就前四个：@staticmethod、@classmethod、@property、@abstractmethod。
# 详细的你可以查一下资料，比如菜鸟之类的
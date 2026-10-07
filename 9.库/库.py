# 这里我们说一下什么叫库
# 通常情况下可以直接地理解为工具箱
# 这个工具箱分为两种，一个是标准库，即为官方py自带的。另一种为三方库，顾名思义，即为第三方也就是社区开发者制作的
import random
# 这里的random就是一个库，这个是标准库，就是py自带的
# 这一章也可以说讲的是import
import random as ra
# 这个意思是导入random库更名为ra，也就是说后面使用的时候不需要写random，直接写成ra就ok
from random import randint
# 这个意思是从random只取出randint这个工具，当然，我们也可以
from random import randint as rai
# 对，我们也可以给这个工具更名
# 然后我们就说怎么用了
# 通常情况下，我们都是<库名+工具名>
# 比如这样：
print(random.randint(1, 10))
# 这里 random 是库名，randint 是工具名，中间用点连起来
# 意思是：从 random 这个工具箱里，拿出 randint 这个工具来用

# 但是，如果你用了 from random import randint
# 就不用写库名了，直接写工具名：
print(randint(1, 10))
# 因为 randint 已经被你单独拿出来了，不用再通过工具箱拿

# 如果你用了 import random as ra
# 那就写别名：
print(ra.randint(1, 10))
# ra 就是 random 的别名，效果一模一样

# 如果你用了 from random import randint as rai
# 那就写工具别名：
print(rai(1, 10))
# rai 就是 randint 的别名，效果也一模一样


# 最后提醒一句：
# 同一个文件里，别重复导入同一个库
# 比如你上面同时写了 import random 和 import random as ra
# 演示可以，实际写代码选一种就行
# 不然你自己都会乱：到底是用 random 还是 ra？


# 提一嘴，我们这里的random是py标准库里面的随机数生成/使用

# 这篇是py的正式起点，因为标准库+三方库 ≈ ∞
# 也就是说，如果你试图去探寻py的极限，那么你将研究到死都研究不完

# 所以，别想着学完。
# 你只需要学会“怎么查、怎么用”，而不是“背下来”。
# 以后你写代码，大部分时间是在查文档、搜报错、看别人怎么用。
# 会用一些常用的就够了，剩下的用到再查。
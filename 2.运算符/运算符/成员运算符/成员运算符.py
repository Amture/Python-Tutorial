
# 这个文件讲的是 in 和 not in


# 先造一个列表
a = [1, 2, 3]
# in：看看某个东西在不在列表里面
if 2 in a:
    print('True_2')
else:
    print('False')
# 2 在不在 a 里面？在。所以输出 True_2

if 4 in a:
    print('True')
else:
    print('False_4')
# 4 在不在 a 里面？不在。所以输出 False_4

# not in：看看某个东西是不是不在列表里面
if 2 not in a:
    print('False')
else:
    print('True_2')
# 2 不在 a 里面？不是啊，2 在的。所以走 else，输出 True_2

if 4 not in a:
    print('False_4')
else:
    print('True')
# 4 不在 a 里面？真的不在。所以输出 False_4

#  总结 
# in：在不在里面？
# not in：不在里面？
#
# 说白了就是两个问题：
# 1. 这个元素存不存在？
# 2. 这个元素是不是不存在？（绕口，但就是反着问）
#
# 这玩意儿叫“成员运算符”，意思就是：某个东西是不是这个组里的成员
# 组可以是列表、元组、字符串、字典、变量等等

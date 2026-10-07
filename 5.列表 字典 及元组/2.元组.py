# 这次说的是元组
a = (1,2,3,4,5)
# 注意哈，元组唯一能做的只有调用和遍历
# 也就是说，元组就是只读版本的列表
# 看一下修改测试
a = (1, 2, 3, 4, 5)

print("===== 元组只读测试 =====")


try:
    a[1] = 99
except TypeError as e:
    print(f"{e}")


try:
    a.append(6)
except AttributeError as e:
    print(f"{e}")


try:
    a.pop(1)
except AttributeError as e:
    print(f"{e}")


try:
    del a[1]
except TypeError as e:
    print(f"{e}")
print(a)
# 运行一下看报错去吧
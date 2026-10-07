
#  for 循环 
# 把东西一个一个拿出来
for i in range(1, 10):
    print(i)
# range(1,10) 生成了 1 到 9
# i 依次等于 1 2 3 4 5 6 7 8 9
# 注意：10 不包含，到 10 就停了
x = 'Finally'
for xx in x:
    print(xx)

# 字符串也能拆开遍历
# 把 'Finally' 拆成一个一个字符
# 依次输出 F i n a l l y

#  while 循环 
# 条件成立就一直跑

while True:
    a = None
    a = int(input('a'))
    if a == 1:
        break
    else:
        print('重新')

# while True 是死循环，条件永远成立
# 所以必须用 break 跳出去
# 这里用户输入 1 就 break，否则一直问


while a == 1:
    print('1')
    a = int(input("a="))
    break

# 这个 while 判断 a 是不是 1
# 是 1 就进去，打印 1，然后改 a 的值，break 跳出
# 注意：如果 a 不是 1，这个循环压根不执行


#  循环里能用的“跳转” 

# break：强行结束整个循环
for i in range(1, 10):
    if i == 5:
        break
    print(i)
# 输出 1 2 3 4，到 5 就停了


# continue：跳过这一次，继续下一次
for i in range(1, 10):
    if i == 5:
        continue
    print(i)
# 输出 1 2 3 4 6 7 8 9，  5 被跳过了

import time


# print()函数的.center()方法
# 将print()函数内部数据居中，用30个"="字符填充
print("你好".center(30, "="))
print("")

# print()函数的.format()方法
# {}内部先用":"引导,"-"填充,"^"代表居中,"16"为带非填充部分共16个字符
print("{:-^16}".format("执行开始"))
# 获取程序开始执行的时间
start_time = time.perf_counter()

# 问题规模
scales = 10
for i in range(0, 11):
    # 进度条的数值部分
    process = i * 10
    # 进度条的未经过部分
    j = scales - i
    # ,end=""为取消print()函数的自动换行，\r为将光标定位至本行行首
    print("\r{:^3}%[{}->{}]".format(process, i * "*", j * "-"), end="")
    time.sleep(1)

print("")
# 获取程序结束执行的时间
end_time = time.perf_counter()
print("本次进度条加载了{}秒！".format(end_time - start_time))
print("{:-^16}".format("执行结束"))

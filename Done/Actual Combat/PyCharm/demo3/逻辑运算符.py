## 逻辑运算符

# and : 左右表达式都为True，整个表达式结果才为 True
if (1 == 1) and (10 > 3):
    print("条件成立！")

# or : 左右表达式有一个为True，整个表达式结果就为 True
if (1 == 2) or (10 > 3):
    print("条件成立！")

# not：将右边表达式的结果取反，Ture变为False，False变为True
if not (1 == 2):
    print("条件成立！")
# -*- coding: utf-8 -*-
"""构建 EXP01 实验 Notebook：20244080115_胡勇彦_exp01.ipynb"""
import nbformat as nbf
from nbformat.v4 import new_notebook, new_markdown_cell, new_code_cell

cells = []

def md(text):
    cells.append(new_markdown_cell(text))

def code(text):
    cells.append(new_code_cell(text))

# ============ 标题 ============
md("""# 实验报告01：Python基础与数据处理入门

- 学号：20244080115
- 姓名：胡勇彦""")

# ============ 1.1 身份与环境记录 ============
md("## 一、实验环境与提交要求\n\n### 1.1 第一个代码框：身份与环境记录")
code("""import os, uuid, hashlib, platform, getpass

# ===== 1. 填写学号 =====
STUDENT_ID = 20244080115  # 修改为自己的学号

# ===== 2. 打印 conda 环境 =====
CONDA_ENV = os.environ.get("CONDA_DEFAULT_ENV", "base")
print(f"[Conda 环境] {CONDA_ENV}")

# ===== 3. 机器指纹（绑定当前电脑）======
MACHINE_FP = hashlib.sha256(
    f"{platform.node()} | {platform.machine()} | {platform.system()} | {uuid.getnode()}".encode()
).hexdigest()[:16]

# ===== 4. 生成唯一 ID =====
RUN_ID = f"{STUDENT_ID}-{MACHINE_FP}"
print(f"[学号] {STUDENT_ID}")
print(f"[机器指纹] {MACHINE_FP}")
print(f"[RUN_ID] {RUN_ID}")""")

# ================= 实验1 =================
md("""## 二、实验内容与过程

## 实验1：基本运算、数据类型与字符串

### 任务1：算术运算符 `/`、`//`、`%`、`**`""")
code("""r1 = 8 / 3    # 除法：结果为浮点数
r2 = 8 // 3   # 整除（地板除）：向下取整的商
r3 = 8 % 3    # 取模（取余）：除法的余数
r4 = 2 ** 7   # 幂运算：2 的 7 次方

for name, value in [("8 / 3", r1), ("8 // 3", r2), ("8 % 3", r3), ("2 ** 7", r4)]:
    print(f"{name:>7} = {value:<8} 类型为 {type(value).__name__}")

print('''
运算符含义：
/  普通除法，无论是否整除，结果一律为 float
// 整除（地板除），得到商向下取整的整数部分
%  取模（求余数），得到不能整除时剩下的部分
** 幂（乘方）运算，a ** b 表示 a 的 b 次方
''')""")

md("### 任务2：四种基本数据类型与 type()")
code("""my_int = 20244080115      # 整数 int
my_float = 3.14           # 浮点数 float
my_str = "胡勇彦"          # 字符串 str
my_bool = True            # 布尔值 bool

for var in (my_int, my_float, my_str, my_bool):
    print(f"值 {var!r:<14} 的类型是 {type(var).__name__}")""")

md("### 任务3：类型转换与异常捕获")
code("""print("int(\\"123\\") =", int("123"), "  —— 数字字符串可直接转为整数")
print("float(\\"3.14\\") =", float("3.14"), "  —— 数字字符串转为浮点数")
print("int(3.9) =", int(3.9), "  —— 浮点数转整数直接截断小数部分（向零取整），不是四舍五入")

print()
try:
    int("goat")
except ValueError as e:
    print(f"int(\\"goat\\") 抛出 ValueError: {e}")
    print("原因：int() 只能转换内容为合法整数的字符串，'goat' 不含数字，无法解析为整数。")""")

md("### 任务4：字符串常用处理（去空白、大小写、切片、拆分、连接）")
code("""s = " Python Data Analysis "

s_stripped = s.strip()                       # 去除首尾空白
print("strip 后:", repr(s_stripped))
print("全部大写:", s_stripped.upper())
print("全部小写:", s_stripped.lower())
print("首字母大写:", s_stripped.title())
print("切片前6个字符:", s_stripped[:6])
print("切片后8个字符:", s_stripped[-8:])
print("逆序切片:", s_stripped[::-1])

words = s_stripped.split()                   # 按空白拆分为单词列表
print("split 拆分:", words)

joined = "-".join(words)                     # 用 '-' 把单词连接起来
print("'-'.join 连接:", joined)
print("' '.join 还原:", " ".join(words))""")

md("### 任务5：字符串拼接、重复与不可变性")
code("""a, b = "Python", "数据分析"
print("拼接 (+):", a + " " + b)
print("重复 (*):", a * 3)

# 字符串是不可变对象，不能直接修改其中某个字符
try:
    a[0] = "J"
except TypeError as e:
    print(f"直接修改字符抛出 TypeError: {e}")

# 正确做法：利用切片/拼接构造一个新字符串
new_a = "J" + a[1:]
print("构造新字符串的方式:", new_a, "（原字符串保持不变:", a, ")")""")

# ================= 实验2 =================
md("""## 实验2：函数、条件、循环与递归

### 任务1：score_level(score) 成绩等级函数""")
code("""def score_level(score):
    if not (0 <= score <= 100):
        raise ValueError(f"成绩 {score} 超出 0~100 的合法范围")
    if score >= 90:
        return "优秀"
    if score >= 80:
        return "良好"
    if score >= 60:
        return "及格"
    return "不及格"

for s in (95, 85, 70, 59, 0, 100):
    print(f"{s:>3} 分 -> {score_level(s)}")

try:
    score_level(101)
except ValueError as e:
    print("非法输入测试:", e)""")

md("### 任务2：for 与 while 分别计算 1~100 整数和")
code("""sum_for = 0
for i in range(1, 101):
    sum_for += i

sum_while = 0
i = 1
while i <= 100:
    sum_while += i
    i += 1

print("for   循环结果:", sum_for)
print("while 循环结果:", sum_while)
print("两种实现结果一致:", sum_for == sum_while, "（公式校验 n(n+1)/2 =", 100 * 101 // 2, ")")""")

md("### 任务3：递归版与迭代版阶乘（约定 0! = 1）")
code("""def factorial_rec(n):
    if n < 0:
        raise ValueError("阶乘只接受非负整数")
    if n <= 1:          # 0! = 1, 1! = 1（递归终止条件）
        return 1
    return n * factorial_rec(n - 1)

def factorial_iter(n):
    if n < 0:
        raise ValueError("阶乘只接受非负整数")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(f"{'n':>3} | {'递归版':>10} | {'迭代版':>10} | 是否一致")
print("-" * 42)
for n in (0, 1, 5, 10):
    fr, fi = factorial_rec(n), factorial_iter(n)
    print(f"{n:>3} | {fr:>10} | {fi:>10} | {fr == fi}")""")

md("### 任务4：summary(values) 返回 (最小值, 最大值, 平均值) 并解包")
code("""def summary(values):
    if not values:
        raise ValueError("输入列表不能为空")
    return min(values), max(values), sum(values) / len(values)

data = [85, 58, 92, 76, 60, 89]
low, high, avg = summary(data)      # 元组解包
result = summary(data)
print("返回的元组:", result, "，类型:", type(result).__name__)
print(f"最小值 {low}，最大值 {high}，平均值 {avg:.2f}")""")

md("### 任务5：sum_all(*args) 可变参数求和")
code("""def sum_all(*args):
    total = 0
    for x in args:
        total += x
    return total

print("无参数   :", sum_all())
print("单个参数 :", sum_all(42))
print("多个参数 :", sum_all(1, 2, 3, 4, 5))""")

# ================= 实验3 =================
md("""## 实验3：列表、字典、元组与基础统计

使用模拟成绩数据（非真实学生信息）。""")
code("""names = ["Alice", "Bob", "Carol", "David", "Eva", "Frank"]
scores = [85, 58, 92, 76, 60, 89]""")

md("### 任务1：zip() 构建字典并用 items() 遍历")
code("""score_dict = dict(zip(names, scores))
print("姓名到成绩的字典:", score_dict)
print()
for name, score in score_dict.items():
    print(f"{name:<6} : {score}")""")

md("### 任务2：enumerate() 输出序号（从 1 开始）")
code("""for idx, (name, score) in enumerate(zip(names, scores), start=1):
    print(f"第 {idx} 名：{name:<6} 成绩 {score}")""")

md("### 任务3：列表推导式——及格名单与成绩平方")
code("""passed_names = [name for name, score in zip(names, scores) if score >= 60]
squared_scores = [s ** 2 for s in scores]
print("及格学生姓名:", passed_names)
print("成绩平方列表:", squared_scores)""")

md("### 任务4：基础统计与字符串格式化")
code("""count = len(scores)
mean_score = sum(scores) / count
highest = max(scores)
lowest = min(scores)
pass_rate = sum(1 for s in scores if s >= 60) / count

print(f"人数       : {count}")
print(f"平均分     : {mean_score:.2f}")        # 两位小数
print(f"最高分     : {highest}")
print(f"最低分     : {lowest}")
print(f"及格率     : {pass_rate:.1%}")          # 百分数
print("另一种百分数写法: {:.2f}%".format(pass_rate * 100))""")

md("### 任务5：别名 alias 与 copy() 副本的区别（使用独立演示列表）")
code("""demo = [1, 2, 3]
alias = demo          # 别名：与原列表指向同一个对象
copied = demo.copy()  # 浅拷贝：生成一个新的列表对象

alias[0] = 99
print("修改 alias[0] 后：")
print("原列表 demo :", demo, "  <- 被连带修改（别名指向同一对象）")
print("副本 copied  :", copied, "  <- 不受影响（独立的新对象）")
print("demo is alias :", demo is alias, "| demo is copied :", demo is copied)""")

md("### 任务6：元组不可变 与 zip() 对不等长序列的处理")
code("""record = ("Alice", 85, "女")        # 用元组保存一条学生记录
print("学生记录元组:", record)
try:
    record[1] = 90
except TypeError as e:
    print("元组重新赋值抛出 TypeError:", e)

a = [1, 2, 3]
b = ["x", "y"]
print("不等长序列 zip 结果:", list(zip(a, b)), "  <- zip 在最短序列结束时停止，多出的元素被忽略")""")

# ================= 实验4 =================
md("""## 实验4：文件读写、异常处理与模块

### 任务1：查看工作目录、构造路径并创建 exp01_data 目录""")
code("""import os

cwd = os.getcwd()
print("当前工作目录:", cwd)

data_dir = os.path.join(cwd, "exp01_data")
data_file = os.path.join(data_dir, "students.txt")
os.makedirs(data_dir, exist_ok=True)
print("数据目录:", data_dir)
print("数据文件路径:", data_file)""")

md("### 任务2：写入 students.txt 并读取解析（跳过表头）")
code("""content = '''name,score
Alice,85
Bob,58
Carol,92
David,76
Eva,60
Frank,89
Grace,abc
Henry,105
Incomplete
'''

with open(data_file, "w", encoding="utf-8") as f:
    f.write(content)

with open(data_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

print("跳过表头，逐行解析原始字段：")
for line in lines[1:]:
    fields = line.strip().split(",")
    print("原始字段:", fields)""")

md("### 任务3：parse_student(line) 校验函数")
code("""def parse_student(line):
    fields = line.strip().split(",")
    if len(fields) != 2:
        raise ValueError(f"字段数量错误，应为 2 个，实际 {len(fields)} 个: {line.strip()!r}")

    name, score_text = fields[0].strip(), fields[1].strip()
    if not name:
        raise ValueError("姓名不能为空")

    try:
        score = int(score_text)
    except ValueError:
        raise ValueError(f"成绩无法转换为整数: {score_text!r}")

    if not (0 <= score <= 100):
        raise ValueError(f"成绩 {score} 超出 0~100 范围")

    return {"name": name, "score": score}""")

md("### 任务4：按行处理、捕获异常、记录行号与原因")
code("""valid_records = []
invalid_records = []

with open(data_file, "r", encoding="utf-8") as f:
    file_lines = f.readlines()

for line_no, line in enumerate(file_lines[1:], start=2):   # 数据从第 2 行开始
    if not line.strip():
        continue
    try:
        valid_records.append(parse_student(line))
    except ValueError as e:
        invalid_records.append((line_no, str(e)))
        print(f"[第 {line_no} 行] 无效记录，已跳过 -> {e}")

print()
print("有效记录:", valid_records)
print("无效记录数:", len(invalid_records))""")

md("### 任务5：生成 report.txt，演示 w 与 a 模式")
code("""report_path = os.path.join(data_dir, "report.txt")

valid_count = len(valid_records)
invalid_count = len(invalid_records)
report_mean = sum(r["score"] for r in valid_records) / valid_count
report_pass_rate = sum(1 for r in valid_records if r["score"] >= 60) / valid_count

report_body = (
    f"有效记录数: {valid_count}\\n"
    f"无效记录数: {invalid_count}\\n"
    f"平均分: {report_mean:.2f}\\n"
    f"及格率: {report_pass_rate:.1%}\\n"
)

# w 模式：打开时清空原文件，重新写入（覆盖已有内容）
with open(report_path, "w", encoding="utf-8") as f:
    f.write(report_body)

# a 模式：在文件末尾追加，不清空原有内容
with open(report_path, "a", encoding="utf-8") as f:
    f.write("（本行由 a 追加模式写入）\\n")

with open(report_path, "r", encoding="utf-8") as f:
    print(f.read())""")

md("### 任务6：pickle 序列化保存与读取验证")
code("""import pickle

pkl_path = os.path.join(data_dir, "students.pkl")
with open(pkl_path, "wb") as f:
    pickle.dump(valid_records, f)

with open(pkl_path, "rb") as f:
    restored = pickle.load(f)

print("pickle 恢复的数据:", restored)
print("恢复数据与原数据相等:", restored == valid_records)""")

md("### 任务7：将 parse_student 保存为 student_utils.py 模块并 import 调用")
code("""module_path = os.path.join(cwd, "student_utils.py")
module_code = '''def parse_student(line):
    fields = line.strip().split(",")
    if len(fields) != 2:
        raise ValueError(f"字段数量错误，应为 2 个，实际 {len(fields)} 个")
    name, score_text = fields[0].strip(), fields[1].strip()
    if not name:
        raise ValueError("姓名不能为空")
    try:
        score = int(score_text)
    except ValueError:
        raise ValueError(f"成绩无法转换为整数: {score_text!r}")
    if not (0 <= score <= 100):
        raise ValueError(f"成绩 {score} 超出 0~100 范围")
    return {"name": name, "score": score}
'''
with open(module_path, "w", encoding="utf-8") as f:
    f.write(module_code)
print("模块文件已写入:", module_path)""")

code("""import student_utils

print("有效输入测试:", student_utils.parse_student("Alice,85"))
try:
    student_utils.parse_student("Henry,105")
except ValueError as e:
    print("无效输入测试 -> ValueError:", e)""")

md("### 任务8：读取不存在的文件并捕获 FileNotFoundError")
code("""missing_path = os.path.join(data_dir, "this_file_does_not_exist.txt")
try:
    with open(missing_path, "r", encoding="utf-8") as f:
        f.read()
except FileNotFoundError as e:
    print(f"捕获到 FileNotFoundError: {e}")
    print("说明：该路径下没有此文件，open() 读取前不会自动创建，因此抛出文件不存在异常。")""")

# ================= 实验5 =================
md("""## 实验5：类、继承与对象复制

### 任务1：Student 类""")
code("""class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def is_passed(self):
        return self.score >= 60

    def __str__(self):
        status = "及格" if self.is_passed() else "不及格"
        return f"学生 {self.name}，成绩 {self.score}，{status}"

# 简单自测
print(Student("Alice", 85))
print(Student("Bob", 58))""")

md("### 任务2：为实验4每条有效记录创建 Student 对象")
code("""students = [Student(r["name"], r["score"]) for r in valid_records]
for stu in students:
    print(f"{stu}  | is_passed() -> {stu.is_passed()}")""")

md("### 任务3：GraduateStudent 子类（继承、super()、重写 __str__）")
code("""class GraduateStudent(Student):
    def __init__(self, name, score, research_topic):
        super().__init__(name, score)          # 调用父类初始化
        self.research_topic = research_topic   # 子类新增属性

    def __str__(self):
        status = "及格" if self.is_passed() else "不及格"
        return (f"研究生 {self.name}，成绩 {self.score}，{status}，"
                f"研究方向：{self.research_topic}")

grad = GraduateStudent("Alice", 92, "机器学习")
print(grad)""")

md("### 任务4：直接赋值、copy.copy()、copy.deepcopy() 的区别（每次从新对象开始）")
code("""import copy

def fresh_original():
    '''每次比较都从全新的原始对象开始。'''
    return {"name": "Alice", "scores": [85, 90]}

# 1) 直接赋值：只是别名，内部列表仍是同一个
o1 = fresh_original()
ref = o1
ref["scores"][0] = 100
print("直接赋值后 原始对象:", o1, "  <- 内部列表被连带修改")

# 2) copy.copy() 浅拷贝：外层是新对象，内部嵌套列表仍共享
o2 = fresh_original()
shallow = copy.copy(o2)
shallow["scores"][0] = 100
print("浅拷贝后 原始对象:", o2, "  <- 嵌套列表被连带修改（只拷贝了最外层）")
print("           浅拷贝的外层是新对象:", o2 is not shallow, "但内层列表共享:", o2["scores"] is shallow["scores"])

# 3) copy.deepcopy() 深拷贝：嵌套列表也完全独立
o3 = fresh_original()
deep = copy.deepcopy(o3)
deep["scores"][0] = 100
print("深拷贝后 原始对象:", o3, "  <- 完全不受影响")
print("           深拷贝的内层列表也独立:", o3["scores"] is not deep["scores"])""")

md("""## 三、实验小结

1. 掌握了 `/ // % **` 等运算符、四种基本类型、类型转换与字符串常用方法。
2. 掌握了函数定义、条件分支、for/while 循环、递归、元组解包与可变参数。
3. 掌握了列表/字典/元组、`zip()`、`enumerate()`、列表推导式与基础统计。
4. 掌握了文件读写、`with` 语句、异常捕获、pickle 序列化、自定义模块与目录操作。
5. 掌握了类与继承、`super()`、方法重写，以及浅拷贝与深拷贝的本质区别。""")

nb = new_notebook(cells=cells, metadata={
    "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
    "language_info": {"name": "python", "version": "3.12"}
})

out_path = r"C:\Users\胡勇彦\Doubao\chats\2026-10-20\new-chat\20244080115_胡勇彦_exp01.ipynb"
with open(out_path, "w", encoding="utf-8") as f:
    nbf.write(nb, f)
print("Notebook 已生成:", out_path)

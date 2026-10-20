# python-work（Python 课程作业）

- 学号：20244080115
- 姓名：胡勇彦

## 作业目录

| 目录/文件 | 内容 |
| --- | --- |
| `HW01/` | HW01：Data Types, Functions and Conditionals（数据类型、函数与条件语句） |
| `20244080115_胡勇彦_exp01.ipynb` 等 | EXP01：Python 基础与数据处理入门（独立 conda 环境 `exp01`，Python 3.12 + Jupyter） |

---

# 实验报告01：Python基础与数据处理入门

- 运行环境：独立 conda 虚拟环境 `exp01`（Python 3.12 + Jupyter）

## 文件说明

| 文件 | 说明 |
| --- | --- |
| `20244080115_胡勇彦_exp01.ipynb` | 实验主 Notebook，包含全部 5 个实验及运行输出 |
| `student_utils.py` | 实验4 任务7 生成的自定义模块（`parse_student`） |
| `exp01_data/students.txt` | 实验输入数据（含无效记录） |
| `exp01_data/report.txt` | 统计结果（有效/无效记录数、平均分、及格率） |
| `exp01_data/students.pkl` | 有效记录的 pickle 序列化文件 |
| `build_notebook.py` | 生成该 Notebook 的辅助脚本（可选查看） |

## 实验内容

1. 基本运算、数据类型与字符串
2. 函数、条件、循环与递归
3. 列表、字典、元组与基础统计
4. 文件读写、异常处理与模块
5. 类、继承与对象复制

## 复现方式

```bash
conda create -n exp01 python=3.12 jupyter nbconvert ipykernel -y
conda activate exp01
jupyter nbconvert --to notebook --execute --inplace 20244080115_胡勇彦_exp01.ipynb
```

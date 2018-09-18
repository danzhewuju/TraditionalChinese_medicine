#!usr/bin/python3
#主要是用于数据的第二次处理
import os
import re


def replace_bracket(str_test):        #将中括号进行替换
    stack = []
    stack_query = []
    if ("［" in str_test or "[" in str_test) and ("］" in str_test or "]" in str_test):
        stack.append(str_test)
    while stack.__len__() != 0:
        str_test = stack.pop()
        if ("［" in str_test or "[" in str_test) and ("］" in str_test or "]" in str_test):
            start = 0
            if "［" in str_test:
                start = str_test.index("［")                                       #对于不规则的括号的修改
            if "[" in str_test:
                start = str_test.index("[")
            end = 0
            if "］" in str_test:
                end = str_test.index("］")
            if "]" in str_test:
                end = str_test.index("]")
            replace_word = str_test[start + 1:end]
            # print(replace_word)
            step = end - start
            str_r1 = str_test[:start] + str_test[end + 1:]
            new_start = start - step + 1
            new_end = end - step
            str_r2 = str_r1[:new_start] + replace_word + str_r1[new_end:]
            if "［" in str_r1 or "[" in str_r1:      #用来判断是否还有中括号
                stack.append(str_r1)
            else:
                # print(str_r1)
                stack_query.append(str_r1)
            if "［" in str_r2 or "[" in str_r2:
                stack.append(str_r2)
            else:
                # print(str_r2)
                stack_query.append(str_r2)
        else:
            stack_query.append(str_test)                                      #部分的中括号是不规则的，因此这个部分暂时放弃处理
    return stack_query


def file_name(file_path):                                             #获取一个指定文件夹之下的所有的文件（在本例中是txt文件）
    paths = []
    for root, dirs, files in os.walk(file_path):
        # print(root)
        # print(dirs)
        # print(files)
        for x in files:
            path = root + "\\" + x
            # print(path)
            paths.append(path)
        # path = root + files
        # print("path:", path)
    return paths


def remove_curves(str_test):                              #去除圆括号
    str_tem = re.split(r"（.+）", str_test)
    str_line = "".join(str_tem)
    return str_line


def remove_bracket():     #主要的用途是中括号的处理 以及圆括号的处理
    paths = file_name("result")
    for p in paths:
        new_path = p[:-4] + "_second" + p[-4:]
        f = open(p, "r", encoding="UTF-8")
        print(p)
        data = f.readlines()
        f.close()
        f = open(new_path, "w", encoding="UTF-8")
        for line in data:
            write_line = line
            if "［" in write_line and "］" in write_line:
                line_query = replace_bracket(write_line)
                for w in line_query:
                    f.write(remove_curves(w))
            else:
                f.write(remove_curves(write_line))
        f.close()
    return True


remove_bracket()

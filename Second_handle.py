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
            path = root + "\\" + x                               #上级目录
            # print(path)
            paths.append(path)                                   #全部路径
        # path = root + files
        # print("path:", path)
    return paths


def remove_curves(str_test):                              #去除圆括号
    str_tem = re.split(r"（.+）", str_test)
    str_line = "".join(str_tem)
    return str_line


def remove_bracket():                                        #主要的用途是中括号的处理 以及圆括号的处理
    paths = file_name("result")
    for p in paths:
        if "first" in p:
            str_t = p.split("_first")
            str_p = "".join(str_t)
            new_path = str_p[:-4] + "_second" + str_p[-4:]
            f = open(p, "r", encoding="UTF-8")
            print(p)
            data = f.readlines()
            f.close()
            f = open(new_path, "w", encoding="UTF-8")
            for line in data:
                write_line = line
                if ("［" in write_line or "[" in write_line) and ("］" in write_line or "]" in write_line):
                    line_query = replace_bracket(write_line)
                    for w in line_query:
                        f.write(remove_curves(w))
                else:
                    f.write(remove_curves(write_line))
            f.close()
    return True


def remove_keyword(str_test):
    f = open("data/sample/keyword.txt", "r", encoding="UTF-8")
    keywords = f.readlines()
    f.close()
    for i in range(keywords.__len__()):                                    #去除掉每行的最后面的换行符
        if keywords[i][-1] == '\n':
            keywords[i] = keywords[i][:-1]
    for word in keywords:
        if word in str_test:
            str_q = str_test.split(word)
            str_test = "".join(str_q)
    return str_test


def remove_key_word():
    paths = file_name("result")
    for x in paths:                            #只获取第二部的处理结果，其余的不再获取
        if "second" not in x:
            paths.remove(x)
    for x in paths:
        str_q = x.split("_second")
        new_path = str_q[0] + "_thirdly" + str_q[1]
        f = open(x, "r", encoding="UTF-8")
        data = f.readlines()
        f.close()
        f = open(new_path, "w", encoding="UTF-8")
        for line in data:
            str_q = line.split(" ")
            str_p1 = str_q[:-1]
            str_p2 = str_q[-1]
            new_line = " ".join(str_p1) + " " + remove_keyword(str_p2) + "\n"
            f.write(new_line)
        f.close()
    return True


remove_bracket()
# remove_key_word()
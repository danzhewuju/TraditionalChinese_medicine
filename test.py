#!usr/bin/python3
import os
import re


def replace_bracket(str_test):        #将中括号进行替换
    stack = []
    stack_query = []
    if "［" in str_test and "］" in str_test:
        stack.append(str_test)
    while stack.__len__() != 0:
        str_test = stack.pop()
        start = str_test.index("［")
        end = str_test.index("］")
        replace_word = str_test[start + 1:end]
        print(replace_word)
        step = end - start
        str_r1 = str_test[:start] + str_test[end + 1:]
        new_start = start - step + 1
        new_end = end - step
        str_r2 = str_r1[:new_start] + replace_word + str_r1[new_end:]
        if "［" in str_r1:
            stack.append(str_r1)
        else:
            # print(str_r1)
            stack_query.append(str_r1)
        if "［" in str_r2:
            stack.append(str_r2)
        else:
            # print(str_r2)
            stack_query.append(str_r2)
    return stack_query


def file_name(file_path):                                             #获取一个指定文件夹之下的所有的文件（在本例中是txt文件）
    paths = []
    for root, dirs, files in os.walk(file_path):
        # print(root)
        # print(dirs)
        # print(files)
        for x in files:
            path = root + "\\" + x
            print(path)
            paths.append(path)
        # path = root + files
        # print("path:", path)
    return paths


def remove_curves(str_test):                              #去除圆括号
    str_tem = re.split(r"（.+）", str_test)
    str_line = "".join(str_tem)
    return str_line


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


def word_split(str_test):
    f = open("data/sample/split_word.txt", "r", encoding="UTF-8")
    word_splits = f.readlines()
    f.close()
    split_query = []
    result_query = []
    result_query.append(str_test)
    word_splits = [x for x in word_splits if x != "\n"]                                                #剔除掉之前记录下的多余空白符的位置
    for index in range(word_splits.__len__()):
        if word_splits[index][-1] == "\n":
            word_splits[index] = word_splits[index][:-1]
    #需要去除空白分割符
    while result_query.__len__() != 0:
        str_test = result_query.pop()
        count = 0
        for x in word_splits:
            if x in str_test:
                str_qt = str_test.split(x)
                for s in str_qt:
                    result_query.append(s)
            else:
                count += 1
        if count == word_splits.__len__():
            # print(str_test)
            split_query.append(str_test)
    split_query = sorted(set(split_query), key=split_query.index)     #删除列表中重复的元素
    return split_query


def test():
    str_test = "脂瘤 类别 躯体痹、痿、瘤病类"
    str_query = str_test.split(" ")
    str_tem = " ".join(str_query[:-1])
    str1 = word_split(str_query[-1])
    for x in str1:
        str_r = str_tem + " " + x
        print(str_r)
    return True


# test()
str_test = "胁痈 病因 多由肝胆火郁"
print(str_test.split(" ").__len__())
# f = open("result/治法_2/治法_second.txt", "w", encoding="UTF-8")
# f.write("this is test writing!")
# f.close()
# print(os.path.exists("result"))


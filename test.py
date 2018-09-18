#!usr/bin/python3
import os


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


def test():
    str_test = "./result\疾病\关系三元组.txt"
    new_path = str_test[:-4] + "_second" + str_test[-4:]
    print(new_path)
    return True


test()




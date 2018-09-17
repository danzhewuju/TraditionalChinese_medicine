#!usr/bin/python3
import re

class Illness:
    class_name = ""
    illness_name = ""
    illness_explain = ""

    def __init__(self, class_name, illness_name, illness_explain):
        self.class_name = class_name
        self.illness_name = illness_name
        self.illness_explain = illness_explain


def create_class():
    f = open("data/疾病.txt", 'r', encoding='UTF-8')
    data = f.readlines()
    f.close()
    count = 0
    sum = data.__len__()
    class_query = []
    name_query = []
    explain_query = []
    while count < sum:
        line = data[count]
        line = line[:-1]
        trip_info = line.split(' ')  # 分词后的信息
        if trip_info[0] == "[分类]":
            class_query.append(trip_info[2])
        else:
            if trip_info[0] == "[疾病名称]":
                name_query.append(trip_info[2])
            else:
                if trip_info[0] == "[注释]":
                    explain_query.append(trip_info[2])
        count += 1
    ill = []
    for i in range(class_query.__len__()):
        illness_tem = Illness(class_query[i], name_query[i], explain_query[i])
        ill.append(illness_tem)
    return ill   #返回一个包含了所有疾病的信息


def write_class_tri():
    ill = create_class()
    f = open("result/关系三元组.txt", 'w')
    for x in ill:
        str_tem = x.illness_name + " 类别 " + x.class_name + '\n'
        print(str_tem)
        f.write(str_tem)
    f.close()
    return True


def write_class_reason():               #构建了病因三元组 格式： 疾病名称 病因 疾病原因
    ill = create_class()
    f = open("result/病因三元组.txt", 'w', encoding="UTF-8")
    for x in ill:
        str1 = x.illness_explain
        str_tem = str1.split("。")
        if str_tem.__len__() > 2:
            str_test = str_tem[0]
            start = str_test.count("因")
            str_test = str_test[start:]
            print(str_test)
            str_write = x.illness_name + " 病因 " + str_test + "\n"
            f.write(str_write)
    f.close()
    return True


def write_class_symptom():
    ill = create_class()
    f =open("result/症状三元组..txt", 'w', encoding="UTF-8")
    for x in ill:
        str_tem = x.illness_explain
        str_query = str_tem.split('。')
        if str_query.__len__() > 2:
            str_symptom = str_query.pop(-2)
            match_obj = re.search("以(.*)为", str_symptom)
            if match_obj != None :
                str_symptom = match_obj.group(1)
            str_line = x.illness_name + " 症状 " + str_symptom + '\n'
            f.write(str_line)
            print(str_line)
    f.close()
    return True

# write_class_tri()
# write_class_reason()
write_class_symptom()
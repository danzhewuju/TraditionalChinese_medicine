#!usr/bin/python3
import re
                                #第一轮的数据处理收集


class Illness:                   #疾病的相关信息类
    class_name = ""
    illness_name = ""            #疾病或者是征候的名称
    illness_explain = ""

    def __init__(self, class_name, illness_name, illness_explain):
        self.class_name = class_name
        self.illness_name = illness_name
        self.illness_explain = illness_explain


class TherapyMethod:      #药房的相关信息类
    class_name = ""       #疾病的类别
    method_name = ""      #药方的名称
    method_explain = ""   #药房的解释

    def __init__(self, class_name, method_name, method_explain):
        self.class_name = class_name
        self.method_explain = method_explain
        self.method_name = method_name


def create_method_query():
    methods = []
    f = open("data/治法.txt", 'r', encoding="UTF-8")
    data = f.readlines()
    f.close()
    count = 0
    sum = data.__len__()
    method_class_name = " "       #药房类别的名称
    method_name = " "             #药房的名名称
    method_explain = " "          #药房的注解
    for i in range(sum):
        str_temp = data[i]
        str_temp = str_temp[:-1]
        if str_temp[:3] != "同义词":
            if str_temp[-1] == "法" and str_temp.split("，").__len__() == 1 and "．" not in str_temp:  # 大类的方法一般是 xxxx法,去除其中关某些其他冗余数据 观察结构
                str_query = re.finditer(r"\D", str_temp)
                str1 = ""
                for x in str_query:
                    if x.group() != "．" and x.group() != " ":
                        str1 += x.group()  # 此时生成药房的类别
                method_class_name = str1
            else:
                if str_temp.split("．").__len__() >= 2:  # 这个小数点不是在英文状态下的小数点
                    str_query = re.finditer(r"\D", str_temp)
                    str1 = ""
                    for x in str_query:
                        if str(x.group()) != '．' and x.group() != " ":
                            str1 += x.group()
                    # print(str1)
                    method_name = str1
                else:
                    method_explain = str_temp
                    therapy_methods = TherapyMethod(method_class_name, method_name, method_explain)
                    methods.append(therapy_methods)
    return methods


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


def create_illness_class():                            #返回一个证候的全部信息实体
    f = open("data/证候.txt", 'r', encoding='UTF-8')
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
            if trip_info[0] == "[证候名称]":
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
    f = open("result/疾病/关系三元组_first.txt", 'w', encoding="UTF-8")
    for x in ill:
        str_tem = x.illness_name + " 类别 " + x.class_name + '\n'
        # print(str_tem)
        f.write(str_tem)
    f.close()
    return True


def write_class_reason():               #构建了病因三元组 格式： 疾病名称 病因 疾病原因
    ill = create_class()
    f = open("result/疾病/病因三元组_first.txt", 'w', encoding="UTF-8")
    for x in ill:
        str1 = x.illness_explain
        str_tem = str1.split("。")
        if str_tem.__len__() > 2:
            str_test = str_tem[0]
            start = str_test.count("因")
            str_test = str_test[start:]
            # print(str_test)
            str_write = x.illness_name + " 病因 " + str_test + "\n"
            f.write(str_write)
    f.close()
    return True


def write_class_symptom():
    ill = create_class()
    f =open("result/疾病/症状三元组_first.txt", 'w', encoding="UTF-8")
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
            # print(str_line)
    f.close()
    return True


def write_therapy_method():
    methods = create_method_query()
    f = open("result/治法/治法_first.txt", 'w', encoding="UTF-8")
    for x in methods:
        str_tem = x.class_name + " 包含 " + x.method_name + "\n"
        f.write(str_tem)
        # print(str_tem)
    f.close()
    return True


def write_therapy_range():       #药房的使用范围
    methods = create_method_query()
    f = open("result/治法/适用范围_first.txt", "w", encoding="UTF-8")
    for x in methods:
        tem_query = x.method_explain.split("用于")                            #设计的提取方法  可能不是准确
        method_rang = tem_query[-1]
        method_rang = method_rang[:-1]
        tem_query = method_rang.split("治疗方法")
        method_rang = tem_query[0]
        method_rang = method_rang.split("治疗")[-1]
        method_rang = method_rang.split("用")[-1]
        if method_rang is not None and method_rang.__len__() >= 2:
            if method_rang[-1] == "的" or method_rang[-1] == "等":
                method_rang = method_rang[:-1]
                str_tem = x.method_name + " 适用范围 " + method_rang + "\n"
                f.write(str_tem)
                # print(str_tem)
    f.close()
    return True


def write_therapy_effect():                                         #药房所具有的功效
    methods = create_method_query()
    f = open("result/治法/作用_first.txt", "w", encoding="UTF-8")
    for x in methods:
        str_tem = x.method_explain.split("，")[0].split("。")[0]
        if str_tem.__len__() > 2:
            if str_tem[:2] == "运用" or str_tem[:2] == "具有" or str_tem[:2] == "通过":
                str_tem = str_tem[2:]
                if str_tem[-2:] == "作用":
                    str_tem = str_tem[:-2]
                    str_line = x.method_name + " 作用 " + str_tem + "\n"
                    f.write(str_line)
                    # print(str_tem)
    f.close()
    return True


def write_illness_class():                            #证候的分类
    illness = create_illness_class()
    f = open("result/证候/证候分类_first.txt", "w", encoding="UTF-8")
    for x in illness:
        str_tem = x.illness_name + " 属于 " + x.class_name + "\n"
        f.write(str_tem)
    f.close()
    return True


def write_illness_symptom():   #证候的症状
    illness = create_illness_class()
    f = open("result/证候/证候症状_first.txt", "w", encoding="UTF-8")
    for x in illness:
        str_explain = x.illness_explain
        if str_explain.__len__() > 3 and str_explain[-4:-1] == "的证候":
            str_explain = str_explain[:-4]
        str_explain = str_explain.split("等")[0]
        str_tem = x.illness_name + " 症状特征 " + str_explain + "\n"
        # print(str_tem)
        f.write(str_tem)
    f.close()
    return True


def run():
    print("文件处理过程......")
    write_illness_symptom()
    write_class_symptom()
    write_therapy_effect()
    write_therapy_range()
    write_class_reason()
    write_therapy_method()
    write_class_tri()
    write_illness_class()
    print("文件处理完成!")
    return True


# run()
#初步的数据预处理过程
# write_class_tri()
# write_class_reason()
# write_class_symptom()
# write_therapy_method()
# write_therapy_range()
# write_therapy_effect()
# write_illness_class()
# write_illness_symptom()
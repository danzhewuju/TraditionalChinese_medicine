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


class TherapyMethod():
    class_name = ""       #疾病的类别
    method_name = ""      #药方的名称
    method_explain = ""   #药房的解释

    def __init__(self, class_name, method_name, method_explain):
        self.class_name = class_name
        self.method_explain = method_explain
        self.method_explain = method_explain


# str1 = "肺病日久，痰气阻滞，进而导致心脉瘀阻。以咳嗽气喘，咯痰，心悸水肿，唇舌紫暗等为主要表现的肺病及心的疾病。"
# str_tem = str1.split("。")
# str_test = str_tem[0]
# start = str_test.count("因")
# str_test = str_test[start:]
# print(str_tem)
# print(str_test)
# str2 = "22以晶珠混浊，视力渐降，终至瞳神内呈圆形银白色翳障，视力障碍为主要表现的内障类疾病"
# match_obj = re.search("以(.*)为", str2)
# print(match_obj.groups())
str_test = "5解表法"
print(str_test[-1])
str_query = re.finditer(r"\D", str_test)
str1 = ""
for x in str_query:
    str1 += x.group()
print(str1)
# print(str_query.group(1))


# print(str2.split().__len__())


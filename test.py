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
str_test = "用口、蚂蝗或医疗器械吸引患部，以吸引出痰涎、脓血、毒液等，用以治疗疾病的一种方法。用蚂蝗吸咂患处以治病者，称为蜞针疗法。常用于较深部的脓疡或痈肿、急性乳痈、风眩、中风痰闭、痰壅窒息、毒蛇咬伤、毒虫咬伤等。"
# print(str_test[-1])
# str_query = re.finditer(r"\D", str_test)
# str1 = ""
# for x in str_query:
#     if str(x.group()) != '．' and x.group() != " " :
#         str1 += x.group()
# print(str1)
# str2 = str_test.split("．")
# print(str2.__len__())
str_query = str_test.split("。")
print(str_query)


# print(str2.split().__len__())


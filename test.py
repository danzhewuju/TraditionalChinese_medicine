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


# str1 = "肺病日久，痰气阻滞，进而导致心脉瘀阻。以咳嗽气喘，咯痰，心悸水肿，唇舌紫暗等为主要表现的肺病及心的疾病。"
# str_tem = str1.split("。")
# str_test = str_tem[0]
# start = str_test.count("因")
# str_test = str_test[start:]
# print(str_tem)
# print(str_test)
str2 = "22以晶珠混浊，视力渐降，终至瞳神内呈圆形银白色翳障，视力障碍为主要表现的内障类疾病"
match_obj = re.search("以(.*)为", str2)
print(match_obj.groups())
# print(str2.split().__len__())


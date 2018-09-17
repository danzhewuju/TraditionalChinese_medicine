#!usr/bin/python3


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
str2 = "婚后女方正常，有正常性生活而两年不能生育为主要表现的肾系疾病。"
print(str2.split('。'))
# print(str2.split().__len__())


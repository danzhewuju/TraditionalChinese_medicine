#!usr/bin/python3
import os
import re
import jieba

str_1 = "生于臀部肌肉丰厚处痈病类疾病"
jieba.add_word("丰厚处")
str_result = jieba.cut_for_search(str_1)
print("|".join(str_result))
str_result = jieba




#!usr/bin/python

f = open("data/疾病.txt", 'r', encoding='UTF-8')
line = f.read()
f.close()
print(line)
print(line.__len__())

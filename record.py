import json
import openpyxl
import os


def get_text(file_name):
    answer_a = []
    with open(file_name, 'r', encoding='utf-8') as f:
        for a in f:
            b = json.loads(a)
            answer_a.append(b['text'])
    return answer_a


answer_list = {}
os.chdir(r"C:\PythonCode\pythonProject\answer")
filename = []
for _, _, files in os.walk('.', topdown=False):
    for name in files:
        filename.append(str(name))
for name in filename:
    listy = get_text(name)
    answer_list[name] = listy

question_list = []
with open(r"C:\PythonCode\pythonProject\eval_dataset_chn.json", 'r', encoding='utf-8') as rf:
    for line in rf:
        data = json.loads(line)
        question_list.append(data['question_chn'])

category_list = []
with open(r"C:\PythonCode\pythonProject\eval_dataset_chn.json", 'r', encoding='utf-8') as rf:
    for line in rf:
        data = json.loads(line)
        category_list.append(data['category'])
score_list = []
with open(r"C:\PythonCode\pythonProject\eval_dataset_chn.json", 'r', encoding='utf-8') as rf:
    for line in rf:
        data = json.loads(line)
        score_list.append(data['score'])

xlsxfile = r"C:\Users\76118\Desktop\Record.xlsx"
workbook = openpyxl.load_workbook(xlsxfile)
sheet = workbook['Sheet1']
sheet['A1'] = 'question'
sheet['B1'] = 'category'
sheet['C1'] = 'difficulty'
a = 2
for question in question_list:
    loca = "A" + str(a)
    sheet[loca] = question
    a = a + 1
d = 2
for category in category_list:
    loca = "B" + str(d)
    sheet[loca] = category
    d = d + 1
e = 2
for score in score_list:
    loca = "C" + str(e)
    sheet[loca] = score
    e = e + 1
b = 68
for key in answer_list:
    loca2 = chr(b) + str(1)
    sheet[str(loca2)] = str(key)
    c = 2
    for answer in answer_list[key]:
        loca1 = chr(b) + str(c)
        sheet[str(loca1)] = answer
        c = c + 1
    b = b + 1
workbook.save(xlsxfile)

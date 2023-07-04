import json
import openpyxl


# switch answer mode
def switch_mode(filename):
    all_list = []
    with open(filename, 'r', encoding='utf-8') as f:
        my_list = json.loads(f.readline())
        for i in my_list:
            a_list = i.split('\n')
            for j in a_list:
                if j == '':
                    continue
                if j[0].isdigit():
                    all_list.append(j[3:].strip().replace('\"',''))
    all_dict = {}
    for i, text in enumerate(all_list):
        all_dict[str(i+1)] = text
    with open("question_new_new.json", 'w', encoding='utf-8', newline='\n') as wf:
        wf.write(json.dumps(all_dict, ensure_ascii=False, indent=1))


def check_json(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        i = json.loads(f.readline())
        # instance = data['instances']
        # print(len(instance))
        max_length = 0
        # for i in instance:
        length = len(i['positive']) + len(i['negative'])
        print(length)
        length = len(i['positive']) * 2
        print(length)
        length = 2 * len(i['negative'])
        print(length)
        #     if length > max_length:
        #         max_length = length
        # print(max_length)


def make_json(filename):
    data = [{"positive": "我" * 500, "negative": "我" * 500} for _ in range(10)]

    with open(filename, 'w') as f:
        my_dict = {"type": "text_only", "instances": data}
        f.write(json.dumps(my_dict))


def write_exl():
    xlsx_file = r"C:\Users\76118\Desktop\length.xlsx"
    workbook = openpyxl.load_workbook(xlsx_file)
    sheet = workbook['Sheet1']
    with open("length.json", 'r', encoding='utf-8') as f:
        data = json.loads(f.readline())
        a = 1
        for i in data.keys():
            sheet["A" + str(a)] = i
            sheet['B' + str(a)] = data[i]
            a = a + 1
    workbook.save(xlsx_file)


def eva_model(filename):
    win = 0
    with open(filename, 'r', encoding='utf-8') as f:
        count = 0
        for line in f.readlines():
            if line[0:4] == 'mean':
                continue
            flag = line.find('0')
            result = line[flag:]
            result = float(result)
            count = count + 1
            if result > 0.5:
                win = win + 1
    accuracy = win / count
    print(accuracy)


def read_xsl(filename):
    answer_dict = {}
    workbook = openpyxl.load_workbook(filename)
    sheet = workbook['Sheet1']
    for i in range(2, 107):
        number = sheet['A' + str(i)].value
        answer = sheet['B' + str(i)].value
        answer_dict[number] = answer
    with open('answer_data.json', 'w', encoding='utf-8') as wf:
        wf.write(json.dumps(answer_dict, ensure_ascii=False))


switch_mode('question_make.json')

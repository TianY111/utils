import json
from itertools import combinations

all_list = []
test_list = []
answer_list = []
train_list = []
a = 0
gap_dict = {}
len_dict = {}
prompt_list = []
with open('datasets/review_output_mix_training_summary_rank_score_lcs_all.json', 'r', encoding='utf-8') as f:
    mean_len = 0
    max_len = 0
    order_num = 0
    for line in f:
        prompt_list.append(0)
        data = json.loads(line)
        prompt = "请概括: " + data['prompt'].replace('\r\n', '\n') + '\n'

        for i in combinations(range(1, 11), 2):
            answer1 = "answer_" + str(i[0])
            answer2 = "answer_" + str(i[1])
            if data[answer1]['score'] == 'None' or data[answer2]['score'] == 'None':
                continue
            score1 = int(data[answer1]['score'][-2:])
            score2 = int(data[answer2]['score'][-2:])
            # gap = abs(score1 - score2)
            # if str(gap) in gap_dict:
            #     gap_dict[str(gap)] = gap_dict[str(gap)] + 1
            # else:
            #     gap_dict[str(gap)] = 1

            if abs(score1 - score2) < 15:
                continue

            if score1 > score2:
                pos = data[answer1]['answer']
                neg = data[answer2]['answer']
            else:
                pos = data[answer2]['answer'].replace('\r\n', '\n')
                neg = data[answer1]['answer'].replace('\r\n', '\n')
            positive = prompt + "答案: " + pos
            negative = prompt + "答案: " + neg
            batch_len = len(positive) + len(negative)
            # if str(batch_len) in len_dict:
            #     len_dict[str(batch_len)] = len_dict[str(batch_len)] + 1
            # else:
            #     len_dict[str(batch_len)] = 1
            if batch_len > 4000:
                continue
            a_dict = {"positive": positive, "negative": negative, "length": batch_len}
            all_list.append(a_dict)
            prompt_list[order_num] = prompt_list[order_num] + 1
        order_num = order_num + 1
# print(len(all_list))
# train_list = all_list[0:6295]
# test_list = all_list[6295:]
# print(len(train_list))
# print(len(test_list))
# if a < 12212:
#     answer_list.append(a_dict)
# else:
#     test_list.append(a_dict)
for i in prompt_list:
    if i == 0:
        prompt_list.remove(i)
print(len(prompt_list))
# train_dict = {'type': 'text_only', "instances": train_list}
# test_dict = {'type': 'text_only', "instances": test_list}
# prompt_dict = {"list": prompt_list}
# with open("train_15_4000.json", 'w', encoding='utf-8') as wf:
#     wf.write(json.dumps(train_dict, ensure_ascii=False))
# with open("prompt_distribution.json", "w", encoding='utf-8') as wf:
#     wf.write(json.dumps(prompt_dict, ensure_ascii=False))
# with open('length.json', 'w', encoding='utf-8') as wf:
#     wf.write(json.dumps(len_dict, ensure_ascii=False))
# with open('gap.json', 'w', encoding='utf-8') as wf:
#     wf.write(json.dumps(gap_dict, ensure_ascii=False))

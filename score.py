import json

# score
my_list = []
with open("result/glm_vsbelle.jsonl", "r", encoding="utf-8") as readfile:
    for line in readfile:
        # print(type(line))
        result = json.loads(line)
        my_list.append(result)

loss_num, tie_num, win_num = 0, 0, 0
mean_challenger = 0
mean_baseline = 0
num = 0
err = []
cat = []
for res in my_list:
    sc = res["score"]
    baseline = float(sc[0])
    challenger = float(sc[1])
    if baseline < 0 or challenger < 0:
        err.append(res["question_id"])
        continue
    num = num + 1
    mean_baseline = mean_baseline + baseline
    mean_challenger = mean_challenger + challenger
    if baseline > challenger:
        loss_num = loss_num + 1
    elif baseline == challenger:
        tie = tie_num + 1
    else:
        win_num = win_num + 1
mean_challenger = mean_challenger / num
mean_baseline = mean_baseline / num
# print('win: ', win_num)
# print('tie: ', tie_num)
# print('loss: ', loss_num)
# print('mean: ', mean)
# print(err)
with open('result/glm_vs_belle.txt', 'w', encoding='utf-8') as f:
    f.write('win: ' + str(win_num))
    f.write('\n')
    f.write('loss: ' + str(loss_num))
    f.write('\n')
    f.write('mean_challenger: ' + str(mean_challenger))
    f.write('\n')
    f.write('mean_baseline: ' + str(mean_baseline))
    f.write('\n')
    f.write('erroe question: ')
    for i in err:
        f.write(str(i) + ', ')

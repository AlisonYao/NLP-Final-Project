import json
from collections import defaultdict
import matplotlib.pyplot as plt

#############################################
# first concatenate test and final data
#############################################
# with open('./TableQA/test/test.json', 'r') as f:
#   lines = len(f.readlines())

# question_file = open('./TableQA/test/test.json', 'r')
# query_file = open('./TableQA/test/standard.json', 'r')
# concate_file = open('./TableQA/test/test_complete.json', 'w')

# for i in range(lines):
#   question = json.loads(question_file.readline())
#   query = json.loads(query_file.readline())
#   question['sql'] = query
#   concate_file.writelines(json.dumps(question, ensure_ascii=False) + '\n')

# question_file.close()
# query_file.close()
# concate_file.close()


# with open('./TableQA/final/final_test.json', 'r') as f:
#   lines = len(f.readlines())

# question_file = open('./TableQA/final/final_test.json', 'r')
# query_file = open('./TableQA/final/standard.json', 'r')
# concate_file = open('./TableQA/final/final_complete.json', 'w')

# for i in range(lines):
#   question = json.loads(question_file.readline())
#   query = json.loads(query_file.readline())
#   question['sql'] = query
#   concate_file.writelines(json.dumps(question, ensure_ascii=False) + '\n')

# question_file.close()
# query_file.close()
# concate_file.close()


#############################################
# counts & basic statistics
#############################################
def counter(path):
    selectCountDict, condsCountDict = defaultdict(int), defaultdict(int)
    with open(path, 'r') as load_f:
        for line in load_f:
            line = json.loads(line) # convert to dict
            sql = line['sql']
            # print(sql, len(sql['sel']), len(sql['conds']))
            selectCountDict[len(sql['sel'])] += 1
            condsCountDict[len(sql['conds'])] += 1
    return selectCountDict, condsCountDict

def visulization(d):
    labels, frequencies = [], []
    for label_frequency in d.items():
        label, frequency = label_frequency
        labels.append(label)
        frequencies.append(frequency)
    # print(labels)
    # print(frequencies)
    plt.bar(labels, frequencies)
    plt.show() 


selectCountDict, condsCountDict = counter("TableQA/test/test_complete.json")
print('#selects:', selectCountDict)
print('#where conditions:', condsCountDict)
visulization(selectCountDict)
print('DONE')

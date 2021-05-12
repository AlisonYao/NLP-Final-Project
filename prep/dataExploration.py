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
# SQL counts & basic statistics
#############################################
def SQLcounter(path):
    selectCountDict, condsCountDict, cond_conn_opCountDict = defaultdict(int), defaultdict(int), defaultdict(int)
    with open(path, 'r') as load_f:
        for line in load_f:
            line = json.loads(line) # convert to dict
            sql = line['sql']
            selectCountDict[len(sql['sel'])] += 1
            condsCountDict[len(sql['conds'])] += 1
            cond_conn_opCountDict[sql['cond_conn_op']] += 1
    return selectCountDict, condsCountDict, cond_conn_opCountDict

def TABLEcounter(path):
    columnCountDict = defaultdict(int)
    with open(path, 'r') as load_f:
        for line in load_f:
            line = json.loads(line) # convert to dict
            header = line['header']
            columnCountDict[len(header)] += 1
    return columnCountDict

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


selectCountDict, condsCountDict, cond_conn_opCountDict = SQLcounter("TableQA/train/train.json")
print('#selects:', selectCountDict)
print('#where conditions:', condsCountDict)
print('#cond_conn_opCountDict:', cond_conn_opCountDict)
# visulization(selectCountDict)
columnCountDict = TABLEcounter('TableQA/train/train.tables.json')
print('#columns in a table:', columnCountDict)
print('DONE')

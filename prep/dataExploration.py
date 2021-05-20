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
    selectCountDict, condsCountDict, cond_conn_opCountDict, aggCountDict, condsCountDict2, selectColumnDict, whereColumnDict = defaultdict(int), defaultdict(int), defaultdict(int), defaultdict(int), defaultdict(int), defaultdict(int), defaultdict(int)
    with open(path, 'r') as load_f:
        for line in load_f:
            line = json.loads(line) # convert to dict
            sql = line['sql']
            selectCountDict[len(sql['sel'])] += 1
            condsCountDict[len(sql['conds'])] += 1
            cond_conn_opCountDict[sql['cond_conn_op']] += 1
            aggs = sql['agg']
            for agg in aggs:
                aggCountDict[agg] += 1
            conds = sql['conds']
            for cond in conds:
                condsCountDict2[cond[1]] += 1
                whereColumnDict[cond[0]] += 1
            sel = sql['sel']
            for i in sel:
                selectColumnDict[i] += 1
    return selectCountDict, condsCountDict, cond_conn_opCountDict, aggCountDict, condsCountDict2, selectColumnDict, whereColumnDict

def TABLEcounter(path):
    columnCountDict = defaultdict(int)
    with open(path, 'r') as load_f:
        for line in load_f:
            line = json.loads(line) # convert to dict
            header = line['header']
            columnCountDict[len(header)] += 1
    return columnCountDict

def baseline(path):
    with open(path, 'r') as load_f:
        Count, selCount, aggCount, opCount, wheCount = 0, 0, 0, 0, 0
        for line in load_f:
            Count += 1
            line = json.loads(line) # convert to dict
            sql = line['sql']
            # S-col
            sel = sql['sel']
            if sel == [1] * len(sel):
                selCount += 1
            # S-agg
            aggs = sql['agg']
            if aggs == [0] * len(aggs):
                aggCount += 1
            # W-col & W-col-op
            conds = sql['conds']
            operators, columns = [], []
            for cond in conds:
                operators.append(cond[1])
                columns.append(cond[0])
            if operators == [0] * len(operators):
                opCount += 1
            if columns == [1] * len(columns):
                wheCount += 1
            
    return selCount/Count , aggCount/Count, wheCount/Count, opCount/Count

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


selectCountDict, condsCountDict, cond_conn_opCountDict, aggCountDict, condsCountDict, selectColumnDict, whereColumnDict = SQLcounter("TableQA/final/final_complete.json")
print('#selects:', selectCountDict)
print('#where conditions:', condsCountDict)
print('#and/or/null:', cond_conn_opCountDict)
print('#agg:', aggCountDict)
print('#><==!=', condsCountDict)
print('#selectColumns:', selectColumnDict)
print('#whereColumns:', whereColumnDict)
# visulization(selectCountDict)
# columnCountDict = TABLEcounter('TableQA/final/final.tables.json')
# print('#columns in a table:', columnCountDict)
print(baseline("TableQA/final/final_complete.json"))
print('DONE')

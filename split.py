import json
import os
import re

data_dir = "data/MULTIWOZ2.4"


testListFile = []
fin = open(os.path.join(data_dir,'testListFile.json'), 'r')
for line in fin:
    testListFile.append(line[:-1])
fin.close()

valListFile = []
fin = open(os.path.join(data_dir,'valListFile.json'), 'r')
for line in fin:
    valListFile.append(line[:-1])
fin.close()

data = json.load(open(os.path.join(data_dir, "data.json")))

test_dials = {}
val_dials = {}
train_dials = {}
count_train, count_val, count_test = 0, 0, 0    
for dialogue_name in data:
    if dialogue_name in testListFile:
        test_dials[dialogue_name] = data[dialogue_name]
        count_test += 1
    elif dialogue_name in valListFile:
        val_dials[dialogue_name] = data[dialogue_name]
        count_val += 1
    else:
        train_dials[dialogue_name] = data[dialogue_name]
        count_train += 1
        
print("# of dialogues: Train {}, Val {}, Test {}".format(count_train, count_val, count_test))

# save all dialogues
with open(os.path.join(data_dir, 'dev_dials.json'), 'w') as f:
    json.dump(val_dials, f, indent=4)

with open(os.path.join(data_dir, 'test_dials.json'), 'w') as f:
    json.dump(test_dials, f, indent=4)

with open(os.path.join(data_dir, 'train_dials.json'), 'w') as f:
    json.dump(train_dials, f, indent=4)

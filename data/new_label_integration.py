import copy
import json
import os
import re
import collections

data_dir = "dev_test_refined"
full_data_file = "data_mwz2.1.json"
refined_data_files = ["dev_dials_manually-modified-v2.json", "test_dials_manually-modified-v2.json"]

full_data = json.load(open(os.path.join(data_dir, full_data_file), "r"))

for file_id in refined_data_files:
    dials = json.load(open(os.path.join(data_dir, file_id), "r"))
    
    for dial_dict in dials:        
        dialogue_idx = dial_dict["dialogue_idx"]
        d_full = full_data[dialogue_idx]["log"]
        assert len(d_full) == 2 * len(dial_dict["dialogue"])
        
        for i in range(len(d_full)):
            if i % 2 == 1:  # sys turn
                turn_id = i // 2
                
                assert turn_id == dial_dict["dialogue"][turn_id]["turn_idx"]
                bvs = dial_dict["dialogue"][turn_id]["belief_state"]
                
                for item in bvs:
                    d, s = item[0].split("-") # domain, slot
                    v = item[1] # value
                    
                    if "book" in s:
                        s = s.split(" ")[1]
                        d_full[i]["metadata"][d]["book"][s] = v
                    else:
                        if "leaveat" in s:
                            s = "leaveAt"
                        if "arriveby" in s:
                            s = "arriveBy"
                        
                        # in some preprocessing scripts, "not mentioned" is used to decide the active domains of a turn
                        # we keep these original annotations if the updated value is none
                        if d_full[i]["metadata"][d]["semi"][s] == "not mentioned" and v == "":
                            v = "not mentioned"
                        
                        d_full[i]["metadata"][d]["semi"][s] = v
                        
                    
with open(os.path.join("MULTIWOZ2.4", 'data.json'), 'w') as f:
        json.dump(full_data, f, indent=4)

# extract ontology by traversing the whole dataset
ontology = {}
for dialogue_idx in full_data:
    dialogue = full_data[dialogue_idx]["log"]    
    for i in range(len(dialogue)):
        if i % 2 == 1:
            bstate = dialogue[i]["metadata"]
            for dom in bstate.keys():
                for slot in bstate[dom]["book"].keys():
                    if slot != "booked":
                        s = dom + "-book " + slot
                        if s not in ontology:
                            ontology[s] = []
                        v = bstate[dom]["book"][slot]
                        if v == "" or v == "not mentioned":
                            v = "none"
                        ontology[s].append(v)
                for slot in bstate[dom]["semi"].keys():
                    s = dom + "-" + slot
                    if s not in ontology:
                        ontology[s] = []
                    v = bstate[dom]["semi"][slot]
                    if v == "" or v == "not mentioned":
                        v = "none"
                    ontology[s].append(v)

for slot in ontology:
    ontology[slot] = sorted(list(set(ontology[slot])))
ontology.pop("train-book ticket")    
ontology = collections.OrderedDict(sorted(ontology.items()))
with open(os.path.join("MULTIWOZ2.4", 'ontology.json'), 'w') as f:
    json.dump(ontology, f, indent=4)

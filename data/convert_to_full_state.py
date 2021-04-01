import json
import os
import re
from copy import deepcopy


data_dir = "dev_test_refined"
data_files = ["dev_dials_manually-modified.json", "test_dials_manually-modified.json"]


slot_meta = json.load(open(os.path.join(data_dir, "slot_meta.json"), "r"))["slot_meta"]
print(slot_meta)

ontology_modified = {}
for slot in slot_meta:
    ontology_modified[slot] = []
    
for idx, file_id in enumerate(data_files):   
    fp_data = open(os.path.join(data_dir, file_id), "r")
    dials = json.load(fp_data)
    
    dials_v2 = []
    for dial_dict in dials:
        new_dial_dict = {} 
        new_dial_dict["dialogue_idx"] = dial_dict["dialogue_idx"]
        new_dial_dict["dialogue"] = []
       
        prev_turn_state = {}
        for slot in slot_meta:
            prev_turn_state[slot] = "none"
            ontology_modified[slot].append("none")
        
        for ti, turn in enumerate(dial_dict["dialogue"]):
            # state
            turn_label = dict([(l[0], l[1]) for l in turn["turn_label"]])
            turn_dialog_state = deepcopy(prev_turn_state)
            
            for slot in turn_label:
                turn_dialog_state[slot] = turn_label[slot]
                ontology_modified[slot].append(turn_dialog_state[slot])
                                   
            active_domains = [] 
            for slot in slot_meta:
                if turn_dialog_state[slot] != "none":
                    active_domains.append(slot.split("-")[0])
            active_domains = list(set(active_domains))
            
            bvs = [] # full belief state
            # if one domain is not active, all the slot values are set to "" rather than "none"
            # if the domain is active and the slot takes value "none", for book-related slots, the value 
            # is set to ""; for other slots, the value is set to "not mentioned"
            for slot in slot_meta:
                if slot.split("-")[0] not in active_domains:
                    bvs.append([slot, ""])
                else:
                    if turn_dialog_state[slot] == "none":
                        if "book" in slot:
                            bvs.append([slot, ""])
                        else:
                            bvs.append([slot, "not mentioned"])
                    else:
                        bvs.append([slot, turn_dialog_state[slot]])

            turn["belief_state"] = bvs
            new_dial_dict["dialogue"].append(turn)
            
            prev_turn_state = turn_dialog_state
            
        dials_v2.append(new_dial_dict)
        
    with open(os.path.join(data_dir, file_id.split(".")[0]+"-v2.json"), 'w') as outfile:
        json.dump(dials_v2, outfile, indent=4)
                
# ontology extracted from dev and test set
for slot in slot_meta:
    ontology_modified[slot] = sorted(list(set(ontology_modified[slot])))
    
with open(os.path.join(data_dir, 'ontology-modified-dev-test.json'), 'w') as outfile:
     json.dump(ontology_modified, outfile, indent=4)

----
There are two folders: 
+ The **dev_test_refined** folder contains the modified validation set and test set, and also the original data.json from MULTIWOZ 2.1.
+ The **MULTIWOZ2.4** folder is the complete version, which conforms exactly to the format of MULTIWOZ 2.1.

----
We also provide the scripts which we utilized to integrate the updated validation set and test set into the full data.json. There are two steps:
+ First, transform the turn-active state into full state
  ```console
  ❱❱❱ python3 convert_to_full_state.py
  ```
+ Second, integrate the new validation set and test set into the original data
  ```console
  ❱❱❱ python3 new_label_integration.py
  ```

Basically, there is no need to perform the two steps again. We provide the scripts just for reference. 

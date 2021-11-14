import json
import os
import sys
import copy
import cv2 as cv
import numpy as np
from config import *
from tools import *
import time

print("Start Inspection...")
print("Now Loading json file...")
target = os.path.join(BASE,sys.argv[1])

# target = os.path.join(BASE,'test.json')




with open(target,'r') as f:
    data = json.load(f)
new_data = copy.deepcopy(data)
print("json loaded!")

("Press SPACE if label is correct or press NEW NUMBER to re-label")
print("3", end = "...")
time.sleep(1)
print("2",end = "...")
time.sleep(1)
print("1")
time.sleep(1)


length = len(data["annotations"])
for idx, ann in enumerate(data["annotations"]):
    start_xy, end_xy = get_coordinate(ann)
    img = cv.imread(get_img_path(data,ann['image_id']), cv.IMREAD_COLOR)
    img = cv.rectangle(img,start_xy,end_xy,(0,0,255),2)
    cv.imshow(f"[{idx+1}/{length}] {get_file_name(data, ann['image_id'])}[Label: {ann['category_id']}]", img)
    key = cv.waitKey(0)
    if key != 32: # if key is not space
        new_label = int(chr(key))
        change_label(new_data,idx,new_label)

    cv.destroyAllWindows()

print("Would You Like To Save into New JSON??")
yes = input("Press y if you want to.")

if yes.lower() == 'y':
    new_json_name = os.path.join(BASE,input("New Name(.json must be added!): "))
    with open(new_json_name,'w') as f:
        json.dump(new_data, f)
    print("File Saved as", new_json_name)

print("Now Closing...")


# print("Inspection Closed.")
# print(f"Now Relabel for {len(relabel_idx)} Bounding Boxes")
# while relabel_idx:
#     idx = relabel_idx.pop()
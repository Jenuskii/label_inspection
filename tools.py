import os
from config import *

def change_label(data,ann_idx,new_id):
    data['annotations'][ann_idx]['category_id'] = new_id

def get_img_path(data, image_id):
    return os.path.join(IMG, data['images'][image_id-1]['file_name'])

def get_file_name(data, image_id):
    return data['images'][image_id-1]['file_name']

def get_coordinate(ann):
    start_xy = round(ann['segmentation'][0][0]), round(ann['segmentation'][0][1])
    end_xy = round(ann['segmentation'][0][4]), round(ann['segmentation'][0][5])
    return start_xy, end_xy


from ultralytics import YOLO
import config as cfg
import re
import shutil
from nanoid import generate
import os
import urllib.request

model = YOLO(cfg.MODEL_PATH)

def get_predict (filepath):
    model.predict(source = filepath,save_txt=True,conf=0.30) #save=True (to save the annotated image)
    

    class_dict = cfg.CLASSES_DICT
    path_split = os.path.split(filepath)
    txt_name = path_split[1].split('.')[0] + '.txt'
    txt_path = os.path.join(cfg.PRED_TXT_PATH,"labels",txt_name)
    no_dets = "[{'topwear_type': 'Not detected', 'conf': 0},{'sleeve_type': 'Not detected', 'conf': 0},\
                {'neck_type': 'Not detected', 'conf': 0},{'design_type': 'Not detected', 'conf': 0},\
                {'bottomwear_type': 'Not detected', 'conf': 0},{'footwear_type': 'Not detected', 'conf': 0}]"
    try:
        with open(txt_path) as f:
            data = [re.split('[ ]+|\t',x) for x in f.read().split('\n')]
    except:
        return no_dets

    pred = data[0:-1]
    pred.sort(key = lambda x: x[-1])  #sort the nested list predictions by ascending order of confidence

    pred_dict = {}
    for i in pred:
        # print(i[0])
        # print(i[-1])
        pred_dict[int(i[0])] = float(i[-1])

    final_pred = {}
    for i in pred_dict:
        final_pred[class_dict[i]] = float(pred_dict[i])
    
    top_wear_lst = cfg.TOP_WEAR_LIST
    sleeve_lst = cfg.SLEEVE_LIST
    neck_lst = cfg.NECK_LIST
    design_lst = cfg.DESIGN_LIST
    footwear_lst = cfg.FOOTWEAR_LIST
    bottomwear_lst = cfg.BOTTOMWEAR_LIST
    fashion_accessories_lst = cfg.FASHION_ACCESSORIES_LIST

    topwear_dict= {}
    sleeve_dict = {}
    design_dict = {}
    neck_dict = {}
    bottomwear_dict = {}
    footwear_dict = {}
    fashion_accessories_dict = {}

                #default no detection
                #topwear
    topwear_dict["topwear_type"] = 'Not detected'
    topwear_dict["conf"] = 0
                #sleeve
    sleeve_dict["sleeve_type"] = 'Not detected'
    sleeve_dict["conf"] = 0
                #design
    design_dict["design_type"] = 'Not detected'
    design_dict["conf"] = 0
                #neck
    neck_dict["neck_type"] = 'Not detected'
    neck_dict["conf"] = 0
                #bottomwear
    bottomwear_dict["bottomwear_type"] = 'Not detected'
    bottomwear_dict["conf"] = 0
                #footwear
    footwear_dict["footwear_type"] = 'Not detected'
    footwear_dict["conf"] = 0
                #accessories
    fashion_accessories_dict["accessory_type"] = 'Not detected'
    fashion_accessories_dict["conf"] = 0

    final_dets = []

    final_dets.append(topwear_dict)
    final_dets.append(sleeve_dict)
    final_dets.append(neck_dict)
    final_dets.append(design_dict)
    final_dets.append(bottomwear_dict)
    final_dets.append(footwear_dict)


    for key, value in final_pred.items():
        if key in top_wear_lst:
            topwear_dict["topwear_type"] = key
            topwear_dict["conf"] = value  
                        
    for key, value in final_pred.items():
        if key in sleeve_lst:
            sleeve_dict["sleeve_type"] = key
            sleeve_dict["conf"] = value

    for key, value in final_pred.items():
        if key in neck_lst:
            neck_dict["neck_type"] = key
            neck_dict["conf"] = value

    for key, value in final_pred.items():
        if key in design_lst:
            design_dict["design_type"] = key
            design_dict["conf"] = value

    for key, value in final_pred.items():
        if key in bottomwear_lst:
            bottomwear_dict["bottomwear_type"] = key
            bottomwear_dict["conf"] = value

    for key, value in final_pred.items():
        if key in footwear_lst:
            footwear_dict["footwear_type"] = key
            footwear_dict["conf"] = value

    return final_dets

def del_dir(path):
    status = shutil.rmtree(path, ignore_errors=False, onerror=None)
    return status

def generate_name(filename):    
    ext = filename.split('.')[-1]
    name = generate(size=12)
    random_name  = "{}.{}".format(name,ext)
    return random_name

def generate_urlname(url):   
    ext = url.split('.')[-1]
    name = generate(size=12)
    random_name  = "{}.{}".format(name,ext)
    return random_name

def rename_file(filename, random_name):
    try :
        status = os.rename(filename, random_name)
    except:
        pass
    return status

def clear_image(path):
    status = os.remove(path)
    return status



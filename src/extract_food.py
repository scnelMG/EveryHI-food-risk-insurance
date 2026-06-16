def extract_food_label(filelist):
    foodlist = []
    for filename in filelist:
        filename1 = filename.lstrip('Label/trans_labels_')
        findname = filename1.find('_')
        foodname = filename1[findname+1:]
        foodlist.append(foodname)
    return foodlist

def extract_food_img(filelist):
    foodlist = []
    for filename in filelist:
        filename1 = filename.rstrip('New')
        findname = filename1.find(' ')
        foodname = filename1[findname+1:]
        foodlist.append(foodname)
    return foodlist

def match_food(foodname, filelist):
    x = ''
    for filename in filelist:
        if foodname in filename:
            x = filename
    return x
    


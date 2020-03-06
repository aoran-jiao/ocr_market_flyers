from PIL import Image
import pytesseract

import os
import cv2


directory_in_str =  './Cropped photo'
directory = os.fsencode(directory_in_str)

f_name = None
n = 0
ind = -1
image_list = []
for file in os.listdir(directory):
     filename = os.fsdecode(file)
     n+=1
     if filename.endswith(".jpg"):
        f_name = os.path.join(directory, file)
        im = Image.open(f_name) 
        image_list.append(im)

        if n == ind:
            break
     else:
         continue

# label'./files/flyer_images/week_15_page_2.jpg'

def within(lab, corners):
    for pin in [corners[:2],corners[2:],[corners[0],corners[3]],[corners[2],corners[1]]]:
        for c in lab:
            if c[0]<=pin[0]<=c[2] and c[1]<=pin[1]<=c[3]:
                return True 
            for kin in [c[:2],c[2:],[c[0],c[3]],[c[2],c[1]]]:
                if corners[0]<=kin[0]<=corners[2] and corners[1]<=kin[1]<=corners[3]:
                    return True
                    
            if corners[0]<=c[0]<=c[2]<=corners[2] and (c[1]<=corners[1]<=corners[3]<=c[3]):
                return True
            if c[0]<=corners[0]<=corners[2]<=c[2] and (corners[1]<=c[1]<=c[3]<=corners[3]):
                return True

        if pin[0]<0 or pin[1]<0 or pin[0]>3326 or pin[1]>3401: 
            return True
    return False

s = 3326,3401
p_matrix = []
rows = list(np.linspace(200,s[0]-320,10).astype(np.int32))
cols = list(np.linspace(200,s[1]-320,10).astype(np.int32))

for r in rows:
    for j in cols:
        p_matrix.append([r,j])

p_matrix = np.array(p_matrix)

# for i in position:
#     print(' ')
#     for j in i:
#         print(j,end = ' ')

label = []
data = []
for d in range(60):
    # max_n = np.random.randint(8,8)
    max_n = 12
    per = np.random.permutation(np.arange(len(image_list)))[:max_n]
    temp_image_list = [image_list[i] for i in per]
    im = Image.new("RGB", (3300, 3401), color = (255, 255, 255))
    lab = []
    for _ in range(len(temp_image_list)):
        temp_p = p_matrix[:]

        img = temp_image_list.pop()
        repeat = True
        n_times = 100
        skip = False
        while repeat:
            n_times-=1
            if n_times == 0:
                skip = True
                break
            position = temp_p[np.random.choice(np.arange(temp_p.shape[0]))]
            
            np.delete(temp_p,np.where(temp_p==position))
            p = [position[0]-img.size[0]//2, position[1]-img.size[1]//2]
            corners = [*p,p[0]+img.size[0],p[1]+img.size[1]]
            repeat = within(lab,corners)

        if skip:
            continue


        im.paste(img,corners)
        
        lab.append(corners)
    
    im.save('data/'+str(d)+'.jpg')
    label.append(lab)
    # data.append(im)

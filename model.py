# importing required libraries
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
from matplotlib import patches

pd_data = []
for i in range(len(label)):
    for j in range(len(label[i])):
        pd_data.append(np.array([str(i)+'.jpg',0,*list(map(int,label[i][j]))]))

pd_data =np.vstack(pd_data)

train = pd.DataFrame(data=pd_data,columns=['id','type','xmin','ymin','xmax','ymax'])
for i in train.columns[1:]:
    train[i] = train[i].astype(np.int32)
# train.head()
train,test = train.iloc[:train.shape[0]*8//10],train.iloc[train.shape[0]*8//10]
train.to_csv('train.csv',index=False)
test.to_csv('test.csv',index = False)

import tensorflow as tf
trainset = tf.data.Dataset.from_tensor_slices((train[['id']].values,train[['xmin','ymin','xmax','ymax']].values))
for loc,label in trainset:
    print(loc.numpy()[0],label)
    break
    
fig = plt.figure()

#add axes to the image
ax = fig.add_axes([0,0,1,1])

# read and plot the image
image = plt.imread('data/1.jpg')
plt.imshow(image)

# iterating over the image for different objects
for _,row in train[train.id == "1.jpg"].iterrows():
    xmin = row.xmin
    xmax = row.xmax
    ymin = row.ymin
    ymax = row.ymax
    
    width = xmax - xmin
    height = ymax - ymin

    print(width,height,xmin,xmax,ymin,ymax)

    # assign different color to different classes of objects
    # if row.type == 'font':
    edgecolor = 'r'
    ax.annotate('font', xy=(xmax-40,ymin+20))

    rect = patches.Rectangle((xmin,ymin), width, height, edgecolor = edgecolor, facecolor = 'none')
    ax.add_patch(rect)
# plt.show()


!git clone https://github.com/kbardool/keras-frcnn.git

data = pd.DataFrame()
data['format'] = train['id']

# as the images are in train_images folder, add train_images before the image name
for i in range(data.shape[0]):
    data['format'][i] = 'data/' + data['format'][i]

# add xmin, ymin, xmax, ymax and class as per the format required
for i in range(data.shape[0]):
    data['format'][i] = data['format'][i] + ',' + str(train['xmin'][i]) + ',' + str(train['ymin'][i]) + ',' + str(train['xmax'][i]) + ',' + str(train['ymax'][i]) + ',' + train['type'][i]

data.to_csv('annotate.txt', header=None, index=None, sep=' ')

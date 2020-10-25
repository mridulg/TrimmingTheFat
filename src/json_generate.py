import json
from tqdm import trange
import random

n_frames = 1000

LABELS = ['person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 'boat', 'traffic light', 'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball', 'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket', 'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed', 'dining table', 'toilet', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone', 'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush']

n_labels = len(LABELS)

temp = [0,0,0,0,0,0,0,0,0,1,3,5,1,1,3]

box_size = [3,5,10,50,]

dictionary = {}

img_size = 416


for l in LABELS:
	dictionary[l]=[]

# print json.dumps(dictionary,indent=2)

for frame_num in trange(n_frames):
	rnum = random.choice(temp)
	subset = [ LABELS[i] for i in sorted(random.sample(xrange(len(LABELS)), rnum)) ]
	# print subset

	for label in subset:
		length = random.choice(box_size)
		width = random.randint(1, length)
		center_x = random.randint(0 + length//2 + 1, img_size - length//2 - 1)
		center_y = random.randint(0 + width//2 + 1, img_size - width//2 - 1)
		dictionary[label].append({"frame_num":frame_num, "coordinates": (center_x,center_y), "length":length, "width":width})
		# print dictionary[label][frame_num]
		# print

print json.dumps(dictionary)

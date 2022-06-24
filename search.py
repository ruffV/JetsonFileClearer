#!/usr/bin/python3
import jetson.inference
import jetson.utils
import argparse
import os
from os.path import isfile, join
network =input("which network to use? googlenet/resnet-18\n")
target = input("What should the classified photos contain?\n")
file_names_raw=os.listdir(".")
file_names=[]
for f in file_names_raw:
	if f.endswith(".jpg"):
		file_names.append(f)
net=jetson.inference.imageNet(network)
matching_files=[]
non_matches=[]
for f in file_names:
	img=jetson.utils.loadImage(f)
	class_idx, confidence = net.Classify(img)
	if((target in net.GetClassDesc(class_idx) or net.GetClassDesc(class_idx) in target) and confidence>=0.5):
		matching_files.append(f)
	else:
		non_matches.append(f)
print("matching files: "+str(matching_files))
print("non-matching files: "+str(non_matches))

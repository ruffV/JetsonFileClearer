#!/usr/bin/python3
import jetson.inference
import jetson.utils
import argparse
import os
from os.path import isfile, join
network =input("which network to use? googlenet/resnet-18\n")
target = input("What should the classified photos contain?\neach object should be seperated by a comma\n").split(",")
file_names_raw=os.listdir(".")
file_names=[]
for f in file_names_raw:
	if f.endswith(".jpg"):
		file_names.append(f)
net=jetson.inference.imageNet(network)
matching_files=[]
non_matches=[]
for f in file_names:
	added=False
	img=jetson.utils.loadImage(f)
	class_idx, confidence = net.Classify(img)
	for term in target:
		if((term in net.GetClassDesc(class_idx) or net.GetClassDesc(class_idx) in term) and confidence>=0.5):
			matching_files.append(f)
			added=True
	if(added==False):
		non_matches.append(f)
print("matching files: "+str(matching_files))
print("non-matching files: "+str(non_matches))

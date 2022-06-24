# idTechFinal
Program to look for which images in a folder contain a certain object. If you have many photos and only need some, this would be useful.

## The Algorithm
Gets names of all files in current folder that end with ".jpg". Loops through all, running user chosen network on each. Which images contain the desired object and contain it with a confidence level greater than 0.5 are added to a list which is returned to the user.

## Running this project
1. SSH into a jetson Nano with cmake, git, and jetson-inference package
2. googlenet and resnet-18 installed with cmake
3. Import search.py into a seperate directory
4. Import all images you would like to perform the program on into this directory(must be .jpg format)
5. run python3 search.py
6. When prompted, select a network and desired object
7. Will return list of files containing object and list of all files without

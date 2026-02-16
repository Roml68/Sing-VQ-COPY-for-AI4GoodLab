import pandas as pd
import pickle
import torch
import os

# root= "/home/summy/projects/batch/batch" # Replace with the actual path to your PKL file
# # file="01April_2010_Thursday_heute-6694.pt"
# file="01April_2010_Thursday_heute-6695.pt"

# file_path=os.path.join(root,file)


# data = torch.load(file_path, map_location='cpu', weights_only=False)
# poses = data['poses_3d_filtered']  # Shape: (T, 61, 3)
# if isinstance(poses, torch.Tensor):
#         poses = poses.numpy()

# print(len(poses[0]))


root= "/home/summy/projects/Sign-VQ/Sign-VQ-Transformer/summy_files/data" # Replace with the actual path to your PKL file
# file="01April_2010_Thursday_heute-6694.pt"
file="train_original.pt"
file="train.pt"


file_path=os.path.join(root,file)


data = torch.load(file_path, map_location='cpu', weights_only=False)
# print(data.keys())
poses = data['22November_2009_Sunday_tagesschau-5479']  # Shape: (T, 61, 3)
if isinstance(poses, torch.Tensor):
        poses = poses.numpy()



print(poses.keys())
print(poses["text"])

print(poses['poses_3d'])
print(poses['poses_3d'][0].size())



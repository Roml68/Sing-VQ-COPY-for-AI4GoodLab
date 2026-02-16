import os
import torch
import pandas as pd
from tqdm import tqdm

# -----------------------------
# PATHS
# -----------------------------
pt_folder = "/home/summy/projects/batch/batch"
csv_path = "/home/summy/projects/CorrNet_Plus-main/CorrNet_Plus_CSLR/dataset/phoenix2014-T/annotations/manual/PHOENIX-2014-T.train.corpus.csv"
output_path = "/home/summy/projects/Sign-VQ/Sign-VQ-Transformer/summy_files/data/train_s.pt"

# -----------------------------
# LOAD CSV
# -----------------------------
df = pd.read_csv(csv_path, sep="|")

# Create dictionary indexed by name for fast lookup
metadata_dict = {
    row["name"]: {
        "text": row["translation"],     # translation column
        "gloss": row["orth"],           # gloss column
        "speaker": row["speaker"],
    }
    for _, row in df.iterrows()
}

# -----------------------------
# BUILD FINAL DATASET
# -----------------------------
final_dataset = {}

for filename in tqdm(os.listdir(pt_folder)):
    if filename.endswith(".pt"):

        key = filename.replace(".pt", "")
        pt_path = os.path.join(pt_folder, filename)

        # Load pose tensor (T, 61, 3)
        poses_3d = torch.load(pt_path)
        poses_3d= poses_3d["poses_3d_filtered"]

        if key not in metadata_dict:
            print(f"Warning: {key} not found in CSV")
            continue

        final_dataset[key] = {
            "name": key,
            "text": metadata_dict[key]["text"],
            "gloss": metadata_dict[key]["gloss"],
            "poses_3d": poses_3d,  # (T, 61, 3)
            "speaker": metadata_dict[key]["speaker"],
        }

# -----------------------------
# SAVE EVERYTHING
# -----------------------------
torch.save(final_dataset, output_path)

print(f"\nSaved dataset with {len(final_dataset)} samples to {output_path}")

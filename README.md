## Installation

### Requirements

```bash
# Create and activate a new conda environment (recommended)
conda create --name signVQ python=3.8
conda activate signVQ

# Install PyTorch with CUDA support
# Please change PyTorch CUDA version to match your system!
conda install pytorch==2.4.0 torchvision==0.19.0 torchaudio==2.4.0 pytorch-cuda=11.8 -c pytorch -c nvidia

# Install other dependencies
pip install -r ./requirements.txt
```
### Transforming the format of the .pt files

```bash
# download the pt files for train, dev and test save into a folder and
# then run the file construct_the_format_sign_vq.py to get the right format

python construct_the_format_sign_vq.py --folder_pt --gt_file --output_folder ./data/name_file.pt

# Make sure the resulting files are saved under the data folder with the names train.pt, dev.pt and test,pt
```

### Train the model

```bash
python __main__.py train vq ./config/codebook/codebook_config.yaml
```


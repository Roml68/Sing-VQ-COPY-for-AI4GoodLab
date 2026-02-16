### MAIN FOR REPLYCATING


import os
import argparse

from train_s import train, test


def main():
    os.environ["WANDB_DIR"] = "/tmp"
    # ap = argparse.ArgumentParser("Sign Level VQVAE!!")

    # ap.add_argument("mode", choices=["train", "test"], help="train or test a model")
    # ap.add_argument("type", choices=["translate", "vq"], help=" translation or VQ")
    # ap.add_argument(
    #     "config_path", metavar="config-path", type=str, help="path to YAML config file"
    # )
    # # VQ model
    # ap.add_argument(
    #     "--var-vq_path", type=str, help="path to the VQ model for translation"
    # )


    # args = ap.parse_args()

    mode="train"
    type="vq"
    config_path="/home/summy/projects/Sign-VQ/Sign-VQ-Transformer/config/codebook/codebook_config.yaml"



    if mode == "train":
        config_path = train(cfg_file=config_path, mode=type)
        test(cfg_file=config_path, mode=type)
    elif mode == "test":
        test(cfg_file=config_path, mode=type)
    else:
        raise ValueError("Unknown mode")


if __name__ == "__main__":
    main()

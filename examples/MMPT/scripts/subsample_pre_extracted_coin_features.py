#!/usr/bin/env python
import argparse
import os

import numpy as np
from tqdm.auto import tqdm


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Fixes the S3D features provided by COIN dataset authors to be used here."
                    " These provided features have 10 features per second, as opposed to 1, which is what's required.")
    parser.add_argument("input_feature_dir")
    parser.add_argument("output_feature_dir")
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    for filename in tqdm(os.listdir(args.input_feature_dir)):
        if filename.endswith(".npy"):
            try:
                video_features = np.load(os.path.join(args.input_feature_dir, filename))
                np.save(os.path.join(args.output_feature_dir, filename), video_features[::10])
            except ValueError as e:
                print(f"Failed to process the file {filename}:", e)


if __name__ == "__main__":
    main()

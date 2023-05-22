# Action co-occurrence

## Setup

Clone this repo:

```bash
git clone https://github.com/facebookresearch/fairseq
```

Then set it up with Conda:

```bash
cd examples/MMPT/
conda env create
conda activate videoclip
```

Follow the instructions to have COIN set up and ready, including:

```bash
mkdir pretrained_models
wget https://www.rocq.inria.fr/cluster-willow/amiech/howto100m/s3d_howto100m.pth -P pretrained_models
wget https://www.rocq.inria.fr/cluster-willow/amiech/howto100m/s3d_dict.npy -P pretrained_models

mkdir -p runs/retri/videoclip
wget https://dl.fbaipublicfiles.com/MMPT/retri/videoclip/checkpoint_best.pt -P runs/retri/videoclip

mkdir -p data/coin
wget https://raw.githubusercontent.com/coin-dataset/annotations/master/COIN.json -P data/coin
```

**The following didn't work for fine-tuning, we couldn't reproduce the results
(we managed to do it for zero-shot but it's basically predicting all as 0).
Seems like COIN's provided S3D features don't come from MIL-NCE.**

Download COIN S3D features and save the path in the env var `$COIN_S3D_FOLDER`. Then run:

```bash
./arrange_coin_files.sh
mkdir data/feat
ln -s $COIN_S3D_FOLDER/all data/feat/feat_coin_s3d
```

Then:

```bash
python locallaunch.py projects/retri/videoclip.yaml --dryrun
```

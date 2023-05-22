#!/usr/bin/env bash

cd "$COIN_S3D_FOLDER"
find {0..5}/ -type f -name '*.npy' -exec sh -c 'ln -s "../{}" "all/$(basename {})"' \;

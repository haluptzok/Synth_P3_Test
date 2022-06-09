#!/bin/bash -x

# generate the src and tests
python gen_P3.py
# run the src code - make sure it works
python src_gen_P3.py
cat src_gen_P3.py

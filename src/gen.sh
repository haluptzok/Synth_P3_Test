#!/bin/bash -x
# generate the src and tests
python gen_P3.py
# Take a look at the code - look OK?
# head -150 src_gen_P3.py
# cat src_gen_P3.py
# cat test_gen_P3.py
# run the src code - make sure it works
python src_gen_P3.py
python test_gen_P3.py
grep assert test_gen_P3.py | wc -l


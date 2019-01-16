#%%
from src.constant import *
from src.core import transcribe
import numpy as np
import argparse
#%%
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--sentence', type=str, required=True)
    parser.add_argument('-d', '--debug', type=int, default=0, help="debugger - 0: False; 1: True")
    parser.add_argument('-e', '--is_enable_espeak', type=int, default=1)
    args = parser.parse_args()
    print(transcribe(**vars(args)))    



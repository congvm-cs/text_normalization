#%%
import pandas as pd

#%%
data = pd.read_csv('./britfone.main.3.0.1.csv', names=['word', 'ipa'])

#%%
# for i in data.iterrow():
    # preprocess()
list_data = []
for i in data.iterrows():
    list_data.append(i)

#%%
next(i)[1]['word']

#%%
dict_1 = {}
prev = ""
current = ""
for i in list_data[::-1]:
    current = preprocess(str(i[1]['word']))
    if current != prev:
        dict_1[current] = str(i[1]['ipa']).strip().split()

    prev = current
#%%
dict_1

#%%
list_data[0][1]['word']

#%%
import numpy as np
np.save('ipa_pronounce_dict.npy', dict_1)


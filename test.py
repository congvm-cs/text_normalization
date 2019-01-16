#%%
from constant import *
import subprocess
#import cmudict
import numpy as np
import argparse

#%%
ipa_pronounce_dict = np.load('ipa_pronounce_dict.npy').item()

#%%
def remove_spec_punc(word):
    ret_= []
    for i in word:
        tmp = ""
        for j in i:
            if ord(j) not in removed_pun_ipa_list:
                tmp += j
        ret_.append(tmp)
    return ret_


def remove_single_word(ipa_list):
    ret_ = []
    if len(ipa_list) < 2:
        return ipa_list
    else:
        ret_.append(ipa_list[0])
        for i in range(1, len(ipa_list)):
            if len(ipa_list[i]) > 1 or i in viet_vowel_alpha:
                ret_.append(ipa_list[i])
    return ret_

def remove_viet_single_word(viet_words):
    ret_ = []
    viet_compound_alpha.extend(viet_consonant_apha)
    if len(viet_words) < 2:
        return viet_words
    else:
        ret_.append(viet_words[0])

        for i in range(1, len(viet_words)):
            if i not in viet_compound_alpha:
                ret_.append(viet_words[i])

    return ret_


def postprocessing(ipa_list):
    ret_ = []
    for i in ipa_list:
        if len(i) <= 0:
            ret_.append(i)
        else:
            if len(i) > 1 and i[-1] in ['s', 'd', 'z', 'đ', 'v', '_', 'l', 'b', 'x']:
                ret_.append(i[:-1])
            else:
                ret_.append(i)
    return ret_


def remove_invalid_tail(viet_words):
    ret_= [tail_map_dict[w] if w in tail_map_dict else w for w in viet_words]
    return ret_


def mapping(ipa_list):
    ret_= []
    
    if len(ipa_list) < 1:
        return ipa_list
    else:
        # Check first words
        # For exception
        if ipa_list[0] in first_exception_word:
            ret_.append(first_exception_word[ipa_list[0]])
        elif ipa_list[0] in map_dict:
            ret_.append(map_dict[ipa_list[0]])
        else:
            ret_.append(ipa_list[0] )

        for w in ipa_list[1:]:
            if w in map_dict:
                ret_.append(map_dict[w])
            else:
                ret_.append(w)
    return ret_


def get_ipa(word):
    cmd = "espeak {} --ipa=1 -q".format(word)
    result = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
    result = result.stdout.read().decode('utf-8').split("\n")[0]
    result = result.split("_")
    return remove_spec_punc(result)


def merge_ipa(ipa_form):
    ipa_list = list(map_dict.keys())
    ret_= []
    current_idx = 0
    while current_idx < len(ipa_form):
        temp = ""
        if "".join([i for i in ipa_form[current_idx:current_idx+2]]) in ipa_list:
            temp += "".join([i for i in ipa_form[current_idx:current_idx+2]])
            ret_.append(temp)
            current_idx += 2
        else:
            ret_.append(ipa_form[current_idx])
            current_idx += 1
    return ret_ 


def preprocess_ipa_form(ipa_list):
    ret_ = []
    for i in ipa_list:
        if len(i) != 0:
            ret_.append(i)
    return ret_


def ipa_to_viet(ipa_form):
    ret_= []
    current_idx = 0
    while current_idx < len(ipa_form):
        if ipa_form[current_idx:current_idx+2] in viet_compound_alpha:
            ret_.append(ipa_form[current_idx:current_idx+2])
            current_idx += 2
        else:
            ret_.append(ipa_form[current_idx])
            current_idx += 1
    return ret_ 


def split_consonant_vowel_combination(viet_form):
    viet_form.extend(['_'])
    viet_consonant_apha.extend(viet_compound_alpha)
    ret_ = []
    temp = ""
    for i in range(len(viet_form)-1):
        if (viet_form[i] in viet_consonant_apha) and (viet_form[i+1] in viet_consonant_apha):
            temp += viet_form[i]
            ret_.append(temp)
            temp = ""
        else:
            temp += viet_form[i]
    ret_.append(temp)
    return ret_

#%%
def preprocess(word):
    """Returns a string of words stripped of punctuation"""
    punct_str = '!"#$%&\'\()*+,-./:;<=>/?@[\\]^_`{|}~«» '
    word =  word.strip(punct_str).lower()
    word = ''.join([i for i in word if not i.isdigit()])
    word = word.replace("(", "")
    word = word.replace(")", "")
    return word


def vowel_count(word):
    count = 0
    for i in word:
        if i in viet_vowel_alpha:
            count += 1
    return count


def double_consonant(ipa_list):
    ipa_list.append('_')
    viet_consonant_apha.extend(viet_compound_alpha)
    ret_ = []
    i = 0
    while i < len(ipa_list)-1:
        if ipa_list[i] not in viet_consonant_apha and ipa_list[i+1] in viet_consonant_apha:
            ret_.append(ipa_list[i])
            ret_.append(ipa_list[i+1])
            i+=1
        else:
            ret_.append(ipa_list[i])
            i+=1
    return ret_


def vowel_form_split(single_viet_word):
    ret_= []
    current_idx = 0
    viet_char_with_vowel.extend(viet_char_with_consonant)
    while current_idx < len(single_viet_word):
        temp = ""
        if "".join([i for i in single_viet_word[current_idx:current_idx+5]]) in viet_char_with_vowel:
            temp += "".join([i for i in single_viet_word[current_idx:current_idx+5]])
            ret_.append(temp)
            current_idx += 5
        elif "".join([i for i in single_viet_word[current_idx:current_idx+4]]) in viet_char_with_vowel:
            temp += "".join([i for i in single_viet_word[current_idx:current_idx+4]])
            ret_.append(temp)
            current_idx += 4
            
        elif "".join([i for i in single_viet_word[current_idx:current_idx+3]]) in viet_char_with_vowel:
            temp += "".join([i for i in single_viet_word[current_idx:current_idx+3]])
            ret_.append(temp)
            current_idx += 3
            
        elif "".join([i for i in single_viet_word[current_idx:current_idx+2]]) in viet_char_with_vowel:
            temp += "".join([i for i in single_viet_word[current_idx:current_idx+2]])
            ret_.append(temp)
            current_idx += 2
        else:
            ret_.append(single_viet_word[current_idx])
            current_idx += 1
    return ret_ 


def merge(word_list):
    word_list.append('_')
    ret = []
    i = 0
    while i < len(word_list)-1:
        temp = ""
        if word_list[i] in viet_consonant_apha and word_list[i+1] in viet_char_with_vowel:
            temp += word_list[i]
            temp += word_list[i+1]
            i+=2
        else:
            temp+= word_list[i]
            i+=1
        ret.append(temp)
    return ret

def combine_valid_viet(viet_words):
    ret1 = [merge(vowel_form_split(i)) for i in viet_words]
    
    ret2 = []
    for i in ret1:
        ret2.extend(i)

    ret2 = remove_single_word(ret2)
    return ret2

def split_special_ipa(ipa_list):
    ret = []
    for char in ipa_list:
        if char in special_ipa_char:
            ret.extend(special_ipa_char[char])
        else:
            ret.append(char)
    return ret

def get_ipa_from_dictionary(word):
    try:
        return ipa_pronounce_dict[word]
    except:
        raise Exception("'{}' is not in dictionary".format(word))


#%%
def add_diacritic(viet_words):
    ret = []
    for single_viet_word in viet_words:
        ret_= []
        current_idx = 0
        while current_idx < len(single_viet_word):
            temp = ""   
            if "".join([i for i in single_viet_word[current_idx:current_idx+2]]) in viet_valid_with_diacritic:
                temp += "".join([i for i in single_viet_word[current_idx:current_idx+2]])
                ret_.append(viet_valid_with_diacritic[temp])
                current_idx += 2
            else:
                ret_.append(single_viet_word[current_idx])
                current_idx += 1
        ret.append("".join([i for i in ret_]))
    return ret


#%%
def translate_with_printer(words):
    words  = words.strip().split()
    ret = ""
    for word in words:
        ipa = get_ipa_from_dictionary(word); print(ipa)
        ipa = remove_spec_punc(ipa); print(ipa)
        ipa = split_special_ipa(ipa); print(ipa)
        ipa = double_consonant(ipa); print(ipa)
        ipa = merge_ipa(ipa); print(ipa)
        viet_words = mapping(ipa); print(viet_words)
        viet_words = split_consonant_vowel_combination(viet_words); print(viet_words)
        viet_words = remove_single_word(viet_words); print(viet_words)
        viet_words = combine_valid_viet(viet_words); print(viet_words)
        viet_words = remove_invalid_tail(viet_words); print(viet_words)
        viet_words = remove_viet_single_word(viet_words); print(viet_words)
        viet_words = add_diacritic(viet_words); print(viet_words)
        ret += " ".join([word for word in viet_words]) + " "
    return ret

def translate(words):
    words  = words.strip().split()
    ret = ""
    for word in words:
        word = word.lower()
        ipa = get_ipa_from_dictionary(word)
        ipa = remove_spec_punc(ipa)
        ipa = split_special_ipa(ipa)
        ipa = double_consonant(ipa)
        ipa = merge_ipa(ipa)
        viet_words = mapping(ipa)
        viet_words = split_consonant_vowel_combination(viet_words)
        viet_words = remove_single_word(viet_words)
        viet_words = combine_valid_viet(viet_words)
        viet_words = remove_invalid_tail(viet_words)
        viet_words = remove_viet_single_word(viet_words)
        viet_words = add_diacritic(viet_words)
        ret += " ".join([word for word in viet_words]) + " "
    return ret

#%%
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--s', type=str, required=True)
    args = parser.parse_args()

    print(translate_with_printer(args.s))




#===================================================================##

# #%%
# import pandas as pd

# #%%
# data = pd.read_csv('./britfone.main.3.0.1.csv', names=['word', 'ipa'])

# #%%
# # for i in data.iterrow():
#     # preprocess()
# list_data = []
# for i in data.iterrows():
#     list_data.append(i)

# #%%
# next(i)[1]['word']

# #%%
# dict_1 = {}
# prev = ""
# current = ""
# for i in list_data[::-1]:
#     current = preprocess(str(i[1]['word']))
#     if current != prev:
#         dict_1[current] = str(i[1]['ipa']).strip().split()

#     prev = current
# #%%
# dict_1

# #%%
# list_data[0][1]['word']

# #%%
# import numpy as np
# np.save('ipa_pronounce_dict.npy', dict_1)

# #%%

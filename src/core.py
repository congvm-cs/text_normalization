#%%
from src.constant import *
import subprocess
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
    viet_vowel_alpha.extend(kept_single_char) # open set
    ret_ = []
    if len(ipa_list) < 2:
        return ipa_list
    else:
        ret_.append(ipa_list[0])
        for i in range(1, len(ipa_list)):
            if (len(ipa_list[i]) > 1) or (ipa_list[i] in viet_vowel_alpha):
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
    viet_consonant_apha.extend(viet_compound_alpha)

    if len(viet_words) < 2:
        return [tail_map_dict[w] if w in tail_map_dict else w for w in viet_words]
    else:
        last_word = viet_words[-1]
        if last_word in viet_consonant_apha:
            return viet_words[:-1]
        else:
            return viet_words

def mapping_single_char(viet_words):
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
    viet_consonant_apha_with_exception.extend(viet_compound_alpha)
    ret_ = []
    i = 0
    while i < len(ipa_list)-1:
        if ipa_list[i] not in viet_consonant_apha_with_exception and ipa_list[i+1] in viet_consonant_apha_with_exception:
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
def transcribe(sentence, is_enable_espeak,  debug=False):
    if is_enable_espeak:
        ipa_getter = get_ipa
    else:
	    ipa_getter = get_ipa_from_dictionary
	    
    function_list = [ipa_getter, remove_spec_punc, split_special_ipa, 
                    double_consonant, merge_ipa, mapping, split_consonant_vowel_combination,
                    remove_single_word, combine_valid_viet, remove_invalid_tail, mapping_single_char, 
                    remove_viet_single_word, add_diacritic]

    if len(sentence) == 0:
        return sentence
    else:
        words  = sentence.strip().split()
        ret = ""
        for word in words:
            for func in function_list:
                word = func(word)
                if debug: print(func.__name__,"----->", word, sep="\t")
            
            curr = ""
            prev = ""    
            for i in range(len(word)):
                curr = word[i]
                if curr != prev:
                    ret += curr + " "
                prev = curr
    return ret 



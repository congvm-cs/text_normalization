from constant import *
import subprocess
import cmudict
import numpy as np


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


def post_mapping(ipa_list):
    ret_= []
    for w in ipa_list:
        ret_.append(tail_map_dict[w] if w in tail_map_dict else w)
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
    cmd = "espeak {} --ipa=1".format(word)
    result = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
    result = result.stdout.read().decode('utf-8').split("\n")[0]
    print(result)
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


def split(viet_form):
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


def preprocess(word):
    """Returns a string of words stripped of punctuation"""
    punct_str = '!"#$%&\'()*+,-./:;<=>/?@[\\]^_`{|}~«» '
    return word.strip(punct_str).lower()

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

def run(word):
    print("------------------------------------------")
    print(word)
    print("--")
    ipa = get_ipa(word)
    print(ipa)

    ret = double_consonant(ipa)
    print(ret)

    ret = merge_ipa(ret)
    print(ret)

    ret = mapping(ret)
    print(ret)

    ret = split(ret)
    print(ret)

    ret = mapping(ret)
    print(ret)

    ret = postprocessing(ret)
    print(ret)
    
    ret = remove_single_word(ret)
    print(ret)

    ret = post_mapping(ret)
    print(ret)

    ret = preprocess_ipa_form(ret)
    print(ret)

    ret = remove_single_word(ret)
    print(ret)

    ret1 = []
    for i in ret:
        ret1.append(merge(vowel_form_split(i)))
    
    ret2 = []
    for i in ret1:
        ret2.extend(i)
    # print(ret2)


    ret2= remove_single_word(ret2)
    print(ret2)


#==========================================================#
cmu_dict = dict(cmudict.dict())

# list_of_words = "English is a West Germanic language that was first spoken in early medieval England and is now the third most widespread native language in the world after Standard Chinese and Spanish as well as the most widely spoken Germanic language Welcome to the WikiWikiWeb, also known as. A lot of people had their first wiki experience here. This community has been around since 1995 and consists of many people. We always accept newcomers with valuable contributions. If you haven't used a wiki before, be prepared for a bit of CultureShock. The usefulness of Wiki is in the freedom, simplicity, and power it offers."
# list_of_words = preprocess(word=list_of_words).split(' ')

# for word in cmu_dict.keys():
#     run(word)

run('malaysia')
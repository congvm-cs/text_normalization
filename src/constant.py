def get_num():
    return 1

removed_pun_ipa_list = [712, 716]

special_ipa_char = {
    "əl" : ['əl', 'l']
}

tail_map_dict = {
    "juː": "iu",
    "st" : "t",
    "s": "sờ",
    "p": "pờ",
    "b": "bờ",
    "t": "tờ",
    "ol": "o",
    "ov": "op",
    "ph": "phờ",
    "v": "vờ"
}


viet_consonant_apha_with_exception = [
 'b',
 'c',
 'k',
 'l',
 'n',
 'm',
 'p',
 'q',
 's',
 't',
 'f',
 'dʒ',
 'ʃ',
 'tʃ',
 '_']


viet_consonant_apha = [
 'b',
 'c',
 'd',
 'đ',
 'g',
 'h',
 'k',
 'l',
 'n',
 'm',
 'p',
 'q',
 'r',
 's',
 't',
 'v',
 'x',
 'f',
 'dʒ',
 'ʃ',
 'tʃ',
 '_']

viet_vowel_alpha = ['a','ă', 'â', 'e', 'ê', 'o', 'ô', 'ơ', 'u', 'ư', 'i', 'y']

viet_compound_alpha = ['gi', 'ch', 'gh', 'ph', 'tr', 'th', 'qu', 'kh', 'gi', 'ng', 'nɡ', '_', 'nɡ', 'ng', 'tɹ', 'tr']

kept_single_char = ['v']

first_exception_word = {
    "juː": "du",
    "ju": "du",
    "f": "ph"
}

viet_char_with_consonant = ['ch', 'gh', 'gi', 'kh', 'ng', 'ngh', 'nh', 'ph', 'qu', 'th', 'tr']

viet_char_with_vowel = ['a',
 'ac',
 'ach',
 'ai',
 'am',
 'an',
 'ang',
 'anh',
 'ao',
 'ap',
 'at',
 'au',
 'ay',
 'ăc',
 'ăm',
 'ăn',
 'ăng',
 'ăp',
 'ăt',
 'âc',
 'âm',
 'ân',
 'âng',
 'âp',
 'ât',
 'âu',
 'ây',
 'e',
 'ec',
 'em',
 'en',
 'eng',
 'eo',
 'ep',
 'et',
 'ê',
 'êch',
 'ênh',
 'êm',
 'ên',
 'êp',
 'êt',
 'êu',
 'i',
 'ic',
 'ich',
 'im',
 'in',
 'ing',
 'inh',
 'ip',
 'it',
 'iu',
 'ia',
 'iêc',
 'iêm',
 'iên',
 'iêng',
 'iêp',
 'iêt',
 'iêu',
 'o',
 'oc',
 'oi',
 'om',
 'on',
 'ong',
 'op',
 'ot',
 'oong',
 'ooc',
 'oa',
 'oac',
 'oach',
 'oai',
 'oam',
 'oan',
 'oang',
 'oanh',
 'oao',
 'oap',
 'oat',
 'oay,oăc',
 'oăm',
 'oăn',
 'oăng',
 'oăt,',
 'oe',
 'oen',
 'oeo',
 'oet oem',
 'oeng',
 'ô',
 'ôc',
 'ôi',
 'ôm',
 'ôn',
 'ông',
 'ôp',
 'ôt',
 'ơ',
 'ơc',
 'ơi',
 'ơm',
 'ơn',
 'ơp',
 'ơt',
 'u',
 'uc',
 'ui',
 'um',
 'un',
 'ung',
 'up',
 'ut',
 'ua',
 'uôc',
 'uôi',
 'uôm',
 'uôn',
 'uông',
 'uôt',
 'uây',
 'uân',
 'uâng',
 'uât',
 'uơ',
 'uê',
 'uênh',
 'uêch',
 'uy',
 'uych',
 'uynh',
 'uyt',
 'uyu,uyn',
 'uyp',
 'uya',
 'uyên',
 'uyêt',
 'ư',
 'ưc',
 'ưi',
 'ưu',
 'ưng',
 'ưt',
 'ưm',
 'ưa',
 'ươc',
 'ươi',
 'ươm',
 'ươn',
 'ương',
 'ươp',
 'ươt',
 'ươu',
 'y',
 'yêm',
 'yên',
 'yêng',
 'yêt',
 'yêu']

# http://www.antimoon.com/how/pronunc-soundsipa.htm
map_dict = {
    "ɡ" : "g",
    "a": "a",
    "iə": "ơ",
    "ɐ": "â",
    "ə": "ơ",
    "əʊ": "âu",
    "ʌ":    "â",
    "ɑː": "a",
    "ɑ":    "o",
    "æ":    "a",
    "e":    "e",
    "ə":    "ơ",
    "ɜ":    "ơ",
    "ɪ":    "i",
    "i":    "i",
    "ɒ":    "o",
    "ɔ":    "ô",
    "ʊ":    "u",
    "u":    "u",
    "b":    "b",
    "d":    "đ",
    "f":    "ph",
    "g":    "g",
    "h":    "h",
    "j":    "d",
    "k":    "c",
    "l":    "l",
    "m":    "m",
    "n":    "n",
    "ŋ":    "ng",
    "p":    "p",
    "r":    "r",
    "s":    "s",
    "ʃ":    "s",
    "t":    "t",
    "tʃ":   "ch",
    "θ":    "th",
    "ð":    "đ",
    "v":    "v",
    "w":    "qu",
    "z":    "d",
    "ʒ":    "d",
    "dʒ":   "ch", 
    "ju":   "iu", # exception
    "juː": "iu",
    "ɔk":   "oc",
    "ɑʊ": "ao",
    "tɹ": "tr",
    "ɒs" : "ot",
    "ɪl": "iu", 
    "ɪv": "i",
    "əl": "ô",
    "ɛ": "e",
    "ɹ" : "r",
    "ɜː": "ơ",
    "iː": "i",
    "uː": "u",
    "ɔː": "o",
    "juː": "iu",
    "t" : "t",
    "ʌl": "âu",
    "əs": "et",
    "ol": "o",
    "ɪð": "it",
    "ɪs": "it",
    "ʌb": "âp",
    "ɪʃ": "it",
    # "ɪ": "i"
    "ɜːd": "ơt",
    "ov": "op",
    "os": "ot",
    "ab": "ap",
    "ɪd": "it",
    "ʌs": "ât",
    "kh": "kh",
    "ag": "a",
    "ʌɡ": "âc",
    "ʌz": "ơt",
    "aɪ": "ai",
    "aʊ": "ao",
    "eɪ": "ây",
    "oʊ": "âu", # go >< home
    "ɔɪ": "oi",
    "eə": "e",
    "ɪə": "ia",
    "ʊə": "ua",
    'ɛl': "eo",
    "ɜːb": "ơp",
    "ɛs" : "et",
    "əʊn" : "ôn"
}

phoneme_dict = {
 '#'  : "",
 'aa0': "ờ",
 'aa1': "ớ",
 'aa2': "ờ",
 'ae0': "ờ" ,
 'ae1': "ớ",
 'ae2': "ờ",
 'ah0': "ờ",
 'ah1': "",
 'ah2': "",
 'ao0': "",
 'ao1': "",
 'ao2': "",
 'aw0': "",
 'aw1': "áu",
 'aw2': "ó",
 'ay0': "",
 'ay1': "",
 'ay2': "",
 'b': "",
 'ch': "",
 'd': "",
 'dh': "",
 'eh0': "",
 'eh1': "ế",
 'eh2': "",
 'er0': "ơ",
 'er1': "",
 'er2': "",
 'ey0': "",
 'ey1': "ấy",
 'ey2': "",
 'f': "",
 'g': "",
 'hh': "",
 'ih0': "",
 'ih1': "",
 'ih2': "",
 'iy0': "i",
 'iy1': "í",
 'iy2': "ì",
 'jh': "",
 'k': "",
 'l': "",
 'm': "",
 'n': "",
 'ng': "",
 'ow0': "âu",
 'ow1': "ấu",
 'ow2': "ầu",
 'oy0': "",
 'oy1': "",
 'oy2': "",
 'p': "",
 'r': "",
 's': "",
 'sh': "",
 't': "",
 'th': "",
 'uh0': "",
 'uh1': "",
 'uh2': "",
 'uw0': "u",
 'uw1': "ú",
 'uw2': "ù",
 'v': "",
 'w': "",
 'y': "",
 'z': "",
 'zh': ""
}

viet_valid_with_diacritic = {
    'ac': 'ác',
    'at': 'át',
    'ap': 'áp',
    'âc': 'ấc',
    'ât': 'ất',
    'âp': 'ấp',
    'ăc': 'ắc',
    'ăt': 'ắt',
    'ăp': 'ắp',
    'ot': 'ót',
    'oc': 'óc',
    'ôc': 'ốc',
    'ôt' : 'ốt',
    'ơt': 'ớt',
    'ơp': 'ớp',
    'ic': 'íc',
    'it': 'ít',
    'ip': 'íp',
    'et': 'ét',
    'ec': 'éc',
    'ep': 'ép',
    'êc': 'ếc',
    'êt': 'ết',
    'ut': 'út',
    'uc': 'úc',
    'up': 'úp',
    'ưc': 'ức',
    'ưt': 'ứt',
    'yt': 'ýt',
    "pô": "pồ",
    "đơ": "đờ"
    
}
from tqdm import tqdm
import jieba

def load_dictionary(dict_path):
    print("\nStart loading dictionary ...")
    dictionary = []
    max_word_length = 1
    word_count = 0
    dict_file = open(dict_path, 'r', encoding='utf-8')
    for line in tqdm(dict_file.readlines()):
        dictionary.append(line.split()[0])
        word_count += 1
        if len(line.split()[0]) > max_word_length:
            max_word_length = len(line.split()[0])
            # print(line.split()[0])  # 当前分词长度最长的词
    dict_file.close()
    print('Complete dictionary initialization.')
    print('Dictionary has "', word_count, '" words.')
    print('Max-word-length is "', max_word_length, '".')
    return dictionary, max_word_length

def RMMSegment(raw_file, result_file, dict_path):
    dictionary, max_word_length = load_dictionary(dict_path)




path = "../data/dictionary/dict.txt"
dict, maxWordLength = load_dictionary(path)
# print(dict)



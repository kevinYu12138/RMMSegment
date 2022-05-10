from tqdm import tqdm
import jieba

def load_dictionary(dict_path):
    print("\nStart loading dictionary ...")
    dictionary = []
    max_word_length = 1
    word_count = 0
    dict_file = open(dict_path, 'r', encoding='utf-8')
    for line in tqdm(dict_file.readlines()):
        dictionary.append(line.split()[0])  # 将原dict.txt中的第一列提取出来
        word_count += 1
        if len(line.split()[0]) > max_word_length:
            max_word_length = len(line.split()[0])
            # print(line.split()[0])  # 当前分词长度最长的词
    dict_file.close()
    print('Complete dictionary initialization.')
    print('Dictionary has "', word_count, '" words.')
    print('Max-word-length is "', max_word_length, '".')
    return dictionary, max_word_length

def RMMSegment(input_file, output_file, dict_path):
    dictionary, max_word_length = load_dictionary(dict_path)
    f1 = open(input_file, 'r', encoding='utf-8')
    f2 = open(output_file, 'w', encoding='utf-8')
    input = f1.read()
    output = []
    text_length = len(input)  # 整个文本长度
    begin = text_length - max_word_length  # 开始匹配的位置，是词典中最大分词长度的大小
    end = 0
    while begin > 0:
        word = input[begin: begin+max_word_length]
        while len(word) > 1:
            if word in dictionary:
                output.append(word)
                input = input[:len(input)-len(word)]
                break  # 匹配成功，则保留长度大的词，停止匹配
            else:
                word = word[1:]  # 若词典中没有当前所截的词，则每次向后缩小匹配的长度，直至word只剩1个字符
                if len(word) == 1:
                    output.append(word)
                    input = input[:len(input) - len(word)]
        begin -= 1  # 当前最大分词长度的词

    # 当begin = 0时，不可再向前收缩，须由后向前截断匹配词
    if begin == 0:
        end = len(input)  # 此时input的长度应小于最大分词长度
        while end > 0:
            word = input
            while len(word) > 0:
                if word in dictionary:
                    output.append(word)
                    input = input[:len(input) - len(word)]
                    end = end - len(word)
                    break
                else:
                    word = word[1:]
                    if(len(word) == 1):
                        output.append(word)
                        input = input[:len(input) - len(word)]
                        end = end - len(word)
                        break

    print('After reverse-max-match segment: ', output)
    while len(output) > 0:
        f2.write(output.pop()+'\n')
    f1.close()
    f2.close()

path = "data/dictionary/dict.txt"
RMMSegment("data/text/背影.txt", "data/text/rmm_segment.txt", "data/dictionary/dict.txt")



import jieba
rawFile = open("../data/text/背影.txt", 'r', encoding='utf-8')
correctFile = open("../data/text/correct.txt", 'w', encoding='utf-8')
word_lists = jieba.lcut_for_search(rawFile.read())  # 使用jieba分词的精确搜索引擎模式分词
for word in word_lists:
    correctFile.write(word + '\n')  # 将jieba分词后的文本，用作正确的分词文本
rawFile.close()
correctFile.close()
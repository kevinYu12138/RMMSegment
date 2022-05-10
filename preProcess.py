import jieba
rawFile = open("../data/text/背影.txt", 'r', encoding='utf-8')
correctFile = open("../data/text/correct.txt", 'w', encoding='utf-8')
word_lists = jieba.cut(rawFile.read(), cut_all=False)  # 使用jieba分词的精确模式分词,因为全模式和精确引擎搜索模式会对长词再次进行分解，造成冗余
for word in word_lists:
    correctFile.write(word + '\n')  # 将jieba分词后的文本，用作正确的分词文本
rawFile.close()
correctFile.close()
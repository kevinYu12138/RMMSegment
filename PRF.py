correct_segment = open("../data/text/correct.txt", 'r', encoding="utf-8")
rmm_segment = open("../data/text/rmm_segment.txt", 'r', encoding="utf-8")
correct = []
my_segment = []
print("\nStart loading correct text ...")
for line in correct_segment.readlines():  # 加载正确分词结果
    correct.append(line)
print("Correct segmentation has ", len(correct), "words.")

print("\nStart loading rmm_segment text ...")
for line in rmm_segment.readlines():  # 加载rmm分词结果
    my_segment.append(line)
print("RMM_segmentation has ", len(my_segment), "words.\n")

seg_correct = 0  # 正确分词个数
for i in range(len(my_segment)):
    if my_segment[i] in correct:
        seg_correct += 1
print(seg_correct, "correct words in rmm_segmentation.\n")

precision = seg_correct / len(my_segment)
recall = seg_correct / len(correct)
F1 = (2*precision) / (precision + recall)

print("Precision is", precision)
print("Recall is", recall)
print("F1 is", F1)

import csv
pos_words = []
neg_words = []

print("\n The Given Training Data Set \n")
with open('6NAVIEBAYESIANCLASSIFIER2/data6.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        if row[-1] == "pos":

            for word in row[0].split():
                pos_words.append(word)
        else:
            for word in row[0].split():
                neg_words.append(word)


print("Positive words:", pos_words)
print("Negative words:", neg_words)

print("\n The Given Test Data Set \n")
test_sentence = "I feel good"
print("Test Sentence:", test_sentence)

test_words = test_sentence.split()

pos_prob = len(pos_words)/(len(pos_words)+len(neg_words))
neg_prob = len(neg_words)/(len(pos_words)+len(neg_words))

for i in range(len(test_words)):
    pos_count = pos_words.count(test_words[i])
    neg_count = neg_words.count(test_words[i])
    pos_prob = pos_prob * pos_count/(len(pos_words))
    neg_prob = neg_prob * neg_count/(len(neg_words))


if pos_prob > neg_prob:
    print("Positive Sentiment")
else:
    print("Negative Sentiment")

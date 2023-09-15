from transformers import pipeline
import csv
import string


def read_data(url):
    data = []
    with open(url) as file:
        reader = csv.reader(file, delimiter="\t")
        for row in reader:
            cur = preprocessing(row[1])
            data.append(cur)
    return data


def remove_punctuation(text):
    no_punctuation = "".join([i for i in text if i not in string.punctuation])
    return no_punctuation


def preprocessing(text):
    clean = remove_punctuation(text).strip()
    return clean


if __name__ == '__main__':

    sentence_url = './stanfordSentimentTreebank/datasetSentences.txt'
    sentence_data = read_data(sentence_url)[1:]  # [1:] is for removing the header

    sentiment_pipeline = pipeline(model="finiteautomata/bertweet-base-sentiment-analysis")
    with (open("./output.txt", "w") as f):
        for i, result in enumerate(sentiment_pipeline(sentence_data[:10])):
            print(result, sentence_data[i], file=f)

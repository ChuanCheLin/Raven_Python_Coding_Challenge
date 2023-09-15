import requests
from zipfile import ZipFile

if __name__ == '__main__':
    url = "http://nlp.stanford.edu/~socherr/stanfordSentimentTreebank.zip"
    response = requests.get(url)
    with open("stanfordSentimentTreebank.zip", 'wb') as f:
        f.write(response.content)

    with ZipFile("./stanfordSentimentTreebank.zip", 'r') as z:
        z.extractall("./")

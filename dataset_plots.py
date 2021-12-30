from matplotlib import pyplot as plt
from collections import Counter
with open("D:/tesis2/cv-corpus-7.0-2021-07-21/es/train.tsv", encoding="utf8") as f:
    headers = f.readline()[:-1].split('\t')
    data = []
    for row in f:
        d = { header:value for header,value in zip(headers,row[:-1].split('\t')) }
        data.append(d)


subdata = [ d['accent'] for d in data ]
labels,heights = zip(*Counter(subdata).items())
plt.bar(range(len(heights)),heights)
plt.xticks(range(len(labels)), labels, rotation='vertical')
plt.title('accent')
plt.show()

subdata = [ d['gender'] for d in data ]
labels,heights = zip(*Counter(subdata).items())
plt.pie(heights)
plt.legend(labels)
plt.title('gender')
plt.show()
import wordcloud
#from wordcloud import WordCloud

import matplotlib.pyplot as plt
import pandas as pd
import ast

df1 = pd.read_csv('total_flood.csv',converters={'text_pre_list':ast.literal_eval}, encoding='utf-8')
f1 = open('stopwords.txt','r',encoding='utf-8')
stopwords = []
for line in f1.readlines() :
    stopwords.append(line.strip())
print(set(stopwords))
print(len(set(stopwords)))
comment_words = ''
#stopwords = set(STOPWORDS)

# iterate through the csv file
for val in df1.text_pre_list:
    #print(val)
    # typecaste each val to string
    for i in val :
        #print(i)
        comment_words += ''.join(i)+' '
    #val = str(val)

    # split the value
    #tokens = val.split()

    # Converts each token into lowercase
    #for i in range(len(tokens)):
        #tokens[i] = tokens[i].lower()

    #comment_words += " ".join(tokens)+" "
#print(comment_words)
wc = wordcloud.WordCloud(width = 1000, height = 800,
                background_color ='white',
                font_path='STFangSong.ttf',
                stopwords = set(stopwords),
                min_font_size = 10).generate(comment_words)

# plot the WordCloud image
plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wc)
plt.axis("off")
plt.tight_layout(pad = 0)

plt.show()
wc.to_file('weibo_word_cloud.png')

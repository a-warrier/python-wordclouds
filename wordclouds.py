import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

# Load data as pandas dataframe
df1 = pd.read_csv('Datafiniti_Hotel_Reviews.csv')

# Filter positive reviews (greater than or equal to 4 out of 5)
df_high = df1[df1['reviews.rating'] >= 4]

# Remove irrelevant words
stopwords = set(STOPWORDS)
stopwords.update(["hotel", "room"])

# Generate wordcloud for positive reviews
positive = " ".join(review for review in df_high['reviews.text'])
wordcloud1 = WordCloud(stopwords=stopwords, background_color = "white",
                       width=1600, height=900)
wordcloud1.generate(positive)
plt.imshow(wordcloud1, interpolation='bilinear')
plt.axis("off")
plt.show()

# Save this wordcloud as a file
wordcloud.to_file("good-reviews.png")

# Filter negative reviews (lesser than or equal to 2 out of 5)
df_low = df1[df1['reviews.rating'] <= 2]

# Remove irrelevant words
stopwords.update(["hotel", "room", "rooms", "stayed", "told", "will", "checked", "u", "us"])

# Generate wordcloud for negative reviews
negative = " ".join(review for review in df_low['reviews.text'])
wordcloud2 = WordCloud(stopwords=stopwords, background_color = "white",
                       width=1600, height=900, colormap=matplotlib.cm.inferno)
wordcloud2.generate(negative)
plt.imshow(wordcloud2, interpolation='bilinear')
plt.axis("off")
plt.show()

# Save this wordcloud as a file
wordcloud2.to_file("bad-reviews.png")

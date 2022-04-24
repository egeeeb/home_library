from matplotlib import pyplot as plt
from wordcloud import WordCloud


class Wordcloud:
    def __init__(self, data):
        self.data = data

    def show(self):
        wordcloud = WordCloud(width=1024, height=1024,
                              background_color='black',
                              min_font_size=10).generate_from_frequencies(frequencies=self.data)

        plt.figure(figsize=(16, 16), facecolor=None)
        plt.imshow(wordcloud)
        plt.axis("off")
        plt.tight_layout(pad=0)

        plt.show()

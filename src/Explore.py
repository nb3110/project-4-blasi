#summary statistics function

import pandas as pd
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

def summary_statistics(df):
    """
    This function returns summary statistics for a Pandas DataFrame input. Categorical variables will have NaNs for distribution related statistics
    """
    sum_stats_df = (df.describe().round(2)).transpose().reset_index()
    describe_df = pd.concat([df.isnull().sum()/(df.shape[0]),df.isnull().sum(),df.dtypes],axis=1)
    describe_df = describe_df.set_axis(["null_%","null_count","dtype"],axis=1).reset_index()
    return pd.merge(describe_df,sum_stats_df, how="left", on="index").sort_values("dtype").set_index("index").round(2)




def wordcloud_plot(series,stopwords):
    # Create stopword list:
    wordcloud = WordCloud(stopwords= stopwords, max_font_size=100, max_words=100, background_color="white",width=800, height=600).generate(' '.join(series.dropna()))
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    return plt.imshow(wordcloud)
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


#read
df = pd.read_csv(r"data\glassdoor_reviews.csv")
#drop unnecesary columns
df = df.drop(["location","diversity_inclusion","ceo_approv","outlook","recommend"], axis=1)


#define sentiment analysis function

sia = SentimentIntensityAnalyzer()
def compound (x):
    try:
        return sia.polarity_scores(x)["compound"]
    except:
        "Nan"

#apply sentiment analysis to headline, pros, cons reviews        

df["headline_compound"] = df.apply(lambda row: compound(row["headline"]),axis=1)
df["pros_compound"] = df.apply(lambda row: compound(row["pros"]),axis=1)
df["cons_compound"] = df.apply(lambda row: compound(row["cons"]),axis=1)

#define new variables for analysis

df["pros_cons_gap"] = df["pros_compound"]-df["cons_compound"]
df["overall_compound_rating"] = df[["work_life_balance","culture_values","career_opp","comp_benefits","senior_mgmt"]].mean(axis=1)

#export to csv

df.to_csv("data\glassdoor_tableau.csv")
# Fake-Real_News
It should be no surprise to us that while news sources provide most of the information we learn every day, it is questionable whether the news we read is credible and trustworthy. Differentiating legitimate and correct news articles
from ‘fake’ or misleading ones is an important task, raising the interest of journalists, policy makers and researchers in many fields such as social science and data science. Specifically in the context of health, the consequences of delivering illegitimate news can be paramount and irreversible.
In this assignment, we will be working on a dataset comprising more than 1,000 health-related news articles, the reviews of these articles, and tweets about the new articles.
Using this dataset, we will have an opportunity to learn how to identify ‘good’ and ‘bad’ news by characterising some linguistic patterns of news, as well as comparing different news outlets based on their correctness of reporting
# Dataset
The dataset consists of more than 1,000 health-related news articles, the reviews of these articles, and tweets about the new articles.
## News articles
The name of each file corresponds to the ID of the article and is in
the format story_reviews_xxxxx.json, where each x is a digit; for example,
story_reviews_00001.json contains the news article of ID story_reviews_00001.
## News reviews
Each article was independently reviewed by at least one expert, based on a list of
criteria. Against each criterion, the article receives a rating of satisfactory, not
satisfactory or not applicable, and an explanation for the rating. Each article is
also assigned an overall rating between 0 (least accurate) to 5 (most accurate).
## Tweets
News articles are shared on Twitter. Each tweet is represented by a unique integer. Note that a tweet may appear
multiple times, so if you count tweets, you need to avoid counting duplicates

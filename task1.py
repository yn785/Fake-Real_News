def task1():
    import json 
    import pathlib 
    import pandas as pd
    Tweets_path="/course/data/a1/engagements/HealthStory.json"
    NewsArticle_path="/course/data/a1/content/HealthStory/"
    NewsReviews_path="/course/data/a1/reviews/HealthStory.json"
    with open(Tweets_path) as json_file:
        sample_json = json.load(json_file)
        Tweets_replies_retweets=[]
        Number_of_tweets=0
        for story in sample_json: #iterate through each story_review
            tweets=sample_json[story]['tweets'] # getting a list of tweets for the story review
            replies=sample_json[story]['replies'] # getting a list of replies for the story review
            retweets=sample_json[story]['retweets']# getting a list of retweets for the story review
            Tweets_replies_retweets.extend(tweets) #adding the tweets to the list
            Tweets_replies_retweets.extend(replies) #adding the replies to the list
            Tweets_replies_retweets.extend(retweets)
        Number_of_tweets=len(set(Tweets_replies_retweets)) #removing duplicates
        json_file.close()

    with open(NewsReviews_path) as json_file: #counting number of reviews
        sample_json = json.load(json_file)
        counter=0
        for titles in sample_json: 
            counter+=1
        json_file.close()

    initial_count = 0
    for path in pathlib.Path(NewsArticle_path).iterdir(): #counting number of articles
        if path.is_file():
            initial_count += 1

    listDf={
        "Total number of articles":initial_count,
        "Total number of reviews":counter,
        "Total number of tweets":Number_of_tweets
    }
    with open("task1.json", "w") as outfile: #dumping into json file
        json.dump(listDf,outfile,indent=1)
    return

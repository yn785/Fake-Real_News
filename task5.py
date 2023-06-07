def task5():
    import pandas as pd
    import json 
    import numpy as np
    Tweets_path="/course/data/a1/engagements/HealthStory.json"
    NewsReviews_path="/course/data/a1/reviews/HealthStory.json"
    counter=0
    ratings=[]
    with open(Tweets_path) as json_file:
        sample_json = json.load(json_file)
        Tweets_replies_retweets=[]
        Number_of_tweets=0
        storyidsinorder=[]
        LIST=[]
        for story in sample_json: #iterate through each story_review
            tweets=sample_json[story]['tweets'] # getting a list of tweets for the story review
            replies=sample_json[story]['replies'] # getting a list of replies for the story review
            retweets=sample_json[story]['retweets']# getting a list of retweets for the story review
            Tweets_replies_retweets.extend(tweets) #adding the tweets to the list
            Tweets_replies_retweets.extend(replies) #adding the replies to the list
            Tweets_replies_retweets.extend(retweets) #adding the retweets to the list
            Number_of_tweets=len(set(Tweets_replies_retweets)) #counter the number of non-duplicate ids
            Tweets_replies_retweets.clear() # clearing the list
            LIST.append({
                "story_review": story,
                "Number of tweets":Number_of_tweets
            })
            Number_of_tweets=0
        with open(NewsReviews_path) as json_files:
            sample_jsons = json.load(json_files)
            for items in sample_jsons:
                ratings.append(items["rating"])
        for inside in LIST:
            inside.update({"rating":ratings[counter]})
            counter+=1
        #switching List to dataframe and creating the table
        LIST_pd= pd.DataFrame(LIST)
        LIST_pd.drop("story_review", axis=1, inplace= True)
        grp=LIST_pd.groupby(ratings)
        SUM=grp['Number of tweets'].agg([np.average])
        SUM=SUM.rename(columns={"average": "Number of Tweets"})
        plt=SUM.plot.bar(y="Number of Tweets", title= "Number of Tweets per Rating")
        plt.set_ylabel("Number of Tweets")
        plt.set_xlabel("Rating")
        plt.figure.savefig("task5.png",bbox_inches='tight')
    return

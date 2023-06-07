def task7():
    import os
    import json
    import math
    import pandas as pd
    path="/course/data/a1/content/HealthStory/"
    NewsReviews_path="/course/data/a1/reviews/HealthStory.json"
    files = os.listdir(path)
    number_of_articles=len(files)
    Real_news=[]
    Fake_news=[]
    List=[]
    
    with open(NewsReviews_path) as json_filez:#creating real and fake news list
        json_samplez=json.load(json_filez)
        for x in json_samplez:
            if(x["rating"]>=3):
                Real_news.append(x["news_id"])
            else:
                Fake_news.append(x["news_id"])
    with open("task6.json") as json_file: #check number of real news articles a word has
        json_sample=json.load(json_file)
        for items in json_sample:
            real_counter=0
            fake_counter=0
            for review in json_sample[items]:
                if review in Real_news:
                    real_counter+=1
                else:
                    fake_counter+=1
            PRw=real_counter/len(Real_news)
            PFw=fake_counter/len(Fake_news)
            if len(json_sample[items])!=number_of_articles and len(json_sample[items])>=10: #check that words is not available in all reviews
                if(PRw>0.0 and PRw<1) and (PFw>0.0 and PFw<1):
                    Rodds=PRw/(1-PRw)
                    Fodds=PFw/(1-PFw)
                    ORw=Fodds/Rodds
                    LORw=math.log10(ORw)
                    List.append({
                        "word":items,
                        "log_odds_ratio":round(LORw,5)
                    })#creating the list             
    List_df=pd.DataFrame(List)
    List_df.to_csv("task7a.csv",index=False)
    #Part B
    plt=List_df.plot.hist(title= "Distribution of Log_odds_ratio")
    plt.set_xlabel("log_odds_ratio")
    plt.figure.savefig("task7b.png")
    #Part C
    table=pd.read_csv("task7a.csv")
    Asc=table.sort_values("log_odds_ratio", ascending=True)
    desc=table.sort_values("log_odds_ratio", ascending=False)
    frames=[Asc.head(15),desc.head(15)]
    result=pd.concat(frames)
    plt=result.plot.bar(x="word", y="log_odds_ratio", title= "Top/lowest 15 Log_odds_ratio per words") 
    plt.set_ylabel("log_odds_ratio")
    plt.figure.savefig("task7c.png",bbox_inches='tight')
    return

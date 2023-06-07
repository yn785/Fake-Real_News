def task4():
    import json 
    import pandas as pd
    import numpy as np
    NewsReviews_path="/course/data/a1/reviews/HealthStory.json"
    List=[]
    with open (NewsReviews_path) as json_file:
        json_sample=json.load(json_file)
        for items in json_sample: #getting information required from the dataset
            if items["news_source"]!="":
                news_source= items["news_source"]
                rating=items["rating"]
                title=items["title"]
                List.append({
                    "news_source": news_source,
                    "rating": rating,
                    "Title": title
                })
    List_pd=pd.DataFrame(List)# changing List to dataframe
    grp=List_pd.groupby("news_source")# grouping by news_source
    averages=grp['rating'].agg([np.average])#getting average rating per news_source
    values=List_pd['news_source'].value_counts().rename("num_articles")# getting the number of articles per news source and renaming it
    new_table = pd.concat([values, averages], axis='columns') # pasting both tables together 
    new_table=new_table.rename_axis("news_source")# renaming the indexs
    new_table.rename(columns={"average" : "avg_rating"} ,inplace=True) # renaming the average column
    new_table=new_table.sort_values('news_source', ascending=True)# sorting the values by new_source
    new_table.to_csv("task4a.csv")# exporting to csv
    table=pd.read_csv("task4a.csv")
    table=table.loc[table["num_articles"]>=5] #finding news sources with more than 5 articles
    table=table.sort_values("avg_rating", ascending=True)
    plt=table.plot.bar(x="news_source", y="avg_rating", title= "Average Rating for each news source with >=5 articles")
    plt.set_ylabel("avg_rating")
    plt.figure.savefig("task4b.png",bbox_inches='tight')
    return

def task3():
    import datetime
    import json
    import os
    import pandas as pd
    import matplotlib as plt
    List=[]
    path="/course/data/a1/content/HealthStory/"
    files = os.listdir(path) #All files in the path
    for items in files: #Accessing all files
        with open(path+items) as json_file: #opening the files 
            sample_json=json.load(json_file)
            if sample_json['publish_date']!=None: #checking for articles with pulishing date
                date=datetime.datetime.fromtimestamp(sample_json['publish_date']) # getting date 
                year=date.year #extracting the year
                month=date.month # extracting the month
                day=date.day # extracting the day
                List.append({
                    "news_id":items.replace(".json",""),
                    "year":year,
                    "month":month,
                    "day":day

                }) 
    List_df=pd.DataFrame(List) #transforming the List to dataframe
    List_df=List_df.sort_values('news_id', ascending=True) # making list in ascending order
    List_df.to_csv("task3a.csv", index=False) #exporting to CVS
    #partB
    Num_articles_per_year=List_df['year'].value_counts().rename_axis('year').reset_index(name='counts')# number of articles published for each year  
    Num_articles_per_year_df=pd.DataFrame(Num_articles_per_year).set_index('year').sort_values('year',ascending=True)
    ax = Num_articles_per_year_df.plot.bar(title="Number of articles per year")
    ax.set_ylabel("Number of Articles")
    ax.set_xlabel("Year")
    ax.figure.savefig("task3b.png",bbox_inches='tight')
    return

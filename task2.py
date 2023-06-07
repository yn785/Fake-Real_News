def task2():
    import json
    import pandas as pd
    NewsReviews_path="/course/data/a1/reviews/HealthStory.json"
    with open(NewsReviews_path) as json_file:
        sample_json=json.load(json_file)
        Num_satisfactory=0
        List=[]
        for items in sample_json:
            news_id=items["news_id"] #getting news ids
            title=items["title"] #getting tilte
            og_title=items["original_title"] #getting original_title
            rating=items["rating"] #getting rating
            for answers in items["criteria"]:   #check if review is Satisfactory
                if(answers["answer"]=="Satisfactory"):
                    Num_satisfactory+=1
            List.append({
                'news_id':news_id,
                'news_title':title,
                'review_title':og_title,
                'rating':rating,
                'num_satisfactory':Num_satisfactory
            }) # creating the list
            Num_satisfactory=0
    List_df=pd.DataFrame(List)
    List_df=List_df.sort_values('news_id', ascending=True)
    List_df.to_csv('task2.csv')
    return

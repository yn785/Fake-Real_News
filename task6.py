def task6():
    import os
    import json
    import re
    import nltk
    import pandas as pd
    from nltk.corpus import stopwords
    def in_stop_words(no_punct):
        no_punct_list=[]
        stopwordz= stopwords.words('english')
        for x in no_punct:
            if not x in stopwordz and len(x)>1:
                no_punct_list.append(x)
        return no_punct_list
    NewsArticle_path="/course/data/a1/content/HealthStory/"
    files = sorted(os.listdir(NewsArticle_path)) #All files in the path
    words=[]
    List={}
    for items in files: #Accessing all files
        with open(NewsArticle_path+items) as json_file: #opening the files 
            sample_json=json.load(json_file)
            non_alpha =re.sub(r'[^a-zA-Z\s\n\t]',' ', sample_json["text"])#1
            no_punct =re.sub(r'[\n\t]',' ', non_alpha)#2
            no_punct=no_punct.lower()#3
            no_punct=nltk.wordpunct_tokenize(no_punct)#4
            no_punct=in_stop_words(no_punct)#5 and 6         
            for word in set(no_punct): # checking if the word exsits in List already or not
                if word in List:
                    List[word].append(items.replace(".json",""))
                else:
                    List[word]=[items.replace(".json","")]
    with open("task6.json", "w") as outfile:
        json.dump(List,outfile, sort_keys=True)
    return

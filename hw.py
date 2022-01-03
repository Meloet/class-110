import statistics
import random
import pandas as pd
import plotly.figure_factory as ff
df=pd.read_csv("medium_data.csv")
data=df["reading_time"].tolist()
finaldata=[]
def sampling():
    dataset=[]
    for i in range(0,100):
        randomIndex=random.randint(0,len(data)-1)
        value=data[randomIndex]
        dataset.append(value)
    mean=statistics.mean(dataset)
    finaldata.append(mean)

for i in range(0,1000):
    sampling()

graph=ff.create_distplot([finaldata],["sampledata"],show_hist=False)
graph.show()
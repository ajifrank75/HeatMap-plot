from matplotlib import pyplot
import pandas as pd
import seaborn as sns
url = 'https://raw.githubusercontent.com/resbaz/r-novice-gapminder-files/master/data/gapminder-FiveYearData.csv'
df1 = pd.read_csv(url)
print(df1)
df1.to_csv('Dataset.csv',index=False)
df2 = pd.pivot_table(df1,values='lifeExp',index='continent',columns='year')
print(df2)
pyplot.figure(figsize=(15,10))# width by height
# This shows the average life expectancy for each year
sns.heatmap(df2,annot=True,fmt=".2f").get_figure().savefig('Seaborn_HeatMap.png')

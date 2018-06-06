import pandas as pd

df = pd.read_csv('M:\Python\\numpy\Pandas\data\data\gapminder.tsv',sep='\t')

#print(df[['year','pop']])

df_year_pop = df[['year','pop','country']]
#print(df_year_pop)

df_year_pop_true = ((df_year_pop['pop'] > 10267083) &
                   (df_year_pop['year'] > 2005) & 
                   (df_year_pop['country'] == 'United Kingdom'))
#print(df_year_pop_true)

print(df[df_year_pop_true])

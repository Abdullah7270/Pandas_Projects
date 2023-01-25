import pandas as pd

df = pd.read_html('https://en.wikipedia.org/wiki/List_of_largest_companies_in_Saudi_Arabia')
df = df[1]
#print(df)
df.to_csv('companies.csv', index=False)





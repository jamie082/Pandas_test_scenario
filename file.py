# Python code demonstrate to create a
# Pandas DataFrame with lists of
# dictionaries as well as
# row and column indexes.
  
import pandas as pd
  
# List1

dict = (['chemical', 'executive', 'recruiter', '>100', 'Australia', 'Chemical', '1/15/23'],
        ['chemical', 'executive', 'recruiter', '>100', 'Canada', 'Chemical', '1/15/23'],
        ['chemical', 'executive', 'recruiter', '>100', 'Germany', 'Chemical', '1/15/23'])


df = pd.DataFrame(dict, columns = ['Keyword', 'Rank', 'URL', 'Location', 'Volume', 'Tags', 'date_scraped'])

df2 = pd.DataFrame(dict, columns = ['Keyword', 'Rank', 'URL', 'Location', 'Volume', 'Tags', 'date_scraped'])

df3 = pd.DataFrame(dict, columns = ['Keyword', 'Rank', 'URL', 'Location', 'Volume', 'Tags', 'date_scraped'])



# print dataframe
print(df, "\n")

print (df2, "\n")

print (df3, "\n")

print (df4)

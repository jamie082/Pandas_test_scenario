# Python code demonstrate to create a
# Pandas DataFrame with lists of
# dictionaries as well as
# row and column indexes.
  
import pandas as pd
  
# List1

dict = (['chemical', 'executive', 'recruiter', '>100', 'Australia', 'Chemical', '2/20/23'],
        ['chemical', 'executive', 'recruiter', '>100', 'Canada', 'Chemical', '2/20/23'],
        ['chemical', 'executive', 'recruiter', '>100', 'Germany', 'Chemical', '2/20/23'])


df = pd.DataFrame(dict, columns = ['Keyword', 'Rank', 'URL', 'Location', 'Volume', 'Tags', 'date_scraped'])

df2 = pd.DataFrame(dict, columns = ['Keyword', 'Rank', 'URL', 'Location', 'Volume', 'Tags', 'date_scraped'])

df3 = pd.DataFrame(dict, columns = ['Keyword', 'Rank', 'URL', 'Location', 'Volume', 'Tags', 'date_scraped'])

# print dataframe
print(df, "\n")

# modify date_scraped
new_df = (['chemical', 'executive', 'recruiter', '>100', 'Australia', 'Chemical', '1/15/23'],
          ['chemical', 'executive', 'recruiter', '>100', 'Canada', 'Chemical', '1/15/23'],
          ['chemical', 'executive', 'recruiter', '>100', 'Germany', 'Chemical', '1/15/23'])

# print second column

new_output = pd.DataFrame(new_df, columns = ['Keyword', 'Rank', 'URL', 'Location', 'Volume', 'Tags', 'date_scraped'])
df.update(new_output)
print(df)

# print third column

third_column = (['chemical', 'executive', 'recruiter', '>100', 'Australia', 'Chemical', '3/1/23'],
                ['chemical', 'executive', 'recruiter', '>100', 'Canada', 'Chemical', '3/15/23'],
                ['chemical', 'executive', 'recruiter', '>100', 'Germany', 'Chemical', '3/1/23'])

new_output_column = pd.DataFrame(third_column, columns = ['Keyword', 'Rank', 'URL', 'Location', 'Volume', 'Tags', 'date_scraped'])
df.update(new_output_column)
print (df)

print (df3, "\n")

# Create a new df that loops like this:
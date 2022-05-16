## 1. Introduction ##

import pandas as pd
# read the data set into a pandas dataframe
f500 = pd.read_csv("f500.csv", index_col=0)
f500.index.name = None

# replace 0 values in the "previous_rank" column with NaN
f500.loc[f500["previous_rank"] == 0, "previous_rank"] = np.nan

f500_selection = f500.loc[:,'rank':'revenue_change'].head(5) #slice of columns




## 2. Reading CSV files with pandas ##

f500 = pd.read_csv('f500.csv')
f500.index.name = 0
f500.loc[f500["previous_rank"] == 0, "previous_rank"] = np.nan

f500.head(5)

## 3. Using iloc to select by integer position ##

fifth_row = f500.iloc[4,]

company_value = f500.iloc[0,0]

## 4. Using iloc to select by integer position continued ##

first_three_rows = f500.iloc[0:3]

first_seventh_row_slice = f500.iloc[[0,6],0:5]


## 5. Using pandas methods to create boolean masks ##

null_previous_rank = f500[f500['previous_rank'].isnull()][["company","rank","previous_rank"]]



## 6. Working with Integer Labels ##

null_previous_rank = f500[f500["previous_rank"].isnull()]

top5_null_prev_rank = null_previous_rank.iloc[:5,]

## 7. Pandas Index Alignment ##

previously_ranked = f500[f500['previous_rank'].notnull()]
rank_change = previously_ranked['previous_rank'] - previously_ranked['rank']
f500['rank_change'] = rank_change

## 8. Using Boolean Operators ##

#R over_265_and_china <- fortune %>% 
#R     filter(revenues > 265000 & country == 'China')

large_revenue = f500['revenues'] > 100000
negative_profits = f500['profits'] < 0

combined = large_revenue & negative_profits

big_rev_neg_profit = f500[combined]



## 9. Using Boolean Operators Continued ##

brazil_venezuela = f500[(f500['country'] == 'Brazil') | (f500['country'] == 'Venezuela')]

tech_outside_usa = f500[(f500['sector'] == 'Technology') & ~(f500['country'] == 'USA')].head()

## 10. Sorting Values ##

selected_rows = f500[f500['country'] == 'Japan']
sorted_rows = selected_rows.sort_values('employees', ascending = False) #remember to indicate what we want to sort by
top_japanese_employer = sorted_rows.iloc[0]['company'] #i must come first, due to iloc

print(top_japanese_employer)

## 11. Using Loops with pandas ##

# Create an empty dictionary, top_employer_by_country to store the results of the exercise.
top_employer_by_country = {}

# Use the Series.unique() method to create an array of unique values from the country column.
countries = f500['country'].unique()

for c in countries:
    # Use boolean comparison to select only rows that
    # correspond to a specific country
    selected_row = f500[f500['country'] == c]
    sorted_rows = selected_row.sort_values('employees', ascending = False)
    top_employer = sorted_rows.iloc[0]
    employer_name = top_employer['company']
    top_employer_by_country[c] = employer_name


## 12. Challenge: Calculating Return on Assets by Country ##

f500['roa'] = f500['profits'] / f500['assets']

top_roa_by_sector = {}

sectors = f500['sector'].unique()

for s in sectors:
    selected_rows = f500[f500['sector'] == s]
    sorted_rows = selected_rows.sort_values('roa', ascending = False)
    top_roa = sorted_rows.iloc[0]
    company_name = top_roa['company']
    top_roa_by_sector[s] = company_name

print(top_roa_by_sector)
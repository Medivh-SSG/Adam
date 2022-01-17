import matplotlib.pyplot as plt
import pandas as pd
cols = [ 'name' , 'gender', 'birth_count']

pieces = []
years = range(1880, 2010 + 1)
for i in years:
    df = pd.read_table('C:\\Users\\duaro\\OneDrive\\Рабочий стол\\names.'%i, sep = ',', engine = 'python' , names = cols)
    df['year'] = i
    pieces.append(df)
    data = pd.concat(pieces, ignore_index = True)
data


babynumber = data['gender'].value_counts()
babynumber


yearbirthcount = data.pivot_table('birth_count', 'year','gender', aggfunc = sum)
yearbirthcount



prop = data.copy()
prop['proportion'] = prop['birth_count'] / prop['birth_count'].sum()
prop




graph = pd.pivot_table(data, index = ['name','year'], values = ['birth_count'], aggfunc = 'sum')
print(graph['Johnny':'Johnny'].plot(y = 'birth_count', use_index = True))
print(graph['Natalie':'Natalie'].plot(y = 'birth_count', use_index = True))
print(graph['Bob':'Bob'].plot(y = 'birth_count', use_index = True))
print(graph['Bogdan':'Bogdan'].plot(y = 'birth_count', use_index = True))


for i in years:
    df = pd.read_table('C:\Users\duaro\OneDrive\Рабочий стол\\names\\yob%d.txt'%i, sep = ',', engine = 'python' , names = cols)
    df['year'] = i
    df = df.sort_values(by = 'birth_count', ascending = False)
    df = df.head(1)
    pieces.append(df)
    data = pd.concat(pieces, ignore_index = True)
df

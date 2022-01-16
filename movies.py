import pandas as pd
mnames = ['film_id', 'film_name_and_year', 'genres']
movies = pd.read_table('C:\\Users\\duaro\\OneDrive\\Рабочий стол\\gfgrf\\movies.dat', sep = '::', engine = 'python', names = mnames)
anames= ['user_id', 'gender', 'age', 'occuptaion', 'zip']
users = pd.read_table('C:\\Users\\duaro\\OneDrive\\Рабочий стол\\gfgrf\\users.dat', sep = '::', engine = 'python', names = anames)
rnames = ['user_id', 'film_id', 'raiting', 'timestemp']
raitings = pd.read_table('C:\\Users\\duaro\\OneDrive\\Рабочий стол\\gfgrf\\ratings.dat', sep = '::', engine = 'python', names = rnames)
data = pd.merge(raitings, users)
data2 = pd.merge(data, movies)
print(data2)
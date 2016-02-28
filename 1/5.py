# Коррелируют ли число братьев/сестер/супругов с числом родителей/детей? Посчитайте корреляцию Пирсона между признаками SibSp и Parch.
import pandas
data = pandas.read_csv('titanic.csv', index_col='PassengerId')
new_date = data[['SibSp', 'Parch']]
print(new_date.corr(method='pearson'))

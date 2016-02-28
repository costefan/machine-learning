# Какую долю пассажиры первого класса составляли среди всех пассажиров? Ответ приведите в процентах (число в интервале от 0 до 100, знак процента не нужен).
import pandas
data = pandas.read_csv('titanic.csv', index_col='PassengerId')
print(data[data['Pclass'] == 1].count()/data['Pclass'].count())

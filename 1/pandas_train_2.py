# Какой части пассажиров удалось выжить? Посчитайте долю выживших пассажиров. Ответ приведите в процентах (число в интервале от 0 до 100, знак процента не нужен).
import pandas
data = pandas.read_csv('titanic.csv', index_col='PassengerId')
print(data[data['Survived'] == 1].count()/data['Survived'].count())
print(len(data[data['Survived'] == 1])/len(data['Survived']))
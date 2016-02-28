# Какое количество мужчин и женщин ехало на корабле? В качестве ответа приведите два числа через пробел.
import pandas
data = pandas.read_csv('titanic.csv', index_col='PassengerId')
print(data[data['Sex'] == 'male'].count())
print(data[data['Sex'] == 'female'].count())
print(len(data[data['Sex'] == 'female']))
print(len(data[data['Sex'] == 'male']))
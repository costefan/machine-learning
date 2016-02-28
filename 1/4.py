# Какого возраста были пассажиры? Посчитайте среднее и медиану возраста пассажиров. В качестве ответа приведите два числа через пробел.
import pandas
data = pandas.read_csv('titanic.csv', index_col='PassengerId')
print(data['Age'].mean())
print(data['Age'].median())

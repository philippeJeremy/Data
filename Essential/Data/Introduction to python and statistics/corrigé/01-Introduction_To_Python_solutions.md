# Introduction to Python

## Exercises


# HackerRank

We've already used it for SQL and it turns out that HackerRank is a great tool to learn how to code in Python too. So let's try the following challenges:



*   [Say "Hello, World!" With Python](https://www.hackerrank.com/challenges/py-hello-world/problem)

```python
if __name__ == '__main__':
    print("Hello, World!")
```

*   [Arithmetic Operators](https://www.hackerrank.com/challenges/python-arithmetic-operators/problem)

```python
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a + b)
    print(a - b)
    print(a * b)

```
*   [Division](https://www.hackerrank.com/challenges/python-division/problem)

```python
if __name__ == '__main__':
   a = int(input())
   b = int(input())
   print(a//b)
   print(a/b)
```

*   [Loops](https://www.hackerrank.com/challenges/python-loops/problem) (conseil : Vous aurez besoin d’utiliser la fonction [range()](https://pynative.com/python-range-function/)

```python
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i**2)
```
*   [Python If-Else](https://www.hackerrank.com/challenges/py-if-else/problem) (conseil : Vous aurez besoin d’utiliser la fonction [range()](https://pynative.com/python-range-function/) et l’opérateur [%](https://data-flair.training/blogs/python-operator/#targetText=Python%20Arithmetic%20Operator,operators%20for%20basic%20mathematical%20operations.&targetText=Adds%20the%20values%20on%20either%20side%20of%20the%20operator.&targetText=Subtracts%20the%20value%20on%20the%20right%20from%20the%20one%20on%20the%20left.&targetText=Multiplies%20the%20values%20on%20either%20side%20of%20the%20operator.))

```python
N = int(input())

if N%2 ==0 and N in range(2,6):
    print("Not Weird")
elif N%2 == 0 and N in range(6, 21):
    print("Weird")
elif N%2 == 0 and N > 20:
    print("Not Weird")
elif N%2 !=0:
    print("Weird")
```

# Pandas

We're going to manipulate data with Pandas.



1. Open a notebook on Google Colab
2. Import Pandas

```python
import pandas as pd
```

3. Apply the code below

```python
from sklearn.datasets import california_housing
cali_houses = california_housing.fetch_california_housing()
cali_houses = pd.DataFrame(columns=cali_houses.feature_names, data=cali_houses.data)
```


4. We have created a dataset and stored it in the variable _cali_houses._ Try to get an overview of the first 5 lines of the dataset

```python
cali_houses.head()
```

5. Calculate the average of all the columns in the dataset

```python
cali_houses.mean()
```
6. Calculate the average of the _HouseAge_ column.

```python
cali_houses["HouseAge"].mean()
```
7. Calculate the standard deviation of the _Population_ column.

```python
cali_houses["Population"].std()
```

8. Give an overview of the main statistics of the dataset
```python
cali_houses.describe()
```
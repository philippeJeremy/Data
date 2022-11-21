
# Advanced SQL - 3A Exercises



* Click on the following link :  [https://sqlbolt.com/lesson/select_queries_with_aggregates](https://sqlbolt.com/lesson/select_queries_with_aggregates). We will do exercises 10 & 11 together.

Exercise 10

```sql
SELECT MAX(years_employed) as Max_years_employed
FROM employees;

SELECT ROLE, AVG(Years_employed) FROM Employees
GROUP BY ROLE;

SELECT Building, SUM(Years_employed) FROM Employees
GROUP BY Building;
```

Exercise 11
```sql

SELECT role, COUNT(*) as Number_of_artists
FROM employees
WHERE role = "Artist";

SELECT ROLE, COUNT(*) FROM Employees
GROUP BY Role;

SELECT ROLE, SUM(Years_employed) FROM Employees
WHERE Role = "Engineer";


```


* Now let's go back to Google Big Query and go to the NYSE (New York Stock Exchange) dataset. The two tables are a description of the different companies as well as the financial indicators.


1. In which sector do we have the most companies?
    * Use the table **NYSE.companies**.
    * Variable sector: **GICS_Sector**

```sql
SELECT GICS_Sector, COUNT(*) AS cnt FROM NYSE.companies 
GROUP BY GICS_Sector
ORDER BY cnt DESC;
```



2. What is the top 5 Californian cities with the most companies in the NYSE?
    * Variable: **Address_of_Headquarters**

```sql
SELECT COUNT(*) as cnt, Address_of_Headquarters FROM `NYSE.companies` 
WHERE Address_of_Headquarters LIKE "%California%"
GROUP BY Address_of_Headquarters
ORDER BY cnt DESC;
```

3. What is the top 5 companies that made the most profit in 2015?
    * Company: **Ticker_Symbol**
    * Profit: **Net_income**
    * Year: **For_Year**

```sql
SELECT Ticker_Symbol, Net_income FROM `NYSE.indicators` 
WHERE For_Year = 2015
ORDER BY Net_income DESC;
```

4. And cumulatively between 2013 and 2016?
    * Company: **Ticker_Symbol**
    * Profit: **Net_income**
    * Year: **For_Year**

```sql
SELECT Ticker_Symbol, SUM(Net_income) as revenue FROM `NYSE.indicators` 
WHERE For_Year BETWEEN 2013 AND 2016
GROUP BY Ticker_Symbol
ORDER BY revenue DESC;

```

5. Which companies are less healthy? We will calculate this by performing a ratio between assets (Total_Assets) and liabilities (Total_Liabilities). We will also round the results to three decimal places.
    * Table: **NYSE.indicators** 

```sql

SELECT Ticker_Symbol, ROUND(Total_Assets/Total_Liabilities,3) AS ratio FROM `NYSE.indicators` 
ORDER BY ratio ASC;
```


6. What is Apple's average income between the years 2014 and 2016?

```sql
SELECT Ticker_Symbol, AVG(Net_income) FROM `NYSE.indicators` 
WHERE Ticker_Symbol = "AAPL" AND For_Year BETWEEN 2014 AND 2016
GROUP BY Ticker_Symbol;

```
7. Which companies have the most after-tax income (Net_income) with long-term debt of less than $1,000,000?
    * Long-term debt: **Long_term_Debt**

```sql
SELECT Ticker_Symbol, AVG(Net_income) as avg_net_income FROM `NYSE.indicators`
GROUP BY Ticker_Symbol
HAVING AVG(Long_term_Debt) < 1000000
ORDER BY avg_net_income DESC;

```


## SUBQUERIES



1. Which foreign films scored higher than the best American film?

```sql
SELECT movie_title FROM IMDB.movies
WHERE imdb_score > (  SELECT imdb_score FROM `IMDB.movies` 
                      WHERE Country = "USA" 
                      ORDER BY imdb_score 
                      LIMIT 1 )
                      
AND Country != "USA"

ORDER BY movie_title;
```


## Let's raise the bar a little

Go to [HackerRank](http://hackerrank.com) and do the following exercises:



* [Weather Observation Station 5](https://www.hackerrank.com/challenges/weather-observation-station-5/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen)
    * Precision: CHAR_LENGTH for text length


```sql
SELECT CITY, char_length(CITY) AS LEN FROM STATION 
WHERE CHAR_LENGTH(CITY) = (SELECT MAX(CHAR_LENGTH(CITY)) FROM STATION)
OR CHAR_LENGTH(CITY) = (SELECT MIN(CHAR_LENGTH(CITY)) FROM STATION)
ORDER BY CITY
LIMIT 1;

SELECT CITY, char_length(CITY) AS LEN FROM STATION 
WHERE CHAR_LENGTH(CITY) = (SELECT MAX(CHAR_LENGTH(CITY)) FROM STATION)
ORDER BY CITY
LIMIT 1;
```

* [Top Earners](https://www.hackerrank.com/challenges/earnings-of-employees/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen)

```sql
SELECT salary * months AS total_earnings, COUNT(salary * months) AS cnt FROM Employee
WHERE salary * months = (SELECT MAX(salary * months))
GROUP BY salary, months
ORDER BY total_earnings DESC
LIMIT 1
```


* [The PADS](https://www.hackerrank.com/challenges/the-pads/problem)** →** **Tip** : Check out [Stack Overflow](https://stackoverflow.com/questions/20284528/how-to-concat-two-columns-into-one-with-the-existing-column-name-in-mysql)
    * Precision: CONCAT to concatenate strings of characters

```sql
SELECT CONCAT(Name, "(", LEFT(Occupation,1), ")") FROM OCCUPATIONS
ORDER BY Name;

SELECT "There are a total of ", COUNT(LOWER(Occupation)) , " ", CONCAT(LOWER(Occupation), "s.") FROM OCCUPATIONS
GROUP BY Occupation 
ORDER BY COUNT(LOWER(Occupation)) ASC, Occupation ASC;
```

* [The Company](https://www.hackerrank.com/challenges/the-company/problem)

**→ Tips:**

    1- No need to JOIN, you can use where to join the columns


    2- You can make a SELECT ___ FROM table1, table2, table3


    3- If you add several tables after your FROM, we advise you to rename them and then to precede the columns by the name of the table.


    Ex: SELECT a.col1, b.col1 FROM table1 AS a, table2 as b_

```sql
select c.company_code, c.founder, 
    count(distinct l.lead_manager_code), count(distinct s.senior_manager_code), 
    count(distinct m.manager_code),count(distinct e.employee_code) 
from Company AS c, Lead_Manager AS l, Senior_Manager AS s, Manager AS m, Employee AS e 
where c.company_code = l.company_code 
    and l.lead_manager_code=s.lead_manager_code 
    and s.senior_manager_code=m.senior_manager_code 
    and m.manager_code=e.manager_code 
group by c.company_code, c.founder 
order by c.company_code;
```

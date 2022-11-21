
# IMDB, World Happiness Record & HackerRank

For this exercise, we will work on the IMDB and World Happiness Record databases.

1. What is the highest budget of all US films?

```sql
SELECT movie_title, budget
FROM IMDB.movies
WHERE country = 'USA';
ORDER BY budget DESC;
```

2. Which actors have "John" in their name?

```sql
SELECT actor_1_name
FROM IMDB.main_actors
WHERE actor_1_name LIKE '%John%'
```

3. What is the movie with the most Facebook likes?

```sql
SELECT movie_title, movie_facebook_likes
FROM IMDB.movies
ORDER BY movie_facebook_likes DESC;
```

4. What are the 15 best movies according to IMDB?

```sql
SELECT movie_title, imdb_score
FROM IMDB.movies
ORDER BY imdb_score DESC;
LIMIT 15;
```

5. Are there any of these 15 movies outside of the US?

```sql
SELECT movie_title, imdb_score, country FROM (SELECT movie_title, imdb_score, country
FROM IMDB.movies
ORDER BY imdb_score DESC
LIMIT 15)

WHERE country != “USA”;
```

6. What is the top 10 best films of the 1990s according to IMDB?

```sql
SELECT movie_title AS Title, title_year AS Year, imdb_score AS Score FROM IMDB.movies
WHERE title_year BETWEEN 1990 AND 2000
ORDER BY imdb_score DESC
LIMIT 15;
```

## Let's change the database now and take World Happiness Record Database :  

7) What are the 5 happiest countries in the world in 2016?

```sql
SELECT Country, Happiness_Score FROM World_happiness_record.2016
ORDER BY Happiness_score DESC
LIMIT 5;
```

8) What are the 5 most unhappy countries in the world in 2016?

```sql
SELECT Country, Happiness_score FROM World_happiness_record.2016
ORDER BY Happiness_score 
LIMIT 5;
```

9) Is the country with the highest life expectancy the happiest?

```sql
SELECT Country, Life_expectancy, Happiness_score FROM World_happiness_record.2016
ORDER BY Life_expectancy DESC, Happiness_score DESC;
```

NB: There is not only one way to arrive at the answer for this question. You can do it differently and tell the students. From this query, it can be clearly seen that Hong Kong has a very high life expectancy but is not the happiest country.

This clause also allows us to see that we can sort by two columns. Which is always a plus.


## Let's raise the bar a little bit

[HackerRank](http://hackerrank.com) is an extremely popular code practice platform. Some recruiters even run coding challenges on it. It is therefore useful to spend some time on it.

So create an account and practice the following exercises (NB: Don't forget to use the MySQL code editor before writing your clauses) :


*   [Weather Observation Station 3](https://www.hackerrank.com/challenges/weather-observation-station-3/problem)

```sql
SELECT DISTINCT CITY FROM STATION
WHERE ID % 2 = 0;
```

*   [Weather Observation Station 4](https://www.hackerrank.com/challenges/weather-observation-station-4/problem?h_r=next-challenge&h_v=zen) (pour cette clause regardez la documentation pour [COUNT()](https://www.w3schools.com/sql/sql_count_avg_sum.asp)

```sql
SELECT COUNT(CITY) - COUNT(DISTINCT CITY) FROM STATION
```

*   [Weather Observation Station 6](https://www.hackerrank.com/challenges/weather-observation-station-6/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen)

```sql
SELECT DISTINCT CITY FROM STATION 
WHERE CITY LIKE 'a%'
OR CITY LIKE 'e%'
OR CITY LIKE 'i%'
OR CITY LIKE 'o%'
OR CITY LIKE 'u%'
```
OR
```sql
SELECT DISTINCT CITY FROM STATION 
WHERE CITY REGEXP '^[aeiou]'
```

*   [Weather Observation Station 8](https://www.hackerrank.com/challenges/weather-observation-station-8/problem)** → **Conseil, regardez [WHERE IN](https://www.dofactory.com/sql/where-in)

```sql
SELECT DISTINCT city FROM station 
WHERE LEFT(city,1) IN ('a','e','i','o','u') 
AND RIGHT(city, 1) IN ('a','e','i','o','u')
```

*   [Weather Observation Station 11](https://www.hackerrank.com/challenges/weather-observation-station-11/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen)

```sql
SELECT DISTINCT city FROM station 
WHERE LEFT(city,1) NOT IN ('a','e','i','o','u') 
OR RIGHT(city, 1) NOT IN ('a','e','i','o','u')
```
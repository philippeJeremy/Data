# Advanced SQL - 3B Exercises


## EXTRACT



1. Find out which day in the month had the most matches

```sql 
SELECT EXTRACT(day FROM date) as day, COUNT(*) AS cnt FROM `european_soccer.Match` 
GROUP BY day
ORDER BY cnt DESC;
```

2. Find out which month in the year had the most matches.

```sql
SELECT EXTRACT(month FROM date) as month, COUNT(*) AS cnt FROM `european_soccer.Match` 
GROUP BY month
ORDER BY cnt DESC;
```


## JOIN

Let's do exercise 12 of this link:  [https://sqlbolt.com/lesson/select_queries_order_of_execution]


```sql
SELECT Director, COUNT(*) FROM movies
GROUP BY Director;

SELECT Title, Director, SUM(Domestic_sales + International_sales) 
FROM movies
JOIN Boxoffice ON Movies.id = Boxoffice.movie_id
GROUP BY Director;
```

### EUROPEAN SOCCER



1. Using JOIN, find the team with the most goals at home
    * **home_team_goal**

```sql
SELECT  team_long_name, SUM(home_team_goal) as sum_of_goals
FROM european_soccer.Match AS match
JOIN `european_soccer.Team` as team ON match.home_team_api_id = team.team_api_id
GROUP BY team_long_name
ORDER BY sum_of_goals DESC;
```

2. Is it the same as the team that put the most goals away **?**
    * **away_team_goal**

```sql
SELECT SUM(away_team_goal) as sum_of_goals, team_long_name FROM european_soccer.Match AS match
JOIN `european_soccer.Team` as team OnN match.away_team_api_id = team.team_api_id
GROUP BY team_long_name
ORDER BY sum_of_goals DESC;
```
3. What is the name of the best player according to our database in 2016?

```sql
SELECT overall_rating, player_name 
FROM european_soccer.Player AS Player
JOIN `european_soccer.Player_attributes` as Player_attributes USING (player_api_id)
WHERE EXTRACT(year FROM date) = 2016
GROUP BY player_name, overall_rating
ORDER BY overall_rating DESC;
```

### NEW YORK STOCK EXCHANGE

Let's switch databases and look at the NY Stock Exchange database.



1. Which company is making the most investment in 2016?

```sql
SELECT Security, Investments FROM `NYSE.companies` 
JOIN `NYSE.indicators` USING(Ticker_Symbol)
WHERE EXTRACT(year FROM Period_Ending) = 2016
ORDER BY Investments DESC;
```

2. Is it the same company that has invested the most over all the years of our base?

```sql
SELECT Security, SUM(Investments) as sum_of_investments
FROM `NYSE.companies` 
JOIN `NYSE.indicators` USING(Ticker_Symbol)
GROUP BY Security
ORDER BY sum_of_investments DESC;
```

3. Which sector generated the most revenue in 2016?

```sql
SELECT GICS_Sector, SUM(total_revenue) as sum_of_revenue FROM `NYSE.companies` 
JOIN `NYSE.indicators` USING(Ticker_Symbol)
WHERE For_Year = 2016
GROUP BY GICS_Sector
ORDER BY sum_of_revenue DESC;
```

4. Which sector generated the most profit in 2016?

```sql
SELECT GICS_Sector, SUM(Profit_Margin) as total_margin FROM `NYSE.companies` 
JOIN `NYSE.indicators` USING(Ticker_Symbol)
WHERE For_Year = 2016
GROUP BY GICS_Sector
ORDER BY total_margin DESC;
```

5. Finally, in which sector is there the most short-term debt?

```sql
SELECT GICS_Sector, SUM(Short_Term_Debt___Current_Portion_of_Long_Term_Debt) as short_term_debt FROM `NYSE.companies` 
JOIN `NYSE.indicators` USING(Ticker_Symbol)
GROUP BY GICS_Sector
ORDER BY short_term_debt DESC;
```

## WITH AS - IMDB



1. Using WITH AS, store all of the movies in which Johnny Depp has played

```sql
WITH movie_with_johnny_depp AS (

  SELECT * FROM `IMDB.movies` 
  JOIN `IMDB.main_actors`  USING(actor_1_id)
  WHERE actor_1_name = "Johnny Depp" )
  
SELECT * FROM movie_with_johnny_depp;
```

2. What's the best movie he's ever been in?

```sql
WITH movie_with_johnny_depp AS (
  SELECT * FROM `IMDB.movies` 
  JOIN `IMDB.main_actors`  USING(actor_1_id)
  WHERE actor_1_name = "Johnny Depp")
  
SELECT movie_title FROM movie_with_johnny_depp 
ORDER BY imdb_score DESC
LIMIT 1;
```

## Let's raise the bar a little bit

Go to [HackerRank](http://hackerrank.com) and answer the following questions:



* [Top Competitors](https://www.hackerrank.com/challenges/full-score/problem)

```sql
SELECT h.hacker_id, h.name FROM submissions s
    JOIN challenges c ON s.challenge_id = c.challenge_id
    JOIN difficulty d ON c.difficulty_level = d.difficulty_level 
    JOIN hackers h ON s.hacker_id = h.hacker_id
WHERE s.score = d.score 
AND c.difficulty_level = d.difficulty_level
GROUP BY h.hacker_id, h.name
HAVING COUNT(s.hacker_id) > 1
ORDER BY COUNT(s.hacker_id) DESC, s.hacker_id ASC
```

* [Challenges](https://www.hackerrank.com/challenges/challenges/problem)

```sql
/* these are the columns we want to output */
select c.hacker_id, h.name ,count(c.hacker_id) as c_count

/* this is the join we want to output them from */
from Hackers as h
    inner join Challenges as c on c.hacker_id = h.hacker_id

/* after they have been grouped by hacker */
group by c.hacker_id, h.name

/* but we want to be selective about which hackers we output */
/* having is required (instead of where) for filtering on groups */
having 

    /* output anyone with a count that is equal to... */
    c_count = 
        /* the max count that anyone has */
        (SELECT MAX(temp1.cnt)
        from (SELECT COUNT(hacker_id) as cnt
             from Challenges
             group by hacker_id
             order by hacker_id) temp1)

    /* or anyone who's count is in... */
    or c_count in 
        /* the set of counts... */
        (select t.cnt
         from (select count(*) as cnt 
               from challenges
               group by hacker_id) t
         /* who's group of counts... */
         group by t.cnt
         /* has only one element */
         having count(t.cnt) = 1)

/* finally, the order the rows should be output */
```
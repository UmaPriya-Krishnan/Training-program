1. Find the titles of all movies directed by Steven Spielberg. (1 point possible)

1> select title from Movie where director = 'Steven Spielberg'
2> go
title
--------------------------------------------------
E.T.
Raiders of the Lost Ark

(2 rows affected)

************************************************************************************************************************************************

2. Find all years that have a movie that received a rating of 4 or 5, and sort them in increasing order. (1 point possible)

1> select year, stars from movie as M join Rating as R on M.mID = R.mID where stars between 4 and 5 order by year;
2> go
year        stars
----------- -----------
       1937           4
       1937           5
       1939           4
       1981           4
       1981           4
       2009           5

(6 rows affected)

*******************************************************************************************
3. Find the titles of all movies that have no ratings. (1 point possible)

1> select title from movie as M join Rating as R on M.mID = R.mID where stars = ' '
2> go
title
--------------------------------------------------

(0 rows affected)

*******************************************************************************************

4. Some reviewers didn't provide a date with their rating. Find the names of all reviewers who have ratings with a NULL value for the date. (1 point possible)

1> select name, ratingDate from reviewer as Re join Rating as Ra on Re.rID = Ra.rID where Ra.ratingDate is Null;
2> go
name                           ratingDate
------------------------------ ----------------
Daniel Lewis                               NULL
Chris Jackson                              NULL

(2 rows affected)

*******************************************************************************************************************************************************

5. Write a query to return the ratings data in a more readable format: reviewer name, movie title, stars, and ratingDate.
 Also, sort the data, first by reviewer name, then by movie title, and lastly by number of stars. (1 point possible)

1> select name as Reviewer_name, title as Movie_title, stars as No_of_stars, ratingDate as date from movie as M join rating as Ra on M.mID = Ra.mID join reviewer as Re on Re.rID = Ra.rID order by name, title, stars, year;
2> go
Reviewer_name                  Movie_title                                        No_of_stars date
------------------------------ -------------------------------------------------- ----------- ----------------
Ashley White                   E.T.                                                         3       2011-01-02
Brittany Harris                Raiders of the Lost Ark                                      2       2011-01-30
Brittany Harris                Raiders of the Lost Ark                                      4       2011-01-12
Brittany Harris                The Sound of Music                                           2       2011-01-20
Chris Jackson                  E.T.                                                         2       2011-01-22
Chris Jackson                  Raiders of the Lost Ark                                      4             NULL
Chris Jackson                  The Sound of Music                                           3       2011-01-27
Daniel Lewis                   Snow White                                                   4             NULL
Elizabeth Thomas               Avatar                                                       3       2011-01-15
Elizabeth Thomas               Snow White                                                   5       2011-01-19
James Cameron                  Avatar                                                       5       2011-01-20
Mike Anderson                  Gone with the Wind                                           3       2011-01-09
Sarah Martinez                 Gone with the Wind                                           2       2011-01-22
Sarah Martinez                 Gone with the Wind                                           4       2011-01-27

(14 rows affected)

***********************************************************************************************************************************************************

6. For all cases where the same reviewer rated the same movie twice and gave it a higher rating the second time, 
return the reviewer's name and the title of the movie. (1 point possible)
1> select name, title from rating as ra1 join rating as ra2 on ra1.rID = ra2.rID  join movie as M on m.mID = ra1.mID join reviewer as Re on Re.rID = ra1.rID where ra1.stars>ra2.stars and ra1.ratingDate > ra2.ratingDate;
2> go
name                           title
------------------------------ --------------------------------------------------
Sarah Martinez                 Gone with the Wind
Chris Jackson                  The Sound of Music
Elizabeth Thomas               Snow White

**************************************************************************************************************************

7. For each movie that has at least one rating, find the highest number of stars that movie received. 
Return the movie title and number of stars. Sort by movie title. (1 point possible)

1> select title, max(stars) as max_stars from movie as M join rating as ra on ra.mID = M.mID group by title order by title;
2> go
title                                              max_stars
-------------------------------------------------- -----------
Avatar                                                       5
E.T.                                                         3
Gone with the Wind                                           4
Raiders of the Lost Ark                                      4
Snow White                                                   5
The Sound of Music                                           3

(6 rows affected)

************************************************************************************************************

8. For each movie, return the title and the 'rating spread', that is, the difference between highest and lowest ratings given to that movie. Sort by rating spread from highest to lowest, then by movie title. (1 point possible)

1> select title, max(stars) - min(stars) as rating_spread from movie as M join rating as Ra on M.mID = Ra.mID group by title order by rating_spread, title;
2> go
title                                              rating_spread
-------------------------------------------------- -------------
E.T.                                                           1
Snow White                                                     1
The Sound of Music                                             1
Avatar                                                         2
Gone with the Wind                                             2
Raiders of the Lost Ark                                        2


********************************************************************************************************************************
10. Find the names of all reviewers who rated Gone with the Wind. (1 point possible)
select re.name, title from reviewer as Re join rating as Ra on ra.rID = re.rID join movie as M on M.mID = Ra.rID group by name;

 1> select name from Reviewer where rID in ( select rID from Rating where mID in ( select mID from movie where title='Gone with the Wind'));
2> go
name
------------------------------
Sarah Martinez
Mike Anderson

(2 rows affected)

********************************************************************************************************************************
11. For any rating where the reviewer is the same as the director of the movie, return the reviewer name, movie title, and number of stars. (1 point possible)

1> select name,title,stars from Movie as M join rating as Ra on M.mID = Ra.mID join reviewer as Re on re.rID = ra.rID where re.name=M.director;
2> go
name                           title                                              stars
------------------------------ -------------------------------------------------- -----------
James Cameron                  Avatar                                                       5

(1 rows affected)

******************************************************************************************************************************
12. Return all reviewer names and movie names together in a single list, alphabetized. (Sorting by the first name of the reviewer and first word in the title is fine; no need for special processing on last names or removing "The".) (1 point possible)

1> select concat (name, '-', title) as Reviewer_title from movie as M join Rating as Ra on M.mid = Ra.mid join reviewer as Re on Re.rid = Ra.rid order by name,title;
2> go
Reviewer_title
---------------------------------------------------------------------------------
Ashley White-E.T.
Brittany Harris-Raiders of the Lost Ark
Brittany Harris-Raiders of the Lost Ark
Brittany Harris-The Sound of Music
Chris Jackson-E.T.
Chris Jackson-Raiders of the Lost Ark
Chris Jackson-The Sound of Music
Daniel Lewis-Snow White
Elizabeth Thomas-Avatar
Elizabeth Thomas-Snow White
James Cameron-Avatar
Mike Anderson-Gone with the Wind
Sarah Martinez-Gone with the Wind
Sarah Martinez-Gone with the Wind

(14 rows affected)

*****************************************************************************************************************************

19. Find the movie(s) with the highest average rating. Return the movie title(s) and average rating.
 (Hint: This query is more difficult to write in SQLite than other systems;
 you might think of it as finding the highest average rating and then choosing the movie(s) with that average rating.) (1 point possible)

1> select top 1 avg(stars) as average ,title from Movie as M join rating as ra on M.mID = ra.mID join reviewer as Re on re.rID = ra.rID group by title,stars order by stars desc;
2> go
average     title
----------- --------------------------------------------------
          5 Avatar

(1 rows affected)

*********************************************************************************************************************************
select avg(stars) ,title from Movie as M join rating as ra on M.mID = ra.mID group by title having avg(stars) = (select min(rates) from (select avg(stars) as rates from rating group by mid)as a);

20. Find the movie(s) with the lowest average rating. Return the movie title(s) and average rating.
 (Hint: This query may be more difficult to write in SQLite than other systems; 
 you might think of it as finding the lowest average rating and then choosing the movie(s) with that average rating.) (1 point possible)

1> select avg(stars) as average ,title from Movie as M join rating as ra on M.mID = ra.mID join reviewer as Re on re.rID = ra.rID group by title,stars order by stars;
2> go
            title
----------- --------------------------------------------------
          2 E.T.
          2 Gone with the Wind

(2 rows affected)
****************************************************************************************************************8

21. For each director, return the director's name together with the title(s) 
of the movie(s) they directed that received the highest rating among all of their movies,
and the value of that rating. Ignore movies whose director is NULL. (1 point possible)
 
1> select title, director,max(stars) from Movie as M join rating as ra on M.mID = ra.mID join reviewer as Re on re.rID = ra.rID where director not in ("") group by title, director;
2> go
title                                              director
-------------------------------------------------- ------------------------------ -----------
Avatar                                             James Cameron                            5
The Sound of Music                                 Robert Wise                              3
E.T.                                               Steven Spielberg                         3
Raiders of the Lost Ark                            Steven Spielberg                         4
Gone with the Wind                                 Victor Fleming                           4

******************************************************************************************************************************

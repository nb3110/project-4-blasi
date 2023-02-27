WITH average_review_rate as
(
SELECT 
YEAR(date_review) as review_year, 
firm, 
AVG(overall_rating) as  mean_overall_rating,
COUNT(overall_rating) as count_rating
FROM glassdoor_reviews.reviews 
GROUP BY 1,2

),

ranking_table as
(
SELECT 
review_year, 
firm, 
DENSE_RANK() OVER(PARTITION BY review_year ORDER BY mean_overall_rating DESC,count_rating DESC ) as ranking,
mean_overall_rating,
count_rating
FROM average_review_rate
WHERE count_rating > (SELECT AVG(count_rating) FROM average_review_rate)
)


SELECT 
firm,
SUM(
CASE 
WHEN ranking = 1
    THEN 1
ELSE 0
END) rank_1,

SUM(
CASE 
WHEN ranking = 2
    THEN 1
ELSE 0
END) rank_2,

SUM(
CASE 
WHEN ranking = 3
    THEN 1
ELSE 0
END) rank_3,


AVG(mean_overall_rating) mean_year_rating

FROM ranking_table
WHERE ranking <= 3
GROUP BY 1
ORDER BY rank_1 DESC, rank_2 DESC, rank_3 DESC
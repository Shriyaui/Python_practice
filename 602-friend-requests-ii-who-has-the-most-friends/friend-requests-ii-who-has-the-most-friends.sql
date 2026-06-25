WITH all_friends AS (
    SELECT requester_id AS id, accepter_id AS friend FROM RequestAccepted
    UNION ALL
    SELECT accepter_id AS id, requester_id AS friend FROM RequestAccepted
),
friend_counts AS (
    SELECT id, COUNT(DISTINCT friend) AS num
    FROM all_friends
    GROUP BY id
)
SELECT id, num
FROM friend_counts
ORDER BY num DESC
LIMIT 1;       

                
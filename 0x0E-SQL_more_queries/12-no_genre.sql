--  Lists all shows contained in hbtn_0d_tvshows
-- that have at least one genre linked.

SELECT
	ts.title, tsg.genre_id
FROM
	tv_shows AS ts
LEFT JOIN
	tv_show_genres AS tsg
ON tsg.show_id = ts.id
WHERE tsg.genre_id IS NULL
ORDER BY
	ts.title, tsg.genre_id;

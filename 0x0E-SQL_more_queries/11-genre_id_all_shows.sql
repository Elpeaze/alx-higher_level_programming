--  Lists all shows contained in hbtn_0d_tvshows
-- that have at least one genre linked.

SELECT
	tv_shows.title, tv_show_genre.genre_id
FROM
	tv_shows AS ts
LEFT JOIN
	tv_show_genre AS tsg
ON tsg.show_id = ts.id
ORDER BY
	ts.title, tsg.genre_id;

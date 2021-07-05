-----------------Top 100 Highest transactions between 7 and 9-------------------
CREATE VIEW top_100_transactions_between_7_and_9 AS
	SELECT * FROM "transaction"
	WHERE CAST("date" as time) BETWEEN '07:00:00' AND '09:00:00'
	ORDER BY amount DESC
	LIMIT 100;


CREATE VIEW total_transactions_less_than_2_dollars AS
	SELECT * 
	FROM (SELECT COUNT(*) AS "Total number of Transactions between 7 AM and 9 AM"
		  FROM top_100_transactions_between_7_and_9
		  WHERE amount <= 2) AS x,
	(SELECT COUNT(*) AS "Total number of Transactions"
	 FROM "transaction"
	 WHERE id NOT IN (SELECT ID FROM top_100_transactions_between_7_and_9)
		  AND amount <= 2) AS y;
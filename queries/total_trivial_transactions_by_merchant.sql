CREATE VIEW total_trivial_transactions_by_merchant AS
	SELECT m.name, COUNT(m.name) AS "Total trivial transactions by merchant"
	FROM "transaction" t
	INNER JOIN merchant m 
	ON m.id = t.id_merchant
	WHERE t.amount <= 2
	GROUP BY m."name"
	ORDER BY COUNT(m."name") DESC;
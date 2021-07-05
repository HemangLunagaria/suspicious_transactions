-------Grouping transactions of each cardholder-----------
CREATE VIEW total_transactions_by_card AS
	SELECT card, COUNT(t.card) as "Total transactions"
	FROM "transaction" t
	GROUP BY card
	ORDER BY COUNT(t.card);

--------------Counting the transactions with amount less than $2 per cardholder----------------
CREATE VIEW total_trivial_transactions_by_card AS
	SELECT t.card, COUNT(t.card) as "Total trivial transactions"
	FROM "transaction" t
	WHERE t.amount <= 2
	GROUP BY t.card
	ORDER BY COUNT(t.card) DESC;
	
	
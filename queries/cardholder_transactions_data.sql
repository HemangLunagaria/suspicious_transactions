select *
from "transaction" t
inner join credit_card c
on c.card = t.card
where c.cardholder_id IN (2,18)
order by c.cardholder_id,t.date;

select EXTRACT(MONTH from date),EXTRACT(DAY FROM date), amount
from "transaction" t
inner join credit_card c
on c.card = t.card
where c.cardholder_id IN (25)
order by c.cardholder_id,t.date;


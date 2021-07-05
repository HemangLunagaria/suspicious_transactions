CREATE TABLE "card_holder"(
    "id" SERIAL NOT NULL,
    "name" VARCHAR(50) NOT NULL
);
ALTER TABLE
    "card_holder" ADD PRIMARY KEY("id");

CREATE TABLE "credit_card"(
    "card" VARCHAR(100) NOT NULL,
    "cardholder_id" INTEGER NOT NULL
);
ALTER TABLE
    "credit_card" ADD PRIMARY KEY("card");

CREATE TABLE "merchant_category"(
    "id" SERIAL NOT NULL,
    "name" VARCHAR(50) NOT NULL
);
ALTER TABLE
    "merchant_category" ADD PRIMARY KEY("id");

CREATE TABLE "merchant"(
    "id" SERIAL NOT NULL,
    "name" VARCHAR(100) NOT NULL,
    "id_merchant_category" INTEGER NOT NULL
);
ALTER TABLE
    "merchant" ADD PRIMARY KEY("id");

CREATE TABLE "transaction"(
    "id" SERIAL NOT NULL,
    "date" TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL,
    "amount" DOUBLE PRECISION NOT NULL,
    "card" VARCHAR(50) NOT NULL,
    "id_merchant" INTEGER NOT NULL
);
ALTER TABLE
    "transaction" ADD PRIMARY KEY("id");
    
ALTER TABLE
    "credit_card" ADD CONSTRAINT "credit_card_cardholder_id_foreign" FOREIGN KEY("cardholder_id") REFERENCES "card_holder"("id");
ALTER TABLE
    "merchant" ADD CONSTRAINT "merchant_id_merchant_category_foreign" FOREIGN KEY("id_merchant_category") REFERENCES "merchant_category"("id");
ALTER TABLE
    "transaction" ADD CONSTRAINT "transaction_id_merchant_foreign" FOREIGN KEY("id_merchant") REFERENCES "merchant"("id");
ALTER TABLE
    "transaction" ADD CONSTRAINT "transaction_id_credit_card_foreign" FOREIGN KEY("card") REFERENCES "credit_card"("card");
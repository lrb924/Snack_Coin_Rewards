BEGIN;

CREATE TABLE IF NOT EXISTS public." Menu"
(
    id integer NOT NULL,
    price money,
    "start date" date,
    "end date" date,
    CONSTRAINT " Menu_pkey" PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public."Food"
(
    food_id integer NOT NULL,
    name character varying(255) COLLATE pg_catalog."default" NOT NULL,
    quantity integer,
    unitprice money,
    category character varying(255) COLLATE pg_catalog."default",
    CONSTRAINT "Food_pkey" PRIMARY KEY (food_id)
);

CREATE TABLE IF NOT EXISTS public."MenuItem"
(
    menu_id integer,
    food_id integer
);

CREATE TABLE IF NOT EXISTS public.customer
(
    id integer NOT NULL,
    "first name" character varying COLLATE pg_catalog."default",
    "last name" character varying COLLATE pg_catalog."default",
    "phone no" character varying COLLATE pg_catalog."default",
    email character varying COLLATE pg_catalog."default",
    CONSTRAINT customer_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public."orderItem"
(
    order_id integer,
    menu_id integer,
    quantity integer,
    price money
);

CREATE TABLE IF NOT EXISTS public.orders
(
    id integer NOT NULL,
    "customerId" integer,
    amount money,
    "orderDate" date,
    CONSTRAINT orders_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.reward
(
    "customerId" integer,
    "snackCoins" integer
);

ALTER TABLE IF EXISTS public."MenuItem"
    ADD CONSTRAINT "fk_menu_item_foodId" FOREIGN KEY (food_id)
    REFERENCES public."Food" (food_id) MATCH SIMPLE
    ON UPDATE CASCADE
    ON DELETE CASCADE;


ALTER TABLE IF EXISTS public."MenuItem"
    ADD CONSTRAINT "fk_menu_item_menuId" FOREIGN KEY (menu_id)
    REFERENCES public." Menu" (id) MATCH SIMPLE
    ON UPDATE CASCADE
    ON DELETE CASCADE;


ALTER TABLE IF EXISTS public."orderItem"
    ADD CONSTRAINT fk_oderitem_orderid FOREIGN KEY (order_id)
    REFERENCES public.orders (id) MATCH SIMPLE
    ON UPDATE CASCADE
    ON DELETE CASCADE;


ALTER TABLE IF EXISTS public."orderItem"
    ADD CONSTRAINT fk_orderitem_menuid FOREIGN KEY (menu_id)
    REFERENCES public." Menu" (id) MATCH SIMPLE
    ON UPDATE CASCADE
    ON DELETE CASCADE;


ALTER TABLE IF EXISTS public.orders
    ADD CONSTRAINT fk_ordercustomer_cid FOREIGN KEY ("customerId")
    REFERENCES public.customer (id) MATCH SIMPLE
    ON UPDATE CASCADE
    ON DELETE CASCADE;


ALTER TABLE IF EXISTS public.reward
    ADD CONSTRAINT "fk_reward_custId" FOREIGN KEY ("customerId")
    REFERENCES public.customer (id) MATCH SIMPLE
    ON UPDATE CASCADE
    ON DELETE CASCADE;

END;
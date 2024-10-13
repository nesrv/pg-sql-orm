
## Создание и наполнение таблиц



```sql
CREATE TABLE public.table_t1 (
    id integer NOT NULL,
    code text
);



COPY public.table_t1 (id, code) FROM stdin;
1	красный
2	зеленый
3	синий
4	белый
5	\N
6	\N
\.


ALTER TABLE ONLY public.table_t1
    ADD CONSTRAINT table_t1_pkey PRIMARY KEY (id);
```


```sql
CREATE TABLE table_t3 (
    id integer PRIMARY KEY,
    code text
);

INSERT INTO table_t3 VALUES (1, 'color-1'), (2, 'color-2');


```


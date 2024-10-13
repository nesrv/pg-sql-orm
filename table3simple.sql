--
-- PostgreSQL database dump
--

-- Dumped from database version 16.3
-- Dumped by pg_dump version 16.3

-- Started on 2024-10-13 13:15:33

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 219 (class 1259 OID 16823)
-- Name: table_t3; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.table_t3 (
    id integer NOT NULL,
    code text
);


ALTER TABLE public.table_t3 OWNER TO postgres;

--
-- TOC entry 4787 (class 0 OID 16823)
-- Dependencies: 219
-- Data for Name: table_t3; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.table_t3 (id, code) FROM stdin;
1	color-1
2	color-2
\.


--
-- TOC entry 4643 (class 2606 OID 16829)
-- Name: table_t3 table_t3_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.table_t3
    ADD CONSTRAINT table_t3_pkey PRIMARY KEY (id);


-- Completed on 2024-10-13 13:15:33

--
-- PostgreSQL database dump complete
--


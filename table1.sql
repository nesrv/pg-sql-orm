PGDMP                  	    |            train    16.3    16.3     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    16726    train    DATABASE     y   CREATE DATABASE train WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Russian_Russia.1251';
    DROP DATABASE train;
                postgres    false            �            1259    16809    table_t1    TABLE     I   CREATE TABLE public.table_t1 (
    id integer NOT NULL,
    code text
);
    DROP TABLE public.table_t1;
       public         heap    postgres    false            �          0    16809    table_t1 
   TABLE DATA           ,   COPY public.table_t1 (id, code) FROM stdin;
    public          postgres    false    217                      2606    16815    table_t1 table_t1_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.table_t1
    ADD CONSTRAINT table_t1_pkey PRIMARY KEY (id);
 @   ALTER TABLE ONLY public.table_t1 DROP CONSTRAINT table_t1_pkey;
       public            postgres    false    217            �   F   x�3估�bÅ/��}a'����^��cN�܎{�x'�	煍 Y��)g�������� ��'?     
--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

--
-- Name: action; Type: TYPE; Schema: public; Owner: postgres
--

CREATE TYPE action AS ENUM (
    'message',
    'emote',
    'join',
    'part',
    'quit'
);


ALTER TYPE public.action OWNER TO postgres;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: message_table; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE message_table (
    id integer NOT NULL,
    "user" integer NOT NULL,
    "timestamp" timestamp without time zone NOT NULL,
    content text,
    host text,
    action action
);


ALTER TABLE public.message_table OWNER TO postgres;

--
-- Name: user_table; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE user_table (
    nick text,
    id integer NOT NULL
);


ALTER TABLE public.user_table OWNER TO postgres;

--
-- Data for Name: message_table; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY message_table (id, "user", "timestamp", content, host, action) FROM stdin;
\.


--
-- Data for Name: user_table; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY user_table (nick, id) FROM stdin;
\.


--
-- Name: Unique ID; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY message_table
    ADD CONSTRAINT "Unique ID" UNIQUE (id);


--
-- Name: message_table_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY message_table
    ADD CONSTRAINT message_table_pkey PRIMARY KEY (id);


--
-- Name: primary; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY user_table
    ADD CONSTRAINT "primary" PRIMARY KEY (id);


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--


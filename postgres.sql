--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: postgres; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON DATABASE postgres IS 'default administrative connection database';


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
-- Name: messages; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE messages (
    "user" integer NOT NULL,
    content text,
    action action,
    id integer NOT NULL,
    "timestamp" timestamp without time zone DEFAULT now()
);


ALTER TABLE public.messages OWNER TO postgres;

--
-- Name: messages_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE messages_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.messages_id_seq OWNER TO postgres;

--
-- Name: messages_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE messages_id_seq OWNED BY messages.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE users (
    "user" text,
    id integer NOT NULL,
    host character varying
);


ALTER TABLE public.users OWNER TO postgres;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE users_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO postgres;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE users_id_seq OWNED BY users.id;


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY messages ALTER COLUMN id SET DEFAULT nextval('messages_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY users ALTER COLUMN id SET DEFAULT nextval('users_id_seq'::regclass);


--
-- Data for Name: messages; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY messages ("user", content, action, id, "timestamp") FROM stdin;
11	test\r	message	8	2013-12-31 02:54:00.8601
11	pingu3:  still about?\r	message	9	2013-12-31 02:54:54.003227
12	Jayflux: hi, yep, lurking in other windows\r	message	10	2013-12-31 02:55:26.752727
11	any interesting windows?\r	message	11	2013-12-31 02:55:40.504302
12	not really.  dating websites, quick skype with a girl i'd been chatting to a lot who was up for some reason at 3am\r	message	12	2013-12-31 02:56:29.935917
11	ah yep\r	message	13	2013-12-31 02:56:53.80718
12	some most likely reason being some other guy she was talking to\r	message	14	2013-12-31 02:56:55.534061
12	im planning something boring to send me to sleep.  this might do it http://www.bbc.co.uk/iplayer/episode/b03npt4m/Sacred_Wonders_Of_Britain_Episode_1/\r	message	15	2013-12-31 02:58:05.680229
11	looks good\r	message	16	2013-12-31 02:58:52.429545
12	that guy is quite good if i remember right.  good expression\r	message	17	2013-12-31 02:59:19.073189
11	just\r	message	18	2013-12-31 03:01:16.146075
11	oops\r	message	19	2013-12-31 03:01:19.233966
11	well\r	message	20	2013-12-31 03:02:15.886281
11	im off\r	message	21	2013-12-31 03:02:17.425134
12	night\r	message	22	2013-12-31 03:02:37.567244
13	laravel php framework with mysql\r	message	23	2014-01-04 13:15:05.948924
14	ah\r	message	24	2014-01-04 13:19:02.205663
14	i've been using sf2 for a work project\r	message	25	2014-01-04 13:19:25.140173
13	i built this to learn laravel: http://southland.nztrader.co/\r	message	26	2014-01-04 13:19:28.68951
\.


--
-- Name: messages_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('messages_id_seq', 26, true);


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY users ("user", id, host) FROM stdin;
Jayflux	1	Jayflux@lol.com
Jayflux	11	unaffiliated/jayflux
pingu3	12	94-195-190-160.zone9.bethere.co.uk
TheJHNZ	13	203.86.203.162
Technodrome	14	unaffiliated/technodrome
\.


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('users_id_seq', 14, true);


--
-- Name: messages_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY messages
    ADD CONSTRAINT messages_pkey PRIMARY KEY (id);


--
-- Name: users_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY users
    ADD CONSTRAINT users_id_key UNIQUE (id);


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


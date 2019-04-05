--
-- PostgreSQL database dump
--

-- Dumped from database version 9.6.9
-- Dumped by pg_dump version 10.4

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: -
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);


--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(30) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.auth_user_groups_id_seq OWNED BY public.auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNED BY public.auth_user_user_permissions.id;


--
-- Name: components_bannercomponent; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.components_bannercomponent (
    page_ptr_id integer NOT NULL,
    service_name character varying(100),
    banner_content text NOT NULL,
    banner_content_en_gb text,
    banner_content_de text,
    banner_content_ja text,
    banner_content_ru text,
    banner_content_zh_hans text,
    banner_content_fr text,
    banner_content_es text,
    banner_content_pt text,
    banner_content_pt_br text,
    banner_content_ar text,
    banner_label character varying(50),
    banner_label_en_gb character varying(50),
    banner_label_de character varying(50),
    banner_label_ja character varying(50),
    banner_label_ru character varying(50),
    banner_label_zh_hans character varying(50),
    banner_label_fr character varying(50),
    banner_label_es character varying(50),
    banner_label_pt character varying(50),
    banner_label_pt_br character varying(50),
    banner_label_ar character varying(50)
);


--
-- Name: components_componentsapp; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.components_componentsapp (
    page_ptr_id integer NOT NULL,
    service_name character varying(100)
);


--
-- Name: core_breadcrumb; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.core_breadcrumb (
    id integer NOT NULL,
    service_name character varying(50),
    object_id integer NOT NULL,
    content_type_id integer NOT NULL,
    label character varying(50) NOT NULL,
    slug character varying(50) NOT NULL,
    label_ar character varying(50),
    label_de character varying(50),
    label_en_gb character varying(50),
    label_es character varying(50),
    label_fr character varying(50),
    label_ja character varying(50),
    label_pt character varying(50),
    label_pt_br character varying(50),
    label_ru character varying(50),
    label_zh_hans character varying(50),
    CONSTRAINT core_breadcrumb_object_id_check CHECK ((object_id >= 0))
);


--
-- Name: core_breadcrumb_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.core_breadcrumb_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: core_breadcrumb_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.core_breadcrumb_id_seq OWNED BY public.core_breadcrumb.id;


--
-- Name: core_documenthash; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.core_documenthash (
    id integer NOT NULL,
    content_hash character varying(1000) NOT NULL,
    document_id integer
);


--
-- Name: core_documenthash_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.core_documenthash_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: core_documenthash_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.core_documenthash_id_seq OWNED BY public.core_documenthash.id;


--
-- Name: core_imagehash; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.core_imagehash (
    id integer NOT NULL,
    content_hash character varying(1000) NOT NULL,
    image_id integer
);


--
-- Name: core_imagehash_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.core_imagehash_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: core_imagehash_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.core_imagehash_id_seq OWNED BY public.core_imagehash.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


--
-- Name: export_readiness_allcontactpagespage; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.export_readiness_allcontactpagespage (
    page_ptr_id integer NOT NULL,
    service_name character varying(100)
);


--
-- Name: export_readiness_articlelistingpage; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.export_readiness_articlelistingpage (
    page_ptr_id integer NOT NULL,
    service_name character varying(100),
    landing_page_title character varying(255) NOT NULL,
    hero_teaser character varying(255),
    list_teaser text,
    hero_image_id integer
);


--
-- Name: export_readiness_articlepage; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.export_readiness_articlepage (
    page_ptr_id integer NOT NULL,
    service_name character varying(100),
    article_title character varying(255) NOT NULL,
    article_teaser character varying(255) NOT NULL,
    article_body_text text NOT NULL,
    article_image_id integer,
    related_page_one_id integer,
    related_page_three_id integer,
    related_page_two_id integer
);


--
-- Name: export_readiness_articlepage_tags; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.export_readiness_articlepage_tags (
    id integer NOT NULL,
    articlepage_id integer NOT NULL,
    tag_id integer NOT NULL
);


--
-- Name: export_readiness_articlepage_tags_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.export_readiness_articlepage_tags_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: export_readiness_articlepage_tags_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.export_readiness_articlepage_tags_id_seq OWNED BY public.export_readiness_articlepage_tags.id;


--
-- Name: export_readiness_campaignpage; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.export_readiness_campaignpage (
    page_ptr_id integer NOT NULL,
    service_name character varying(100),
    campaign_heading character varying(255) NOT NULL,
    section_one_heading character varying(255) NOT NULL,
    section_one_intro text NOT NULL,
    selling_point_one_heading character varying(255) NOT NULL,
    selling_point_one_content text NOT NULL,
    selling_point_two_heading character varying(255),
    selling_point_two_content text,
    selling_point_three_heading character varying(255),
    selling_point_three_content text,
    section_one_contact_button_url character varying(255),
    section_one_contact_button_text character varying(255),
    section_two_heading character varying(255) NOT NULL,
    section_two_intro text NOT NULL,
    section_two_contact_button_url character varying(255),
    section_two_contact_button_text character varying(255),
    related_content_heading character varying(255) NOT NULL,
    related_content_intro text NOT NULL,
    cta_box_message character varying(255) NOT NULL,
    cta_box_button_url character varying(255) NOT NULL,
    cta_box_button_text character varying(255) NOT NULL,
    campaign_hero_image_id integer,
    section_one_image_id integer,
    section_two_image_id integer,
    selling_point_one_icon_id integer,
    selling_point_three_icon_id integer,
    selling_point_two_icon_id integer,
    related_page_one_id integer,
    related_page_three_id integer,
    related_page_two_id integer
);


--
-- Name: export_readiness_contactsuccesspage; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.export_readiness_contactsuccesspage (
    page_ptr_id integer NOT NULL,
    service_name character varying(100),
    heading character varying(255) NOT NULL,
    body_text character varying(255) NOT NULL,
    next_title character varying(255) NOT NULL,
    next_body_text character varying(255) NOT NULL,
    topic text NOT NULL
);


--
-- Name: export_readiness_contactsuccesspages; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.export_readiness_contactsuccesspages (
    page_ptr_id integer NOT NULL,
    service_name character varying(100)
);


--
-- Name: export_readiness_contactusguidancepage; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.export_readiness_contactusguidancepage (
    page_ptr_id integer NOT NULL,
    service_name character varying(100),
    topic text NOT NULL,
    body text NOT NULL
);


--
-- Name: export_readiness_contactusguidancepages; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.export_readiness_contactusguidancepages (
    page_ptr_id integer NOT NULL,
    service_name character varying(100)
);


--
-- Name: export_readiness_countryguidepage; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.export_readiness_countryguidepage (
    page_ptr_id integer NOT NULL,
    service_name character varying(100),
    landing_page_title character varying(255) NOT NULL,
    section_one_heading character varying(50) NOT NULL,
    section_one_content text NOT NULL,
    selling_point_one_heading character varying(255) NOT NULL,
    selling_point_one_content text NOT NULL,
    selling_point_two_heading character varying(255),
    selling_point_two_content text,
    selling_point_three_heading character varying(255),
    selling_point_three_content text,
    section_two_heading character varying(255) NOT NULL,
    section_two_content text NOT NULL,
    related_content_heading character varying(255) NOT NULL,
    related_content_intro text NOT NULL,
    hero_image_id integer,
    related_page_one_id integer,
    related_page_three_id integer,
    related_page_two_id integer,
    selling_point_one_icon_id integer,
    selling_point_three_icon_id integer,
    selling_point_two_icon_id integer
);


--
-- Name: export_readiness_euexitdomesticformpage; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.export_readiness_euexitdomesticformpage (
    page_ptr_id integer NOT NULL,
    service_name character varying(100),
    breadcrumbs_label character varying(50) NOT NULL,
    first_name_help_text character varying(200),
    first_name_label character varying(200) NOT NULL,
    last_name_help_text character varying(200),
    last_name_label character varying(200) NOT NULL,
    email_help_text character varying(200),
    email_label character varying(200) NOT NULL,
    organisation_type_help_text character varying(200),
    organisation_type_label character varying(200) NOT NULL,
    company_name_help_text character varying(200),
    company_name_label character varying(200) NOT NULL,
    comment_help_text character varying(200),
    comment_label character varying(200) NOT NULL,
    body_text text NOT NULL,
    heading character varying(255) NOT NULL,
    submit_button_text character varying(50) NOT NULL,
    disclaimer text NOT NULL
);


--
-- Name: export_readiness_euexitformpages; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.export_readiness_euexitformpages (
    page_ptr_id integer NOT NULL,
    service_name character varying(100)
);


--
-- Name: export_readiness_euexitformsuccesspage; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.export_readiness_euexitformsuccesspage (
    page_ptr_id integer NOT NULL,
    service_name character varying(100),
    breadcrumbs_label character varying(50) NOT NULL,
    heading character varying(255) NOT NULL,
    body_text character varying(255) NOT NULL,
    next_title character varying(255) NOT NULL,
    next_body_text character varying(255) NOT NULL
);


--
-- Name: export_readiness_euexitinternationalformpage; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.export_readiness_euexitinternationalformpage (
    page_ptr_id integer NOT NULL,
    service_name character varying(100),
    breadcrumbs_label character varying(50) NOT NULL,
    first_name_label character varying(200) NOT NULL,
    first_name_help_text character varying(200),
    last_name_label character varying(200) NOT NULL,
    last_name_help_text character varying(200),
    email_label character varying(200) NOT NULL,
    email_help_text character varying(200),
    organisation_type_label character varying(200) NOT NULL,
    organisation_type_help_text character varying(200),
    company_name_label character varying(200) NOT NULL,
    company_name_help_text character varying(200),
    country_label character varying(200) NOT NULL,
    country_help_text character varying(200),
    city_label character varying(200) NOT NULL,
    city_help_text character varying(200),
    comment_label character varying(200) NOT NULL,
    comment_help_text character varying(200),
    body_text text NOT NULL,
    heading character varying(255) NOT NULL,
    submit_button_text character varying(50) NOT NULL,
    disclaimer text NOT NULL
);


--
-- Name: export_readiness_exportreadinessapp; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.export_readiness_exportreadinessapp (
    page_ptr_id integer NOT NULL,
    service_name character varying(100)
);


--
-- Name: export_readiness_getfinancepage; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.export_readiness_getfinancepage (
    page_ptr_id integer NOT NULL,
    service_name character varying(100),
    breadcrumbs_label character varying(50) NOT NULL,
    hero_text text NOT NULL,
    contact_proposition text NOT NULL,
    contact_button character varying(500) NOT NULL,
    advantages_title character varying(500) NOT NULL,
    advantages_one text NOT NULL,
    advantages_two text NOT NULL,
    advantages_three text NOT NULL,
    evidence text NOT NULL,
    hero_image_id integer,
    ukef_logo_id integer,
    advantages_one_icon_id integer,
    advantages_three_icon_id integer,
    advantages_two_icon_id integer,
    evidence_video_id integer
);


--
-- Name: export_readiness_homepage; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.export_readiness_homepage (
    page_ptr_id integer NOT NULL,
    service_name character varying(100),
    news_title character varying(255) NOT NULL,
    news_description text NOT NULL,
    banner_content text NOT NULL,
    banner_label character varying(50)
);


--
-- Name: export_readiness_internationallandingpage; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.export_readiness_internationallandingpage (
    page_ptr_id integer NOT NULL,
    service_name character varying(100)
);


--
-- Name: export_readiness_marketingpages; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.export_readiness_marketingpages (
    page_ptr_id integer NOT NULL,
    service_name character varying(100)
);


--
-- Name: export_readiness_performancedashboardnotespage; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.export_readiness_performancedashboardnotespage (
    page_ptr_id integer NOT NULL,
    body text NOT NULL,
    service_name character varying(100)
);


--
-- Name: export_readiness_performancedashboardpage; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.export_readiness_performancedashboardpage (
    page_ptr_id integer NOT NULL,
    heading character varying(255) NOT NULL,
    description text NOT NULL,
    product_link text NOT NULL,
    data_title_row_one character varying(100) NOT NULL,
    data_number_row_one character varying(15) NOT NULL,
    data_period_row_one character varying(100) NOT NULL,
    data_description_row_one text NOT NULL,
    data_title_row_two character varying(100) NOT NULL,
    data_number_row_two character varying(15) NOT NULL,
    data_period_row_two character varying(100) NOT NULL,
    data_description_row_two text NOT NULL,
    data_title_row_three character varying(100) NOT NULL,
    data_number_row_three character varying(15) NOT NULL,
    data_period_row_three character varying(100) NOT NULL,
    data_description_row_three text NOT NULL,
    data_title_row_four character varying(100),
    data_number_row_four character varying(15),
    data_period_row_four character varying(100),
    data_description_row_four text,
    landing_dashboard boolean NOT NULL,
    guidance_notes text,
    service_name character varying(100)
);


--
-- Name: export_readiness_privacyandcookiespage; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.export_readiness_privacyandcookiespage (
    page_ptr_id integer NOT NULL,
    body text NOT NULL,
    service_name character varying(100)
);


--
-- Name: export_readiness_sitepolicypages; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.export_readiness_sitepolicypages (
    page_ptr_id integer NOT NULL,
    service_name character varying(100)
);


--
-- Name: export_readiness_superregionpage; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.export_readiness_superregionpage (
    topiclandingpage_ptr_id integer NOT NULL
);


--
-- Name: export_readiness_tag; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.export_readiness_tag (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    slug character varying(255) NOT NULL
);


--
-- Name: export_readiness_tag_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.export_readiness_tag_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: export_readiness_tag_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.export_readiness_tag_id_seq OWNED BY public.export_readiness_tag.id;


--
-- Name: export_readiness_termsandconditionspage; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.export_readiness_termsandconditionspage (
    page_ptr_id integer NOT NULL,
    body text NOT NULL,
    service_name character varying(100)
);


--
-- Name: export_readiness_topiclandingpage; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.export_readiness_topiclandingpage (
    page_ptr_id integer NOT NULL,
    service_name character varying(100),
    landing_page_title character varying(255) NOT NULL,
    hero_teaser character varying(255),
    hero_image_id integer
);


--
-- Name: find_a_supplier_findasupplierapp; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.find_a_supplier_findasupplierapp (
    page_ptr_id integer NOT NULL,
    service_name character varying(100)
);


--
-- Name: find_a_supplier_industryarticlepage; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.find_a_supplier_industryarticlepage (
    page_ptr_id integer NOT NULL,
    body text NOT NULL,
    body_en_gb text,
    body_de text,
    body_ja text,
    body_ru text,
    body_zh_hans text,
    body_fr text,
    body_es text,
    body_pt text,
    body_pt_br text,
    body_ar text,
    author_name character varying(255) NOT NULL,
    author_name_en_gb character varying(255),
    author_name_de character varying(255),
    author_name_ja character varying(255),
    author_name_ru character varying(255),
    author_name_zh_hans character varying(255),
    author_name_fr character varying(255),
    author_name_es character varying(255),
    author_name_pt character varying(255),
    author_name_pt_br character varying(255),
    author_name_ar character varying(255),
    job_title character varying(255) NOT NULL,
    job_title_en_gb character varying(255),
    job_title_de character varying(255),
    job_title_ja character varying(255),
    job_title_ru character varying(255),
    job_title_zh_hans character varying(255),
    job_title_fr character varying(255),
    job_title_es character varying(255),
    job_title_pt character varying(255),
    job_title_pt_br character varying(255),
    job_title_ar character varying(255),
    date date NOT NULL,
    date_en_gb date,
    date_de date,
    date_ja date,
    date_ru date,
    date_zh_hans date,
    date_fr date,
    date_es date,
    date_pt date,
    date_pt_br date,
    date_ar date,
    introduction_title character varying(255) NOT NULL,
    introduction_title_ar character varying(255),
    introduction_title_de character varying(255),
    introduction_title_en_gb character varying(255),
    introduction_title_es character varying(255),
    introduction_title_fr character varying(255),
    introduction_title_ja character varying(255),
    introduction_title_pt character varying(255),
    introduction_title_pt_br character varying(255),
    introduction_title_ru character varying(255),
    introduction_title_zh_hans character varying(255),
    breadcrumbs_label character varying(50) NOT NULL,
    breadcrumbs_label_ar character varying(50),
    breadcrumbs_label_de character varying(50),
    breadcrumbs_label_en_gb character varying(50),
    breadcrumbs_label_es character varying(50),
    breadcrumbs_label_fr character varying(50),
    breadcrumbs_label_ja character varying(50),
    breadcrumbs_label_pt character varying(50),
    breadcrumbs_label_pt_br character varying(50),
    breadcrumbs_label_ru character varying(50),
    breadcrumbs_label_zh_hans character varying(50),
    call_to_action_text character varying(500) NOT NULL,
    call_to_action_text_ar character varying(500),
    call_to_action_text_de character varying(500),
    call_to_action_text_en_gb character varying(500),
    call_to_action_text_es character varying(500),
    call_to_action_text_fr character varying(500),
    call_to_action_text_ja character varying(500),
    call_to_action_text_pt character varying(500),
    call_to_action_text_pt_br character varying(500),
    call_to_action_text_ru character varying(500),
    call_to_action_text_zh_hans character varying(500),
    proposition_text character varying(255) NOT NULL,
    proposition_text_ar character varying(255),
    proposition_text_de character varying(255),
    proposition_text_en_gb character varying(255),
    proposition_text_es character varying(255),
    proposition_text_fr character varying(255),
    proposition_text_ja character varying(255),
    proposition_text_pt character varying(255),
    proposition_text_pt_br character varying(255),
    proposition_text_ru character varying(255),
    proposition_text_zh_hans character varying(255),
    show_table_of_content boolean NOT NULL,
    back_to_home_link_text character varying(100) NOT NULL,
    back_to_home_link_text_ar character varying(100),
    back_to_home_link_text_de character varying(100),
    back_to_home_link_text_en_gb character varying(100),
    back_to_home_link_text_es character varying(100),
    back_to_home_link_text_fr character varying(100),
    back_to_home_link_text_ja character varying(100),
    back_to_home_link_text_pt character varying(100),
    back_to_home_link_text_pt_br character varying(100),
    back_to_home_link_text_ru character varying(100),
    back_to_home_link_text_zh_hans character varying(100),
    social_share_title character varying(100) NOT NULL,
    social_share_title_ar character varying(100),
    social_share_title_de character varying(100),
    social_share_title_en_gb character varying(100),
    social_share_title_es character varying(100),
    social_share_title_fr character varying(100),
    social_share_title_ja character varying(100),
    social_share_title_pt character varying(100),
    social_share_title_pt_br character varying(100),
    social_share_title_ru character varying(100),
    social_share_title_zh_hans character varying(100),
    service_name character varying(100)
);


--
-- Name: find_a_supplier_industrycontactpage; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.find_a_supplier_industrycontactpage (
    page_ptr_id integer NOT NULL,
    introduction_text text NOT NULL,
    introduction_text_en_gb text,
    introduction_text_de text,
    introduction_text_ja text,
    introduction_text_ru text,
    introduction_text_zh_hans text,
    introduction_text_fr text,
    introduction_text_es text,
    introduction_text_pt text,
    introduction_text_pt_br text,
    introduction_text_ar text,
    submit_button_text character varying(100) NOT NULL,
    submit_button_text_en_gb character varying(100),
    submit_button_text_de character varying(100),
    submit_button_text_ja character varying(100),
    submit_button_text_ru character varying(100),
    submit_button_text_zh_hans character varying(100),
    submit_button_text_fr character varying(100),
    submit_button_text_es character varying(100),
    submit_button_text_pt character varying(100),
    submit_button_text_pt_br character varying(100),
    submit_button_text_ar character varying(100),
    success_message_text text NOT NULL,
    success_message_text_en_gb text,
    success_message_text_de text,
    success_message_text_ja text,
    success_message_text_ru text,
    success_message_text_zh_hans text,
    success_message_text_fr text,
    success_message_text_es text,
    success_message_text_pt text,
    success_message_text_pt_br text,
    success_message_text_ar text,
    success_back_link_text character varying(100) NOT NULL,
    success_back_link_text_en_gb character varying(100),
    success_back_link_text_de character varying(100),
    success_back_link_text_ja character varying(100),
    success_back_link_text_ru character varying(100),
    success_back_link_text_zh_hans character varying(100),
    success_back_link_text_fr character varying(100),
    success_back_link_text_es character varying(100),
    success_back_link_text_pt character varying(100),
    success_back_link_text_pt_br character varying(100),
    success_back_link_text_ar character varying(100),
    breadcrumbs_label character varying(50) NOT NULL,
    breadcrumbs_label_ar character varying(50),
    breadcrumbs_label_de character varying(50),
    breadcrumbs_label_en_gb character varying(50),
    breadcrumbs_label_es character varying(50),
    breadcrumbs_label_fr character varying(50),
    breadcrumbs_label_ja character varying(50),
    breadcrumbs_label_pt character varying(50),
    breadcrumbs_label_pt_br character varying(50),
    breadcrumbs_label_ru character varying(50),
    breadcrumbs_label_zh_hans character varying(50),
    service_name character varying(100)
);


--
-- Name: find_a_supplier_industrylandingpage; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.find_a_supplier_industrylandingpage (
    page_ptr_id integer NOT NULL,
    proposition_text character varying(500) NOT NULL,
    proposition_text_en_gb character varying(500),
    proposition_text_de character varying(500),
    proposition_text_ja character varying(500),
    proposition_text_ru character varying(500),
    proposition_text_zh_hans character varying(500),
    proposition_text_fr character varying(500),
    proposition_text_es character varying(500),
    proposition_text_pt character varying(500),
    proposition_text_pt_br character varying(500),
    proposition_text_ar character varying(500),
    call_to_action_text character varying(500) NOT NULL,
    call_to_action_text_en_gb character varying(500),
    call_to_action_text_de character varying(500),
    call_to_action_text_ja character varying(500),
    call_to_action_text_ru character varying(500),
    call_to_action_text_zh_hans character varying(500),
    call_to_action_text_fr character varying(500),
    call_to_action_text_es character varying(500),
    call_to_action_text_pt character varying(500),
    call_to_action_text_pt_br character varying(500),
    call_to_action_text_ar character varying(500),
    breadcrumbs_label character varying(50) NOT NULL,
    breadcrumbs_label_en_gb character varying(50),
    breadcrumbs_label_de character varying(50),
    breadcrumbs_label_ja character varying(50),
    breadcrumbs_label_ru character varying(50),
    breadcrumbs_label_zh_hans character varying(50),
    breadcrumbs_label_fr character varying(50),
    breadcrumbs_label_es character varying(50),
    breadcrumbs_label_pt character varying(50),
    breadcrumbs_label_pt_br character varying(50),
    breadcrumbs_label_ar character varying(50),
    hero_image_id integer,
    hero_title character varying(500) NOT NULL,
    hero_title_ar character varying(500),
    hero_title_de character varying(500),
    hero_title_en_gb character varying(500),
    hero_title_es character varying(500),
    hero_title_fr character varying(500),
    hero_title_ja character varying(500),
    hero_title_pt character varying(500),
    hero_title_pt_br character varying(500),
    hero_title_ru character varying(500),
    hero_title_zh_hans character varying(500),
    mobile_hero_image_id integer,
    more_industries_title character varying(100) NOT NULL,
    more_industries_title_ar character varying(100),
    more_industries_title_de character varying(100),
    more_industries_title_en_gb character varying(100),
    more_industries_title_es character varying(100),
    more_industries_title_fr character varying(100),
    more_industries_title_ja character varying(100),
    more_industries_title_pt character varying(100),
    more_industries_title_pt_br character varying(100),
    more_industries_title_ru character varying(100),
    more_industries_title_zh_hans character varying(100),
    hero_image_caption character varying(255) NOT NULL,
    hero_image_caption_ar character varying(255),
    hero_image_caption_de character varying(255),
    hero_image_caption_en_gb character varying(255),
    hero_image_caption_es character varying(255),
    hero_image_caption_fr character varying(255),
    hero_image_caption_ja character varying(255),
    hero_image_caption_pt character varying(255),
    hero_image_caption_pt_br character varying(255),
    hero_image_caption_ru character varying(255),
    hero_image_caption_zh_hans character varying(255),
    service_name character varying(100)
);


--
-- Name: find_a_supplier_industrypage; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.find_a_supplier_industrypage (
    page_ptr_id integer NOT NULL,
    hero_text text NOT NULL,
    hero_text_en_gb text,
    hero_text_de text,
    hero_text_ja text,
    hero_text_zh_hans text,
    hero_text_fr text,
    hero_text_es text,
    hero_text_pt text,
    hero_text_pt_br text,
    hero_text_ar text,
    introduction_text character varying(400) NOT NULL,
    introduction_text_en_gb character varying(400),
    introduction_text_de character varying(400),
    introduction_text_ja character varying(400),
    introduction_text_zh_hans character varying(400),
    introduction_text_fr character varying(400),
    introduction_text_es character varying(400),
    introduction_text_pt character varying(400),
    introduction_text_pt_br character varying(400),
    introduction_text_ar character varying(400),
    introduction_column_one_text text NOT NULL,
    introduction_column_one_text_en_gb text,
    introduction_column_one_text_de text,
    introduction_column_one_text_ja text,
    introduction_column_one_text_zh_hans text,
    introduction_column_one_text_fr text,
    introduction_column_one_text_es text,
    introduction_column_one_text_pt text,
    introduction_column_one_text_pt_br text,
    introduction_column_one_text_ar text,
    introduction_column_two_text text NOT NULL,
    introduction_column_two_text_en_gb text,
    introduction_column_two_text_de text,
    introduction_column_two_text_ja text,
    introduction_column_two_text_zh_hans text,
    introduction_column_two_text_fr text,
    introduction_column_two_text_es text,
    introduction_column_two_text_pt text,
    introduction_column_two_text_pt_br text,
    introduction_column_two_text_ar text,
    introduction_column_three_text text NOT NULL,
    introduction_column_three_text_en_gb text,
    introduction_column_three_text_de text,
    introduction_column_three_text_ja text,
    introduction_column_three_text_zh_hans text,
    introduction_column_three_text_fr text,
    introduction_column_three_text_es text,
    introduction_column_three_text_pt text,
    introduction_column_three_text_pt_br text,
    introduction_column_three_text_ar text,
    hero_image_id integer,
    hero_text_ru text,
    introduction_column_one_text_ru text,
    introduction_column_three_text_ru text,
    introduction_column_two_text_ru text,
    introduction_text_ru character varying(400),
    introduction_column_one_icon_id integer,
    introduction_column_three_icon_id integer,
    introduction_column_two_icon_id integer,
    company_list_call_to_action_text character varying(255) NOT NULL,
    company_list_call_to_action_text_ar character varying(255),
    company_list_call_to_action_text_de character varying(255),
    company_list_call_to_action_text_en_gb character varying(255),
    company_list_call_to_action_text_es character varying(255),
    company_list_call_to_action_text_fr character varying(255),
    company_list_call_to_action_text_ja character varying(255),
    company_list_call_to_action_text_pt character varying(255),
    company_list_call_to_action_text_pt_br character varying(255),
    company_list_call_to_action_text_ru character varying(255),
    company_list_call_to_action_text_zh_hans character varying(255),
    company_list_text text NOT NULL,
    company_list_text_ar text,
    company_list_text_de text,
    company_list_text_en_gb text,
    company_list_text_es text,
    company_list_text_fr text,
    company_list_text_ja text,
    company_list_text_pt text,
    company_list_text_pt_br text,
    company_list_text_ru text,
    company_list_text_zh_hans text,
    company_list_search_input_placeholder_text character varying(255) NOT NULL,
    company_list_search_input_placeholder_text_ar character varying(255),
    company_list_search_input_placeholder_text_de character varying(255),
    company_list_search_input_placeholder_text_en_gb character varying(255),
    company_list_search_input_placeholder_text_es character varying(255),
    company_list_search_input_placeholder_text_fr character varying(255),
    company_list_search_input_placeholder_text_ja character varying(255),
    company_list_search_input_placeholder_text_pt character varying(255),
    company_list_search_input_placeholder_text_pt_br character varying(255),
    company_list_search_input_placeholder_text_ru character varying(255),
    company_list_search_input_placeholder_text_zh_hans character varying(255),
    breadcrumbs_label character varying(50) NOT NULL,
    breadcrumbs_label_ar character varying(50),
    breadcrumbs_label_de character varying(50),
    breadcrumbs_label_en_gb character varying(50),
    breadcrumbs_label_es character varying(50),
    breadcrumbs_label_fr character varying(50),
    breadcrumbs_label_ja character varying(50),
    breadcrumbs_label_pt character varying(50),
    breadcrumbs_label_pt_br character varying(50),
    breadcrumbs_label_ru character varying(50),
    breadcrumbs_label_zh_hans character varying(50),
    introduction_call_to_action_button_text character varying(50) NOT NULL,
    introduction_call_to_action_button_text_ar character varying(50),
    introduction_call_to_action_button_text_de character varying(50),
    introduction_call_to_action_button_text_en_gb character varying(50),
    introduction_call_to_action_button_text_es character varying(50),
    introduction_call_to_action_button_text_fr character varying(50),
    introduction_call_to_action_button_text_ja character varying(50),
    introduction_call_to_action_button_text_pt character varying(50),
    introduction_call_to_action_button_text_pt_br character varying(50),
    introduction_call_to_action_button_text_ru character varying(50),
    introduction_call_to_action_button_text_zh_hans character varying(50),
    summary_image_id integer,
    search_filter_sector character varying(255)[],
    search_filter_text character varying(100),
    mobile_hero_image_id integer,
    search_filter_showcase_only boolean NOT NULL,
    hero_image_caption character varying(255) NOT NULL,
    hero_image_caption_ar character varying(255),
    hero_image_caption_de character varying(255),
    hero_image_caption_en_gb character varying(255),
    hero_image_caption_es character varying(255),
    hero_image_caption_fr character varying(255),
    hero_image_caption_ja character varying(255),
    hero_image_caption_pt character varying(255),
    hero_image_caption_pt_br character varying(255),
    hero_image_caption_ru character varying(255),
    hero_image_caption_zh_hans character varying(255),
    introduction_title character varying(400) NOT NULL,
    introduction_title_ar character varying(400),
    introduction_title_de character varying(400),
    introduction_title_en_gb character varying(400),
    introduction_title_es character varying(400),
    introduction_title_fr character varying(400),
    introduction_title_ja character varying(400),
    introduction_title_pt character varying(400),
    introduction_title_pt_br character varying(400),
    introduction_title_ru character varying(400),
    introduction_title_zh_hans character varying(400),
    show_on_homepage boolean NOT NULL,
    show_on_industries_showcase_page boolean NOT NULL,
    service_name character varying(100)
);


--
-- Name: find_a_supplier_industrypagearticlesummary; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.find_a_supplier_industrypagearticlesummary (
    id integer NOT NULL,
    sort_order integer,
    industry_name character varying(255) NOT NULL,
    title character varying(255) NOT NULL,
    body text NOT NULL,
    image_id integer,
    page_id integer,
    page_ar_id integer,
    page_de_id integer,
    page_en_gb_id integer,
    page_es_id integer,
    page_fr_id integer,
    page_ja_id integer,
    page_pt_id integer,
    page_pt_br_id integer,
    page_ru_id integer,
    page_zh_hans_id integer,
    video_media_id integer
);


--
-- Name: find_a_supplier_industrypagearticlesummary_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.find_a_supplier_industrypagearticlesummary_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: find_a_supplier_industrypagearticlesummary_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.find_a_supplier_industrypagearticlesummary_id_seq OWNED BY public.find_a_supplier_industrypagearticlesummary.id;


--
-- Name: find_a_supplier_landingpage; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.find_a_supplier_landingpage (
    page_ptr_id integer NOT NULL,
    hero_text text NOT NULL,
    hero_text_en_gb text,
    hero_text_de text,
    hero_text_ja text,
    hero_text_ru text,
    hero_text_zh_hans text,
    hero_text_fr text,
    hero_text_es text,
    hero_text_pt text,
    hero_text_pt_br text,
    hero_text_ar text,
    search_field_placeholder character varying(500) NOT NULL,
    search_field_placeholder_en_gb character varying(500),
    search_field_placeholder_de character varying(500),
    search_field_placeholder_ja character varying(500),
    search_field_placeholder_ru character varying(500),
    search_field_placeholder_zh_hans character varying(500),
    search_field_placeholder_fr character varying(500),
    search_field_placeholder_es character varying(500),
    search_field_placeholder_pt character varying(500),
    search_field_placeholder_pt_br character varying(500),
    search_field_placeholder_ar character varying(500),
    search_button_text character varying(500) NOT NULL,
    search_button_text_en_gb character varying(500),
    search_button_text_de character varying(500),
    search_button_text_ja character varying(500),
    search_button_text_ru character varying(500),
    search_button_text_zh_hans character varying(500),
    search_button_text_fr character varying(500),
    search_button_text_es character varying(500),
    search_button_text_pt character varying(500),
    search_button_text_pt_br character varying(500),
    search_button_text_ar character varying(500),
    proposition_text text NOT NULL,
    proposition_text_en_gb text,
    proposition_text_de text,
    proposition_text_ja text,
    proposition_text_ru text,
    proposition_text_zh_hans text,
    proposition_text_fr text,
    proposition_text_es text,
    proposition_text_pt text,
    proposition_text_pt_br text,
    proposition_text_ar text,
    call_to_action_text character varying(500) NOT NULL,
    call_to_action_text_en_gb character varying(500),
    call_to_action_text_de character varying(500),
    call_to_action_text_ja character varying(500),
    call_to_action_text_ru character varying(500),
    call_to_action_text_zh_hans character varying(500),
    call_to_action_text_fr character varying(500),
    call_to_action_text_es character varying(500),
    call_to_action_text_pt character varying(500),
    call_to_action_text_pt_br character varying(500),
    call_to_action_text_ar character varying(500),
    industries_list_text text NOT NULL,
    industries_list_text_en_gb text,
    industries_list_text_de text,
    industries_list_text_ja text,
    industries_list_text_ru text,
    industries_list_text_zh_hans text,
    industries_list_text_fr text,
    industries_list_text_es text,
    industries_list_text_pt text,
    industries_list_text_pt_br text,
    industries_list_text_ar text,
    industries_list_call_to_action_text character varying(500) NOT NULL,
    industries_list_call_to_action_text_en_gb character varying(500),
    industries_list_call_to_action_text_de character varying(500),
    industries_list_call_to_action_text_ja character varying(500),
    industries_list_call_to_action_text_ru character varying(500),
    industries_list_call_to_action_text_zh_hans character varying(500),
    industries_list_call_to_action_text_fr character varying(500),
    industries_list_call_to_action_text_es character varying(500),
    industries_list_call_to_action_text_pt character varying(500),
    industries_list_call_to_action_text_pt_br character varying(500),
    industries_list_call_to_action_text_ar character varying(500),
    services_list_text text NOT NULL,
    services_list_text_en_gb text,
    services_list_text_de text,
    services_list_text_ja text,
    services_list_text_ru text,
    services_list_text_zh_hans text,
    services_list_text_fr text,
    services_list_text_es text,
    services_list_text_pt text,
    services_list_text_pt_br text,
    services_list_text_ar text,
    services_column_one text NOT NULL,
    services_column_one_en_gb text,
    services_column_one_de text,
    services_column_one_ja text,
    services_column_one_ru text,
    services_column_one_zh_hans text,
    services_column_one_fr text,
    services_column_one_es text,
    services_column_one_pt text,
    services_column_one_pt_br text,
    services_column_one_ar text,
    services_column_two text NOT NULL,
    services_column_two_en_gb text,
    services_column_two_de text,
    services_column_two_ja text,
    services_column_two_ru text,
    services_column_two_zh_hans text,
    services_column_two_fr text,
    services_column_two_es text,
    services_column_two_pt text,
    services_column_two_pt_br text,
    services_column_two_ar text,
    services_column_three text NOT NULL,
    services_column_three_en_gb text,
    services_column_three_de text,
    services_column_three_ja text,
    services_column_three_ru text,
    services_column_three_zh_hans text,
    services_column_three_fr text,
    services_column_three_es text,
    services_column_three_pt text,
    services_column_three_pt_br text,
    services_column_three_ar text,
    services_column_four text NOT NULL,
    services_column_four_en_gb text,
    services_column_four_de text,
    services_column_four_ja text,
    services_column_four_ru text,
    services_column_four_zh_hans text,
    services_column_four_fr text,
    services_column_four_es text,
    services_column_four_pt text,
    services_column_four_pt_br text,
    services_column_four_ar text,
    hero_image_id integer,
    services_column_four_icon_id integer,
    services_column_four_icon_ar_id integer,
    services_column_four_icon_de_id integer,
    services_column_four_icon_en_gb_id integer,
    services_column_four_icon_es_id integer,
    services_column_four_icon_fr_id integer,
    services_column_four_icon_ja_id integer,
    services_column_four_icon_pt_id integer,
    services_column_four_icon_pt_br_id integer,
    services_column_four_icon_ru_id integer,
    services_column_four_icon_zh_hans_id integer,
    services_column_one_icon_id integer,
    services_column_one_icon_ar_id integer,
    services_column_one_icon_de_id integer,
    services_column_one_icon_en_gb_id integer,
    services_column_one_icon_es_id integer,
    services_column_one_icon_fr_id integer,
    services_column_one_icon_ja_id integer,
    services_column_one_icon_pt_id integer,
    services_column_one_icon_pt_br_id integer,
    services_column_one_icon_ru_id integer,
    services_column_one_icon_zh_hans_id integer,
    services_column_three_icon_id integer,
    services_column_three_icon_ar_id integer,
    services_column_three_icon_de_id integer,
    services_column_three_icon_en_gb_id integer,
    services_column_three_icon_es_id integer,
    services_column_three_icon_fr_id integer,
    services_column_three_icon_ja_id integer,
    services_column_three_icon_pt_id integer,
    services_column_three_icon_pt_br_id integer,
    services_column_three_icon_ru_id integer,
    services_column_three_icon_zh_hans_id integer,
    services_column_two_icon_id integer,
    services_column_two_icon_ar_id integer,
    services_column_two_icon_de_id integer,
    services_column_two_icon_en_gb_id integer,
    services_column_two_icon_es_id integer,
    services_column_two_icon_fr_id integer,
    services_column_two_icon_ja_id integer,
    services_column_two_icon_pt_id integer,
    services_column_two_icon_pt_br_id integer,
    services_column_two_icon_ru_id integer,
    services_column_two_icon_zh_hans_id integer,
    breadcrumbs_label character varying(50) NOT NULL,
    breadcrumbs_label_ar character varying(50),
    breadcrumbs_label_de character varying(50),
    breadcrumbs_label_en_gb character varying(50),
    breadcrumbs_label_es character varying(50),
    breadcrumbs_label_fr character varying(50),
    breadcrumbs_label_ja character varying(50),
    breadcrumbs_label_pt character varying(50),
    breadcrumbs_label_pt_br character varying(50),
    breadcrumbs_label_ru character varying(50),
    breadcrumbs_label_zh_hans character varying(50),
    mobile_hero_image_id integer,
    hero_image_caption character varying(255) NOT NULL,
    hero_image_caption_ar character varying(255),
    hero_image_caption_de character varying(255),
    hero_image_caption_en_gb character varying(255),
    hero_image_caption_es character varying(255),
    hero_image_caption_fr character varying(255),
    hero_image_caption_ja character varying(255),
    hero_image_caption_pt character varying(255),
    hero_image_caption_pt_br character varying(255),
    hero_image_caption_ru character varying(255),
    hero_image_caption_zh_hans character varying(255),
    service_name character varying(100)
);


--
-- Name: find_a_supplier_landingpagearticlesummary; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.find_a_supplier_landingpagearticlesummary (
    id integer NOT NULL,
    sort_order integer,
    industry_name character varying(255) NOT NULL,
    title character varying(255) NOT NULL,
    body text NOT NULL,
    image_id integer,
    page_id integer,
    page_ar_id integer,
    page_de_id integer,
    page_en_gb_id integer,
    page_es_id integer,
    page_fr_id integer,
    page_ja_id integer,
    page_pt_id integer,
    page_pt_br_id integer,
    page_ru_id integer,
    page_zh_hans_id integer,
    video_media_id integer
);


--
-- Name: find_a_supplier_landingpagearticlesummary_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.find_a_supplier_landingpagearticlesummary_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: find_a_supplier_landingpagearticlesummary_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.find_a_supplier_landingpagearticlesummary_id_seq OWNED BY public.find_a_supplier_landingpagearticlesummary.id;


--
-- Name: great_international_greatinternationalapp; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.great_international_greatinternationalapp (
    page_ptr_id integer NOT NULL,
    service_name character varying(100)
);


--
-- Name: great_international_internationalarticlelistingpage; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.great_international_internationalarticlelistingpage (
    page_ptr_id integer NOT NULL,
    service_name character varying(100),
    landing_page_title character varying(255) NOT NULL,
    hero_teaser character varying(255),
    list_teaser text,
    hero_image_id integer
);


--
-- Name: great_international_internationalarticlelistingpage_tags; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.great_international_internationalarticlelistingpage_tags (
    id integer NOT NULL,
    internationalarticlelistingpage_id integer NOT NULL,
    tag_id integer NOT NULL
);


--
-- Name: great_international_internationalarticlelistingpage_tags_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.great_international_internationalarticlelistingpage_tags_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: great_international_internationalarticlelistingpage_tags_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.great_international_internationalarticlelistingpage_tags_id_seq OWNED BY public.great_international_internationalarticlelistingpage_tags.id;


--
-- Name: great_international_internationalarticlepage; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.great_international_internationalarticlepage (
    page_ptr_id integer NOT NULL,
    service_name character varying(100),
    article_title character varying(255) NOT NULL,
    article_teaser character varying(255) NOT NULL,
    article_body_text text NOT NULL,
    article_image_id integer,
    related_page_one_id integer,
    related_page_three_id integer,
    related_page_two_id integer
);


--
-- Name: great_international_internationalarticlepage_tags; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.great_international_internationalarticlepage_tags (
    id integer NOT NULL,
    internationalarticlepage_id integer NOT NULL,
    tag_id integer NOT NULL
);


--
-- Name: great_international_internationalarticlepage_tags_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.great_international_internationalarticlepage_tags_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: great_international_internationalarticlepage_tags_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.great_international_internationalarticlepage_tags_id_seq OWNED BY public.great_international_internationalarticlepage_tags.id;


--
-- Name: great_international_internationalcampaignpage; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.great_international_internationalcampaignpage (
    page_ptr_id integer NOT NULL,
    service_name character varying(100),
    campaign_heading character varying(255) NOT NULL,
    section_one_heading character varying(255) NOT NULL,
    section_one_intro text NOT NULL,
    selling_point_one_heading character varying(255) NOT NULL,
    selling_point_one_content text NOT NULL,
    selling_point_two_heading character varying(255),
    selling_point_two_content text,
    selling_point_three_heading character varying(255),
    selling_point_three_content text,
    section_one_contact_button_url character varying(255),
    section_one_contact_button_text character varying(255),
    section_two_heading character varying(255) NOT NULL,
    section_two_intro text NOT NULL,
    section_two_contact_button_url character varying(255),
    section_two_contact_button_text character varying(255),
    related_content_heading character varying(255) NOT NULL,
    related_content_intro text NOT NULL,
    cta_box_message character varying(255) NOT NULL,
    cta_box_button_url character varying(255) NOT NULL,
    cta_box_button_text character varying(255) NOT NULL,
    campaign_hero_image_id integer,
    related_page_one_id integer,
    related_page_three_id integer,
    related_page_two_id integer,
    section_one_image_id integer,
    section_two_image_id integer,
    selling_point_one_icon_id integer,
    selling_point_three_icon_id integer,
    selling_point_two_icon_id integer,
    campaign_teaser character varying(255)
);


--
-- Name: great_international_internationalcampaignpage_tags; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.great_international_internationalcampaignpage_tags (
    id integer NOT NULL,
    internationalcampaignpage_id integer NOT NULL,
    tag_id integer NOT NULL
);


--
-- Name: great_international_internationalcampaignpage_tags_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.great_international_internationalcampaignpage_tags_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: great_international_internationalcampaignpage_tags_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.great_international_internationalcampaignpage_tags_id_seq OWNED BY public.great_international_internationalcampaignpage_tags.id;


--
-- Name: great_international_internationalhomepage; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.great_international_internationalhomepage (
    page_ptr_id integer NOT NULL,
    service_name character varying(100),
    tariffs_title character varying(255) NOT NULL,
    tariffs_description text NOT NULL,
    tariffs_link character varying(200) NOT NULL,
    news_title character varying(255) NOT NULL,
    tariffs_image_id integer,
    related_page_one_id integer,
    related_page_three_id integer,
    related_page_two_id integer
);


--
-- Name: great_international_internationallocalisedfolderpage; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.great_international_internationallocalisedfolderpage (
    page_ptr_id integer NOT NULL,
    service_name character varying(100)
);


--
-- Name: great_international_internationalregionpage; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.great_international_internationalregionpage (
    page_ptr_id integer NOT NULL,
    service_name character varying(100)
);


--
-- Name: great_international_internationalregionpage_tags; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.great_international_internationalregionpage_tags (
    id integer NOT NULL,
    internationalregionpage_id integer NOT NULL,
    tag_id integer NOT NULL
);


--
-- Name: great_international_internationalregionpages_tags_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.great_international_internationalregionpages_tags_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: great_international_internationalregionpages_tags_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.great_international_internationalregionpages_tags_id_seq OWNED BY public.great_international_internationalregionpage_tags.id;


--
-- Name: great_international_internationalsectorpage; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.great_international_internationalsectorpage (
    page_ptr_id integer NOT NULL,
    service_name character varying(100),
    heading character varying(255) NOT NULL,
    sub_heading character varying(255) NOT NULL,
    heading_teaser character varying(255) NOT NULL,
    section_one_body text,
    statistic_1_number character varying(255) NOT NULL,
    statistic_1_heading character varying(255) NOT NULL,
    statistic_1_smallprint character varying(255) NOT NULL,
    statistic_2_number character varying(255) NOT NULL,
    statistic_2_heading character varying(255) NOT NULL,
    statistic_2_smallprint character varying(255) NOT NULL,
    statistic_3_number character varying(255) NOT NULL,
    statistic_3_heading character varying(255) NOT NULL,
    statistic_3_smallprint character varying(255) NOT NULL,
    statistic_4_number character varying(255) NOT NULL,
    statistic_4_heading character varying(255) NOT NULL,
    statistic_4_smallprint character varying(255) NOT NULL,
    statistic_5_number character varying(255) NOT NULL,
    statistic_5_heading character varying(255) NOT NULL,
    statistic_5_smallprint character varying(255) NOT NULL,
    statistic_6_number character varying(255) NOT NULL,
    statistic_6_heading character varying(255) NOT NULL,
    statistic_6_smallprint character varying(255) NOT NULL,
    section_two_heading character varying(255) NOT NULL,
    section_two_teaser character varying(255) NOT NULL,
    section_two_subsection_one_heading character varying(255) NOT NULL,
    section_two_subsection_one_body character varying(255) NOT NULL,
    section_two_subsection_two_heading character varying(255) NOT NULL,
    section_two_subsection_two_body character varying(255) NOT NULL,
    section_two_subsection_three_heading character varying(255) NOT NULL,
    section_two_subsection_three_body character varying(255) NOT NULL,
    case_study_title character varying(255) NOT NULL,
    case_study_description character varying(255) NOT NULL,
    case_study_cta_text character varying(255) NOT NULL,
    case_study_cta_url character varying(255) NOT NULL,
    section_three_heading character varying(255) NOT NULL,
    section_three_teaser character varying(255) NOT NULL,
    section_three_subsection_one_heading character varying(255) NOT NULL,
    section_three_subsection_one_teaser character varying(255) NOT NULL,
    section_three_subsection_one_body text,
    section_three_subsection_two_heading character varying(255) NOT NULL,
    section_three_subsection_two_teaser character varying(255) NOT NULL,
    section_three_subsection_two_body text,
    next_steps_heading character varying(255) NOT NULL,
    next_steps_description character varying(255) NOT NULL,
    case_study_image_id integer,
    hero_image_id integer,
    related_page_one_id integer,
    related_page_three_id integer,
    related_page_two_id integer,
    section_one_image_id integer,
    section_two_subsection_one_icon_id integer,
    section_two_subsection_three_icon_id integer,
    section_two_subsection_two_icon_id integer
);


--
-- Name: great_international_internationaltopiclandingpage; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.great_international_internationaltopiclandingpage (
    page_ptr_id integer NOT NULL,
    service_name character varying(100),
    landing_page_title character varying(255) NOT NULL,
    hero_teaser character varying(255),
    hero_image_id integer
);


--
-- Name: great_international_internationaltopiclandingpage_tags; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.great_international_internationaltopiclandingpage_tags (
    id integer NOT NULL,
    internationaltopiclandingpage_id integer NOT NULL,
    tag_id integer NOT NULL
);


--
-- Name: great_international_internationaltopiclandingpage_tags_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.great_international_internationaltopiclandingpage_tags_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: great_international_internationaltopiclandingpage_tags_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.great_international_internationaltopiclandingpage_tags_id_seq OWNED BY public.great_international_internationaltopiclandingpage_tags.id;


--
-- Name: health_check_db_testmodel; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.health_check_db_testmodel (
    id integer NOT NULL,
    title character varying(128) NOT NULL
);


--
-- Name: health_check_db_testmodel_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.health_check_db_testmodel_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: health_check_db_testmodel_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.health_check_db_testmodel_id_seq OWNED BY public.health_check_db_testmodel.id;


--
-- Name: invest_highpotentialopportunitydetailpage; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.invest_highpotentialopportunitydetailpage (
    page_ptr_id integer NOT NULL,
    service_name character varying(100),
    breadcrumbs_label character varying(50) NOT NULL,
    heading character varying(255) NOT NULL,
    contact_proposition text NOT NULL,
    contact_button character varying(500) NOT NULL,
    proposition_one text NOT NULL,
    opportunity_list_title character varying(300) NOT NULL,
    opportunity_list_item_one text NOT NULL,
    opportunity_list_item_two text NOT NULL,
    opportunity_list_item_three text NOT NULL,
    proposition_two text NOT NULL,
    proposition_two_list_item_one text NOT NULL,
    proposition_two_list_item_two text NOT NULL,
    proposition_two_list_item_three text NOT NULL,
    competitive_advantages_title character varying(300) NOT NULL,
    competitive_advantages_list_item_one text NOT NULL,
    competitive_advantages_list_item_two text NOT NULL,
    competitive_advantages_list_item_three text NOT NULL,
    testimonial text NOT NULL,
    companies_list_text text NOT NULL,
    case_study_list_title character varying(300) NOT NULL,
    case_study_one_text text NOT NULL,
    case_study_two_text text NOT NULL,
    case_study_three_text text NOT NULL,
    case_study_four_text text NOT NULL,
    case_study_four_image_id integer,
    case_study_one_image_id integer,
    case_study_three_image_id integer,
    case_study_two_image_id integer,
    companies_list_item_image_eight_id integer,
    companies_list_item_image_five_id integer,
    companies_list_item_image_four_id integer,
    companies_list_item_image_one_id integer,
    companies_list_item_image_seven_id integer,
    companies_list_item_image_six_id integer,
    companies_list_item_image_three_id integer,
    companies_list_item_image_two_id integer,
    hero_image_id integer,
    opportunity_list_image_id integer,
    proposition_one_image_id integer,
    proposition_one_video_id integer,
    proposition_two_image_id integer,
    proposition_two_video_id integer,
    competitive_advantages_list_item_one_icon_id integer,
    competitive_advantages_list_item_three_icon_id integer,
    competitive_advantages_list_item_two_icon_id integer,
    other_opportunities_title character varying(300) NOT NULL,
    summary_image_id integer,
    pdf_document_id integer,
    testimonial_background_id integer
);


--
-- Name: invest_highpotentialopportunityformpage; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.invest_highpotentialopportunityformpage (
    page_ptr_id integer NOT NULL,
    service_name character varying(100),
    comment_help_text character varying(200),
    comment_label character varying(200) NOT NULL,
    company_name_help_text character varying(200),
    company_name_label character varying(200) NOT NULL,
    company_size_help_text character varying(200),
    company_size_label character varying(200) NOT NULL,
    country_help_text character varying(200),
    country_label character varying(200) NOT NULL,
    email_address_help_text character varying(200),
    email_address_label character varying(200) NOT NULL,
    full_name_help_text character varying(200),
    full_name_label character varying(200) NOT NULL,
    opportunities_help_text character varying(200),
    opportunities_label character varying(200) NOT NULL,
    phone_number_help_text character varying(200),
    phone_number_label character varying(200) NOT NULL,
    role_in_company_help_text character varying(200),
    role_in_company_label character varying(200) NOT NULL,
    website_url_help_text character varying(200),
    website_url_label character varying(200) NOT NULL,
    heading character varying(255) NOT NULL,
    sub_heading character varying(255) NOT NULL,
    breadcrumbs_label character varying(50) NOT NULL
);


--
-- Name: invest_highpotentialopportunityformsuccesspage; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.invest_highpotentialopportunityformsuccesspage (
    page_ptr_id integer NOT NULL,
    service_name character varying(100),
    breadcrumbs_label character varying(50) NOT NULL,
    heading character varying(255) NOT NULL,
    sub_heading character varying(255) NOT NULL,
    next_steps_title character varying(255) NOT NULL,
    next_steps_body character varying(255) NOT NULL,
    documents_title character varying(255) NOT NULL,
    documents_body character varying(255) NOT NULL
);


--
-- Name: invest_infopage; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.invest_infopage (
    page_ptr_id integer NOT NULL,
    content text NOT NULL,
    content_en_gb text,
    content_de text,
    content_ja text,
    content_ru text,
    content_zh_hans text,
    content_fr text,
    content_es text,
    content_pt text,
    content_pt_br text,
    content_ar text,
    service_name character varying(100)
);


--
-- Name: invest_investapp; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.invest_investapp (
    page_ptr_id integer NOT NULL,
    service_name character varying(100)
);


--
-- Name: invest_investhomepage; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.invest_investhomepage (
    page_ptr_id integer NOT NULL,
    heading character varying(255) NOT NULL,
    heading_en_gb character varying(255),
    heading_de character varying(255),
    heading_ja character varying(255),
    heading_ru character varying(255),
    heading_zh_hans character varying(255),
    heading_fr character varying(255),
    heading_es character varying(255),
    heading_pt character varying(255),
    heading_pt_br character varying(255),
    heading_ar character varying(255),
    sub_heading character varying(255) NOT NULL,
    sub_heading_en_gb character varying(255),
    sub_heading_de character varying(255),
    sub_heading_ja character varying(255),
    sub_heading_ru character varying(255),
    sub_heading_zh_hans character varying(255),
    sub_heading_fr character varying(255),
    sub_heading_es character varying(255),
    sub_heading_pt character varying(255),
    sub_heading_pt_br character varying(255),
    sub_heading_ar character varying(255),
    sector_title text NOT NULL,
    sector_title_en_gb text,
    sector_title_de text,
    sector_title_ja text,
    sector_title_ru text,
    sector_title_zh_hans text,
    sector_title_fr text,
    sector_title_es text,
    sector_title_pt text,
    sector_title_pt_br text,
    sector_title_ar text,
    sector_button_text text NOT NULL,
    sector_button_text_en_gb text,
    sector_button_text_de text,
    sector_button_text_ja text,
    sector_button_text_ru text,
    sector_button_text_zh_hans text,
    sector_button_text_fr text,
    sector_button_text_es text,
    sector_button_text_pt text,
    sector_button_text_pt_br text,
    sector_button_text_ar text,
    setup_guide_title character varying(255) NOT NULL,
    setup_guide_title_en_gb character varying(255),
    setup_guide_title_de character varying(255),
    setup_guide_title_ja character varying(255),
    setup_guide_title_ru character varying(255),
    setup_guide_title_zh_hans character varying(255),
    setup_guide_title_fr character varying(255),
    setup_guide_title_es character varying(255),
    setup_guide_title_pt character varying(255),
    setup_guide_title_pt_br character varying(255),
    setup_guide_title_ar character varying(255),
    setup_guide_lead_in text,
    setup_guide_lead_in_en_gb text,
    setup_guide_lead_in_de text,
    setup_guide_lead_in_ja text,
    setup_guide_lead_in_ru text,
    setup_guide_lead_in_zh_hans text,
    setup_guide_lead_in_fr text,
    setup_guide_lead_in_es text,
    setup_guide_lead_in_pt text,
    setup_guide_lead_in_pt_br text,
    setup_guide_lead_in_ar text,
    how_we_help_title character varying(255) NOT NULL,
    how_we_help_title_en_gb character varying(255),
    how_we_help_title_de character varying(255),
    how_we_help_title_ja character varying(255),
    how_we_help_title_ru character varying(255),
    how_we_help_title_zh_hans character varying(255),
    how_we_help_title_fr character varying(255),
    how_we_help_title_es character varying(255),
    how_we_help_title_pt character varying(255),
    how_we_help_title_pt_br character varying(255),
    how_we_help_title_ar character varying(255),
    how_we_help_lead_in text,
    how_we_help_lead_in_en_gb text,
    how_we_help_lead_in_de text,
    how_we_help_lead_in_ja text,
    how_we_help_lead_in_ru text,
    how_we_help_lead_in_zh_hans text,
    how_we_help_lead_in_fr text,
    how_we_help_lead_in_es text,
    how_we_help_lead_in_pt text,
    how_we_help_lead_in_pt_br text,
    how_we_help_lead_in_ar text,
    hero_image_id integer,
    how_we_help_icon_five_id integer,
    how_we_help_icon_five_ar_id integer,
    how_we_help_icon_five_de_id integer,
    how_we_help_icon_five_en_gb_id integer,
    how_we_help_icon_five_es_id integer,
    how_we_help_icon_five_fr_id integer,
    how_we_help_icon_five_ja_id integer,
    how_we_help_icon_five_pt_id integer,
    how_we_help_icon_five_pt_br_id integer,
    how_we_help_icon_five_ru_id integer,
    how_we_help_icon_five_zh_hans_id integer,
    how_we_help_icon_four_id integer,
    how_we_help_icon_four_ar_id integer,
    how_we_help_icon_four_de_id integer,
    how_we_help_icon_four_en_gb_id integer,
    how_we_help_icon_four_es_id integer,
    how_we_help_icon_four_fr_id integer,
    how_we_help_icon_four_ja_id integer,
    how_we_help_icon_four_pt_id integer,
    how_we_help_icon_four_pt_br_id integer,
    how_we_help_icon_four_ru_id integer,
    how_we_help_icon_four_zh_hans_id integer,
    how_we_help_icon_one_id integer,
    how_we_help_icon_one_ar_id integer,
    how_we_help_icon_one_de_id integer,
    how_we_help_icon_one_en_gb_id integer,
    how_we_help_icon_one_es_id integer,
    how_we_help_icon_one_fr_id integer,
    how_we_help_icon_one_ja_id integer,
    how_we_help_icon_one_pt_id integer,
    how_we_help_icon_one_pt_br_id integer,
    how_we_help_icon_one_ru_id integer,
    how_we_help_icon_one_zh_hans_id integer,
    how_we_help_icon_three_id integer,
    how_we_help_icon_three_ar_id integer,
    how_we_help_icon_three_de_id integer,
    how_we_help_icon_three_en_gb_id integer,
    how_we_help_icon_three_es_id integer,
    how_we_help_icon_three_fr_id integer,
    how_we_help_icon_three_ja_id integer,
    how_we_help_icon_three_pt_id integer,
    how_we_help_icon_three_pt_br_id integer,
    how_we_help_icon_three_ru_id integer,
    how_we_help_icon_three_zh_hans_id integer,
    how_we_help_icon_two_id integer,
    how_we_help_icon_two_ar_id integer,
    how_we_help_icon_two_de_id integer,
    how_we_help_icon_two_en_gb_id integer,
    how_we_help_icon_two_es_id integer,
    how_we_help_icon_two_fr_id integer,
    how_we_help_icon_two_ja_id integer,
    how_we_help_icon_two_pt_id integer,
    how_we_help_icon_two_pt_br_id integer,
    how_we_help_icon_two_ru_id integer,
    how_we_help_icon_two_zh_hans_id integer,
    how_we_help_text_five character varying(255) NOT NULL,
    how_we_help_text_five_ar character varying(255),
    how_we_help_text_five_de character varying(255),
    how_we_help_text_five_en_gb character varying(255),
    how_we_help_text_five_es character varying(255),
    how_we_help_text_five_fr character varying(255),
    how_we_help_text_five_ja character varying(255),
    how_we_help_text_five_pt character varying(255),
    how_we_help_text_five_pt_br character varying(255),
    how_we_help_text_five_ru character varying(255),
    how_we_help_text_five_zh_hans character varying(255),
    how_we_help_text_four character varying(255) NOT NULL,
    how_we_help_text_four_ar character varying(255),
    how_we_help_text_four_de character varying(255),
    how_we_help_text_four_en_gb character varying(255),
    how_we_help_text_four_es character varying(255),
    how_we_help_text_four_fr character varying(255),
    how_we_help_text_four_ja character varying(255),
    how_we_help_text_four_pt character varying(255),
    how_we_help_text_four_pt_br character varying(255),
    how_we_help_text_four_ru character varying(255),
    how_we_help_text_four_zh_hans character varying(255),
    how_we_help_text_one character varying(255) NOT NULL,
    how_we_help_text_one_ar character varying(255),
    how_we_help_text_one_de character varying(255),
    how_we_help_text_one_en_gb character varying(255),
    how_we_help_text_one_es character varying(255),
    how_we_help_text_one_fr character varying(255),
    how_we_help_text_one_ja character varying(255),
    how_we_help_text_one_pt character varying(255),
    how_we_help_text_one_pt_br character varying(255),
    how_we_help_text_one_ru character varying(255),
    how_we_help_text_one_zh_hans character varying(255),
    how_we_help_text_six character varying(255) NOT NULL,
    how_we_help_text_six_ar character varying(255),
    how_we_help_text_six_de character varying(255),
    how_we_help_text_six_en_gb character varying(255),
    how_we_help_text_six_es character varying(255),
    how_we_help_text_six_fr character varying(255),
    how_we_help_text_six_ja character varying(255),
    how_we_help_text_six_pt character varying(255),
    how_we_help_text_six_pt_br character varying(255),
    how_we_help_text_six_ru character varying(255),
    how_we_help_text_six_zh_hans character varying(255),
    how_we_help_text_three character varying(255) NOT NULL,
    how_we_help_text_three_ar character varying(255),
    how_we_help_text_three_de character varying(255),
    how_we_help_text_three_en_gb character varying(255),
    how_we_help_text_three_es character varying(255),
    how_we_help_text_three_fr character varying(255),
    how_we_help_text_three_ja character varying(255),
    how_we_help_text_three_pt character varying(255),
    how_we_help_text_three_pt_br character varying(255),
    how_we_help_text_three_ru character varying(255),
    how_we_help_text_three_zh_hans character varying(255),
    how_we_help_text_two character varying(255) NOT NULL,
    how_we_help_text_two_ar character varying(255),
    how_we_help_text_two_de character varying(255),
    how_we_help_text_two_en_gb character varying(255),
    how_we_help_text_two_es character varying(255),
    how_we_help_text_two_fr character varying(255),
    how_we_help_text_two_ja character varying(255),
    how_we_help_text_two_pt character varying(255),
    how_we_help_text_two_pt_br character varying(255),
    how_we_help_text_two_ru character varying(255),
    how_we_help_text_two_zh_hans character varying(255),
    subsection_content_five text NOT NULL,
    subsection_content_five_ar text,
    subsection_content_five_de text,
    subsection_content_five_en_gb text,
    subsection_content_five_es text,
    subsection_content_five_fr text,
    subsection_content_five_ja text,
    subsection_content_five_pt text,
    subsection_content_five_pt_br text,
    subsection_content_five_ru text,
    subsection_content_five_zh_hans text,
    subsection_content_four text NOT NULL,
    subsection_content_four_ar text,
    subsection_content_four_de text,
    subsection_content_four_en_gb text,
    subsection_content_four_es text,
    subsection_content_four_fr text,
    subsection_content_four_ja text,
    subsection_content_four_pt text,
    subsection_content_four_pt_br text,
    subsection_content_four_ru text,
    subsection_content_four_zh_hans text,
    subsection_content_one text NOT NULL,
    subsection_content_one_ar text,
    subsection_content_one_de text,
    subsection_content_one_en_gb text,
    subsection_content_one_es text,
    subsection_content_one_fr text,
    subsection_content_one_ja text,
    subsection_content_one_pt text,
    subsection_content_one_pt_br text,
    subsection_content_one_ru text,
    subsection_content_one_zh_hans text,
    subsection_content_seven text NOT NULL,
    subsection_content_seven_ar text,
    subsection_content_seven_de text,
    subsection_content_seven_en_gb text,
    subsection_content_seven_es text,
    subsection_content_seven_fr text,
    subsection_content_seven_ja text,
    subsection_content_seven_pt text,
    subsection_content_seven_pt_br text,
    subsection_content_seven_ru text,
    subsection_content_seven_zh_hans text,
    subsection_content_six text NOT NULL,
    subsection_content_six_ar text,
    subsection_content_six_de text,
    subsection_content_six_en_gb text,
    subsection_content_six_es text,
    subsection_content_six_fr text,
    subsection_content_six_ja text,
    subsection_content_six_pt text,
    subsection_content_six_pt_br text,
    subsection_content_six_ru text,
    subsection_content_six_zh_hans text,
    subsection_content_three text NOT NULL,
    subsection_content_three_ar text,
    subsection_content_three_de text,
    subsection_content_three_en_gb text,
    subsection_content_three_es text,
    subsection_content_three_fr text,
    subsection_content_three_ja text,
    subsection_content_three_pt text,
    subsection_content_three_pt_br text,
    subsection_content_three_ru text,
    subsection_content_three_zh_hans text,
    subsection_content_two text NOT NULL,
    subsection_content_two_ar text,
    subsection_content_two_de text,
    subsection_content_two_en_gb text,
    subsection_content_two_es text,
    subsection_content_two_fr text,
    subsection_content_two_ja text,
    subsection_content_two_pt text,
    subsection_content_two_pt_br text,
    subsection_content_two_ru text,
    subsection_content_two_zh_hans text,
    subsection_title_five character varying(255) NOT NULL,
    subsection_title_five_ar character varying(255),
    subsection_title_five_de character varying(255),
    subsection_title_five_en_gb character varying(255),
    subsection_title_five_es character varying(255),
    subsection_title_five_fr character varying(255),
    subsection_title_five_ja character varying(255),
    subsection_title_five_pt character varying(255),
    subsection_title_five_pt_br character varying(255),
    subsection_title_five_ru character varying(255),
    subsection_title_five_zh_hans character varying(255),
    subsection_title_four character varying(255) NOT NULL,
    subsection_title_four_ar character varying(255),
    subsection_title_four_de character varying(255),
    subsection_title_four_en_gb character varying(255),
    subsection_title_four_es character varying(255),
    subsection_title_four_fr character varying(255),
    subsection_title_four_ja character varying(255),
    subsection_title_four_pt character varying(255),
    subsection_title_four_pt_br character varying(255),
    subsection_title_four_ru character varying(255),
    subsection_title_four_zh_hans character varying(255),
    subsection_title_one character varying(255) NOT NULL,
    subsection_title_one_ar character varying(255),
    subsection_title_one_de character varying(255),
    subsection_title_one_en_gb character varying(255),
    subsection_title_one_es character varying(255),
    subsection_title_one_fr character varying(255),
    subsection_title_one_ja character varying(255),
    subsection_title_one_pt character varying(255),
    subsection_title_one_pt_br character varying(255),
    subsection_title_one_ru character varying(255),
    subsection_title_one_zh_hans character varying(255),
    subsection_title_seven character varying(255) NOT NULL,
    subsection_title_seven_ar character varying(255),
    subsection_title_seven_de character varying(255),
    subsection_title_seven_en_gb character varying(255),
    subsection_title_seven_es character varying(255),
    subsection_title_seven_fr character varying(255),
    subsection_title_seven_ja character varying(255),
    subsection_title_seven_pt character varying(255),
    subsection_title_seven_pt_br character varying(255),
    subsection_title_seven_ru character varying(255),
    subsection_title_seven_zh_hans character varying(255),
    subsection_title_six character varying(255) NOT NULL,
    subsection_title_six_ar character varying(255),
    subsection_title_six_de character varying(255),
    subsection_title_six_en_gb character varying(255),
    subsection_title_six_es character varying(255),
    subsection_title_six_fr character varying(255),
    subsection_title_six_ja character varying(255),
    subsection_title_six_pt character varying(255),
    subsection_title_six_pt_br character varying(255),
    subsection_title_six_ru character varying(255),
    subsection_title_six_zh_hans character varying(255),
    subsection_title_three character varying(255) NOT NULL,
    subsection_title_three_ar character varying(255),
    subsection_title_three_de character varying(255),
    subsection_title_three_en_gb character varying(255),
    subsection_title_three_es character varying(255),
    subsection_title_three_fr character varying(255),
    subsection_title_three_ja character varying(255),
    subsection_title_three_pt character varying(255),
    subsection_title_three_pt_br character varying(255),
    subsection_title_three_ru character varying(255),
    subsection_title_three_zh_hans character varying(255),
    subsection_title_two character varying(255) NOT NULL,
    subsection_title_two_ar character varying(255),
    subsection_title_two_de character varying(255),
    subsection_title_two_en_gb character varying(255),
    subsection_title_two_es character varying(255),
    subsection_title_two_fr character varying(255),
    subsection_title_two_ja character varying(255),
    subsection_title_two_pt character varying(255),
    subsection_title_two_pt_br character varying(255),
    subsection_title_two_ru character varying(255),
    subsection_title_two_zh_hans character varying(255),
    service_name character varying(100)
);


--
-- Name: invest_regionlandingpage; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.invest_regionlandingpage (
    page_ptr_id integer NOT NULL,
    heading character varying(255) NOT NULL,
    heading_en_gb character varying(255),
    heading_de character varying(255),
    heading_ja character varying(255),
    heading_ru character varying(255),
    heading_zh_hans character varying(255),
    heading_fr character varying(255),
    heading_es character varying(255),
    heading_pt character varying(255),
    heading_pt_br character varying(255),
    heading_ar character varying(255),
    hero_image_id integer,
    service_name character varying(100)
);


--
-- Name: invest_sectorlandingpage; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.invest_sectorlandingpage (
    page_ptr_id integer NOT NULL,
    heading character varying(255) NOT NULL,
    heading_en_gb character varying(255),
    heading_de character varying(255),
    heading_ja character varying(255),
    heading_ru character varying(255),
    heading_zh_hans character varying(255),
    heading_fr character varying(255),
    heading_es character varying(255),
    heading_pt character varying(255),
    heading_pt_br character varying(255),
    heading_ar character varying(255),
    hero_image_id integer,
    service_name character varying(100)
);


--
-- Name: invest_sectorpage; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.invest_sectorpage (
    page_ptr_id integer NOT NULL,
    featured boolean NOT NULL,
    description text NOT NULL,
    description_en_gb text,
    description_de text,
    description_ja text,
    description_ru text,
    description_zh_hans text,
    description_fr text,
    description_es text,
    description_pt text,
    description_pt_br text,
    description_ar text,
    heading character varying(255) NOT NULL,
    heading_en_gb character varying(255),
    heading_de character varying(255),
    heading_ja character varying(255),
    heading_ru character varying(255),
    heading_zh_hans character varying(255),
    heading_fr character varying(255),
    heading_es character varying(255),
    heading_pt character varying(255),
    heading_pt_br character varying(255),
    heading_ar character varying(255),
    hero_image_id integer,
    pullout_stat character varying(255),
    pullout_stat_ar character varying(255),
    pullout_stat_de character varying(255),
    pullout_stat_en_gb character varying(255),
    pullout_stat_es character varying(255),
    pullout_stat_fr character varying(255),
    pullout_stat_ja character varying(255),
    pullout_stat_pt character varying(255),
    pullout_stat_pt_br character varying(255),
    pullout_stat_ru character varying(255),
    pullout_stat_text character varying(255),
    pullout_stat_text_ar character varying(255),
    pullout_stat_text_de character varying(255),
    pullout_stat_text_en_gb character varying(255),
    pullout_stat_text_es character varying(255),
    pullout_stat_text_fr character varying(255),
    pullout_stat_text_ja character varying(255),
    pullout_stat_text_pt character varying(255),
    pullout_stat_text_pt_br character varying(255),
    pullout_stat_text_ru character varying(255),
    pullout_stat_text_zh_hans character varying(255),
    pullout_stat_zh_hans character varying(255),
    pullout_text text,
    pullout_text_ar text,
    pullout_text_de text,
    pullout_text_en_gb text,
    pullout_text_es text,
    pullout_text_fr text,
    pullout_text_ja text,
    pullout_text_pt text,
    pullout_text_pt_br text,
    pullout_text_ru text,
    pullout_text_zh_hans text,
    subsection_content_five text NOT NULL,
    subsection_content_five_ar text,
    subsection_content_five_de text,
    subsection_content_five_en_gb text,
    subsection_content_five_es text,
    subsection_content_five_fr text,
    subsection_content_five_ja text,
    subsection_content_five_pt text,
    subsection_content_five_pt_br text,
    subsection_content_five_ru text,
    subsection_content_five_zh_hans text,
    subsection_content_four text NOT NULL,
    subsection_content_four_ar text,
    subsection_content_four_de text,
    subsection_content_four_en_gb text,
    subsection_content_four_es text,
    subsection_content_four_fr text,
    subsection_content_four_ja text,
    subsection_content_four_pt text,
    subsection_content_four_pt_br text,
    subsection_content_four_ru text,
    subsection_content_four_zh_hans text,
    subsection_content_one text NOT NULL,
    subsection_content_one_ar text,
    subsection_content_one_de text,
    subsection_content_one_en_gb text,
    subsection_content_one_es text,
    subsection_content_one_fr text,
    subsection_content_one_ja text,
    subsection_content_one_pt text,
    subsection_content_one_pt_br text,
    subsection_content_one_ru text,
    subsection_content_one_zh_hans text,
    subsection_content_seven text NOT NULL,
    subsection_content_seven_ar text,
    subsection_content_seven_de text,
    subsection_content_seven_en_gb text,
    subsection_content_seven_es text,
    subsection_content_seven_fr text,
    subsection_content_seven_ja text,
    subsection_content_seven_pt text,
    subsection_content_seven_pt_br text,
    subsection_content_seven_ru text,
    subsection_content_seven_zh_hans text,
    subsection_content_six text NOT NULL,
    subsection_content_six_ar text,
    subsection_content_six_de text,
    subsection_content_six_en_gb text,
    subsection_content_six_es text,
    subsection_content_six_fr text,
    subsection_content_six_ja text,
    subsection_content_six_pt text,
    subsection_content_six_pt_br text,
    subsection_content_six_ru text,
    subsection_content_six_zh_hans text,
    subsection_content_three text NOT NULL,
    subsection_content_three_ar text,
    subsection_content_three_de text,
    subsection_content_three_en_gb text,
    subsection_content_three_es text,
    subsection_content_three_fr text,
    subsection_content_three_ja text,
    subsection_content_three_pt text,
    subsection_content_three_pt_br text,
    subsection_content_three_ru text,
    subsection_content_three_zh_hans text,
    subsection_content_two text NOT NULL,
    subsection_content_two_ar text,
    subsection_content_two_de text,
    subsection_content_two_en_gb text,
    subsection_content_two_es text,
    subsection_content_two_fr text,
    subsection_content_two_ja text,
    subsection_content_two_pt text,
    subsection_content_two_pt_br text,
    subsection_content_two_ru text,
    subsection_content_two_zh_hans text,
    subsection_map_five_id integer,
    subsection_map_five_ar_id integer,
    subsection_map_five_de_id integer,
    subsection_map_five_en_gb_id integer,
    subsection_map_five_es_id integer,
    subsection_map_five_fr_id integer,
    subsection_map_five_ja_id integer,
    subsection_map_five_pt_id integer,
    subsection_map_five_pt_br_id integer,
    subsection_map_five_ru_id integer,
    subsection_map_five_zh_hans_id integer,
    subsection_map_four_id integer,
    subsection_map_four_ar_id integer,
    subsection_map_four_de_id integer,
    subsection_map_four_en_gb_id integer,
    subsection_map_four_es_id integer,
    subsection_map_four_fr_id integer,
    subsection_map_four_ja_id integer,
    subsection_map_four_pt_id integer,
    subsection_map_four_pt_br_id integer,
    subsection_map_four_ru_id integer,
    subsection_map_four_zh_hans_id integer,
    subsection_map_one_id integer,
    subsection_map_one_ar_id integer,
    subsection_map_one_de_id integer,
    subsection_map_one_en_gb_id integer,
    subsection_map_one_es_id integer,
    subsection_map_one_fr_id integer,
    subsection_map_one_ja_id integer,
    subsection_map_one_pt_id integer,
    subsection_map_one_pt_br_id integer,
    subsection_map_one_ru_id integer,
    subsection_map_one_zh_hans_id integer,
    subsection_map_seven_id integer,
    subsection_map_seven_ar_id integer,
    subsection_map_seven_de_id integer,
    subsection_map_seven_en_gb_id integer,
    subsection_map_seven_es_id integer,
    subsection_map_seven_fr_id integer,
    subsection_map_seven_ja_id integer,
    subsection_map_seven_pt_id integer,
    subsection_map_seven_pt_br_id integer,
    subsection_map_seven_ru_id integer,
    subsection_map_seven_zh_hans_id integer,
    subsection_map_six_id integer,
    subsection_map_six_ar_id integer,
    subsection_map_six_de_id integer,
    subsection_map_six_en_gb_id integer,
    subsection_map_six_es_id integer,
    subsection_map_six_fr_id integer,
    subsection_map_six_ja_id integer,
    subsection_map_six_pt_id integer,
    subsection_map_six_pt_br_id integer,
    subsection_map_six_ru_id integer,
    subsection_map_six_zh_hans_id integer,
    subsection_map_three_id integer,
    subsection_map_three_ar_id integer,
    subsection_map_three_de_id integer,
    subsection_map_three_en_gb_id integer,
    subsection_map_three_es_id integer,
    subsection_map_three_fr_id integer,
    subsection_map_three_ja_id integer,
    subsection_map_three_pt_id integer,
    subsection_map_three_pt_br_id integer,
    subsection_map_three_ru_id integer,
    subsection_map_three_zh_hans_id integer,
    subsection_map_two_id integer,
    subsection_map_two_ar_id integer,
    subsection_map_two_de_id integer,
    subsection_map_two_en_gb_id integer,
    subsection_map_two_es_id integer,
    subsection_map_two_fr_id integer,
    subsection_map_two_ja_id integer,
    subsection_map_two_pt_id integer,
    subsection_map_two_pt_br_id integer,
    subsection_map_two_ru_id integer,
    subsection_map_two_zh_hans_id integer,
    subsection_title_five character varying(200) NOT NULL,
    subsection_title_five_ar character varying(200),
    subsection_title_five_de character varying(200),
    subsection_title_five_en_gb character varying(200),
    subsection_title_five_es character varying(200),
    subsection_title_five_fr character varying(200),
    subsection_title_five_ja character varying(200),
    subsection_title_five_pt character varying(200),
    subsection_title_five_pt_br character varying(200),
    subsection_title_five_ru character varying(200),
    subsection_title_five_zh_hans character varying(200),
    subsection_title_four character varying(200) NOT NULL,
    subsection_title_four_ar character varying(200),
    subsection_title_four_de character varying(200),
    subsection_title_four_en_gb character varying(200),
    subsection_title_four_es character varying(200),
    subsection_title_four_fr character varying(200),
    subsection_title_four_ja character varying(200),
    subsection_title_four_pt character varying(200),
    subsection_title_four_pt_br character varying(200),
    subsection_title_four_ru character varying(200),
    subsection_title_four_zh_hans character varying(200),
    subsection_title_one character varying(200) NOT NULL,
    subsection_title_one_ar character varying(200),
    subsection_title_one_de character varying(200),
    subsection_title_one_en_gb character varying(200),
    subsection_title_one_es character varying(200),
    subsection_title_one_fr character varying(200),
    subsection_title_one_ja character varying(200),
    subsection_title_one_pt character varying(200),
    subsection_title_one_pt_br character varying(200),
    subsection_title_one_ru character varying(200),
    subsection_title_one_zh_hans character varying(200),
    subsection_title_seven character varying(200) NOT NULL,
    subsection_title_seven_ar character varying(200),
    subsection_title_seven_de character varying(200),
    subsection_title_seven_en_gb character varying(200),
    subsection_title_seven_es character varying(200),
    subsection_title_seven_fr character varying(200),
    subsection_title_seven_ja character varying(200),
    subsection_title_seven_pt character varying(200),
    subsection_title_seven_pt_br character varying(200),
    subsection_title_seven_ru character varying(200),
    subsection_title_seven_zh_hans character varying(200),
    subsection_title_six character varying(200) NOT NULL,
    subsection_title_six_ar character varying(200),
    subsection_title_six_de character varying(200),
    subsection_title_six_en_gb character varying(200),
    subsection_title_six_es character varying(200),
    subsection_title_six_fr character varying(200),
    subsection_title_six_ja character varying(200),
    subsection_title_six_pt character varying(200),
    subsection_title_six_pt_br character varying(200),
    subsection_title_six_ru character varying(200),
    subsection_title_six_zh_hans character varying(200),
    subsection_title_three character varying(200) NOT NULL,
    subsection_title_three_ar character varying(200),
    subsection_title_three_de character varying(200),
    subsection_title_three_en_gb character varying(200),
    subsection_title_three_es character varying(200),
    subsection_title_three_fr character varying(200),
    subsection_title_three_ja character varying(200),
    subsection_title_three_pt character varying(200),
    subsection_title_three_pt_br character varying(200),
    subsection_title_three_ru character varying(200),
    subsection_title_three_zh_hans character varying(200),
    subsection_title_two character varying(200) NOT NULL,
    subsection_title_two_ar character varying(200),
    subsection_title_two_de character varying(200),
    subsection_title_two_en_gb character varying(200),
    subsection_title_two_es character varying(200),
    subsection_title_two_fr character varying(200),
    subsection_title_two_ja character varying(200),
    subsection_title_two_pt character varying(200),
    subsection_title_two_pt_br character varying(200),
    subsection_title_two_ru character varying(200),
    subsection_title_two_zh_hans character varying(200),
    service_name character varying(100)
);


--
-- Name: invest_setupguidelandingpage; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.invest_setupguidelandingpage (
    page_ptr_id integer NOT NULL,
    heading character varying(255) NOT NULL,
    heading_en_gb character varying(255),
    heading_de character varying(255),
    heading_ja character varying(255),
    heading_ru character varying(255),
    heading_zh_hans character varying(255),
    heading_fr character varying(255),
    heading_es character varying(255),
    heading_pt character varying(255),
    heading_pt_br character varying(255),
    heading_ar character varying(255),
    sub_heading character varying(255) NOT NULL,
    sub_heading_en_gb character varying(255),
    sub_heading_de character varying(255),
    sub_heading_ja character varying(255),
    sub_heading_ru character varying(255),
    sub_heading_zh_hans character varying(255),
    sub_heading_fr character varying(255),
    sub_heading_es character varying(255),
    sub_heading_pt character varying(255),
    sub_heading_pt_br character varying(255),
    sub_heading_ar character varying(255),
    lead_in text NOT NULL,
    lead_in_en_gb text,
    lead_in_de text,
    lead_in_ja text,
    lead_in_ru text,
    lead_in_zh_hans text,
    lead_in_fr text,
    lead_in_es text,
    lead_in_pt text,
    lead_in_pt_br text,
    lead_in_ar text,
    service_name character varying(100)
);


--
-- Name: invest_setupguidepage; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.invest_setupguidepage (
    page_ptr_id integer NOT NULL,
    description text NOT NULL,
    description_en_gb text,
    description_de text,
    description_ja text,
    description_ru text,
    description_zh_hans text,
    description_fr text,
    description_es text,
    description_pt text,
    description_pt_br text,
    description_ar text,
    heading character varying(255) NOT NULL,
    heading_en_gb character varying(255),
    heading_de character varying(255),
    heading_ja character varying(255),
    heading_ru character varying(255),
    heading_zh_hans character varying(255),
    heading_fr character varying(255),
    heading_es character varying(255),
    heading_pt character varying(255),
    heading_pt_br character varying(255),
    heading_ar character varying(255),
    sub_heading character varying(255) NOT NULL,
    sub_heading_en_gb character varying(255),
    sub_heading_de character varying(255),
    sub_heading_ja character varying(255),
    sub_heading_ru character varying(255),
    sub_heading_zh_hans character varying(255),
    sub_heading_fr character varying(255),
    sub_heading_es character varying(255),
    sub_heading_pt character varying(255),
    sub_heading_pt_br character varying(255),
    sub_heading_ar character varying(255),
    subsection_content_five text NOT NULL,
    subsection_content_five_ar text,
    subsection_content_five_de text,
    subsection_content_five_en_gb text,
    subsection_content_five_es text,
    subsection_content_five_fr text,
    subsection_content_five_ja text,
    subsection_content_five_pt text,
    subsection_content_five_pt_br text,
    subsection_content_five_ru text,
    subsection_content_five_zh_hans text,
    subsection_content_four text NOT NULL,
    subsection_content_four_ar text,
    subsection_content_four_de text,
    subsection_content_four_en_gb text,
    subsection_content_four_es text,
    subsection_content_four_fr text,
    subsection_content_four_ja text,
    subsection_content_four_pt text,
    subsection_content_four_pt_br text,
    subsection_content_four_ru text,
    subsection_content_four_zh_hans text,
    subsection_content_one text NOT NULL,
    subsection_content_one_ar text,
    subsection_content_one_de text,
    subsection_content_one_en_gb text,
    subsection_content_one_es text,
    subsection_content_one_fr text,
    subsection_content_one_ja text,
    subsection_content_one_pt text,
    subsection_content_one_pt_br text,
    subsection_content_one_ru text,
    subsection_content_one_zh_hans text,
    subsection_content_seven text NOT NULL,
    subsection_content_seven_ar text,
    subsection_content_seven_de text,
    subsection_content_seven_en_gb text,
    subsection_content_seven_es text,
    subsection_content_seven_fr text,
    subsection_content_seven_ja text,
    subsection_content_seven_pt text,
    subsection_content_seven_pt_br text,
    subsection_content_seven_ru text,
    subsection_content_seven_zh_hans text,
    subsection_content_six text NOT NULL,
    subsection_content_six_ar text,
    subsection_content_six_de text,
    subsection_content_six_en_gb text,
    subsection_content_six_es text,
    subsection_content_six_fr text,
    subsection_content_six_ja text,
    subsection_content_six_pt text,
    subsection_content_six_pt_br text,
    subsection_content_six_ru text,
    subsection_content_six_zh_hans text,
    subsection_content_three text NOT NULL,
    subsection_content_three_ar text,
    subsection_content_three_de text,
    subsection_content_three_en_gb text,
    subsection_content_three_es text,
    subsection_content_three_fr text,
    subsection_content_three_ja text,
    subsection_content_three_pt text,
    subsection_content_three_pt_br text,
    subsection_content_three_ru text,
    subsection_content_three_zh_hans text,
    subsection_content_two text NOT NULL,
    subsection_content_two_ar text,
    subsection_content_two_de text,
    subsection_content_two_en_gb text,
    subsection_content_two_es text,
    subsection_content_two_fr text,
    subsection_content_two_ja text,
    subsection_content_two_pt text,
    subsection_content_two_pt_br text,
    subsection_content_two_ru text,
    subsection_content_two_zh_hans text,
    subsection_title_five character varying(255) NOT NULL,
    subsection_title_five_ar character varying(255),
    subsection_title_five_de character varying(255),
    subsection_title_five_en_gb character varying(255),
    subsection_title_five_es character varying(255),
    subsection_title_five_fr character varying(255),
    subsection_title_five_ja character varying(255),
    subsection_title_five_pt character varying(255),
    subsection_title_five_pt_br character varying(255),
    subsection_title_five_ru character varying(255),
    subsection_title_five_zh_hans character varying(255),
    subsection_title_four character varying(255) NOT NULL,
    subsection_title_four_ar character varying(255),
    subsection_title_four_de character varying(255),
    subsection_title_four_en_gb character varying(255),
    subsection_title_four_es character varying(255),
    subsection_title_four_fr character varying(255),
    subsection_title_four_ja character varying(255),
    subsection_title_four_pt character varying(255),
    subsection_title_four_pt_br character varying(255),
    subsection_title_four_ru character varying(255),
    subsection_title_four_zh_hans character varying(255),
    subsection_title_one character varying(255) NOT NULL,
    subsection_title_one_ar character varying(255),
    subsection_title_one_de character varying(255),
    subsection_title_one_en_gb character varying(255),
    subsection_title_one_es character varying(255),
    subsection_title_one_fr character varying(255),
    subsection_title_one_ja character varying(255),
    subsection_title_one_pt character varying(255),
    subsection_title_one_pt_br character varying(255),
    subsection_title_one_ru character varying(255),
    subsection_title_one_zh_hans character varying(255),
    subsection_title_seven character varying(255) NOT NULL,
    subsection_title_seven_ar character varying(255),
    subsection_title_seven_de character varying(255),
    subsection_title_seven_en_gb character varying(255),
    subsection_title_seven_es character varying(255),
    subsection_title_seven_fr character varying(255),
    subsection_title_seven_ja character varying(255),
    subsection_title_seven_pt character varying(255),
    subsection_title_seven_pt_br character varying(255),
    subsection_title_seven_ru character varying(255),
    subsection_title_seven_zh_hans character varying(255),
    subsection_title_six character varying(255) NOT NULL,
    subsection_title_six_ar character varying(255),
    subsection_title_six_de character varying(255),
    subsection_title_six_en_gb character varying(255),
    subsection_title_six_es character varying(255),
    subsection_title_six_fr character varying(255),
    subsection_title_six_ja character varying(255),
    subsection_title_six_pt character varying(255),
    subsection_title_six_pt_br character varying(255),
    subsection_title_six_ru character varying(255),
    subsection_title_six_zh_hans character varying(255),
    subsection_title_three character varying(255) NOT NULL,
    subsection_title_three_ar character varying(255),
    subsection_title_three_de character varying(255),
    subsection_title_three_en_gb character varying(255),
    subsection_title_three_es character varying(255),
    subsection_title_three_fr character varying(255),
    subsection_title_three_ja character varying(255),
    subsection_title_three_pt character varying(255),
    subsection_title_three_pt_br character varying(255),
    subsection_title_three_ru character varying(255),
    subsection_title_three_zh_hans character varying(255),
    subsection_title_two character varying(255) NOT NULL,
    subsection_title_two_ar character varying(255),
    subsection_title_two_de character varying(255),
    subsection_title_two_en_gb character varying(255),
    subsection_title_two_es character varying(255),
    subsection_title_two_fr character varying(255),
    subsection_title_two_ja character varying(255),
    subsection_title_two_pt character varying(255),
    subsection_title_two_pt_br character varying(255),
    subsection_title_two_ru character varying(255),
    subsection_title_two_zh_hans character varying(255),
    service_name character varying(100)
);


--
-- Name: taggit_tag; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.taggit_tag (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    slug character varying(100) NOT NULL
);


--
-- Name: taggit_tag_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.taggit_tag_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: taggit_tag_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.taggit_tag_id_seq OWNED BY public.taggit_tag.id;


--
-- Name: taggit_taggeditem; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.taggit_taggeditem (
    id integer NOT NULL,
    object_id integer NOT NULL,
    content_type_id integer NOT NULL,
    tag_id integer NOT NULL
);


--
-- Name: taggit_taggeditem_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.taggit_taggeditem_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: taggit_taggeditem_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.taggit_taggeditem_id_seq OWNED BY public.taggit_taggeditem.id;


--
-- Name: wagtailcore_collection; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailcore_collection (
    id integer NOT NULL,
    path character varying(255) COLLATE pg_catalog."C" NOT NULL,
    depth integer NOT NULL,
    numchild integer NOT NULL,
    name character varying(255) NOT NULL,
    CONSTRAINT wagtailcore_collection_depth_check CHECK ((depth >= 0)),
    CONSTRAINT wagtailcore_collection_numchild_check CHECK ((numchild >= 0))
);


--
-- Name: wagtailcore_collection_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.wagtailcore_collection_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: wagtailcore_collection_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.wagtailcore_collection_id_seq OWNED BY public.wagtailcore_collection.id;


--
-- Name: wagtailcore_collectionviewrestriction; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailcore_collectionviewrestriction (
    id integer NOT NULL,
    restriction_type character varying(20) NOT NULL,
    password character varying(255) NOT NULL,
    collection_id integer NOT NULL
);


--
-- Name: wagtailcore_collectionviewrestriction_groups; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailcore_collectionviewrestriction_groups (
    id integer NOT NULL,
    collectionviewrestriction_id integer NOT NULL,
    group_id integer NOT NULL
);


--
-- Name: wagtailcore_collectionviewrestriction_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.wagtailcore_collectionviewrestriction_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: wagtailcore_collectionviewrestriction_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.wagtailcore_collectionviewrestriction_groups_id_seq OWNED BY public.wagtailcore_collectionviewrestriction_groups.id;


--
-- Name: wagtailcore_collectionviewrestriction_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.wagtailcore_collectionviewrestriction_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: wagtailcore_collectionviewrestriction_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.wagtailcore_collectionviewrestriction_id_seq OWNED BY public.wagtailcore_collectionviewrestriction.id;


--
-- Name: wagtailcore_groupcollectionpermission; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailcore_groupcollectionpermission (
    id integer NOT NULL,
    collection_id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


--
-- Name: wagtailcore_groupcollectionpermission_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.wagtailcore_groupcollectionpermission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: wagtailcore_groupcollectionpermission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.wagtailcore_groupcollectionpermission_id_seq OWNED BY public.wagtailcore_groupcollectionpermission.id;


--
-- Name: wagtailcore_grouppagepermission; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailcore_grouppagepermission (
    id integer NOT NULL,
    permission_type character varying(20) NOT NULL,
    group_id integer NOT NULL,
    page_id integer NOT NULL
);


--
-- Name: wagtailcore_grouppagepermission_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.wagtailcore_grouppagepermission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: wagtailcore_grouppagepermission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.wagtailcore_grouppagepermission_id_seq OWNED BY public.wagtailcore_grouppagepermission.id;


--
-- Name: wagtailcore_page; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailcore_page (
    id integer NOT NULL,
    path character varying(255) COLLATE pg_catalog."C" NOT NULL,
    depth integer NOT NULL,
    numchild integer NOT NULL,
    title character varying(255) NOT NULL,
    slug character varying(255) NOT NULL,
    live boolean NOT NULL,
    has_unpublished_changes boolean NOT NULL,
    url_path text NOT NULL,
    seo_title character varying(255) NOT NULL,
    show_in_menus boolean NOT NULL,
    search_description text NOT NULL,
    go_live_at timestamp with time zone,
    expire_at timestamp with time zone,
    expired boolean NOT NULL,
    content_type_id integer NOT NULL,
    owner_id integer,
    locked boolean NOT NULL,
    latest_revision_created_at timestamp with time zone,
    first_published_at timestamp with time zone,
    live_revision_id integer,
    last_published_at timestamp with time zone,
    draft_title character varying(255) NOT NULL,
    seo_title_en_gb character varying(255),
    seo_title_de character varying(255),
    seo_title_ja character varying(255),
    seo_title_ru character varying(255),
    seo_title_zh_hans character varying(255),
    seo_title_fr character varying(255),
    seo_title_es character varying(255),
    seo_title_pt character varying(255),
    seo_title_pt_br character varying(255),
    seo_title_ar character varying(255),
    title_en_gb character varying(255),
    title_de character varying(255),
    title_ja character varying(255),
    title_ru character varying(255),
    title_zh_hans character varying(255),
    title_fr character varying(255),
    title_es character varying(255),
    title_pt character varying(255),
    title_pt_br character varying(255),
    title_ar character varying(255),
    search_description_en_gb text,
    search_description_de text,
    search_description_ja text,
    search_description_ru text,
    search_description_zh_hans text,
    search_description_fr text,
    search_description_es text,
    search_description_pt text,
    search_description_pt_br text,
    search_description_ar text,
    CONSTRAINT wagtailcore_page_depth_check CHECK ((depth >= 0)),
    CONSTRAINT wagtailcore_page_numchild_check CHECK ((numchild >= 0))
);


--
-- Name: wagtailcore_page_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.wagtailcore_page_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: wagtailcore_page_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.wagtailcore_page_id_seq OWNED BY public.wagtailcore_page.id;


--
-- Name: wagtailcore_pagerevision; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailcore_pagerevision (
    id integer NOT NULL,
    submitted_for_moderation boolean NOT NULL,
    created_at timestamp with time zone NOT NULL,
    content_json text NOT NULL,
    approved_go_live_at timestamp with time zone,
    page_id integer NOT NULL,
    user_id integer
);


--
-- Name: wagtailcore_pagerevision_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.wagtailcore_pagerevision_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: wagtailcore_pagerevision_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.wagtailcore_pagerevision_id_seq OWNED BY public.wagtailcore_pagerevision.id;


--
-- Name: wagtailcore_pageviewrestriction; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailcore_pageviewrestriction (
    id integer NOT NULL,
    password character varying(255) NOT NULL,
    page_id integer NOT NULL,
    restriction_type character varying(20) NOT NULL
);


--
-- Name: wagtailcore_pageviewrestriction_groups; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailcore_pageviewrestriction_groups (
    id integer NOT NULL,
    pageviewrestriction_id integer NOT NULL,
    group_id integer NOT NULL
);


--
-- Name: wagtailcore_pageviewrestriction_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.wagtailcore_pageviewrestriction_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: wagtailcore_pageviewrestriction_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.wagtailcore_pageviewrestriction_groups_id_seq OWNED BY public.wagtailcore_pageviewrestriction_groups.id;


--
-- Name: wagtailcore_pageviewrestriction_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.wagtailcore_pageviewrestriction_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: wagtailcore_pageviewrestriction_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.wagtailcore_pageviewrestriction_id_seq OWNED BY public.wagtailcore_pageviewrestriction.id;


--
-- Name: wagtailcore_site; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailcore_site (
    id integer NOT NULL,
    hostname character varying(255) NOT NULL,
    port integer NOT NULL,
    is_default_site boolean NOT NULL,
    root_page_id integer NOT NULL,
    site_name character varying(255)
);


--
-- Name: wagtailcore_site_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.wagtailcore_site_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: wagtailcore_site_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.wagtailcore_site_id_seq OWNED BY public.wagtailcore_site.id;


--
-- Name: wagtaildocs_document; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtaildocs_document (
    id integer NOT NULL,
    title character varying(255) NOT NULL,
    file character varying(100) NOT NULL,
    created_at timestamp with time zone NOT NULL,
    uploaded_by_user_id integer,
    collection_id integer NOT NULL,
    file_size integer,
    CONSTRAINT wagtaildocs_document_file_size_check CHECK ((file_size >= 0))
);


--
-- Name: wagtaildocs_document_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.wagtaildocs_document_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: wagtaildocs_document_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.wagtaildocs_document_id_seq OWNED BY public.wagtaildocs_document.id;


--
-- Name: wagtailembeds_embed; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailembeds_embed (
    id integer NOT NULL,
    url character varying(200) NOT NULL,
    max_width smallint,
    type character varying(10) NOT NULL,
    html text NOT NULL,
    title text NOT NULL,
    author_name text NOT NULL,
    provider_name text NOT NULL,
    thumbnail_url character varying(200),
    width integer,
    height integer,
    last_updated timestamp with time zone NOT NULL
);


--
-- Name: wagtailembeds_embed_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.wagtailembeds_embed_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: wagtailembeds_embed_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.wagtailembeds_embed_id_seq OWNED BY public.wagtailembeds_embed.id;


--
-- Name: wagtailforms_formsubmission; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailforms_formsubmission (
    id integer NOT NULL,
    form_data text NOT NULL,
    submit_time timestamp with time zone NOT NULL,
    page_id integer NOT NULL
);


--
-- Name: wagtailforms_formsubmission_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.wagtailforms_formsubmission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: wagtailforms_formsubmission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.wagtailforms_formsubmission_id_seq OWNED BY public.wagtailforms_formsubmission.id;


--
-- Name: wagtailimages_image; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailimages_image (
    id integer NOT NULL,
    title character varying(255) NOT NULL,
    file character varying(100) NOT NULL,
    width integer NOT NULL,
    height integer NOT NULL,
    created_at timestamp with time zone NOT NULL,
    focal_point_x integer,
    focal_point_y integer,
    focal_point_width integer,
    focal_point_height integer,
    uploaded_by_user_id integer,
    file_size integer,
    collection_id integer NOT NULL,
    file_hash character varying(40) NOT NULL,
    CONSTRAINT wagtailimages_image_file_size_check CHECK ((file_size >= 0)),
    CONSTRAINT wagtailimages_image_focal_point_height_check CHECK ((focal_point_height >= 0)),
    CONSTRAINT wagtailimages_image_focal_point_width_check CHECK ((focal_point_width >= 0)),
    CONSTRAINT wagtailimages_image_focal_point_x_check CHECK ((focal_point_x >= 0)),
    CONSTRAINT wagtailimages_image_focal_point_y_check CHECK ((focal_point_y >= 0))
);


--
-- Name: wagtailimages_image_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.wagtailimages_image_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: wagtailimages_image_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.wagtailimages_image_id_seq OWNED BY public.wagtailimages_image.id;


--
-- Name: wagtailimages_rendition; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailimages_rendition (
    id integer NOT NULL,
    file character varying(100) NOT NULL,
    width integer NOT NULL,
    height integer NOT NULL,
    focal_point_key character varying(16) NOT NULL,
    image_id integer NOT NULL,
    filter_spec character varying(255) NOT NULL
);


--
-- Name: wagtailimages_rendition_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.wagtailimages_rendition_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: wagtailimages_rendition_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.wagtailimages_rendition_id_seq OWNED BY public.wagtailimages_rendition.id;


--
-- Name: wagtailmedia_media; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailmedia_media (
    id integer NOT NULL,
    title character varying(255) NOT NULL,
    file character varying(100) NOT NULL,
    type character varying(255) NOT NULL,
    duration integer NOT NULL,
    width integer,
    height integer,
    thumbnail character varying(100) NOT NULL,
    created_at timestamp with time zone NOT NULL,
    collection_id integer NOT NULL,
    uploaded_by_user_id integer,
    CONSTRAINT wagtailmedia_media_duration_check CHECK ((duration >= 0)),
    CONSTRAINT wagtailmedia_media_height_check CHECK ((height >= 0)),
    CONSTRAINT wagtailmedia_media_width_check CHECK ((width >= 0))
);


--
-- Name: wagtailmedia_media_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.wagtailmedia_media_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: wagtailmedia_media_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.wagtailmedia_media_id_seq OWNED BY public.wagtailmedia_media.id;


--
-- Name: wagtailsearch_editorspick; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailsearch_editorspick (
    id integer NOT NULL,
    sort_order integer,
    description text NOT NULL,
    page_id integer NOT NULL,
    query_id integer NOT NULL
);


--
-- Name: wagtailsearch_editorspick_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.wagtailsearch_editorspick_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: wagtailsearch_editorspick_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.wagtailsearch_editorspick_id_seq OWNED BY public.wagtailsearch_editorspick.id;


--
-- Name: wagtailsearch_query; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailsearch_query (
    id integer NOT NULL,
    query_string character varying(255) NOT NULL
);


--
-- Name: wagtailsearch_query_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.wagtailsearch_query_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: wagtailsearch_query_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.wagtailsearch_query_id_seq OWNED BY public.wagtailsearch_query.id;


--
-- Name: wagtailsearch_querydailyhits; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailsearch_querydailyhits (
    id integer NOT NULL,
    date date NOT NULL,
    hits integer NOT NULL,
    query_id integer NOT NULL
);


--
-- Name: wagtailsearch_querydailyhits_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.wagtailsearch_querydailyhits_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: wagtailsearch_querydailyhits_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.wagtailsearch_querydailyhits_id_seq OWNED BY public.wagtailsearch_querydailyhits.id;


--
-- Name: wagtailusers_userprofile; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.wagtailusers_userprofile (
    id integer NOT NULL,
    submitted_notifications boolean NOT NULL,
    approved_notifications boolean NOT NULL,
    rejected_notifications boolean NOT NULL,
    user_id integer NOT NULL,
    preferred_language character varying(10) NOT NULL,
    current_time_zone character varying(40) NOT NULL,
    avatar character varying(100) NOT NULL
);


--
-- Name: wagtailusers_userprofile_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.wagtailusers_userprofile_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: wagtailusers_userprofile_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.wagtailusers_userprofile_id_seq OWNED BY public.wagtailusers_userprofile.id;


--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: auth_user id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);


--
-- Name: auth_user_groups id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('public.auth_user_groups_id_seq'::regclass);


--
-- Name: auth_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_user_user_permissions_id_seq'::regclass);


--
-- Name: core_breadcrumb id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.core_breadcrumb ALTER COLUMN id SET DEFAULT nextval('public.core_breadcrumb_id_seq'::regclass);


--
-- Name: core_documenthash id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.core_documenthash ALTER COLUMN id SET DEFAULT nextval('public.core_documenthash_id_seq'::regclass);


--
-- Name: core_imagehash id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.core_imagehash ALTER COLUMN id SET DEFAULT nextval('public.core_imagehash_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Name: export_readiness_articlepage_tags id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_articlepage_tags ALTER COLUMN id SET DEFAULT nextval('public.export_readiness_articlepage_tags_id_seq'::regclass);


--
-- Name: export_readiness_tag id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_tag ALTER COLUMN id SET DEFAULT nextval('public.export_readiness_tag_id_seq'::regclass);


--
-- Name: find_a_supplier_industrypagearticlesummary id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_industrypagearticlesummary ALTER COLUMN id SET DEFAULT nextval('public.find_a_supplier_industrypagearticlesummary_id_seq'::regclass);


--
-- Name: find_a_supplier_landingpagearticlesummary id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_landingpagearticlesummary ALTER COLUMN id SET DEFAULT nextval('public.find_a_supplier_landingpagearticlesummary_id_seq'::regclass);


--
-- Name: great_international_internationalarticlelistingpage_tags id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.great_international_internationalarticlelistingpage_tags ALTER COLUMN id SET DEFAULT nextval('public.great_international_internationalarticlelistingpage_tags_id_seq'::regclass);


--
-- Name: great_international_internationalarticlepage_tags id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.great_international_internationalarticlepage_tags ALTER COLUMN id SET DEFAULT nextval('public.great_international_internationalarticlepage_tags_id_seq'::regclass);


--
-- Name: great_international_internationalcampaignpage_tags id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.great_international_internationalcampaignpage_tags ALTER COLUMN id SET DEFAULT nextval('public.great_international_internationalcampaignpage_tags_id_seq'::regclass);


--
-- Name: great_international_internationalregionpage_tags id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.great_international_internationalregionpage_tags ALTER COLUMN id SET DEFAULT nextval('public.great_international_internationalregionpages_tags_id_seq'::regclass);


--
-- Name: great_international_internationaltopiclandingpage_tags id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.great_international_internationaltopiclandingpage_tags ALTER COLUMN id SET DEFAULT nextval('public.great_international_internationaltopiclandingpage_tags_id_seq'::regclass);


--
-- Name: health_check_db_testmodel id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.health_check_db_testmodel ALTER COLUMN id SET DEFAULT nextval('public.health_check_db_testmodel_id_seq'::regclass);


--
-- Name: taggit_tag id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.taggit_tag ALTER COLUMN id SET DEFAULT nextval('public.taggit_tag_id_seq'::regclass);


--
-- Name: taggit_taggeditem id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.taggit_taggeditem ALTER COLUMN id SET DEFAULT nextval('public.taggit_taggeditem_id_seq'::regclass);


--
-- Name: wagtailcore_collection id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_collection ALTER COLUMN id SET DEFAULT nextval('public.wagtailcore_collection_id_seq'::regclass);


--
-- Name: wagtailcore_collectionviewrestriction id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_collectionviewrestriction ALTER COLUMN id SET DEFAULT nextval('public.wagtailcore_collectionviewrestriction_id_seq'::regclass);


--
-- Name: wagtailcore_collectionviewrestriction_groups id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_collectionviewrestriction_groups ALTER COLUMN id SET DEFAULT nextval('public.wagtailcore_collectionviewrestriction_groups_id_seq'::regclass);


--
-- Name: wagtailcore_groupcollectionpermission id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_groupcollectionpermission ALTER COLUMN id SET DEFAULT nextval('public.wagtailcore_groupcollectionpermission_id_seq'::regclass);


--
-- Name: wagtailcore_grouppagepermission id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_grouppagepermission ALTER COLUMN id SET DEFAULT nextval('public.wagtailcore_grouppagepermission_id_seq'::regclass);


--
-- Name: wagtailcore_page id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_page ALTER COLUMN id SET DEFAULT nextval('public.wagtailcore_page_id_seq'::regclass);


--
-- Name: wagtailcore_pagerevision id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_pagerevision ALTER COLUMN id SET DEFAULT nextval('public.wagtailcore_pagerevision_id_seq'::regclass);


--
-- Name: wagtailcore_pageviewrestriction id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_pageviewrestriction ALTER COLUMN id SET DEFAULT nextval('public.wagtailcore_pageviewrestriction_id_seq'::regclass);


--
-- Name: wagtailcore_pageviewrestriction_groups id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_pageviewrestriction_groups ALTER COLUMN id SET DEFAULT nextval('public.wagtailcore_pageviewrestriction_groups_id_seq'::regclass);


--
-- Name: wagtailcore_site id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_site ALTER COLUMN id SET DEFAULT nextval('public.wagtailcore_site_id_seq'::regclass);


--
-- Name: wagtaildocs_document id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtaildocs_document ALTER COLUMN id SET DEFAULT nextval('public.wagtaildocs_document_id_seq'::regclass);


--
-- Name: wagtailembeds_embed id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailembeds_embed ALTER COLUMN id SET DEFAULT nextval('public.wagtailembeds_embed_id_seq'::regclass);


--
-- Name: wagtailforms_formsubmission id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailforms_formsubmission ALTER COLUMN id SET DEFAULT nextval('public.wagtailforms_formsubmission_id_seq'::regclass);


--
-- Name: wagtailimages_image id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailimages_image ALTER COLUMN id SET DEFAULT nextval('public.wagtailimages_image_id_seq'::regclass);


--
-- Name: wagtailimages_rendition id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailimages_rendition ALTER COLUMN id SET DEFAULT nextval('public.wagtailimages_rendition_id_seq'::regclass);


--
-- Name: wagtailmedia_media id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailmedia_media ALTER COLUMN id SET DEFAULT nextval('public.wagtailmedia_media_id_seq'::regclass);


--
-- Name: wagtailsearch_editorspick id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailsearch_editorspick ALTER COLUMN id SET DEFAULT nextval('public.wagtailsearch_editorspick_id_seq'::regclass);


--
-- Name: wagtailsearch_query id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailsearch_query ALTER COLUMN id SET DEFAULT nextval('public.wagtailsearch_query_id_seq'::regclass);


--
-- Name: wagtailsearch_querydailyhits id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailsearch_querydailyhits ALTER COLUMN id SET DEFAULT nextval('public.wagtailsearch_querydailyhits_id_seq'::regclass);


--
-- Name: wagtailusers_userprofile id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailusers_userprofile ALTER COLUMN id SET DEFAULT nextval('public.wagtailusers_userprofile_id_seq'::regclass);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.auth_group (id, name) FROM stdin;
1	Moderators
2	Editors
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
1	1	1
2	1	2
3	1	3
4	2	1
5	2	2
6	2	3
7	1	4
8	1	5
9	1	6
10	2	4
11	2	5
12	2	6
13	1	8
14	1	9
15	1	7
16	2	8
17	2	9
18	2	7
19	1	10
20	2	10
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add document	2	add_document
2	Can change document	2	change_document
3	Can delete document	2	delete_document
4	Can add media	3	add_media
5	Can change media	3	change_media
6	Can delete media	3	delete_media
7	Can add image	4	add_image
8	Can change image	4	change_image
9	Can delete image	4	delete_image
10	Can access Wagtail admin	5	access_admin
11	Can add permission	6	add_permission
12	Can change permission	6	change_permission
13	Can delete permission	6	delete_permission
14	Can add group	7	add_group
15	Can change group	7	change_group
16	Can delete group	7	delete_group
17	Can add user	8	add_user
18	Can change user	8	change_user
19	Can delete user	8	delete_user
20	Can add content type	9	add_contenttype
21	Can change content type	9	change_contenttype
22	Can delete content type	9	delete_contenttype
23	Can add session	10	add_session
24	Can change session	10	change_session
25	Can delete session	10	delete_session
26	Can add test model	11	add_testmodel
27	Can change test model	11	change_testmodel
28	Can delete test model	11	delete_testmodel
29	Can add image hash	12	add_imagehash
30	Can change image hash	12	change_imagehash
31	Can delete image hash	12	delete_imagehash
32	Can add breadcrumb	13	add_breadcrumb
33	Can change breadcrumb	13	change_breadcrumb
34	Can delete breadcrumb	13	delete_breadcrumb
35	Can add document hash	14	add_documenthash
36	Can change document hash	14	change_documenthash
37	Can delete document hash	14	delete_documenthash
38	Can add form submission	15	add_formsubmission
39	Can change form submission	15	change_formsubmission
40	Can delete form submission	15	delete_formsubmission
41	Can add embed	16	add_embed
42	Can change embed	16	change_embed
43	Can delete embed	16	delete_embed
44	Can add user profile	17	add_userprofile
45	Can change user profile	17	change_userprofile
46	Can delete user profile	17	delete_userprofile
47	Can add rendition	18	add_rendition
48	Can change rendition	18	change_rendition
49	Can delete rendition	18	delete_rendition
50	Can add query	19	add_query
51	Can change query	19	change_query
52	Can delete query	19	delete_query
53	Can add Query Daily Hits	20	add_querydailyhits
54	Can change Query Daily Hits	20	change_querydailyhits
55	Can delete Query Daily Hits	20	delete_querydailyhits
56	Can add page	1	add_page
57	Can change page	1	change_page
58	Can delete page	1	delete_page
59	Can add group page permission	21	add_grouppagepermission
60	Can change group page permission	21	change_grouppagepermission
61	Can delete group page permission	21	delete_grouppagepermission
62	Can add page revision	22	add_pagerevision
63	Can change page revision	22	change_pagerevision
64	Can delete page revision	22	delete_pagerevision
65	Can add page view restriction	23	add_pageviewrestriction
66	Can change page view restriction	23	change_pageviewrestriction
67	Can delete page view restriction	23	delete_pageviewrestriction
68	Can add site	24	add_site
69	Can change site	24	change_site
70	Can delete site	24	delete_site
71	Can add collection	25	add_collection
72	Can change collection	25	change_collection
73	Can delete collection	25	delete_collection
74	Can add group collection permission	26	add_groupcollectionpermission
75	Can change group collection permission	26	change_groupcollectionpermission
76	Can delete group collection permission	26	delete_groupcollectionpermission
77	Can add collection view restriction	27	add_collectionviewrestriction
78	Can change collection view restriction	27	change_collectionviewrestriction
79	Can delete collection view restriction	27	delete_collectionviewrestriction
80	Can add Tag	28	add_tag
81	Can change Tag	28	change_tag
82	Can delete Tag	28	delete_tag
83	Can add Tagged Item	29	add_taggeditem
84	Can change Tagged Item	29	change_taggeditem
85	Can delete Tagged Item	29	delete_taggeditem
86	Can add industry page	30	add_industrypage
87	Can change industry page	30	change_industrypage
88	Can delete industry page	30	delete_industrypage
89	Can add industry article page	31	add_industryarticlepage
90	Can change industry article page	31	change_industryarticlepage
91	Can delete industry article page	31	delete_industryarticlepage
92	Can add industry landing page	32	add_industrylandingpage
93	Can change industry landing page	32	change_industrylandingpage
94	Can delete industry landing page	32	delete_industrylandingpage
95	Can add landing page	33	add_landingpage
96	Can change landing page	33	change_landingpage
97	Can delete landing page	33	delete_landingpage
98	Can add industry contact page	34	add_industrycontactpage
99	Can change industry contact page	34	change_industrycontactpage
100	Can delete industry contact page	34	delete_industrycontactpage
101	Can add find a supplier app	35	add_findasupplierapp
102	Can change find a supplier app	35	change_findasupplierapp
103	Can delete find a supplier app	35	delete_findasupplierapp
104	Can add industry page article summary	36	add_industrypagearticlesummary
105	Can change industry page article summary	36	change_industrypagearticlesummary
106	Can delete industry page article summary	36	delete_industrypagearticlesummary
107	Can add landing page article summary	37	add_landingpagearticlesummary
108	Can change landing page article summary	37	change_landingpagearticlesummary
109	Can delete landing page article summary	37	delete_landingpagearticlesummary
110	Can add terms and conditions page	38	add_termsandconditionspage
111	Can change terms and conditions page	38	change_termsandconditionspage
112	Can delete terms and conditions page	38	delete_termsandconditionspage
113	Can add export readiness app	39	add_exportreadinessapp
114	Can change export readiness app	39	change_exportreadinessapp
115	Can delete export readiness app	39	delete_exportreadinessapp
116	Can add privacy and cookies page	40	add_privacyandcookiespage
117	Can change privacy and cookies page	40	change_privacyandcookiespage
118	Can delete privacy and cookies page	40	delete_privacyandcookiespage
119	Can add performance dashboard page	41	add_performancedashboardpage
120	Can change performance dashboard page	41	change_performancedashboardpage
121	Can delete performance dashboard page	41	delete_performancedashboardpage
122	Can add performance dashboard notes page	42	add_performancedashboardnotespage
123	Can change performance dashboard notes page	42	change_performancedashboardnotespage
124	Can delete performance dashboard notes page	42	delete_performancedashboardnotespage
125	Can add article listing page	43	add_articlelistingpage
126	Can change article listing page	43	change_articlelistingpage
127	Can delete article listing page	43	delete_articlelistingpage
128	Can add article page	44	add_articlepage
129	Can change article page	44	change_articlepage
130	Can delete article page	44	delete_articlepage
131	Can add topic landing page	45	add_topiclandingpage
132	Can change topic landing page	45	change_topiclandingpage
133	Can delete topic landing page	45	delete_topiclandingpage
134	Can add home page	46	add_homepage
135	Can change home page	46	change_homepage
136	Can delete home page	46	delete_homepage
137	Can add eu exit international form page	47	add_euexitinternationalformpage
138	Can change eu exit international form page	47	change_euexitinternationalformpage
139	Can delete eu exit international form page	47	delete_euexitinternationalformpage
140	Can add tag	48	add_tag
141	Can change tag	48	change_tag
142	Can delete tag	48	delete_tag
143	Can add eu exit domestic form page	49	add_euexitdomesticformpage
144	Can change eu exit domestic form page	49	change_euexitdomesticformpage
145	Can delete eu exit domestic form page	49	delete_euexitdomesticformpage
146	Can add eu exit form success page	50	add_euexitformsuccesspage
147	Can change eu exit form success page	50	change_euexitformsuccesspage
148	Can delete eu exit form success page	50	delete_euexitformsuccesspage
149	Can add international landing page	51	add_internationallandingpage
150	Can change international landing page	51	change_internationallandingpage
151	Can delete international landing page	51	delete_internationallandingpage
152	Can add contact us guidance page	52	add_contactusguidancepage
153	Can change contact us guidance page	52	change_contactusguidancepage
154	Can delete contact us guidance page	52	delete_contactusguidancepage
155	Can add contact success page	53	add_contactsuccesspage
156	Can change contact success page	53	change_contactsuccesspage
157	Can delete contact success page	53	delete_contactsuccesspage
158	Can add get finance page	54	add_getfinancepage
159	Can change get finance page	54	change_getfinancepage
160	Can delete get finance page	54	delete_getfinancepage
161	Can add campaign page	55	add_campaignpage
162	Can change campaign page	55	change_campaignpage
163	Can delete campaign page	55	delete_campaignpage
164	Can add marketing pages	56	add_marketingpages
165	Can change marketing pages	56	change_marketingpages
166	Can delete marketing pages	56	delete_marketingpages
167	Can add contact success pages	57	add_contactsuccesspages
168	Can change contact success pages	57	change_contactsuccesspages
169	Can delete contact success pages	57	delete_contactsuccesspages
170	Can add contact us guidance pages	58	add_contactusguidancepages
171	Can change contact us guidance pages	58	change_contactusguidancepages
172	Can delete contact us guidance pages	58	delete_contactusguidancepages
173	Can add country guide page	59	add_countryguidepage
174	Can change country guide page	59	change_countryguidepage
175	Can delete country guide page	59	delete_countryguidepage
176	Can add superregion page	60	add_superregionpage
177	Can change superregion page	60	change_superregionpage
178	Can delete superregion page	60	delete_superregionpage
179	Can add site policy pages	61	add_sitepolicypages
180	Can change site policy pages	61	change_sitepolicypages
181	Can delete site policy pages	61	delete_sitepolicypages
182	Can add eu exit form pages	62	add_euexitformpages
183	Can change eu exit form pages	62	change_euexitformpages
184	Can delete eu exit form pages	62	delete_euexitformpages
185	Can add Forms	63	add_allcontactpagespage
186	Can change Forms	63	change_allcontactpagespage
187	Can delete Forms	63	delete_allcontactpagespage
188	Can add great international app	64	add_greatinternationalapp
189	Can change great international app	64	change_greatinternationalapp
190	Can delete great international app	64	delete_greatinternationalapp
191	Can add international article page	65	add_internationalarticlepage
192	Can change international article page	65	change_internationalarticlepage
193	Can delete international article page	65	delete_internationalarticlepage
194	Can add international home page	66	add_internationalhomepage
195	Can change international home page	66	change_internationalhomepage
196	Can delete international home page	66	delete_internationalhomepage
197	Can add international campaign page	67	add_internationalcampaignpage
198	Can change international campaign page	67	change_internationalcampaignpage
199	Can delete international campaign page	67	delete_internationalcampaignpage
200	Can add international article listing page	68	add_internationalarticlelistingpage
201	Can change international article listing page	68	change_internationalarticlelistingpage
202	Can delete international article listing page	68	delete_internationalarticlelistingpage
203	Can add international topic landing page	69	add_internationaltopiclandingpage
204	Can change international topic landing page	69	change_internationaltopiclandingpage
205	Can delete international topic landing page	69	delete_internationaltopiclandingpage
206	Can add international region page	70	add_internationalregionpage
207	Can change international region page	70	change_internationalregionpage
208	Can delete international region page	70	delete_internationalregionpage
209	Can add international localised folder page	71	add_internationallocalisedfolderpage
210	Can change international localised folder page	71	change_internationallocalisedfolderpage
211	Can delete international localised folder page	71	delete_internationallocalisedfolderpage
212	Can add international sector page	72	add_internationalsectorpage
213	Can change international sector page	72	change_internationalsectorpage
214	Can delete international sector page	72	delete_internationalsectorpage
215	Can add info page	73	add_infopage
216	Can change info page	73	change_infopage
217	Can delete info page	73	delete_infopage
218	Can add invest app	74	add_investapp
219	Can change invest app	74	change_investapp
220	Can delete invest app	74	delete_investapp
221	Can add invest home page	75	add_investhomepage
222	Can change invest home page	75	change_investhomepage
223	Can delete invest home page	75	delete_investhomepage
224	Can add sector landing page	76	add_sectorlandingpage
225	Can change sector landing page	76	change_sectorlandingpage
226	Can delete sector landing page	76	delete_sectorlandingpage
227	Can add sector page	77	add_sectorpage
228	Can change sector page	77	change_sectorpage
229	Can delete sector page	77	delete_sectorpage
230	Can add setup guide landing page	78	add_setupguidelandingpage
231	Can change setup guide landing page	78	change_setupguidelandingpage
232	Can delete setup guide landing page	78	delete_setupguidelandingpage
233	Can add setup guide page	79	add_setupguidepage
234	Can change setup guide page	79	change_setupguidepage
235	Can delete setup guide page	79	delete_setupguidepage
236	Can add region landing page	80	add_regionlandingpage
237	Can change region landing page	80	change_regionlandingpage
238	Can delete region landing page	80	delete_regionlandingpage
239	Can add high potential opportunity detail page	81	add_highpotentialopportunitydetailpage
240	Can change high potential opportunity detail page	81	change_highpotentialopportunitydetailpage
241	Can delete high potential opportunity detail page	81	delete_highpotentialopportunitydetailpage
242	Can add high potential opportunity form page	82	add_highpotentialopportunityformpage
243	Can change high potential opportunity form page	82	change_highpotentialopportunityformpage
244	Can delete high potential opportunity form page	82	delete_highpotentialopportunityformpage
245	Can add high potential opportunity form success page	83	add_highpotentialopportunityformsuccesspage
246	Can change high potential opportunity form success page	83	change_highpotentialopportunityformsuccesspage
247	Can delete high potential opportunity form success page	83	delete_highpotentialopportunityformsuccesspage
248	Can add banner component	84	add_bannercomponent
249	Can change banner component	84	change_bannercomponent
250	Can delete banner component	84	delete_bannercomponent
251	Can add components app	85	add_componentsapp
252	Can change components app	85	change_componentsapp
253	Can delete components app	85	delete_componentsapp
\.


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Data for Name: components_bannercomponent; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.components_bannercomponent (page_ptr_id, service_name, banner_content, banner_content_en_gb, banner_content_de, banner_content_ja, banner_content_ru, banner_content_zh_hans, banner_content_fr, banner_content_es, banner_content_pt, banner_content_pt_br, banner_content_ar, banner_label, banner_label_en_gb, banner_label_de, banner_label_ja, banner_label_ru, banner_label_zh_hans, banner_label_fr, banner_label_es, banner_label_pt, banner_label_pt_br, banner_label_ar) FROM stdin;
\.


--
-- Data for Name: components_componentsapp; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.components_componentsapp (page_ptr_id, service_name) FROM stdin;
\.


--
-- Data for Name: core_breadcrumb; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.core_breadcrumb (id, service_name, object_id, content_type_id, label, slug, label_ar, label_de, label_en_gb, label_es, label_fr, label_ja, label_pt, label_pt_br, label_ru, label_zh_hans) FROM stdin;
\.


--
-- Data for Name: core_documenthash; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.core_documenthash (id, content_hash, document_id) FROM stdin;
\.


--
-- Data for Name: core_imagehash; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.core_imagehash (id, content_hash, image_id) FROM stdin;
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	wagtailcore	page
2	wagtaildocs	document
3	wagtailmedia	media
4	wagtailimages	image
5	wagtailadmin	admin
6	auth	permission
7	auth	group
8	auth	user
9	contenttypes	contenttype
10	sessions	session
11	db	testmodel
12	core	imagehash
13	core	breadcrumb
14	core	documenthash
15	wagtailforms	formsubmission
16	wagtailembeds	embed
17	wagtailusers	userprofile
18	wagtailimages	rendition
19	wagtailsearch	query
20	wagtailsearch	querydailyhits
21	wagtailcore	grouppagepermission
22	wagtailcore	pagerevision
23	wagtailcore	pageviewrestriction
24	wagtailcore	site
25	wagtailcore	collection
26	wagtailcore	groupcollectionpermission
27	wagtailcore	collectionviewrestriction
28	taggit	tag
29	taggit	taggeditem
30	find_a_supplier	industrypage
31	find_a_supplier	industryarticlepage
32	find_a_supplier	industrylandingpage
33	find_a_supplier	landingpage
34	find_a_supplier	industrycontactpage
35	find_a_supplier	findasupplierapp
36	find_a_supplier	industrypagearticlesummary
37	find_a_supplier	landingpagearticlesummary
38	export_readiness	termsandconditionspage
39	export_readiness	exportreadinessapp
40	export_readiness	privacyandcookiespage
41	export_readiness	performancedashboardpage
42	export_readiness	performancedashboardnotespage
43	export_readiness	articlelistingpage
44	export_readiness	articlepage
45	export_readiness	topiclandingpage
46	export_readiness	homepage
47	export_readiness	euexitinternationalformpage
48	export_readiness	tag
49	export_readiness	euexitdomesticformpage
50	export_readiness	euexitformsuccesspage
51	export_readiness	internationallandingpage
52	export_readiness	contactusguidancepage
53	export_readiness	contactsuccesspage
54	export_readiness	getfinancepage
55	export_readiness	campaignpage
56	export_readiness	marketingpages
57	export_readiness	contactsuccesspages
58	export_readiness	contactusguidancepages
59	export_readiness	countryguidepage
60	export_readiness	superregionpage
61	export_readiness	sitepolicypages
62	export_readiness	euexitformpages
63	export_readiness	allcontactpagespage
64	great_international	greatinternationalapp
65	great_international	internationalarticlepage
66	great_international	internationalhomepage
67	great_international	internationalcampaignpage
68	great_international	internationalarticlelistingpage
69	great_international	internationaltopiclandingpage
70	great_international	internationalregionpage
71	great_international	internationallocalisedfolderpage
72	great_international	internationalsectorpage
73	invest	infopage
74	invest	investapp
75	invest	investhomepage
76	invest	sectorlandingpage
77	invest	sectorpage
78	invest	setupguidelandingpage
79	invest	setupguidepage
80	invest	regionlandingpage
81	invest	highpotentialopportunitydetailpage
82	invest	highpotentialopportunityformpage
83	invest	highpotentialopportunityformsuccesspage
84	components	bannercomponent
85	components	componentsapp
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2019-03-01 12:23:10.342677+00
2	contenttypes	0002_remove_content_type_name	2019-03-01 12:23:10.360117+00
3	auth	0001_initial	2019-03-01 12:23:10.424649+00
4	auth	0002_alter_permission_name_max_length	2019-03-01 12:23:10.435434+00
5	auth	0003_alter_user_email_max_length	2019-03-01 12:23:10.449952+00
6	auth	0004_alter_user_username_opts	2019-03-01 12:23:10.460185+00
7	auth	0005_alter_user_last_login_null	2019-03-01 12:23:10.471237+00
8	auth	0006_require_contenttypes_0002	2019-03-01 12:23:10.473602+00
9	auth	0007_alter_validators_add_error_messages	2019-03-01 12:23:10.484858+00
10	auth	0008_alter_user_username_max_length	2019-03-01 12:23:10.501963+00
11	wagtailcore	0001_initial	2019-03-01 12:23:10.704645+00
12	wagtailcore	0002_initial_data	2019-03-01 12:23:10.70643+00
13	wagtailcore	0003_add_uniqueness_constraint_on_group_page_permission	2019-03-01 12:23:10.708074+00
14	wagtailcore	0004_page_locked	2019-03-01 12:23:10.709695+00
15	wagtailcore	0005_add_page_lock_permission_to_moderators	2019-03-01 12:23:10.711315+00
16	wagtailcore	0006_add_lock_page_permission	2019-03-01 12:23:10.712996+00
17	wagtailcore	0007_page_latest_revision_created_at	2019-03-01 12:23:10.7146+00
18	wagtailcore	0008_populate_latest_revision_created_at	2019-03-01 12:23:10.716217+00
19	wagtailcore	0009_remove_auto_now_add_from_pagerevision_created_at	2019-03-01 12:23:10.717807+00
20	wagtailcore	0010_change_page_owner_to_null_on_delete	2019-03-01 12:23:10.719507+00
21	wagtailcore	0011_page_first_published_at	2019-03-01 12:23:10.721115+00
22	wagtailcore	0012_extend_page_slug_field	2019-03-01 12:23:10.722821+00
23	wagtailcore	0013_update_golive_expire_help_text	2019-03-01 12:23:10.724397+00
24	wagtailcore	0014_add_verbose_name	2019-03-01 12:23:10.726012+00
25	wagtailcore	0015_add_more_verbose_names	2019-03-01 12:23:10.727634+00
26	wagtailcore	0016_change_page_url_path_to_text_field	2019-03-01 12:23:10.729297+00
27	wagtailcore	0017_change_edit_page_permission_description	2019-03-01 12:23:10.742696+00
28	wagtailcore	0018_pagerevision_submitted_for_moderation_index	2019-03-01 12:23:10.760817+00
29	wagtailcore	0019_verbose_names_cleanup	2019-03-01 12:23:10.817138+00
30	wagtailcore	0020_add_index_on_page_first_published_at	2019-03-01 12:23:10.834187+00
31	wagtailcore	0021_capitalizeverbose	2019-03-01 12:23:11.289623+00
32	wagtailcore	0022_add_site_name	2019-03-01 12:23:11.304446+00
33	wagtailcore	0023_alter_page_revision_on_delete_behaviour	2019-03-01 12:23:11.325879+00
34	wagtailcore	0024_collection	2019-03-01 12:23:11.338408+00
35	wagtailcore	0025_collection_initial_data	2019-03-01 12:23:11.354857+00
36	wagtailcore	0026_group_collection_permission	2019-03-01 12:23:11.391763+00
37	wagtailcore	0027_fix_collection_path_collation	2019-03-01 12:23:11.411707+00
38	wagtailcore	0024_alter_page_content_type_on_delete_behaviour	2019-03-01 12:23:11.435671+00
39	wagtailcore	0028_merge	2019-03-01 12:23:11.438042+00
40	wagtailcore	0029_unicode_slugfield_dj19	2019-03-01 12:23:11.452528+00
41	wagtailcore	0030_index_on_pagerevision_created_at	2019-03-01 12:23:11.467462+00
42	wagtailcore	0031_add_page_view_restriction_types	2019-03-01 12:23:11.522754+00
43	wagtailcore	0032_add_bulk_delete_page_permission	2019-03-01 12:23:11.536765+00
44	wagtailcore	0033_remove_golive_expiry_help_text	2019-03-01 12:23:11.567042+00
45	wagtailcore	0034_page_live_revision	2019-03-01 12:23:11.587309+00
46	wagtailcore	0035_page_last_published_at	2019-03-01 12:23:11.60257+00
47	wagtailcore	0036_populate_page_last_published_at	2019-03-01 12:23:11.622474+00
48	wagtailcore	0037_set_page_owner_editable	2019-03-01 12:23:11.642921+00
49	wagtailcore	0038_make_first_published_at_editable	2019-03-01 12:23:11.657874+00
50	wagtailcore	0039_collectionviewrestriction	2019-03-01 12:23:11.71896+00
51	wagtailcore	0040_page_draft_title	2019-03-01 12:23:11.763394+00
52	components	0001_initial	2019-03-01 12:23:11.813035+00
53	components	0002_auto_20190206_1355	2019-03-01 12:23:11.844722+00
54	taggit	0001_initial	2019-03-01 12:23:11.881287+00
55	wagtaildocs	0001_initial	2019-03-01 12:23:11.910921+00
56	wagtaildocs	0002_initial_data	2019-03-01 12:23:11.951811+00
57	wagtaildocs	0003_add_verbose_names	2019-03-01 12:23:11.996935+00
58	wagtaildocs	0004_capitalizeverbose	2019-03-01 12:23:12.084929+00
59	wagtaildocs	0005_document_collection	2019-03-01 12:23:12.116108+00
60	wagtaildocs	0006_copy_document_permissions_to_collections	2019-03-01 12:23:12.151088+00
61	wagtaildocs	0005_alter_uploaded_by_user_on_delete_action	2019-03-01 12:23:12.178972+00
62	wagtaildocs	0007_merge	2019-03-01 12:23:12.180908+00
63	wagtaildocs	0008_document_file_size	2019-03-01 12:23:12.199189+00
64	taggit	0002_auto_20150616_2121	2019-03-01 12:23:12.210761+00
65	wagtailmedia	0001_initial	2019-03-01 12:23:12.315221+00
66	wagtailmedia	0002_initial_data	2019-03-01 12:23:12.352332+00
67	wagtailmedia	0003_copy_media_permissions_to_collections	2019-03-01 12:23:12.385557+00
68	wagtailimages	0001_initial	2019-03-01 12:23:12.456298+00
69	wagtailimages	0002_initial_data	2019-03-01 12:23:12.496502+00
70	wagtailimages	0003_fix_focal_point_fields	2019-03-01 12:23:12.537198+00
71	wagtailimages	0004_make_focal_point_key_not_nullable	2019-03-01 12:23:12.585057+00
72	wagtailimages	0005_make_filter_spec_unique	2019-03-01 12:23:12.600475+00
73	wagtailimages	0006_add_verbose_names	2019-03-01 12:23:12.659188+00
74	wagtailimages	0007_image_file_size	2019-03-01 12:23:12.675779+00
75	wagtailimages	0008_image_created_at_index	2019-03-01 12:23:12.694534+00
76	wagtailimages	0009_capitalizeverbose	2019-03-01 12:23:12.796342+00
77	wagtailimages	0010_change_on_delete_behaviour	2019-03-01 12:23:12.822005+00
78	wagtailimages	0011_image_collection	2019-03-01 12:23:12.855046+00
79	wagtailimages	0012_copy_image_permissions_to_collections	2019-03-01 12:23:12.890325+00
80	wagtailimages	0013_make_rendition_upload_callable	2019-03-01 12:23:12.901178+00
81	wagtailimages	0014_add_filter_spec_field	2019-03-01 12:23:12.946856+00
82	wagtailimages	0015_fill_filter_spec_field	2019-03-01 12:23:12.976473+00
83	wagtailimages	0016_deprecate_rendition_filter_relation	2019-03-01 12:23:13.021597+00
84	wagtailimages	0017_reduce_focal_point_key_max_length	2019-03-01 12:23:13.042645+00
85	wagtailimages	0018_remove_rendition_filter	2019-03-01 12:23:13.07474+00
86	wagtailimages	0019_delete_filter	2019-03-01 12:23:13.080617+00
87	wagtailimages	0020_add-verbose-name	2019-03-01 12:23:13.101561+00
88	wagtailimages	0021_image_file_hash	2019-03-01 12:23:13.126231+00
89	invest	0001_squashed_0006_auto_20180719_1302	2019-03-01 12:23:57.526673+00
90	invest	0007_auto_20180719_1414	2019-03-01 12:23:58.465851+00
91	invest	0008_auto_20180817_1630	2019-03-01 12:23:59.164847+00
92	invest	0009_investapp_service_name	2019-03-01 12:23:59.249904+00
93	invest	0009_highpotentialofferformpage	2019-03-01 12:23:59.344786+00
94	wagtailforms	0001_initial	2019-03-01 12:23:59.438825+00
95	wagtailforms	0002_add_verbose_names	2019-03-01 12:23:59.586856+00
96	wagtailforms	0003_capitalizeverbose	2019-03-01 12:23:59.843503+00
97	find_a_supplier	0001_squashed_0050_auto_20180425_1107	2019-03-01 12:24:29.24266+00
98	find_a_supplier	0051_auto_20180501_1706	2019-03-01 12:24:59.434864+00
99	find_a_supplier	0052_html_to_markdown	2019-03-01 12:24:59.590335+00
100	find_a_supplier	0053_industrypage_show_on_industries_showcase_page	2019-03-01 12:24:59.71737+00
101	find_a_supplier	0054_auto_20180510_0902	2019-03-01 12:25:02.189041+00
102	find_a_supplier	0055_industrycontactpage_industry_options	2019-03-01 12:25:02.286546+00
103	find_a_supplier	0056_auto_20180515_1552	2019-03-01 12:25:02.540279+00
104	find_a_supplier	0057_remove_industrycontactpage_industry_options	2019-03-01 12:25:02.642878+00
105	find_a_supplier	0058_auto_20180521_1628	2019-03-01 12:25:21.635016+00
106	find_a_supplier	0059_auto_20180601_1412	2019-03-01 12:25:21.858775+00
107	find_a_supplier	0060_auto_20180604_1058	2019-03-01 12:25:21.992135+00
108	find_a_supplier	0061_auto_20180604_1344	2019-03-01 12:25:22.294044+00
109	find_a_supplier	0062_auto_20180817_1630_squashed_0065_auto_20180829_1027	2019-03-01 12:25:23.056314+00
110	export_readiness	0001_squashed_0009_performancedashboardpage_guidance_notes	2019-03-01 12:25:23.803576+00
111	export_readiness	0010_performancedashboardnotespage	2019-03-01 12:25:23.93802+00
112	export_readiness	0011_auto_20180817_1630	2019-03-01 12:25:24.519263+00
113	export_readiness	0012_auto_20180821_0810	2019-03-01 12:25:25.208246+00
114	core	0001_create	2019-03-01 12:25:25.339065+00
115	core	0002_auto_20180307_1748	2019-03-01 12:25:25.63022+00
116	core	0003_auto_20180423_1122	2019-03-01 12:25:25.865586+00
117	core	0004_auto_20180423_1619	2019-03-01 12:25:26.105782+00
118	core	0005_auto_20180423_1803	2019-03-01 12:25:26.333252+00
119	core	0006_auto_20180508_1331	2019-03-01 12:25:26.335966+00
120	core	0007_auto_20180809_1215	2019-03-01 12:25:26.706641+00
121	core	0008_auto_20180809_1215	2019-03-01 12:25:26.850467+00
122	core	0009_auto_20180813_1746	2019-03-01 12:25:26.992413+00
123	core	0010_auto_20180815_1304	2019-03-01 12:25:27.214083+00
124	core	0011_auto_20180817_1631	2019-03-01 12:25:27.569359+00
125	core	0012_auto_20180821_1634	2019-03-01 12:25:27.780032+00
126	core	0013_auto_20180821_1637	2019-03-01 12:25:27.920944+00
127	core	0014_auto_20180822_0915	2019-03-01 12:25:28.304645+00
128	core	0015_breadcrumb	2019-03-01 12:25:28.443475+00
129	core	0016_auto_20180823_2014	2019-03-01 12:25:28.55161+00
130	core	0017_auto_20180823_1545	2019-03-01 12:25:28.842475+00
131	export_readiness	0013_exportreadinessapp_service_name	2019-03-01 12:25:28.866763+00
132	core	0015_auto_20180822_1456	2019-03-01 12:25:29.007716+00
133	core	0018_merge_20180829_0828	2019-03-01 12:25:29.01246+00
134	core	0018_auto_20180824_1622	2019-03-01 12:25:29.038529+00
135	core	0019_merge_20180829_0939	2019-03-01 12:25:29.041236+00
136	invest	0010_merge_20180829_0939_squashed_0013_auto_20180830_0632	2019-03-01 12:25:35.303489+00
137	invest	0014_auto_20180904_1113	2019-03-01 12:25:36.55874+00
138	invest	0015_auto_20180911_1049	2019-03-01 12:25:36.561041+00
139	invest	0016_auto_20180911_1506	2019-03-01 12:25:36.562989+00
140	invest	0017_auto_20180911_1513	2019-03-01 12:25:36.565286+00
141	invest	0018_auto_20180913_1445	2019-03-01 12:25:36.567517+00
142	invest	0019_auto_20180917_0838	2019-03-01 12:25:36.569767+00
143	invest	0020_auto_20180917_1326	2019-03-01 12:25:36.571759+00
144	invest	0021_auto_20180917_1404	2019-03-01 12:25:36.574064+00
145	invest	0022_auto_20180917_1622	2019-03-01 12:25:36.576303+00
146	invest	0023_auto_20180918_0805	2019-03-01 12:25:36.578382+00
147	invest	0024_highpotentialopportunitydetailpage_testimonial_background	2019-03-01 12:25:36.580546+00
148	invest	0025_auto_20180920_0941	2019-03-01 12:25:36.582823+00
149	invest	0026_auto_20181002_1534	2019-03-01 12:25:36.585122+00
150	find_a_supplier	0066_auto_20180830_0632	2019-03-01 12:25:36.739835+00
151	export_readiness	0014_auto_20180829_1027_squashed_0018_getfinancepage	2019-03-01 12:25:37.438845+00
152	export_readiness	0019_auto_20180905_1350	2019-03-01 12:25:37.82036+00
153	core	0020_auto_20180830_1737	2019-03-01 12:25:38.137171+00
154	core	0021_auto_20180904_1511	2019-03-01 12:25:38.388108+00
155	core	0022_auto_20180906_1344	2019-03-01 12:25:38.603061+00
156	core	0023_auto_20180912_0758	2019-03-01 12:25:38.756921+00
157	core	0024_auto_20180913_1321	2019-03-01 12:25:38.906173+00
158	core	0025_documenthash	2019-03-01 12:25:39.218303+00
159	core	0026_auto_20181024_1112	2019-03-01 12:25:39.231498+00
160	core	0027_auto_20190206_1355	2019-03-01 12:25:39.245926+00
161	health_check_db	0001_initial	2019-03-01 12:25:39.256701+00
162	export_readiness	0020_articlelistingpage_articlepage_topiclandingpage_squashed_0030_auto_20181005_1449	2019-03-01 12:25:42.168901+00
163	export_readiness	0031_internationallandingpage	2019-03-01 12:25:42.310049+00
164	export_readiness	0032_auto_20181012_1507	2019-03-01 12:25:43.344624+00
165	export_readiness	0033_auto_20181023_1600	2019-03-01 12:25:43.804465+00
166	export_readiness	0034_auto_20181024_1112	2019-03-01 12:25:45.847087+00
167	export_readiness	0035_contactusguidance	2019-03-01 12:25:46.227616+00
168	export_readiness	0036_auto_20181105_1258	2019-03-01 12:25:46.548483+00
169	export_readiness	0037_auto_20181106_0952	2019-03-01 12:25:47.172469+00
170	export_readiness	0038_auto_20181106_0953	2019-03-01 12:25:47.506779+00
171	export_readiness	0039_contactsuccesspage_topic	2019-03-01 12:25:47.922768+00
172	export_readiness	0040_auto_20181121_1643	2019-03-01 12:25:48.055778+00
173	export_readiness	0041_campaignpage_marketingpages	2019-03-01 12:25:48.407991+00
174	export_readiness	0042_contactsuccesspages_contactusguidancepages	2019-03-01 12:25:48.722231+00
175	export_readiness	0043_auto_20181205_1413	2019-03-01 12:25:54.539629+00
176	export_readiness	0044_auto_20181214_1605	2019-03-01 12:25:54.666293+00
177	export_readiness	0045_auto_20190115_1058	2019-03-01 12:25:55.401353+00
178	export_readiness	0046_euexitformpages	2019-03-01 12:25:55.553529+00
179	export_readiness	0047_allcontactpagespage	2019-03-01 12:25:55.709637+00
180	export_readiness	0048_auto_20190206_1355	2019-03-01 12:25:59.393753+00
181	export_readiness	0049_auto_20190207_0924	2019-03-01 12:25:59.667653+00
182	export_readiness	0050_auto_20190219_1633	2019-03-01 12:25:59.800737+00
183	find_a_supplier	0067_auto_20181012_1507	2019-03-01 12:26:01.131795+00
184	find_a_supplier	0068_auto_20181024_1112	2019-03-01 12:26:02.211678+00
185	find_a_supplier	0069_auto_20190206_1355	2019-03-01 12:26:03.30842+00
186	great_international	0001_initial	2019-03-01 12:26:04.250292+00
187	great_international	0002_auto_20190206_1146	2019-03-01 12:26:05.029768+00
188	great_international	0003_internationalarticlelistingpage	2019-03-01 12:26:05.383372+00
189	great_international	0003_auto_20190211_1202	2019-03-01 12:26:05.904902+00
190	great_international	0004_merge_20190212_1003	2019-03-01 12:26:05.907932+00
191	great_international	0005_internationalukhqpages	2019-03-01 12:26:06.084446+00
192	great_international	0006_internationaltopiclandingpage	2019-03-01 12:26:06.486788+00
193	great_international	0007_auto_20190219_1114	2019-03-01 12:26:07.949541+00
194	great_international	0008_auto_20190222_1554	2019-03-01 12:26:08.68124+00
195	great_international	0008_auto_20190222_1230	2019-03-01 12:26:09.553686+00
196	great_international	0009_merge_20190225_1214	2019-03-01 12:26:09.556558+00
197	great_international	0010_auto_20190228_0819	2019-03-01 12:26:09.92064+00
198	great_international	0011_auto_20190228_1051	2019-03-01 12:26:10.268717+00
199	great_international	0012_internationalsectorpage	2019-03-01 12:26:10.666902+00
200	invest	0015_auto_20181012_1507	2019-03-01 12:26:11.640664+00
201	invest	0016_auto_20181025_1226	2019-03-01 12:26:13.882988+00
202	invest	0017_auto_20190206_1355	2019-03-01 12:26:16.056215+00
203	sessions	0001_initial	2019-03-01 12:26:16.072981+00
204	wagtailadmin	0001_create_admin_access_permissions	2019-03-01 12:26:16.265848+00
205	wagtailembeds	0001_initial	2019-03-01 12:26:16.291218+00
206	wagtailembeds	0002_add_verbose_names	2019-03-01 12:26:16.302377+00
207	wagtailembeds	0003_capitalizeverbose	2019-03-01 12:26:16.313064+00
208	wagtailsearch	0001_initial	2019-03-01 12:26:16.929659+00
209	wagtailsearch	0002_add_verbose_names	2019-03-01 12:26:17.484236+00
210	wagtailsearch	0003_remove_editors_pick	2019-03-01 12:26:17.832725+00
211	wagtailusers	0001_initial	2019-03-01 12:26:18.03575+00
212	wagtailusers	0002_add_verbose_name_on_userprofile	2019-03-01 12:26:18.0988+00
213	wagtailusers	0003_add_verbose_names	2019-03-01 12:26:18.123643+00
214	wagtailusers	0004_capitalizeverbose	2019-03-01 12:26:18.203642+00
215	wagtailusers	0005_make_related_name_wagtail_specific	2019-03-01 12:26:18.242713+00
216	wagtailusers	0006_userprofile_prefered_language	2019-03-01 12:26:18.268783+00
217	wagtailusers	0007_userprofile_current_time_zone	2019-03-01 12:26:18.298623+00
218	wagtailusers	0008_userprofile_avatar	2019-03-01 12:26:18.328539+00
219	db	0001_initial	2019-03-01 12:26:18.334087+00
220	wagtailcore	0001_squashed_0016_change_page_url_path_to_text_field	2019-03-01 12:26:18.336559+00
221	invest	0014_auto_20180904_1113_squashed_0026_auto_20181002_1534	2019-03-01 12:26:18.339146+00
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
\.


--
-- Data for Name: export_readiness_allcontactpagespage; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.export_readiness_allcontactpagespage (page_ptr_id, service_name) FROM stdin;
\.


--
-- Data for Name: export_readiness_articlelistingpage; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.export_readiness_articlelistingpage (page_ptr_id, service_name, landing_page_title, hero_teaser, list_teaser, hero_image_id) FROM stdin;
\.


--
-- Data for Name: export_readiness_articlepage; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.export_readiness_articlepage (page_ptr_id, service_name, article_title, article_teaser, article_body_text, article_image_id, related_page_one_id, related_page_three_id, related_page_two_id) FROM stdin;
\.


--
-- Data for Name: export_readiness_articlepage_tags; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.export_readiness_articlepage_tags (id, articlepage_id, tag_id) FROM stdin;
\.


--
-- Data for Name: export_readiness_campaignpage; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.export_readiness_campaignpage (page_ptr_id, service_name, campaign_heading, section_one_heading, section_one_intro, selling_point_one_heading, selling_point_one_content, selling_point_two_heading, selling_point_two_content, selling_point_three_heading, selling_point_three_content, section_one_contact_button_url, section_one_contact_button_text, section_two_heading, section_two_intro, section_two_contact_button_url, section_two_contact_button_text, related_content_heading, related_content_intro, cta_box_message, cta_box_button_url, cta_box_button_text, campaign_hero_image_id, section_one_image_id, section_two_image_id, selling_point_one_icon_id, selling_point_three_icon_id, selling_point_two_icon_id, related_page_one_id, related_page_three_id, related_page_two_id) FROM stdin;
\.


--
-- Data for Name: export_readiness_contactsuccesspage; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.export_readiness_contactsuccesspage (page_ptr_id, service_name, heading, body_text, next_title, next_body_text, topic) FROM stdin;
\.


--
-- Data for Name: export_readiness_contactsuccesspages; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.export_readiness_contactsuccesspages (page_ptr_id, service_name) FROM stdin;
\.


--
-- Data for Name: export_readiness_contactusguidancepage; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.export_readiness_contactusguidancepage (page_ptr_id, service_name, topic, body) FROM stdin;
\.


--
-- Data for Name: export_readiness_contactusguidancepages; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.export_readiness_contactusguidancepages (page_ptr_id, service_name) FROM stdin;
\.


--
-- Data for Name: export_readiness_countryguidepage; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.export_readiness_countryguidepage (page_ptr_id, service_name, landing_page_title, section_one_heading, section_one_content, selling_point_one_heading, selling_point_one_content, selling_point_two_heading, selling_point_two_content, selling_point_three_heading, selling_point_three_content, section_two_heading, section_two_content, related_content_heading, related_content_intro, hero_image_id, related_page_one_id, related_page_three_id, related_page_two_id, selling_point_one_icon_id, selling_point_three_icon_id, selling_point_two_icon_id) FROM stdin;
\.


--
-- Data for Name: export_readiness_euexitdomesticformpage; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.export_readiness_euexitdomesticformpage (page_ptr_id, service_name, breadcrumbs_label, first_name_help_text, first_name_label, last_name_help_text, last_name_label, email_help_text, email_label, organisation_type_help_text, organisation_type_label, company_name_help_text, company_name_label, comment_help_text, comment_label, body_text, heading, submit_button_text, disclaimer) FROM stdin;
\.


--
-- Data for Name: export_readiness_euexitformpages; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.export_readiness_euexitformpages (page_ptr_id, service_name) FROM stdin;
\.


--
-- Data for Name: export_readiness_euexitformsuccesspage; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.export_readiness_euexitformsuccesspage (page_ptr_id, service_name, breadcrumbs_label, heading, body_text, next_title, next_body_text) FROM stdin;
\.


--
-- Data for Name: export_readiness_euexitinternationalformpage; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.export_readiness_euexitinternationalformpage (page_ptr_id, service_name, breadcrumbs_label, first_name_label, first_name_help_text, last_name_label, last_name_help_text, email_label, email_help_text, organisation_type_label, organisation_type_help_text, company_name_label, company_name_help_text, country_label, country_help_text, city_label, city_help_text, comment_label, comment_help_text, body_text, heading, submit_button_text, disclaimer) FROM stdin;
\.


--
-- Data for Name: export_readiness_exportreadinessapp; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.export_readiness_exportreadinessapp (page_ptr_id, service_name) FROM stdin;
\.


--
-- Data for Name: export_readiness_getfinancepage; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.export_readiness_getfinancepage (page_ptr_id, service_name, breadcrumbs_label, hero_text, contact_proposition, contact_button, advantages_title, advantages_one, advantages_two, advantages_three, evidence, hero_image_id, ukef_logo_id, advantages_one_icon_id, advantages_three_icon_id, advantages_two_icon_id, evidence_video_id) FROM stdin;
\.


--
-- Data for Name: export_readiness_homepage; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.export_readiness_homepage (page_ptr_id, service_name, news_title, news_description, banner_content, banner_label) FROM stdin;
\.


--
-- Data for Name: export_readiness_internationallandingpage; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.export_readiness_internationallandingpage (page_ptr_id, service_name) FROM stdin;
\.


--
-- Data for Name: export_readiness_marketingpages; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.export_readiness_marketingpages (page_ptr_id, service_name) FROM stdin;
\.


--
-- Data for Name: export_readiness_performancedashboardnotespage; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.export_readiness_performancedashboardnotespage (page_ptr_id, body, service_name) FROM stdin;
\.


--
-- Data for Name: export_readiness_performancedashboardpage; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.export_readiness_performancedashboardpage (page_ptr_id, heading, description, product_link, data_title_row_one, data_number_row_one, data_period_row_one, data_description_row_one, data_title_row_two, data_number_row_two, data_period_row_two, data_description_row_two, data_title_row_three, data_number_row_three, data_period_row_three, data_description_row_three, data_title_row_four, data_number_row_four, data_period_row_four, data_description_row_four, landing_dashboard, guidance_notes, service_name) FROM stdin;
\.


--
-- Data for Name: export_readiness_privacyandcookiespage; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.export_readiness_privacyandcookiespage (page_ptr_id, body, service_name) FROM stdin;
\.


--
-- Data for Name: export_readiness_sitepolicypages; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.export_readiness_sitepolicypages (page_ptr_id, service_name) FROM stdin;
\.


--
-- Data for Name: export_readiness_superregionpage; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.export_readiness_superregionpage (topiclandingpage_ptr_id) FROM stdin;
\.


--
-- Data for Name: export_readiness_tag; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.export_readiness_tag (id, name, slug) FROM stdin;
\.


--
-- Data for Name: export_readiness_termsandconditionspage; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.export_readiness_termsandconditionspage (page_ptr_id, body, service_name) FROM stdin;
\.


--
-- Data for Name: export_readiness_topiclandingpage; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.export_readiness_topiclandingpage (page_ptr_id, service_name, landing_page_title, hero_teaser, hero_image_id) FROM stdin;
\.


--
-- Data for Name: find_a_supplier_findasupplierapp; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.find_a_supplier_findasupplierapp (page_ptr_id, service_name) FROM stdin;
\.


--
-- Data for Name: find_a_supplier_industryarticlepage; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.find_a_supplier_industryarticlepage (page_ptr_id, body, body_en_gb, body_de, body_ja, body_ru, body_zh_hans, body_fr, body_es, body_pt, body_pt_br, body_ar, author_name, author_name_en_gb, author_name_de, author_name_ja, author_name_ru, author_name_zh_hans, author_name_fr, author_name_es, author_name_pt, author_name_pt_br, author_name_ar, job_title, job_title_en_gb, job_title_de, job_title_ja, job_title_ru, job_title_zh_hans, job_title_fr, job_title_es, job_title_pt, job_title_pt_br, job_title_ar, date, date_en_gb, date_de, date_ja, date_ru, date_zh_hans, date_fr, date_es, date_pt, date_pt_br, date_ar, introduction_title, introduction_title_ar, introduction_title_de, introduction_title_en_gb, introduction_title_es, introduction_title_fr, introduction_title_ja, introduction_title_pt, introduction_title_pt_br, introduction_title_ru, introduction_title_zh_hans, breadcrumbs_label, breadcrumbs_label_ar, breadcrumbs_label_de, breadcrumbs_label_en_gb, breadcrumbs_label_es, breadcrumbs_label_fr, breadcrumbs_label_ja, breadcrumbs_label_pt, breadcrumbs_label_pt_br, breadcrumbs_label_ru, breadcrumbs_label_zh_hans, call_to_action_text, call_to_action_text_ar, call_to_action_text_de, call_to_action_text_en_gb, call_to_action_text_es, call_to_action_text_fr, call_to_action_text_ja, call_to_action_text_pt, call_to_action_text_pt_br, call_to_action_text_ru, call_to_action_text_zh_hans, proposition_text, proposition_text_ar, proposition_text_de, proposition_text_en_gb, proposition_text_es, proposition_text_fr, proposition_text_ja, proposition_text_pt, proposition_text_pt_br, proposition_text_ru, proposition_text_zh_hans, show_table_of_content, back_to_home_link_text, back_to_home_link_text_ar, back_to_home_link_text_de, back_to_home_link_text_en_gb, back_to_home_link_text_es, back_to_home_link_text_fr, back_to_home_link_text_ja, back_to_home_link_text_pt, back_to_home_link_text_pt_br, back_to_home_link_text_ru, back_to_home_link_text_zh_hans, social_share_title, social_share_title_ar, social_share_title_de, social_share_title_en_gb, social_share_title_es, social_share_title_fr, social_share_title_ja, social_share_title_pt, social_share_title_pt_br, social_share_title_ru, social_share_title_zh_hans, service_name) FROM stdin;
\.


--
-- Data for Name: find_a_supplier_industrycontactpage; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.find_a_supplier_industrycontactpage (page_ptr_id, introduction_text, introduction_text_en_gb, introduction_text_de, introduction_text_ja, introduction_text_ru, introduction_text_zh_hans, introduction_text_fr, introduction_text_es, introduction_text_pt, introduction_text_pt_br, introduction_text_ar, submit_button_text, submit_button_text_en_gb, submit_button_text_de, submit_button_text_ja, submit_button_text_ru, submit_button_text_zh_hans, submit_button_text_fr, submit_button_text_es, submit_button_text_pt, submit_button_text_pt_br, submit_button_text_ar, success_message_text, success_message_text_en_gb, success_message_text_de, success_message_text_ja, success_message_text_ru, success_message_text_zh_hans, success_message_text_fr, success_message_text_es, success_message_text_pt, success_message_text_pt_br, success_message_text_ar, success_back_link_text, success_back_link_text_en_gb, success_back_link_text_de, success_back_link_text_ja, success_back_link_text_ru, success_back_link_text_zh_hans, success_back_link_text_fr, success_back_link_text_es, success_back_link_text_pt, success_back_link_text_pt_br, success_back_link_text_ar, breadcrumbs_label, breadcrumbs_label_ar, breadcrumbs_label_de, breadcrumbs_label_en_gb, breadcrumbs_label_es, breadcrumbs_label_fr, breadcrumbs_label_ja, breadcrumbs_label_pt, breadcrumbs_label_pt_br, breadcrumbs_label_ru, breadcrumbs_label_zh_hans, service_name) FROM stdin;
\.


--
-- Data for Name: find_a_supplier_industrylandingpage; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.find_a_supplier_industrylandingpage (page_ptr_id, proposition_text, proposition_text_en_gb, proposition_text_de, proposition_text_ja, proposition_text_ru, proposition_text_zh_hans, proposition_text_fr, proposition_text_es, proposition_text_pt, proposition_text_pt_br, proposition_text_ar, call_to_action_text, call_to_action_text_en_gb, call_to_action_text_de, call_to_action_text_ja, call_to_action_text_ru, call_to_action_text_zh_hans, call_to_action_text_fr, call_to_action_text_es, call_to_action_text_pt, call_to_action_text_pt_br, call_to_action_text_ar, breadcrumbs_label, breadcrumbs_label_en_gb, breadcrumbs_label_de, breadcrumbs_label_ja, breadcrumbs_label_ru, breadcrumbs_label_zh_hans, breadcrumbs_label_fr, breadcrumbs_label_es, breadcrumbs_label_pt, breadcrumbs_label_pt_br, breadcrumbs_label_ar, hero_image_id, hero_title, hero_title_ar, hero_title_de, hero_title_en_gb, hero_title_es, hero_title_fr, hero_title_ja, hero_title_pt, hero_title_pt_br, hero_title_ru, hero_title_zh_hans, mobile_hero_image_id, more_industries_title, more_industries_title_ar, more_industries_title_de, more_industries_title_en_gb, more_industries_title_es, more_industries_title_fr, more_industries_title_ja, more_industries_title_pt, more_industries_title_pt_br, more_industries_title_ru, more_industries_title_zh_hans, hero_image_caption, hero_image_caption_ar, hero_image_caption_de, hero_image_caption_en_gb, hero_image_caption_es, hero_image_caption_fr, hero_image_caption_ja, hero_image_caption_pt, hero_image_caption_pt_br, hero_image_caption_ru, hero_image_caption_zh_hans, service_name) FROM stdin;
\.


--
-- Data for Name: find_a_supplier_industrypage; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.find_a_supplier_industrypage (page_ptr_id, hero_text, hero_text_en_gb, hero_text_de, hero_text_ja, hero_text_zh_hans, hero_text_fr, hero_text_es, hero_text_pt, hero_text_pt_br, hero_text_ar, introduction_text, introduction_text_en_gb, introduction_text_de, introduction_text_ja, introduction_text_zh_hans, introduction_text_fr, introduction_text_es, introduction_text_pt, introduction_text_pt_br, introduction_text_ar, introduction_column_one_text, introduction_column_one_text_en_gb, introduction_column_one_text_de, introduction_column_one_text_ja, introduction_column_one_text_zh_hans, introduction_column_one_text_fr, introduction_column_one_text_es, introduction_column_one_text_pt, introduction_column_one_text_pt_br, introduction_column_one_text_ar, introduction_column_two_text, introduction_column_two_text_en_gb, introduction_column_two_text_de, introduction_column_two_text_ja, introduction_column_two_text_zh_hans, introduction_column_two_text_fr, introduction_column_two_text_es, introduction_column_two_text_pt, introduction_column_two_text_pt_br, introduction_column_two_text_ar, introduction_column_three_text, introduction_column_three_text_en_gb, introduction_column_three_text_de, introduction_column_three_text_ja, introduction_column_three_text_zh_hans, introduction_column_three_text_fr, introduction_column_three_text_es, introduction_column_three_text_pt, introduction_column_three_text_pt_br, introduction_column_three_text_ar, hero_image_id, hero_text_ru, introduction_column_one_text_ru, introduction_column_three_text_ru, introduction_column_two_text_ru, introduction_text_ru, introduction_column_one_icon_id, introduction_column_three_icon_id, introduction_column_two_icon_id, company_list_call_to_action_text, company_list_call_to_action_text_ar, company_list_call_to_action_text_de, company_list_call_to_action_text_en_gb, company_list_call_to_action_text_es, company_list_call_to_action_text_fr, company_list_call_to_action_text_ja, company_list_call_to_action_text_pt, company_list_call_to_action_text_pt_br, company_list_call_to_action_text_ru, company_list_call_to_action_text_zh_hans, company_list_text, company_list_text_ar, company_list_text_de, company_list_text_en_gb, company_list_text_es, company_list_text_fr, company_list_text_ja, company_list_text_pt, company_list_text_pt_br, company_list_text_ru, company_list_text_zh_hans, company_list_search_input_placeholder_text, company_list_search_input_placeholder_text_ar, company_list_search_input_placeholder_text_de, company_list_search_input_placeholder_text_en_gb, company_list_search_input_placeholder_text_es, company_list_search_input_placeholder_text_fr, company_list_search_input_placeholder_text_ja, company_list_search_input_placeholder_text_pt, company_list_search_input_placeholder_text_pt_br, company_list_search_input_placeholder_text_ru, company_list_search_input_placeholder_text_zh_hans, breadcrumbs_label, breadcrumbs_label_ar, breadcrumbs_label_de, breadcrumbs_label_en_gb, breadcrumbs_label_es, breadcrumbs_label_fr, breadcrumbs_label_ja, breadcrumbs_label_pt, breadcrumbs_label_pt_br, breadcrumbs_label_ru, breadcrumbs_label_zh_hans, introduction_call_to_action_button_text, introduction_call_to_action_button_text_ar, introduction_call_to_action_button_text_de, introduction_call_to_action_button_text_en_gb, introduction_call_to_action_button_text_es, introduction_call_to_action_button_text_fr, introduction_call_to_action_button_text_ja, introduction_call_to_action_button_text_pt, introduction_call_to_action_button_text_pt_br, introduction_call_to_action_button_text_ru, introduction_call_to_action_button_text_zh_hans, summary_image_id, search_filter_sector, search_filter_text, mobile_hero_image_id, search_filter_showcase_only, hero_image_caption, hero_image_caption_ar, hero_image_caption_de, hero_image_caption_en_gb, hero_image_caption_es, hero_image_caption_fr, hero_image_caption_ja, hero_image_caption_pt, hero_image_caption_pt_br, hero_image_caption_ru, hero_image_caption_zh_hans, introduction_title, introduction_title_ar, introduction_title_de, introduction_title_en_gb, introduction_title_es, introduction_title_fr, introduction_title_ja, introduction_title_pt, introduction_title_pt_br, introduction_title_ru, introduction_title_zh_hans, show_on_homepage, show_on_industries_showcase_page, service_name) FROM stdin;
\.


--
-- Data for Name: find_a_supplier_industrypagearticlesummary; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.find_a_supplier_industrypagearticlesummary (id, sort_order, industry_name, title, body, image_id, page_id, page_ar_id, page_de_id, page_en_gb_id, page_es_id, page_fr_id, page_ja_id, page_pt_id, page_pt_br_id, page_ru_id, page_zh_hans_id, video_media_id) FROM stdin;
\.


--
-- Data for Name: find_a_supplier_landingpage; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.find_a_supplier_landingpage (page_ptr_id, hero_text, hero_text_en_gb, hero_text_de, hero_text_ja, hero_text_ru, hero_text_zh_hans, hero_text_fr, hero_text_es, hero_text_pt, hero_text_pt_br, hero_text_ar, search_field_placeholder, search_field_placeholder_en_gb, search_field_placeholder_de, search_field_placeholder_ja, search_field_placeholder_ru, search_field_placeholder_zh_hans, search_field_placeholder_fr, search_field_placeholder_es, search_field_placeholder_pt, search_field_placeholder_pt_br, search_field_placeholder_ar, search_button_text, search_button_text_en_gb, search_button_text_de, search_button_text_ja, search_button_text_ru, search_button_text_zh_hans, search_button_text_fr, search_button_text_es, search_button_text_pt, search_button_text_pt_br, search_button_text_ar, proposition_text, proposition_text_en_gb, proposition_text_de, proposition_text_ja, proposition_text_ru, proposition_text_zh_hans, proposition_text_fr, proposition_text_es, proposition_text_pt, proposition_text_pt_br, proposition_text_ar, call_to_action_text, call_to_action_text_en_gb, call_to_action_text_de, call_to_action_text_ja, call_to_action_text_ru, call_to_action_text_zh_hans, call_to_action_text_fr, call_to_action_text_es, call_to_action_text_pt, call_to_action_text_pt_br, call_to_action_text_ar, industries_list_text, industries_list_text_en_gb, industries_list_text_de, industries_list_text_ja, industries_list_text_ru, industries_list_text_zh_hans, industries_list_text_fr, industries_list_text_es, industries_list_text_pt, industries_list_text_pt_br, industries_list_text_ar, industries_list_call_to_action_text, industries_list_call_to_action_text_en_gb, industries_list_call_to_action_text_de, industries_list_call_to_action_text_ja, industries_list_call_to_action_text_ru, industries_list_call_to_action_text_zh_hans, industries_list_call_to_action_text_fr, industries_list_call_to_action_text_es, industries_list_call_to_action_text_pt, industries_list_call_to_action_text_pt_br, industries_list_call_to_action_text_ar, services_list_text, services_list_text_en_gb, services_list_text_de, services_list_text_ja, services_list_text_ru, services_list_text_zh_hans, services_list_text_fr, services_list_text_es, services_list_text_pt, services_list_text_pt_br, services_list_text_ar, services_column_one, services_column_one_en_gb, services_column_one_de, services_column_one_ja, services_column_one_ru, services_column_one_zh_hans, services_column_one_fr, services_column_one_es, services_column_one_pt, services_column_one_pt_br, services_column_one_ar, services_column_two, services_column_two_en_gb, services_column_two_de, services_column_two_ja, services_column_two_ru, services_column_two_zh_hans, services_column_two_fr, services_column_two_es, services_column_two_pt, services_column_two_pt_br, services_column_two_ar, services_column_three, services_column_three_en_gb, services_column_three_de, services_column_three_ja, services_column_three_ru, services_column_three_zh_hans, services_column_three_fr, services_column_three_es, services_column_three_pt, services_column_three_pt_br, services_column_three_ar, services_column_four, services_column_four_en_gb, services_column_four_de, services_column_four_ja, services_column_four_ru, services_column_four_zh_hans, services_column_four_fr, services_column_four_es, services_column_four_pt, services_column_four_pt_br, services_column_four_ar, hero_image_id, services_column_four_icon_id, services_column_four_icon_ar_id, services_column_four_icon_de_id, services_column_four_icon_en_gb_id, services_column_four_icon_es_id, services_column_four_icon_fr_id, services_column_four_icon_ja_id, services_column_four_icon_pt_id, services_column_four_icon_pt_br_id, services_column_four_icon_ru_id, services_column_four_icon_zh_hans_id, services_column_one_icon_id, services_column_one_icon_ar_id, services_column_one_icon_de_id, services_column_one_icon_en_gb_id, services_column_one_icon_es_id, services_column_one_icon_fr_id, services_column_one_icon_ja_id, services_column_one_icon_pt_id, services_column_one_icon_pt_br_id, services_column_one_icon_ru_id, services_column_one_icon_zh_hans_id, services_column_three_icon_id, services_column_three_icon_ar_id, services_column_three_icon_de_id, services_column_three_icon_en_gb_id, services_column_three_icon_es_id, services_column_three_icon_fr_id, services_column_three_icon_ja_id, services_column_three_icon_pt_id, services_column_three_icon_pt_br_id, services_column_three_icon_ru_id, services_column_three_icon_zh_hans_id, services_column_two_icon_id, services_column_two_icon_ar_id, services_column_two_icon_de_id, services_column_two_icon_en_gb_id, services_column_two_icon_es_id, services_column_two_icon_fr_id, services_column_two_icon_ja_id, services_column_two_icon_pt_id, services_column_two_icon_pt_br_id, services_column_two_icon_ru_id, services_column_two_icon_zh_hans_id, breadcrumbs_label, breadcrumbs_label_ar, breadcrumbs_label_de, breadcrumbs_label_en_gb, breadcrumbs_label_es, breadcrumbs_label_fr, breadcrumbs_label_ja, breadcrumbs_label_pt, breadcrumbs_label_pt_br, breadcrumbs_label_ru, breadcrumbs_label_zh_hans, mobile_hero_image_id, hero_image_caption, hero_image_caption_ar, hero_image_caption_de, hero_image_caption_en_gb, hero_image_caption_es, hero_image_caption_fr, hero_image_caption_ja, hero_image_caption_pt, hero_image_caption_pt_br, hero_image_caption_ru, hero_image_caption_zh_hans, service_name) FROM stdin;
\.


--
-- Data for Name: find_a_supplier_landingpagearticlesummary; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.find_a_supplier_landingpagearticlesummary (id, sort_order, industry_name, title, body, image_id, page_id, page_ar_id, page_de_id, page_en_gb_id, page_es_id, page_fr_id, page_ja_id, page_pt_id, page_pt_br_id, page_ru_id, page_zh_hans_id, video_media_id) FROM stdin;
\.


--
-- Data for Name: great_international_greatinternationalapp; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.great_international_greatinternationalapp (page_ptr_id, service_name) FROM stdin;
\.


--
-- Data for Name: great_international_internationalarticlelistingpage; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.great_international_internationalarticlelistingpage (page_ptr_id, service_name, landing_page_title, hero_teaser, list_teaser, hero_image_id) FROM stdin;
\.


--
-- Data for Name: great_international_internationalarticlelistingpage_tags; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.great_international_internationalarticlelistingpage_tags (id, internationalarticlelistingpage_id, tag_id) FROM stdin;
\.


--
-- Data for Name: great_international_internationalarticlepage; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.great_international_internationalarticlepage (page_ptr_id, service_name, article_title, article_teaser, article_body_text, article_image_id, related_page_one_id, related_page_three_id, related_page_two_id) FROM stdin;
\.


--
-- Data for Name: great_international_internationalarticlepage_tags; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.great_international_internationalarticlepage_tags (id, internationalarticlepage_id, tag_id) FROM stdin;
\.


--
-- Data for Name: great_international_internationalcampaignpage; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.great_international_internationalcampaignpage (page_ptr_id, service_name, campaign_heading, section_one_heading, section_one_intro, selling_point_one_heading, selling_point_one_content, selling_point_two_heading, selling_point_two_content, selling_point_three_heading, selling_point_three_content, section_one_contact_button_url, section_one_contact_button_text, section_two_heading, section_two_intro, section_two_contact_button_url, section_two_contact_button_text, related_content_heading, related_content_intro, cta_box_message, cta_box_button_url, cta_box_button_text, campaign_hero_image_id, related_page_one_id, related_page_three_id, related_page_two_id, section_one_image_id, section_two_image_id, selling_point_one_icon_id, selling_point_three_icon_id, selling_point_two_icon_id, campaign_teaser) FROM stdin;
\.


--
-- Data for Name: great_international_internationalcampaignpage_tags; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.great_international_internationalcampaignpage_tags (id, internationalcampaignpage_id, tag_id) FROM stdin;
\.


--
-- Data for Name: great_international_internationalhomepage; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.great_international_internationalhomepage (page_ptr_id, service_name, tariffs_title, tariffs_description, tariffs_link, news_title, tariffs_image_id, related_page_one_id, related_page_three_id, related_page_two_id) FROM stdin;
\.


--
-- Data for Name: great_international_internationallocalisedfolderpage; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.great_international_internationallocalisedfolderpage (page_ptr_id, service_name) FROM stdin;
\.


--
-- Data for Name: great_international_internationalregionpage; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.great_international_internationalregionpage (page_ptr_id, service_name) FROM stdin;
\.


--
-- Data for Name: great_international_internationalregionpage_tags; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.great_international_internationalregionpage_tags (id, internationalregionpage_id, tag_id) FROM stdin;
\.


--
-- Data for Name: great_international_internationalsectorpage; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.great_international_internationalsectorpage (page_ptr_id, service_name, heading, sub_heading, heading_teaser, section_one_body, statistic_1_number, statistic_1_heading, statistic_1_smallprint, statistic_2_number, statistic_2_heading, statistic_2_smallprint, statistic_3_number, statistic_3_heading, statistic_3_smallprint, statistic_4_number, statistic_4_heading, statistic_4_smallprint, statistic_5_number, statistic_5_heading, statistic_5_smallprint, statistic_6_number, statistic_6_heading, statistic_6_smallprint, section_two_heading, section_two_teaser, section_two_subsection_one_heading, section_two_subsection_one_body, section_two_subsection_two_heading, section_two_subsection_two_body, section_two_subsection_three_heading, section_two_subsection_three_body, case_study_title, case_study_description, case_study_cta_text, case_study_cta_url, section_three_heading, section_three_teaser, section_three_subsection_one_heading, section_three_subsection_one_teaser, section_three_subsection_one_body, section_three_subsection_two_heading, section_three_subsection_two_teaser, section_three_subsection_two_body, next_steps_heading, next_steps_description, case_study_image_id, hero_image_id, related_page_one_id, related_page_three_id, related_page_two_id, section_one_image_id, section_two_subsection_one_icon_id, section_two_subsection_three_icon_id, section_two_subsection_two_icon_id) FROM stdin;
\.


--
-- Data for Name: great_international_internationaltopiclandingpage; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.great_international_internationaltopiclandingpage (page_ptr_id, service_name, landing_page_title, hero_teaser, hero_image_id) FROM stdin;
\.


--
-- Data for Name: great_international_internationaltopiclandingpage_tags; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.great_international_internationaltopiclandingpage_tags (id, internationaltopiclandingpage_id, tag_id) FROM stdin;
\.


--
-- Data for Name: health_check_db_testmodel; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.health_check_db_testmodel (id, title) FROM stdin;
\.


--
-- Data for Name: invest_highpotentialopportunitydetailpage; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.invest_highpotentialopportunitydetailpage (page_ptr_id, service_name, breadcrumbs_label, heading, contact_proposition, contact_button, proposition_one, opportunity_list_title, opportunity_list_item_one, opportunity_list_item_two, opportunity_list_item_three, proposition_two, proposition_two_list_item_one, proposition_two_list_item_two, proposition_two_list_item_three, competitive_advantages_title, competitive_advantages_list_item_one, competitive_advantages_list_item_two, competitive_advantages_list_item_three, testimonial, companies_list_text, case_study_list_title, case_study_one_text, case_study_two_text, case_study_three_text, case_study_four_text, case_study_four_image_id, case_study_one_image_id, case_study_three_image_id, case_study_two_image_id, companies_list_item_image_eight_id, companies_list_item_image_five_id, companies_list_item_image_four_id, companies_list_item_image_one_id, companies_list_item_image_seven_id, companies_list_item_image_six_id, companies_list_item_image_three_id, companies_list_item_image_two_id, hero_image_id, opportunity_list_image_id, proposition_one_image_id, proposition_one_video_id, proposition_two_image_id, proposition_two_video_id, competitive_advantages_list_item_one_icon_id, competitive_advantages_list_item_three_icon_id, competitive_advantages_list_item_two_icon_id, other_opportunities_title, summary_image_id, pdf_document_id, testimonial_background_id) FROM stdin;
\.


--
-- Data for Name: invest_highpotentialopportunityformpage; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.invest_highpotentialopportunityformpage (page_ptr_id, service_name, comment_help_text, comment_label, company_name_help_text, company_name_label, company_size_help_text, company_size_label, country_help_text, country_label, email_address_help_text, email_address_label, full_name_help_text, full_name_label, opportunities_help_text, opportunities_label, phone_number_help_text, phone_number_label, role_in_company_help_text, role_in_company_label, website_url_help_text, website_url_label, heading, sub_heading, breadcrumbs_label) FROM stdin;
\.


--
-- Data for Name: invest_highpotentialopportunityformsuccesspage; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.invest_highpotentialopportunityformsuccesspage (page_ptr_id, service_name, breadcrumbs_label, heading, sub_heading, next_steps_title, next_steps_body, documents_title, documents_body) FROM stdin;
\.


--
-- Data for Name: invest_infopage; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.invest_infopage (page_ptr_id, content, content_en_gb, content_de, content_ja, content_ru, content_zh_hans, content_fr, content_es, content_pt, content_pt_br, content_ar, service_name) FROM stdin;
\.


--
-- Data for Name: invest_investapp; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.invest_investapp (page_ptr_id, service_name) FROM stdin;
\.


--
-- Data for Name: invest_investhomepage; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.invest_investhomepage (page_ptr_id, heading, heading_en_gb, heading_de, heading_ja, heading_ru, heading_zh_hans, heading_fr, heading_es, heading_pt, heading_pt_br, heading_ar, sub_heading, sub_heading_en_gb, sub_heading_de, sub_heading_ja, sub_heading_ru, sub_heading_zh_hans, sub_heading_fr, sub_heading_es, sub_heading_pt, sub_heading_pt_br, sub_heading_ar, sector_title, sector_title_en_gb, sector_title_de, sector_title_ja, sector_title_ru, sector_title_zh_hans, sector_title_fr, sector_title_es, sector_title_pt, sector_title_pt_br, sector_title_ar, sector_button_text, sector_button_text_en_gb, sector_button_text_de, sector_button_text_ja, sector_button_text_ru, sector_button_text_zh_hans, sector_button_text_fr, sector_button_text_es, sector_button_text_pt, sector_button_text_pt_br, sector_button_text_ar, setup_guide_title, setup_guide_title_en_gb, setup_guide_title_de, setup_guide_title_ja, setup_guide_title_ru, setup_guide_title_zh_hans, setup_guide_title_fr, setup_guide_title_es, setup_guide_title_pt, setup_guide_title_pt_br, setup_guide_title_ar, setup_guide_lead_in, setup_guide_lead_in_en_gb, setup_guide_lead_in_de, setup_guide_lead_in_ja, setup_guide_lead_in_ru, setup_guide_lead_in_zh_hans, setup_guide_lead_in_fr, setup_guide_lead_in_es, setup_guide_lead_in_pt, setup_guide_lead_in_pt_br, setup_guide_lead_in_ar, how_we_help_title, how_we_help_title_en_gb, how_we_help_title_de, how_we_help_title_ja, how_we_help_title_ru, how_we_help_title_zh_hans, how_we_help_title_fr, how_we_help_title_es, how_we_help_title_pt, how_we_help_title_pt_br, how_we_help_title_ar, how_we_help_lead_in, how_we_help_lead_in_en_gb, how_we_help_lead_in_de, how_we_help_lead_in_ja, how_we_help_lead_in_ru, how_we_help_lead_in_zh_hans, how_we_help_lead_in_fr, how_we_help_lead_in_es, how_we_help_lead_in_pt, how_we_help_lead_in_pt_br, how_we_help_lead_in_ar, hero_image_id, how_we_help_icon_five_id, how_we_help_icon_five_ar_id, how_we_help_icon_five_de_id, how_we_help_icon_five_en_gb_id, how_we_help_icon_five_es_id, how_we_help_icon_five_fr_id, how_we_help_icon_five_ja_id, how_we_help_icon_five_pt_id, how_we_help_icon_five_pt_br_id, how_we_help_icon_five_ru_id, how_we_help_icon_five_zh_hans_id, how_we_help_icon_four_id, how_we_help_icon_four_ar_id, how_we_help_icon_four_de_id, how_we_help_icon_four_en_gb_id, how_we_help_icon_four_es_id, how_we_help_icon_four_fr_id, how_we_help_icon_four_ja_id, how_we_help_icon_four_pt_id, how_we_help_icon_four_pt_br_id, how_we_help_icon_four_ru_id, how_we_help_icon_four_zh_hans_id, how_we_help_icon_one_id, how_we_help_icon_one_ar_id, how_we_help_icon_one_de_id, how_we_help_icon_one_en_gb_id, how_we_help_icon_one_es_id, how_we_help_icon_one_fr_id, how_we_help_icon_one_ja_id, how_we_help_icon_one_pt_id, how_we_help_icon_one_pt_br_id, how_we_help_icon_one_ru_id, how_we_help_icon_one_zh_hans_id, how_we_help_icon_three_id, how_we_help_icon_three_ar_id, how_we_help_icon_three_de_id, how_we_help_icon_three_en_gb_id, how_we_help_icon_three_es_id, how_we_help_icon_three_fr_id, how_we_help_icon_three_ja_id, how_we_help_icon_three_pt_id, how_we_help_icon_three_pt_br_id, how_we_help_icon_three_ru_id, how_we_help_icon_three_zh_hans_id, how_we_help_icon_two_id, how_we_help_icon_two_ar_id, how_we_help_icon_two_de_id, how_we_help_icon_two_en_gb_id, how_we_help_icon_two_es_id, how_we_help_icon_two_fr_id, how_we_help_icon_two_ja_id, how_we_help_icon_two_pt_id, how_we_help_icon_two_pt_br_id, how_we_help_icon_two_ru_id, how_we_help_icon_two_zh_hans_id, how_we_help_text_five, how_we_help_text_five_ar, how_we_help_text_five_de, how_we_help_text_five_en_gb, how_we_help_text_five_es, how_we_help_text_five_fr, how_we_help_text_five_ja, how_we_help_text_five_pt, how_we_help_text_five_pt_br, how_we_help_text_five_ru, how_we_help_text_five_zh_hans, how_we_help_text_four, how_we_help_text_four_ar, how_we_help_text_four_de, how_we_help_text_four_en_gb, how_we_help_text_four_es, how_we_help_text_four_fr, how_we_help_text_four_ja, how_we_help_text_four_pt, how_we_help_text_four_pt_br, how_we_help_text_four_ru, how_we_help_text_four_zh_hans, how_we_help_text_one, how_we_help_text_one_ar, how_we_help_text_one_de, how_we_help_text_one_en_gb, how_we_help_text_one_es, how_we_help_text_one_fr, how_we_help_text_one_ja, how_we_help_text_one_pt, how_we_help_text_one_pt_br, how_we_help_text_one_ru, how_we_help_text_one_zh_hans, how_we_help_text_six, how_we_help_text_six_ar, how_we_help_text_six_de, how_we_help_text_six_en_gb, how_we_help_text_six_es, how_we_help_text_six_fr, how_we_help_text_six_ja, how_we_help_text_six_pt, how_we_help_text_six_pt_br, how_we_help_text_six_ru, how_we_help_text_six_zh_hans, how_we_help_text_three, how_we_help_text_three_ar, how_we_help_text_three_de, how_we_help_text_three_en_gb, how_we_help_text_three_es, how_we_help_text_three_fr, how_we_help_text_three_ja, how_we_help_text_three_pt, how_we_help_text_three_pt_br, how_we_help_text_three_ru, how_we_help_text_three_zh_hans, how_we_help_text_two, how_we_help_text_two_ar, how_we_help_text_two_de, how_we_help_text_two_en_gb, how_we_help_text_two_es, how_we_help_text_two_fr, how_we_help_text_two_ja, how_we_help_text_two_pt, how_we_help_text_two_pt_br, how_we_help_text_two_ru, how_we_help_text_two_zh_hans, subsection_content_five, subsection_content_five_ar, subsection_content_five_de, subsection_content_five_en_gb, subsection_content_five_es, subsection_content_five_fr, subsection_content_five_ja, subsection_content_five_pt, subsection_content_five_pt_br, subsection_content_five_ru, subsection_content_five_zh_hans, subsection_content_four, subsection_content_four_ar, subsection_content_four_de, subsection_content_four_en_gb, subsection_content_four_es, subsection_content_four_fr, subsection_content_four_ja, subsection_content_four_pt, subsection_content_four_pt_br, subsection_content_four_ru, subsection_content_four_zh_hans, subsection_content_one, subsection_content_one_ar, subsection_content_one_de, subsection_content_one_en_gb, subsection_content_one_es, subsection_content_one_fr, subsection_content_one_ja, subsection_content_one_pt, subsection_content_one_pt_br, subsection_content_one_ru, subsection_content_one_zh_hans, subsection_content_seven, subsection_content_seven_ar, subsection_content_seven_de, subsection_content_seven_en_gb, subsection_content_seven_es, subsection_content_seven_fr, subsection_content_seven_ja, subsection_content_seven_pt, subsection_content_seven_pt_br, subsection_content_seven_ru, subsection_content_seven_zh_hans, subsection_content_six, subsection_content_six_ar, subsection_content_six_de, subsection_content_six_en_gb, subsection_content_six_es, subsection_content_six_fr, subsection_content_six_ja, subsection_content_six_pt, subsection_content_six_pt_br, subsection_content_six_ru, subsection_content_six_zh_hans, subsection_content_three, subsection_content_three_ar, subsection_content_three_de, subsection_content_three_en_gb, subsection_content_three_es, subsection_content_three_fr, subsection_content_three_ja, subsection_content_three_pt, subsection_content_three_pt_br, subsection_content_three_ru, subsection_content_three_zh_hans, subsection_content_two, subsection_content_two_ar, subsection_content_two_de, subsection_content_two_en_gb, subsection_content_two_es, subsection_content_two_fr, subsection_content_two_ja, subsection_content_two_pt, subsection_content_two_pt_br, subsection_content_two_ru, subsection_content_two_zh_hans, subsection_title_five, subsection_title_five_ar, subsection_title_five_de, subsection_title_five_en_gb, subsection_title_five_es, subsection_title_five_fr, subsection_title_five_ja, subsection_title_five_pt, subsection_title_five_pt_br, subsection_title_five_ru, subsection_title_five_zh_hans, subsection_title_four, subsection_title_four_ar, subsection_title_four_de, subsection_title_four_en_gb, subsection_title_four_es, subsection_title_four_fr, subsection_title_four_ja, subsection_title_four_pt, subsection_title_four_pt_br, subsection_title_four_ru, subsection_title_four_zh_hans, subsection_title_one, subsection_title_one_ar, subsection_title_one_de, subsection_title_one_en_gb, subsection_title_one_es, subsection_title_one_fr, subsection_title_one_ja, subsection_title_one_pt, subsection_title_one_pt_br, subsection_title_one_ru, subsection_title_one_zh_hans, subsection_title_seven, subsection_title_seven_ar, subsection_title_seven_de, subsection_title_seven_en_gb, subsection_title_seven_es, subsection_title_seven_fr, subsection_title_seven_ja, subsection_title_seven_pt, subsection_title_seven_pt_br, subsection_title_seven_ru, subsection_title_seven_zh_hans, subsection_title_six, subsection_title_six_ar, subsection_title_six_de, subsection_title_six_en_gb, subsection_title_six_es, subsection_title_six_fr, subsection_title_six_ja, subsection_title_six_pt, subsection_title_six_pt_br, subsection_title_six_ru, subsection_title_six_zh_hans, subsection_title_three, subsection_title_three_ar, subsection_title_three_de, subsection_title_three_en_gb, subsection_title_three_es, subsection_title_three_fr, subsection_title_three_ja, subsection_title_three_pt, subsection_title_three_pt_br, subsection_title_three_ru, subsection_title_three_zh_hans, subsection_title_two, subsection_title_two_ar, subsection_title_two_de, subsection_title_two_en_gb, subsection_title_two_es, subsection_title_two_fr, subsection_title_two_ja, subsection_title_two_pt, subsection_title_two_pt_br, subsection_title_two_ru, subsection_title_two_zh_hans, service_name) FROM stdin;
\.


--
-- Data for Name: invest_regionlandingpage; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.invest_regionlandingpage (page_ptr_id, heading, heading_en_gb, heading_de, heading_ja, heading_ru, heading_zh_hans, heading_fr, heading_es, heading_pt, heading_pt_br, heading_ar, hero_image_id, service_name) FROM stdin;
\.


--
-- Data for Name: invest_sectorlandingpage; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.invest_sectorlandingpage (page_ptr_id, heading, heading_en_gb, heading_de, heading_ja, heading_ru, heading_zh_hans, heading_fr, heading_es, heading_pt, heading_pt_br, heading_ar, hero_image_id, service_name) FROM stdin;
\.


--
-- Data for Name: invest_sectorpage; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.invest_sectorpage (page_ptr_id, featured, description, description_en_gb, description_de, description_ja, description_ru, description_zh_hans, description_fr, description_es, description_pt, description_pt_br, description_ar, heading, heading_en_gb, heading_de, heading_ja, heading_ru, heading_zh_hans, heading_fr, heading_es, heading_pt, heading_pt_br, heading_ar, hero_image_id, pullout_stat, pullout_stat_ar, pullout_stat_de, pullout_stat_en_gb, pullout_stat_es, pullout_stat_fr, pullout_stat_ja, pullout_stat_pt, pullout_stat_pt_br, pullout_stat_ru, pullout_stat_text, pullout_stat_text_ar, pullout_stat_text_de, pullout_stat_text_en_gb, pullout_stat_text_es, pullout_stat_text_fr, pullout_stat_text_ja, pullout_stat_text_pt, pullout_stat_text_pt_br, pullout_stat_text_ru, pullout_stat_text_zh_hans, pullout_stat_zh_hans, pullout_text, pullout_text_ar, pullout_text_de, pullout_text_en_gb, pullout_text_es, pullout_text_fr, pullout_text_ja, pullout_text_pt, pullout_text_pt_br, pullout_text_ru, pullout_text_zh_hans, subsection_content_five, subsection_content_five_ar, subsection_content_five_de, subsection_content_five_en_gb, subsection_content_five_es, subsection_content_five_fr, subsection_content_five_ja, subsection_content_five_pt, subsection_content_five_pt_br, subsection_content_five_ru, subsection_content_five_zh_hans, subsection_content_four, subsection_content_four_ar, subsection_content_four_de, subsection_content_four_en_gb, subsection_content_four_es, subsection_content_four_fr, subsection_content_four_ja, subsection_content_four_pt, subsection_content_four_pt_br, subsection_content_four_ru, subsection_content_four_zh_hans, subsection_content_one, subsection_content_one_ar, subsection_content_one_de, subsection_content_one_en_gb, subsection_content_one_es, subsection_content_one_fr, subsection_content_one_ja, subsection_content_one_pt, subsection_content_one_pt_br, subsection_content_one_ru, subsection_content_one_zh_hans, subsection_content_seven, subsection_content_seven_ar, subsection_content_seven_de, subsection_content_seven_en_gb, subsection_content_seven_es, subsection_content_seven_fr, subsection_content_seven_ja, subsection_content_seven_pt, subsection_content_seven_pt_br, subsection_content_seven_ru, subsection_content_seven_zh_hans, subsection_content_six, subsection_content_six_ar, subsection_content_six_de, subsection_content_six_en_gb, subsection_content_six_es, subsection_content_six_fr, subsection_content_six_ja, subsection_content_six_pt, subsection_content_six_pt_br, subsection_content_six_ru, subsection_content_six_zh_hans, subsection_content_three, subsection_content_three_ar, subsection_content_three_de, subsection_content_three_en_gb, subsection_content_three_es, subsection_content_three_fr, subsection_content_three_ja, subsection_content_three_pt, subsection_content_three_pt_br, subsection_content_three_ru, subsection_content_three_zh_hans, subsection_content_two, subsection_content_two_ar, subsection_content_two_de, subsection_content_two_en_gb, subsection_content_two_es, subsection_content_two_fr, subsection_content_two_ja, subsection_content_two_pt, subsection_content_two_pt_br, subsection_content_two_ru, subsection_content_two_zh_hans, subsection_map_five_id, subsection_map_five_ar_id, subsection_map_five_de_id, subsection_map_five_en_gb_id, subsection_map_five_es_id, subsection_map_five_fr_id, subsection_map_five_ja_id, subsection_map_five_pt_id, subsection_map_five_pt_br_id, subsection_map_five_ru_id, subsection_map_five_zh_hans_id, subsection_map_four_id, subsection_map_four_ar_id, subsection_map_four_de_id, subsection_map_four_en_gb_id, subsection_map_four_es_id, subsection_map_four_fr_id, subsection_map_four_ja_id, subsection_map_four_pt_id, subsection_map_four_pt_br_id, subsection_map_four_ru_id, subsection_map_four_zh_hans_id, subsection_map_one_id, subsection_map_one_ar_id, subsection_map_one_de_id, subsection_map_one_en_gb_id, subsection_map_one_es_id, subsection_map_one_fr_id, subsection_map_one_ja_id, subsection_map_one_pt_id, subsection_map_one_pt_br_id, subsection_map_one_ru_id, subsection_map_one_zh_hans_id, subsection_map_seven_id, subsection_map_seven_ar_id, subsection_map_seven_de_id, subsection_map_seven_en_gb_id, subsection_map_seven_es_id, subsection_map_seven_fr_id, subsection_map_seven_ja_id, subsection_map_seven_pt_id, subsection_map_seven_pt_br_id, subsection_map_seven_ru_id, subsection_map_seven_zh_hans_id, subsection_map_six_id, subsection_map_six_ar_id, subsection_map_six_de_id, subsection_map_six_en_gb_id, subsection_map_six_es_id, subsection_map_six_fr_id, subsection_map_six_ja_id, subsection_map_six_pt_id, subsection_map_six_pt_br_id, subsection_map_six_ru_id, subsection_map_six_zh_hans_id, subsection_map_three_id, subsection_map_three_ar_id, subsection_map_three_de_id, subsection_map_three_en_gb_id, subsection_map_three_es_id, subsection_map_three_fr_id, subsection_map_three_ja_id, subsection_map_three_pt_id, subsection_map_three_pt_br_id, subsection_map_three_ru_id, subsection_map_three_zh_hans_id, subsection_map_two_id, subsection_map_two_ar_id, subsection_map_two_de_id, subsection_map_two_en_gb_id, subsection_map_two_es_id, subsection_map_two_fr_id, subsection_map_two_ja_id, subsection_map_two_pt_id, subsection_map_two_pt_br_id, subsection_map_two_ru_id, subsection_map_two_zh_hans_id, subsection_title_five, subsection_title_five_ar, subsection_title_five_de, subsection_title_five_en_gb, subsection_title_five_es, subsection_title_five_fr, subsection_title_five_ja, subsection_title_five_pt, subsection_title_five_pt_br, subsection_title_five_ru, subsection_title_five_zh_hans, subsection_title_four, subsection_title_four_ar, subsection_title_four_de, subsection_title_four_en_gb, subsection_title_four_es, subsection_title_four_fr, subsection_title_four_ja, subsection_title_four_pt, subsection_title_four_pt_br, subsection_title_four_ru, subsection_title_four_zh_hans, subsection_title_one, subsection_title_one_ar, subsection_title_one_de, subsection_title_one_en_gb, subsection_title_one_es, subsection_title_one_fr, subsection_title_one_ja, subsection_title_one_pt, subsection_title_one_pt_br, subsection_title_one_ru, subsection_title_one_zh_hans, subsection_title_seven, subsection_title_seven_ar, subsection_title_seven_de, subsection_title_seven_en_gb, subsection_title_seven_es, subsection_title_seven_fr, subsection_title_seven_ja, subsection_title_seven_pt, subsection_title_seven_pt_br, subsection_title_seven_ru, subsection_title_seven_zh_hans, subsection_title_six, subsection_title_six_ar, subsection_title_six_de, subsection_title_six_en_gb, subsection_title_six_es, subsection_title_six_fr, subsection_title_six_ja, subsection_title_six_pt, subsection_title_six_pt_br, subsection_title_six_ru, subsection_title_six_zh_hans, subsection_title_three, subsection_title_three_ar, subsection_title_three_de, subsection_title_three_en_gb, subsection_title_three_es, subsection_title_three_fr, subsection_title_three_ja, subsection_title_three_pt, subsection_title_three_pt_br, subsection_title_three_ru, subsection_title_three_zh_hans, subsection_title_two, subsection_title_two_ar, subsection_title_two_de, subsection_title_two_en_gb, subsection_title_two_es, subsection_title_two_fr, subsection_title_two_ja, subsection_title_two_pt, subsection_title_two_pt_br, subsection_title_two_ru, subsection_title_two_zh_hans, service_name) FROM stdin;
\.


--
-- Data for Name: invest_setupguidelandingpage; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.invest_setupguidelandingpage (page_ptr_id, heading, heading_en_gb, heading_de, heading_ja, heading_ru, heading_zh_hans, heading_fr, heading_es, heading_pt, heading_pt_br, heading_ar, sub_heading, sub_heading_en_gb, sub_heading_de, sub_heading_ja, sub_heading_ru, sub_heading_zh_hans, sub_heading_fr, sub_heading_es, sub_heading_pt, sub_heading_pt_br, sub_heading_ar, lead_in, lead_in_en_gb, lead_in_de, lead_in_ja, lead_in_ru, lead_in_zh_hans, lead_in_fr, lead_in_es, lead_in_pt, lead_in_pt_br, lead_in_ar, service_name) FROM stdin;
\.


--
-- Data for Name: invest_setupguidepage; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.invest_setupguidepage (page_ptr_id, description, description_en_gb, description_de, description_ja, description_ru, description_zh_hans, description_fr, description_es, description_pt, description_pt_br, description_ar, heading, heading_en_gb, heading_de, heading_ja, heading_ru, heading_zh_hans, heading_fr, heading_es, heading_pt, heading_pt_br, heading_ar, sub_heading, sub_heading_en_gb, sub_heading_de, sub_heading_ja, sub_heading_ru, sub_heading_zh_hans, sub_heading_fr, sub_heading_es, sub_heading_pt, sub_heading_pt_br, sub_heading_ar, subsection_content_five, subsection_content_five_ar, subsection_content_five_de, subsection_content_five_en_gb, subsection_content_five_es, subsection_content_five_fr, subsection_content_five_ja, subsection_content_five_pt, subsection_content_five_pt_br, subsection_content_five_ru, subsection_content_five_zh_hans, subsection_content_four, subsection_content_four_ar, subsection_content_four_de, subsection_content_four_en_gb, subsection_content_four_es, subsection_content_four_fr, subsection_content_four_ja, subsection_content_four_pt, subsection_content_four_pt_br, subsection_content_four_ru, subsection_content_four_zh_hans, subsection_content_one, subsection_content_one_ar, subsection_content_one_de, subsection_content_one_en_gb, subsection_content_one_es, subsection_content_one_fr, subsection_content_one_ja, subsection_content_one_pt, subsection_content_one_pt_br, subsection_content_one_ru, subsection_content_one_zh_hans, subsection_content_seven, subsection_content_seven_ar, subsection_content_seven_de, subsection_content_seven_en_gb, subsection_content_seven_es, subsection_content_seven_fr, subsection_content_seven_ja, subsection_content_seven_pt, subsection_content_seven_pt_br, subsection_content_seven_ru, subsection_content_seven_zh_hans, subsection_content_six, subsection_content_six_ar, subsection_content_six_de, subsection_content_six_en_gb, subsection_content_six_es, subsection_content_six_fr, subsection_content_six_ja, subsection_content_six_pt, subsection_content_six_pt_br, subsection_content_six_ru, subsection_content_six_zh_hans, subsection_content_three, subsection_content_three_ar, subsection_content_three_de, subsection_content_three_en_gb, subsection_content_three_es, subsection_content_three_fr, subsection_content_three_ja, subsection_content_three_pt, subsection_content_three_pt_br, subsection_content_three_ru, subsection_content_three_zh_hans, subsection_content_two, subsection_content_two_ar, subsection_content_two_de, subsection_content_two_en_gb, subsection_content_two_es, subsection_content_two_fr, subsection_content_two_ja, subsection_content_two_pt, subsection_content_two_pt_br, subsection_content_two_ru, subsection_content_two_zh_hans, subsection_title_five, subsection_title_five_ar, subsection_title_five_de, subsection_title_five_en_gb, subsection_title_five_es, subsection_title_five_fr, subsection_title_five_ja, subsection_title_five_pt, subsection_title_five_pt_br, subsection_title_five_ru, subsection_title_five_zh_hans, subsection_title_four, subsection_title_four_ar, subsection_title_four_de, subsection_title_four_en_gb, subsection_title_four_es, subsection_title_four_fr, subsection_title_four_ja, subsection_title_four_pt, subsection_title_four_pt_br, subsection_title_four_ru, subsection_title_four_zh_hans, subsection_title_one, subsection_title_one_ar, subsection_title_one_de, subsection_title_one_en_gb, subsection_title_one_es, subsection_title_one_fr, subsection_title_one_ja, subsection_title_one_pt, subsection_title_one_pt_br, subsection_title_one_ru, subsection_title_one_zh_hans, subsection_title_seven, subsection_title_seven_ar, subsection_title_seven_de, subsection_title_seven_en_gb, subsection_title_seven_es, subsection_title_seven_fr, subsection_title_seven_ja, subsection_title_seven_pt, subsection_title_seven_pt_br, subsection_title_seven_ru, subsection_title_seven_zh_hans, subsection_title_six, subsection_title_six_ar, subsection_title_six_de, subsection_title_six_en_gb, subsection_title_six_es, subsection_title_six_fr, subsection_title_six_ja, subsection_title_six_pt, subsection_title_six_pt_br, subsection_title_six_ru, subsection_title_six_zh_hans, subsection_title_three, subsection_title_three_ar, subsection_title_three_de, subsection_title_three_en_gb, subsection_title_three_es, subsection_title_three_fr, subsection_title_three_ja, subsection_title_three_pt, subsection_title_three_pt_br, subsection_title_three_ru, subsection_title_three_zh_hans, subsection_title_two, subsection_title_two_ar, subsection_title_two_de, subsection_title_two_en_gb, subsection_title_two_es, subsection_title_two_fr, subsection_title_two_ja, subsection_title_two_pt, subsection_title_two_pt_br, subsection_title_two_ru, subsection_title_two_zh_hans, service_name) FROM stdin;
\.


--
-- Data for Name: taggit_tag; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.taggit_tag (id, name, slug) FROM stdin;
\.


--
-- Data for Name: taggit_taggeditem; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.taggit_taggeditem (id, object_id, content_type_id, tag_id) FROM stdin;
\.


--
-- Data for Name: wagtailcore_collection; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_collection (id, path, depth, numchild, name) FROM stdin;
1	0001	1	0	Root
\.


--
-- Data for Name: wagtailcore_collectionviewrestriction; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_collectionviewrestriction (id, restriction_type, password, collection_id) FROM stdin;
\.


--
-- Data for Name: wagtailcore_collectionviewrestriction_groups; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_collectionviewrestriction_groups (id, collectionviewrestriction_id, group_id) FROM stdin;
\.


--
-- Data for Name: wagtailcore_groupcollectionpermission; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_groupcollectionpermission (id, collection_id, group_id, permission_id) FROM stdin;
1	1	1	1
2	1	2	1
3	1	1	2
4	1	2	2
5	1	1	4
6	1	2	4
7	1	1	5
8	1	2	5
9	1	1	7
10	1	2	7
11	1	1	8
12	1	2	8
\.


--
-- Data for Name: wagtailcore_grouppagepermission; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_grouppagepermission (id, permission_type, group_id, page_id) FROM stdin;
1	add	1	1
2	edit	1	1
3	publish	1	1
4	add	2	1
5	edit	2	1
6	lock	1	1
\.


--
-- Data for Name: wagtailcore_page; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_page (id, path, depth, numchild, title, slug, live, has_unpublished_changes, url_path, seo_title, show_in_menus, search_description, go_live_at, expire_at, expired, content_type_id, owner_id, locked, latest_revision_created_at, first_published_at, live_revision_id, last_published_at, draft_title, seo_title_en_gb, seo_title_de, seo_title_ja, seo_title_ru, seo_title_zh_hans, seo_title_fr, seo_title_es, seo_title_pt, seo_title_pt_br, seo_title_ar, title_en_gb, title_de, title_ja, title_ru, title_zh_hans, title_fr, title_es, title_pt, title_pt_br, title_ar, search_description_en_gb, search_description_de, search_description_ja, search_description_ru, search_description_zh_hans, search_description_fr, search_description_es, search_description_pt, search_description_pt_br, search_description_ar) FROM stdin;
1	0001	1	1	Root	root	t	f	/		f		\N	\N	f	1	\N	f	\N	\N	\N	\N	Root	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
2	00010001	2	0	Welcome to your new Wagtail site!	home	t	f	/home/		f		\N	\N	f	1	\N	f	\N	\N	\N	\N	Welcome to your new Wagtail site!	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
\.


--
-- Data for Name: wagtailcore_pagerevision; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_pagerevision (id, submitted_for_moderation, created_at, content_json, approved_go_live_at, page_id, user_id) FROM stdin;
\.


--
-- Data for Name: wagtailcore_pageviewrestriction; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_pageviewrestriction (id, password, page_id, restriction_type) FROM stdin;
\.


--
-- Data for Name: wagtailcore_pageviewrestriction_groups; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_pageviewrestriction_groups (id, pageviewrestriction_id, group_id) FROM stdin;
\.


--
-- Data for Name: wagtailcore_site; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailcore_site (id, hostname, port, is_default_site, root_page_id, site_name) FROM stdin;
1	localhost	80	t	2	\N
\.


--
-- Data for Name: wagtaildocs_document; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtaildocs_document (id, title, file, created_at, uploaded_by_user_id, collection_id, file_size) FROM stdin;
\.


--
-- Data for Name: wagtailembeds_embed; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailembeds_embed (id, url, max_width, type, html, title, author_name, provider_name, thumbnail_url, width, height, last_updated) FROM stdin;
\.


--
-- Data for Name: wagtailforms_formsubmission; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailforms_formsubmission (id, form_data, submit_time, page_id) FROM stdin;
\.


--
-- Data for Name: wagtailimages_image; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailimages_image (id, title, file, width, height, created_at, focal_point_x, focal_point_y, focal_point_width, focal_point_height, uploaded_by_user_id, file_size, collection_id, file_hash) FROM stdin;
\.


--
-- Data for Name: wagtailimages_rendition; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailimages_rendition (id, file, width, height, focal_point_key, image_id, filter_spec) FROM stdin;
\.


--
-- Data for Name: wagtailmedia_media; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailmedia_media (id, title, file, type, duration, width, height, thumbnail, created_at, collection_id, uploaded_by_user_id) FROM stdin;
\.


--
-- Data for Name: wagtailsearch_editorspick; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailsearch_editorspick (id, sort_order, description, page_id, query_id) FROM stdin;
\.


--
-- Data for Name: wagtailsearch_query; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailsearch_query (id, query_string) FROM stdin;
\.


--
-- Data for Name: wagtailsearch_querydailyhits; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailsearch_querydailyhits (id, date, hits, query_id) FROM stdin;
\.


--
-- Data for Name: wagtailusers_userprofile; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.wagtailusers_userprofile (id, submitted_notifications, approved_notifications, rejected_notifications, user_id, preferred_language, current_time_zone, avatar) FROM stdin;
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 2, true);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 20, true);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 253, true);


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 1, false);


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);


--
-- Name: core_breadcrumb_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.core_breadcrumb_id_seq', 1, false);


--
-- Name: core_documenthash_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.core_documenthash_id_seq', 1, false);


--
-- Name: core_imagehash_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.core_imagehash_id_seq', 1, false);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 85, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 221, true);


--
-- Name: export_readiness_articlepage_tags_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.export_readiness_articlepage_tags_id_seq', 1, false);


--
-- Name: export_readiness_tag_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.export_readiness_tag_id_seq', 1, false);


--
-- Name: find_a_supplier_industrypagearticlesummary_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.find_a_supplier_industrypagearticlesummary_id_seq', 1, false);


--
-- Name: find_a_supplier_landingpagearticlesummary_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.find_a_supplier_landingpagearticlesummary_id_seq', 1, false);


--
-- Name: great_international_internationalarticlelistingpage_tags_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.great_international_internationalarticlelistingpage_tags_id_seq', 1, false);


--
-- Name: great_international_internationalarticlepage_tags_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.great_international_internationalarticlepage_tags_id_seq', 1, false);


--
-- Name: great_international_internationalcampaignpage_tags_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.great_international_internationalcampaignpage_tags_id_seq', 1, false);


--
-- Name: great_international_internationalregionpages_tags_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.great_international_internationalregionpages_tags_id_seq', 1, false);


--
-- Name: great_international_internationaltopiclandingpage_tags_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.great_international_internationaltopiclandingpage_tags_id_seq', 1, false);


--
-- Name: health_check_db_testmodel_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.health_check_db_testmodel_id_seq', 1, false);


--
-- Name: taggit_tag_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.taggit_tag_id_seq', 1, false);


--
-- Name: taggit_taggeditem_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.taggit_taggeditem_id_seq', 1, false);


--
-- Name: wagtailcore_collection_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_collection_id_seq', 1, true);


--
-- Name: wagtailcore_collectionviewrestriction_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_collectionviewrestriction_groups_id_seq', 1, false);


--
-- Name: wagtailcore_collectionviewrestriction_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_collectionviewrestriction_id_seq', 1, false);


--
-- Name: wagtailcore_groupcollectionpermission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_groupcollectionpermission_id_seq', 12, true);


--
-- Name: wagtailcore_grouppagepermission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_grouppagepermission_id_seq', 6, true);


--
-- Name: wagtailcore_page_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_page_id_seq', 2, true);


--
-- Name: wagtailcore_pagerevision_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_pagerevision_id_seq', 1, false);


--
-- Name: wagtailcore_pageviewrestriction_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_pageviewrestriction_groups_id_seq', 1, false);


--
-- Name: wagtailcore_pageviewrestriction_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_pageviewrestriction_id_seq', 1, false);


--
-- Name: wagtailcore_site_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailcore_site_id_seq', 1, true);


--
-- Name: wagtaildocs_document_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtaildocs_document_id_seq', 1, false);


--
-- Name: wagtailembeds_embed_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailembeds_embed_id_seq', 1, false);


--
-- Name: wagtailforms_formsubmission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailforms_formsubmission_id_seq', 1, false);


--
-- Name: wagtailimages_image_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailimages_image_id_seq', 1, false);


--
-- Name: wagtailimages_rendition_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailimages_rendition_id_seq', 1, false);


--
-- Name: wagtailmedia_media_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailmedia_media_id_seq', 1, false);


--
-- Name: wagtailsearch_editorspick_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailsearch_editorspick_id_seq', 1, false);


--
-- Name: wagtailsearch_query_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailsearch_query_id_seq', 1, false);


--
-- Name: wagtailsearch_querydailyhits_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailsearch_querydailyhits_id_seq', 1, false);


--
-- Name: wagtailusers_userprofile_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.wagtailusers_userprofile_id_seq', 1, false);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- Name: auth_user auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- Name: auth_user auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: components_bannercomponent components_bannercomponent_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.components_bannercomponent
    ADD CONSTRAINT components_bannercomponent_pkey PRIMARY KEY (page_ptr_id);


--
-- Name: components_componentsapp components_componentsapp_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.components_componentsapp
    ADD CONSTRAINT components_componentsapp_pkey PRIMARY KEY (page_ptr_id);


--
-- Name: core_breadcrumb core_breadcrumb_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.core_breadcrumb
    ADD CONSTRAINT core_breadcrumb_pkey PRIMARY KEY (id);


--
-- Name: core_documenthash core_documenthash_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.core_documenthash
    ADD CONSTRAINT core_documenthash_pkey PRIMARY KEY (id);


--
-- Name: core_imagehash core_imagehash_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.core_imagehash
    ADD CONSTRAINT core_imagehash_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: export_readiness_allcontactpagespage export_readiness_allcontactpagespage_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_allcontactpagespage
    ADD CONSTRAINT export_readiness_allcontactpagespage_pkey PRIMARY KEY (page_ptr_id);


--
-- Name: export_readiness_articlepage_tags export_readiness_article_articlepage_id_tag_id_fde91d43_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_articlepage_tags
    ADD CONSTRAINT export_readiness_article_articlepage_id_tag_id_fde91d43_uniq UNIQUE (articlepage_id, tag_id);


--
-- Name: export_readiness_articlelistingpage export_readiness_articlelistingpage_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_articlelistingpage
    ADD CONSTRAINT export_readiness_articlelistingpage_pkey PRIMARY KEY (page_ptr_id);


--
-- Name: export_readiness_articlepage export_readiness_articlepage_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_articlepage
    ADD CONSTRAINT export_readiness_articlepage_pkey PRIMARY KEY (page_ptr_id);


--
-- Name: export_readiness_articlepage_tags export_readiness_articlepage_tags_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_articlepage_tags
    ADD CONSTRAINT export_readiness_articlepage_tags_pkey PRIMARY KEY (id);


--
-- Name: export_readiness_campaignpage export_readiness_campaignpage_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_campaignpage
    ADD CONSTRAINT export_readiness_campaignpage_pkey PRIMARY KEY (page_ptr_id);


--
-- Name: export_readiness_contactsuccesspage export_readiness_contactsuccesspage_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_contactsuccesspage
    ADD CONSTRAINT export_readiness_contactsuccesspage_pkey PRIMARY KEY (page_ptr_id);


--
-- Name: export_readiness_contactsuccesspage export_readiness_contactsuccesspage_topic_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_contactsuccesspage
    ADD CONSTRAINT export_readiness_contactsuccesspage_topic_key UNIQUE (topic);


--
-- Name: export_readiness_contactsuccesspages export_readiness_contactsuccesspages_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_contactsuccesspages
    ADD CONSTRAINT export_readiness_contactsuccesspages_pkey PRIMARY KEY (page_ptr_id);


--
-- Name: export_readiness_contactusguidancepage export_readiness_contactusguidancepage_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_contactusguidancepage
    ADD CONSTRAINT export_readiness_contactusguidancepage_pkey PRIMARY KEY (page_ptr_id);


--
-- Name: export_readiness_contactusguidancepage export_readiness_contactusguidancepage_topic_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_contactusguidancepage
    ADD CONSTRAINT export_readiness_contactusguidancepage_topic_key UNIQUE (topic);


--
-- Name: export_readiness_contactusguidancepages export_readiness_contactusguidancepages_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_contactusguidancepages
    ADD CONSTRAINT export_readiness_contactusguidancepages_pkey PRIMARY KEY (page_ptr_id);


--
-- Name: export_readiness_countryguidepage export_readiness_countryguidepage_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_countryguidepage
    ADD CONSTRAINT export_readiness_countryguidepage_pkey PRIMARY KEY (page_ptr_id);


--
-- Name: export_readiness_euexitdomesticformpage export_readiness_euexitdomesticformpage_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_euexitdomesticformpage
    ADD CONSTRAINT export_readiness_euexitdomesticformpage_pkey PRIMARY KEY (page_ptr_id);


--
-- Name: export_readiness_euexitformpages export_readiness_euexitformpages_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_euexitformpages
    ADD CONSTRAINT export_readiness_euexitformpages_pkey PRIMARY KEY (page_ptr_id);


--
-- Name: export_readiness_euexitformsuccesspage export_readiness_euexitformsuccesspage_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_euexitformsuccesspage
    ADD CONSTRAINT export_readiness_euexitformsuccesspage_pkey PRIMARY KEY (page_ptr_id);


--
-- Name: export_readiness_euexitinternationalformpage export_readiness_euexitinternationalformpage_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_euexitinternationalformpage
    ADD CONSTRAINT export_readiness_euexitinternationalformpage_pkey PRIMARY KEY (page_ptr_id);


--
-- Name: export_readiness_exportreadinessapp export_readiness_exportreadinessapp_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_exportreadinessapp
    ADD CONSTRAINT export_readiness_exportreadinessapp_pkey PRIMARY KEY (page_ptr_id);


--
-- Name: export_readiness_homepage export_readiness_homepage_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_homepage
    ADD CONSTRAINT export_readiness_homepage_pkey PRIMARY KEY (page_ptr_id);


--
-- Name: export_readiness_internationallandingpage export_readiness_internationallandingpage_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_internationallandingpage
    ADD CONSTRAINT export_readiness_internationallandingpage_pkey PRIMARY KEY (page_ptr_id);


--
-- Name: export_readiness_marketingpages export_readiness_marketingpages_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_marketingpages
    ADD CONSTRAINT export_readiness_marketingpages_pkey PRIMARY KEY (page_ptr_id);


--
-- Name: export_readiness_getfinancepage export_readiness_newgetfinancepage_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_getfinancepage
    ADD CONSTRAINT export_readiness_newgetfinancepage_pkey PRIMARY KEY (page_ptr_id);


--
-- Name: export_readiness_performancedashboardpage export_readiness_perform_product_link_c4a8b8c6_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_performancedashboardpage
    ADD CONSTRAINT export_readiness_perform_product_link_c4a8b8c6_uniq UNIQUE (product_link);


--
-- Name: export_readiness_performancedashboardnotespage export_readiness_performancedashboardnotespage_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_performancedashboardnotespage
    ADD CONSTRAINT export_readiness_performancedashboardnotespage_pkey PRIMARY KEY (page_ptr_id);


--
-- Name: export_readiness_performancedashboardpage export_readiness_performancedashboardpage_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_performancedashboardpage
    ADD CONSTRAINT export_readiness_performancedashboardpage_pkey PRIMARY KEY (page_ptr_id);


--
-- Name: export_readiness_privacyandcookiespage export_readiness_privacyandcookiespage_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_privacyandcookiespage
    ADD CONSTRAINT export_readiness_privacyandcookiespage_pkey PRIMARY KEY (page_ptr_id);


--
-- Name: export_readiness_sitepolicypages export_readiness_sitepolicypages_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_sitepolicypages
    ADD CONSTRAINT export_readiness_sitepolicypages_pkey PRIMARY KEY (page_ptr_id);


--
-- Name: export_readiness_superregionpage export_readiness_superregionpage_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_superregionpage
    ADD CONSTRAINT export_readiness_superregionpage_pkey PRIMARY KEY (topiclandingpage_ptr_id);


--
-- Name: export_readiness_tag export_readiness_tag_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_tag
    ADD CONSTRAINT export_readiness_tag_pkey PRIMARY KEY (id);


--
-- Name: export_readiness_termsandconditionspage export_readiness_termsandconditionspage_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_termsandconditionspage
    ADD CONSTRAINT export_readiness_termsandconditionspage_pkey PRIMARY KEY (page_ptr_id);


--
-- Name: export_readiness_topiclandingpage export_readiness_topiclandingpage_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_topiclandingpage
    ADD CONSTRAINT export_readiness_topiclandingpage_pkey PRIMARY KEY (page_ptr_id);


--
-- Name: find_a_supplier_findasupplierapp find_a_supplier_findasupplierapp_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_findasupplierapp
    ADD CONSTRAINT find_a_supplier_findasupplierapp_pkey PRIMARY KEY (page_ptr_id);


--
-- Name: find_a_supplier_industryarticlepage find_a_supplier_industryarticlepage_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_industryarticlepage
    ADD CONSTRAINT find_a_supplier_industryarticlepage_pkey PRIMARY KEY (page_ptr_id);


--
-- Name: find_a_supplier_industrycontactpage find_a_supplier_industrycontactpage_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_industrycontactpage
    ADD CONSTRAINT find_a_supplier_industrycontactpage_pkey PRIMARY KEY (page_ptr_id);


--
-- Name: find_a_supplier_industrylandingpage find_a_supplier_industrylandingpage_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_industrylandingpage
    ADD CONSTRAINT find_a_supplier_industrylandingpage_pkey PRIMARY KEY (page_ptr_id);


--
-- Name: find_a_supplier_industrypage find_a_supplier_industrypage_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_industrypage
    ADD CONSTRAINT find_a_supplier_industrypage_pkey PRIMARY KEY (page_ptr_id);


--
-- Name: find_a_supplier_industrypagearticlesummary find_a_supplier_industrypagearticlesummary_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_industrypagearticlesummary
    ADD CONSTRAINT find_a_supplier_industrypagearticlesummary_pkey PRIMARY KEY (id);


--
-- Name: find_a_supplier_landingpage find_a_supplier_landingpage_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_landingpage
    ADD CONSTRAINT find_a_supplier_landingpage_pkey PRIMARY KEY (page_ptr_id);


--
-- Name: find_a_supplier_landingpagearticlesummary find_a_supplier_landingpagearticlesummary_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_landingpagearticlesummary
    ADD CONSTRAINT find_a_supplier_landingpagearticlesummary_pkey PRIMARY KEY (id);


--
-- Name: great_international_greatinternationalapp great_international_greatinternationalapp_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.great_international_greatinternationalapp
    ADD CONSTRAINT great_international_greatinternationalapp_pkey PRIMARY KEY (page_ptr_id);


--
-- Name: great_international_internationalarticlelistingpage_tags great_international_inte_internationalarticlelist_8bfd4923_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.great_international_internationalarticlelistingpage_tags
    ADD CONSTRAINT great_international_inte_internationalarticlelist_8bfd4923_uniq UNIQUE (internationalarticlelistingpage_id, tag_id);


--
-- Name: great_international_internationalarticlepage_tags great_international_inte_internationalarticlepage_82ea1407_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.great_international_internationalarticlepage_tags
    ADD CONSTRAINT great_international_inte_internationalarticlepage_82ea1407_uniq UNIQUE (internationalarticlepage_id, tag_id);


--
-- Name: great_international_internationalcampaignpage_tags great_international_inte_internationalcampaignpag_b890949a_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.great_international_internationalcampaignpage_tags
    ADD CONSTRAINT great_international_inte_internationalcampaignpag_b890949a_uniq UNIQUE (internationalcampaignpage_id, tag_id);


--
-- Name: great_international_internationalregionpage_tags great_international_inte_internationalregionpages_dc87c200_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.great_international_internationalregionpage_tags
    ADD CONSTRAINT great_international_inte_internationalregionpages_dc87c200_uniq UNIQUE (internationalregionpage_id, tag_id);


--
-- Name: great_international_internationaltopiclandingpage_tags great_international_inte_internationaltopiclandin_86889b50_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.great_international_internationaltopiclandingpage_tags
    ADD CONSTRAINT great_international_inte_internationaltopiclandin_86889b50_uniq UNIQUE (internationaltopiclandingpage_id, tag_id);


--
-- Name: great_international_internationalarticlelistingpage great_international_internationalarticlelistingpage_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.great_international_internationalarticlelistingpage
    ADD CONSTRAINT great_international_internationalarticlelistingpage_pkey PRIMARY KEY (page_ptr_id);


--
-- Name: great_international_internationalarticlelistingpage_tags great_international_internationalarticlelistingpage_tags_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.great_international_internationalarticlelistingpage_tags
    ADD CONSTRAINT great_international_internationalarticlelistingpage_tags_pkey PRIMARY KEY (id);


--
-- Name: great_international_internationalarticlepage great_international_internationalarticlepage_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.great_international_internationalarticlepage
    ADD CONSTRAINT great_international_internationalarticlepage_pkey PRIMARY KEY (page_ptr_id);


--
-- Name: great_international_internationalarticlepage_tags great_international_internationalarticlepage_tags_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.great_international_internationalarticlepage_tags
    ADD CONSTRAINT great_international_internationalarticlepage_tags_pkey PRIMARY KEY (id);


--
-- Name: great_international_internationalcampaignpage great_international_internationalcampaignpage_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.great_international_internationalcampaignpage
    ADD CONSTRAINT great_international_internationalcampaignpage_pkey PRIMARY KEY (page_ptr_id);


--
-- Name: great_international_internationalcampaignpage_tags great_international_internationalcampaignpage_tags_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.great_international_internationalcampaignpage_tags
    ADD CONSTRAINT great_international_internationalcampaignpage_tags_pkey PRIMARY KEY (id);


--
-- Name: great_international_internationalhomepage great_international_internationalhomepage_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.great_international_internationalhomepage
    ADD CONSTRAINT great_international_internationalhomepage_pkey PRIMARY KEY (page_ptr_id);


--
-- Name: great_international_internationallocalisedfolderpage great_international_internationalregionalfolderpage_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.great_international_internationallocalisedfolderpage
    ADD CONSTRAINT great_international_internationalregionalfolderpage_pkey PRIMARY KEY (page_ptr_id);


--
-- Name: great_international_internationalregionpage great_international_internationalregionpages_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.great_international_internationalregionpage
    ADD CONSTRAINT great_international_internationalregionpages_pkey PRIMARY KEY (page_ptr_id);


--
-- Name: great_international_internationalregionpage_tags great_international_internationalregionpages_tags_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.great_international_internationalregionpage_tags
    ADD CONSTRAINT great_international_internationalregionpages_tags_pkey PRIMARY KEY (id);


--
-- Name: great_international_internationalsectorpage great_international_internationalsectorpage_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.great_international_internationalsectorpage
    ADD CONSTRAINT great_international_internationalsectorpage_pkey PRIMARY KEY (page_ptr_id);


--
-- Name: great_international_internationaltopiclandingpage great_international_internationaltopiclandingpage_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.great_international_internationaltopiclandingpage
    ADD CONSTRAINT great_international_internationaltopiclandingpage_pkey PRIMARY KEY (page_ptr_id);


--
-- Name: great_international_internationaltopiclandingpage_tags great_international_internationaltopiclandingpage_tags_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.great_international_internationaltopiclandingpage_tags
    ADD CONSTRAINT great_international_internationaltopiclandingpage_tags_pkey PRIMARY KEY (id);


--
-- Name: health_check_db_testmodel health_check_db_testmodel_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.health_check_db_testmodel
    ADD CONSTRAINT health_check_db_testmodel_pkey PRIMARY KEY (id);


--
-- Name: invest_highpotentialopportunityformpage invest_highpotentialofferformpage_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_highpotentialopportunityformpage
    ADD CONSTRAINT invest_highpotentialofferformpage_pkey PRIMARY KEY (page_ptr_id);


--
-- Name: invest_highpotentialopportunitydetailpage invest_highpotentialopportunitydetailpage_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_highpotentialopportunitydetailpage
    ADD CONSTRAINT invest_highpotentialopportunitydetailpage_pkey PRIMARY KEY (page_ptr_id);


--
-- Name: invest_highpotentialopportunityformsuccesspage invest_highpotentialopportunityformsuccesspage_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_highpotentialopportunityformsuccesspage
    ADD CONSTRAINT invest_highpotentialopportunityformsuccesspage_pkey PRIMARY KEY (page_ptr_id);


--
-- Name: invest_infopage invest_infopage_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_infopage
    ADD CONSTRAINT invest_infopage_pkey PRIMARY KEY (page_ptr_id);


--
-- Name: invest_investapp invest_investapp_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_investapp
    ADD CONSTRAINT invest_investapp_pkey PRIMARY KEY (page_ptr_id);


--
-- Name: invest_investhomepage invest_investhomepage_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_investhomepage
    ADD CONSTRAINT invest_investhomepage_pkey PRIMARY KEY (page_ptr_id);


--
-- Name: invest_regionlandingpage invest_regionlandingpage_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_regionlandingpage
    ADD CONSTRAINT invest_regionlandingpage_pkey PRIMARY KEY (page_ptr_id);


--
-- Name: invest_sectorlandingpage invest_sectorlandingpage_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorlandingpage
    ADD CONSTRAINT invest_sectorlandingpage_pkey PRIMARY KEY (page_ptr_id);


--
-- Name: invest_sectorpage invest_sectorpage_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_pkey PRIMARY KEY (page_ptr_id);


--
-- Name: invest_setupguidelandingpage invest_setupguidelandingpage_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_setupguidelandingpage
    ADD CONSTRAINT invest_setupguidelandingpage_pkey PRIMARY KEY (page_ptr_id);


--
-- Name: invest_setupguidepage invest_setupguidepage_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_setupguidepage
    ADD CONSTRAINT invest_setupguidepage_pkey PRIMARY KEY (page_ptr_id);


--
-- Name: taggit_tag taggit_tag_name_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.taggit_tag
    ADD CONSTRAINT taggit_tag_name_key UNIQUE (name);


--
-- Name: taggit_tag taggit_tag_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.taggit_tag
    ADD CONSTRAINT taggit_tag_pkey PRIMARY KEY (id);


--
-- Name: taggit_tag taggit_tag_slug_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.taggit_tag
    ADD CONSTRAINT taggit_tag_slug_key UNIQUE (slug);


--
-- Name: taggit_taggeditem taggit_taggeditem_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.taggit_taggeditem
    ADD CONSTRAINT taggit_taggeditem_pkey PRIMARY KEY (id);


--
-- Name: wagtailcore_collection wagtailcore_collection_path_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_collection
    ADD CONSTRAINT wagtailcore_collection_path_key UNIQUE (path);


--
-- Name: wagtailcore_collection wagtailcore_collection_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_collection
    ADD CONSTRAINT wagtailcore_collection_pkey PRIMARY KEY (id);


--
-- Name: wagtailcore_collectionviewrestriction_groups wagtailcore_collectionvi_collectionviewrestrictio_988995ae_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_collectionviewrestriction_groups
    ADD CONSTRAINT wagtailcore_collectionvi_collectionviewrestrictio_988995ae_uniq UNIQUE (collectionviewrestriction_id, group_id);


--
-- Name: wagtailcore_collectionviewrestriction_groups wagtailcore_collectionviewrestriction_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_collectionviewrestriction_groups
    ADD CONSTRAINT wagtailcore_collectionviewrestriction_groups_pkey PRIMARY KEY (id);


--
-- Name: wagtailcore_collectionviewrestriction wagtailcore_collectionviewrestriction_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_collectionviewrestriction
    ADD CONSTRAINT wagtailcore_collectionviewrestriction_pkey PRIMARY KEY (id);


--
-- Name: wagtailcore_groupcollectionpermission wagtailcore_groupcollect_group_id_collection_id_p_a21cefe9_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_groupcollectionpermission
    ADD CONSTRAINT wagtailcore_groupcollect_group_id_collection_id_p_a21cefe9_uniq UNIQUE (group_id, collection_id, permission_id);


--
-- Name: wagtailcore_groupcollectionpermission wagtailcore_groupcollectionpermission_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_groupcollectionpermission
    ADD CONSTRAINT wagtailcore_groupcollectionpermission_pkey PRIMARY KEY (id);


--
-- Name: wagtailcore_grouppagepermission wagtailcore_grouppageper_group_id_page_id_permiss_0898bdf8_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_grouppagepermission
    ADD CONSTRAINT wagtailcore_grouppageper_group_id_page_id_permiss_0898bdf8_uniq UNIQUE (group_id, page_id, permission_type);


--
-- Name: wagtailcore_grouppagepermission wagtailcore_grouppagepermission_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_grouppagepermission
    ADD CONSTRAINT wagtailcore_grouppagepermission_pkey PRIMARY KEY (id);


--
-- Name: wagtailcore_page wagtailcore_page_path_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_page
    ADD CONSTRAINT wagtailcore_page_path_key UNIQUE (path);


--
-- Name: wagtailcore_page wagtailcore_page_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_page
    ADD CONSTRAINT wagtailcore_page_pkey PRIMARY KEY (id);


--
-- Name: wagtailcore_pagerevision wagtailcore_pagerevision_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_pagerevision
    ADD CONSTRAINT wagtailcore_pagerevision_pkey PRIMARY KEY (id);


--
-- Name: wagtailcore_pageviewrestriction_groups wagtailcore_pageviewrest_pageviewrestriction_id_g_d23f80bb_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_pageviewrestriction_groups
    ADD CONSTRAINT wagtailcore_pageviewrest_pageviewrestriction_id_g_d23f80bb_uniq UNIQUE (pageviewrestriction_id, group_id);


--
-- Name: wagtailcore_pageviewrestriction_groups wagtailcore_pageviewrestriction_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_pageviewrestriction_groups
    ADD CONSTRAINT wagtailcore_pageviewrestriction_groups_pkey PRIMARY KEY (id);


--
-- Name: wagtailcore_pageviewrestriction wagtailcore_pageviewrestriction_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_pageviewrestriction
    ADD CONSTRAINT wagtailcore_pageviewrestriction_pkey PRIMARY KEY (id);


--
-- Name: wagtailcore_site wagtailcore_site_hostname_port_2c626d70_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_site
    ADD CONSTRAINT wagtailcore_site_hostname_port_2c626d70_uniq UNIQUE (hostname, port);


--
-- Name: wagtailcore_site wagtailcore_site_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_site
    ADD CONSTRAINT wagtailcore_site_pkey PRIMARY KEY (id);


--
-- Name: wagtaildocs_document wagtaildocs_document_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtaildocs_document
    ADD CONSTRAINT wagtaildocs_document_pkey PRIMARY KEY (id);


--
-- Name: wagtailembeds_embed wagtailembeds_embed_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailembeds_embed
    ADD CONSTRAINT wagtailembeds_embed_pkey PRIMARY KEY (id);


--
-- Name: wagtailembeds_embed wagtailembeds_embed_url_max_width_8a2922d8_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailembeds_embed
    ADD CONSTRAINT wagtailembeds_embed_url_max_width_8a2922d8_uniq UNIQUE (url, max_width);


--
-- Name: wagtailforms_formsubmission wagtailforms_formsubmission_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailforms_formsubmission
    ADD CONSTRAINT wagtailforms_formsubmission_pkey PRIMARY KEY (id);


--
-- Name: wagtailimages_image wagtailimages_image_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailimages_image
    ADD CONSTRAINT wagtailimages_image_pkey PRIMARY KEY (id);


--
-- Name: wagtailimages_rendition wagtailimages_rendition_image_id_filter_spec_foc_323c8fe0_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailimages_rendition
    ADD CONSTRAINT wagtailimages_rendition_image_id_filter_spec_foc_323c8fe0_uniq UNIQUE (image_id, filter_spec, focal_point_key);


--
-- Name: wagtailimages_rendition wagtailimages_rendition_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailimages_rendition
    ADD CONSTRAINT wagtailimages_rendition_pkey PRIMARY KEY (id);


--
-- Name: wagtailmedia_media wagtailmedia_media_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailmedia_media
    ADD CONSTRAINT wagtailmedia_media_pkey PRIMARY KEY (id);


--
-- Name: wagtailsearch_editorspick wagtailsearch_editorspick_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailsearch_editorspick
    ADD CONSTRAINT wagtailsearch_editorspick_pkey PRIMARY KEY (id);


--
-- Name: wagtailsearch_query wagtailsearch_query_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailsearch_query
    ADD CONSTRAINT wagtailsearch_query_pkey PRIMARY KEY (id);


--
-- Name: wagtailsearch_query wagtailsearch_query_query_string_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailsearch_query
    ADD CONSTRAINT wagtailsearch_query_query_string_key UNIQUE (query_string);


--
-- Name: wagtailsearch_querydailyhits wagtailsearch_querydailyhits_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailsearch_querydailyhits
    ADD CONSTRAINT wagtailsearch_querydailyhits_pkey PRIMARY KEY (id);


--
-- Name: wagtailsearch_querydailyhits wagtailsearch_querydailyhits_query_id_date_1dd232e6_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailsearch_querydailyhits
    ADD CONSTRAINT wagtailsearch_querydailyhits_query_id_date_1dd232e6_uniq UNIQUE (query_id, date);


--
-- Name: wagtailusers_userprofile wagtailusers_userprofile_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailusers_userprofile
    ADD CONSTRAINT wagtailusers_userprofile_pkey PRIMARY KEY (id);


--
-- Name: wagtailusers_userprofile wagtailusers_userprofile_user_id_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailusers_userprofile
    ADD CONSTRAINT wagtailusers_userprofile_user_id_key UNIQUE (user_id);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);


--
-- Name: components_bannercomponent_service_name_44a9cdbc; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX components_bannercomponent_service_name_44a9cdbc ON public.components_bannercomponent USING btree (service_name);


--
-- Name: components_bannercomponent_service_name_44a9cdbc_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX components_bannercomponent_service_name_44a9cdbc_like ON public.components_bannercomponent USING btree (service_name varchar_pattern_ops);


--
-- Name: components_componentsapp_service_name_b5634112; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX components_componentsapp_service_name_b5634112 ON public.components_componentsapp USING btree (service_name);


--
-- Name: components_componentsapp_service_name_b5634112_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX components_componentsapp_service_name_b5634112_like ON public.components_componentsapp USING btree (service_name varchar_pattern_ops);


--
-- Name: core_breadcrumb_content_type_id_10fedf77; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX core_breadcrumb_content_type_id_10fedf77 ON public.core_breadcrumb USING btree (content_type_id);


--
-- Name: core_breadcrumb_service_name_daacacce; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX core_breadcrumb_service_name_daacacce ON public.core_breadcrumb USING btree (service_name);


--
-- Name: core_breadcrumb_service_name_daacacce_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX core_breadcrumb_service_name_daacacce_like ON public.core_breadcrumb USING btree (service_name varchar_pattern_ops);


--
-- Name: core_breadcrumb_slug_0af9f500; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX core_breadcrumb_slug_0af9f500 ON public.core_breadcrumb USING btree (slug);


--
-- Name: core_breadcrumb_slug_0af9f500_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX core_breadcrumb_slug_0af9f500_like ON public.core_breadcrumb USING btree (slug varchar_pattern_ops);


--
-- Name: core_documenthash_document_id_6783bf52; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX core_documenthash_document_id_6783bf52 ON public.core_documenthash USING btree (document_id);


--
-- Name: core_imagehash_image_id_ee947939; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX core_imagehash_image_id_ee947939 ON public.core_imagehash USING btree (image_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: export_readiness_allcontactpagespage_service_name_9ecef95a; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_allcontactpagespage_service_name_9ecef95a ON public.export_readiness_allcontactpagespage USING btree (service_name);


--
-- Name: export_readiness_allcontactpagespage_service_name_9ecef95a_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_allcontactpagespage_service_name_9ecef95a_like ON public.export_readiness_allcontactpagespage USING btree (service_name varchar_pattern_ops);


--
-- Name: export_readiness_articlelistingpage_hero_image_id_86c32ca9; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_articlelistingpage_hero_image_id_86c32ca9 ON public.export_readiness_articlelistingpage USING btree (hero_image_id);


--
-- Name: export_readiness_articlelistingpage_service_name_03f3affd; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_articlelistingpage_service_name_03f3affd ON public.export_readiness_articlelistingpage USING btree (service_name);


--
-- Name: export_readiness_articlelistingpage_service_name_03f3affd_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_articlelistingpage_service_name_03f3affd_like ON public.export_readiness_articlelistingpage USING btree (service_name varchar_pattern_ops);


--
-- Name: export_readiness_articlepage_article_image_id_89070cd3; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_articlepage_article_image_id_89070cd3 ON public.export_readiness_articlepage USING btree (article_image_id);


--
-- Name: export_readiness_articlepage_related_page_one_id_7634796a; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_articlepage_related_page_one_id_7634796a ON public.export_readiness_articlepage USING btree (related_page_one_id);


--
-- Name: export_readiness_articlepage_related_page_three_id_d04918af; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_articlepage_related_page_three_id_d04918af ON public.export_readiness_articlepage USING btree (related_page_three_id);


--
-- Name: export_readiness_articlepage_related_page_two_id_1173b7c9; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_articlepage_related_page_two_id_1173b7c9 ON public.export_readiness_articlepage USING btree (related_page_two_id);


--
-- Name: export_readiness_articlepage_service_name_fb99dd49; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_articlepage_service_name_fb99dd49 ON public.export_readiness_articlepage USING btree (service_name);


--
-- Name: export_readiness_articlepage_service_name_fb99dd49_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_articlepage_service_name_fb99dd49_like ON public.export_readiness_articlepage USING btree (service_name varchar_pattern_ops);


--
-- Name: export_readiness_articlepage_tags_articlepage_id_f030e54b; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_articlepage_tags_articlepage_id_f030e54b ON public.export_readiness_articlepage_tags USING btree (articlepage_id);


--
-- Name: export_readiness_articlepage_tags_tag_id_5ab392b0; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_articlepage_tags_tag_id_5ab392b0 ON public.export_readiness_articlepage_tags USING btree (tag_id);


--
-- Name: export_readiness_campaignp_selling_point_one_icon_id_fd711190; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_campaignp_selling_point_one_icon_id_fd711190 ON public.export_readiness_campaignpage USING btree (selling_point_one_icon_id);


--
-- Name: export_readiness_campaignp_selling_point_three_icon_i_5c85aa24; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_campaignp_selling_point_three_icon_i_5c85aa24 ON public.export_readiness_campaignpage USING btree (selling_point_three_icon_id);


--
-- Name: export_readiness_campaignp_selling_point_two_icon_id_c262e438; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_campaignp_selling_point_two_icon_id_c262e438 ON public.export_readiness_campaignpage USING btree (selling_point_two_icon_id);


--
-- Name: export_readiness_campaignpage_campaign_hero_image_id_3fcd1917; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_campaignpage_campaign_hero_image_id_3fcd1917 ON public.export_readiness_campaignpage USING btree (campaign_hero_image_id);


--
-- Name: export_readiness_campaignpage_related_page_one_id_cb23b33a; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_campaignpage_related_page_one_id_cb23b33a ON public.export_readiness_campaignpage USING btree (related_page_one_id);


--
-- Name: export_readiness_campaignpage_related_page_three_id_c30330ae; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_campaignpage_related_page_three_id_c30330ae ON public.export_readiness_campaignpage USING btree (related_page_three_id);


--
-- Name: export_readiness_campaignpage_related_page_two_id_c264e13b; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_campaignpage_related_page_two_id_c264e13b ON public.export_readiness_campaignpage USING btree (related_page_two_id);


--
-- Name: export_readiness_campaignpage_section_one_image_id_b31db608; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_campaignpage_section_one_image_id_b31db608 ON public.export_readiness_campaignpage USING btree (section_one_image_id);


--
-- Name: export_readiness_campaignpage_section_two_image_id_ca2e9d7d; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_campaignpage_section_two_image_id_ca2e9d7d ON public.export_readiness_campaignpage USING btree (section_two_image_id);


--
-- Name: export_readiness_campaignpage_service_name_f48d989f; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_campaignpage_service_name_f48d989f ON public.export_readiness_campaignpage USING btree (service_name);


--
-- Name: export_readiness_campaignpage_service_name_f48d989f_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_campaignpage_service_name_f48d989f_like ON public.export_readiness_campaignpage USING btree (service_name varchar_pattern_ops);


--
-- Name: export_readiness_contact_service_name_4a2e32da_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_contact_service_name_4a2e32da_like ON public.export_readiness_contactusguidancepage USING btree (service_name varchar_pattern_ops);


--
-- Name: export_readiness_contact_service_name_87cd12e2_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_contact_service_name_87cd12e2_like ON public.export_readiness_contactusguidancepages USING btree (service_name varchar_pattern_ops);


--
-- Name: export_readiness_contactsuccesspage_service_name_091b2a6e; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_contactsuccesspage_service_name_091b2a6e ON public.export_readiness_contactsuccesspage USING btree (service_name);


--
-- Name: export_readiness_contactsuccesspage_service_name_091b2a6e_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_contactsuccesspage_service_name_091b2a6e_like ON public.export_readiness_contactsuccesspage USING btree (service_name varchar_pattern_ops);


--
-- Name: export_readiness_contactsuccesspage_topic_d0224010_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_contactsuccesspage_topic_d0224010_like ON public.export_readiness_contactsuccesspage USING btree (topic text_pattern_ops);


--
-- Name: export_readiness_contactsuccesspages_service_name_205640d5; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_contactsuccesspages_service_name_205640d5 ON public.export_readiness_contactsuccesspages USING btree (service_name);


--
-- Name: export_readiness_contactsuccesspages_service_name_205640d5_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_contactsuccesspages_service_name_205640d5_like ON public.export_readiness_contactsuccesspages USING btree (service_name varchar_pattern_ops);


--
-- Name: export_readiness_contactusguidancepage_service_name_4a2e32da; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_contactusguidancepage_service_name_4a2e32da ON public.export_readiness_contactusguidancepage USING btree (service_name);


--
-- Name: export_readiness_contactusguidancepage_topic_03eb4241_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_contactusguidancepage_topic_03eb4241_like ON public.export_readiness_contactusguidancepage USING btree (topic text_pattern_ops);


--
-- Name: export_readiness_contactusguidancepages_service_name_87cd12e2; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_contactusguidancepages_service_name_87cd12e2 ON public.export_readiness_contactusguidancepages USING btree (service_name);


--
-- Name: export_readiness_countrygu_related_page_three_id_56823dfc; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_countrygu_related_page_three_id_56823dfc ON public.export_readiness_countryguidepage USING btree (related_page_three_id);


--
-- Name: export_readiness_countrygu_selling_point_one_icon_id_bbe09d0e; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_countrygu_selling_point_one_icon_id_bbe09d0e ON public.export_readiness_countryguidepage USING btree (selling_point_one_icon_id);


--
-- Name: export_readiness_countrygu_selling_point_three_icon_i_b9cb720d; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_countrygu_selling_point_three_icon_i_b9cb720d ON public.export_readiness_countryguidepage USING btree (selling_point_three_icon_id);


--
-- Name: export_readiness_countrygu_selling_point_two_icon_id_8ff624b4; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_countrygu_selling_point_two_icon_id_8ff624b4 ON public.export_readiness_countryguidepage USING btree (selling_point_two_icon_id);


--
-- Name: export_readiness_countryguidepage_hero_image_id_deec3fdd; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_countryguidepage_hero_image_id_deec3fdd ON public.export_readiness_countryguidepage USING btree (hero_image_id);


--
-- Name: export_readiness_countryguidepage_related_page_one_id_5ca8f131; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_countryguidepage_related_page_one_id_5ca8f131 ON public.export_readiness_countryguidepage USING btree (related_page_one_id);


--
-- Name: export_readiness_countryguidepage_related_page_two_id_1ccdaa57; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_countryguidepage_related_page_two_id_1ccdaa57 ON public.export_readiness_countryguidepage USING btree (related_page_two_id);


--
-- Name: export_readiness_countryguidepage_service_name_75eca2c7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_countryguidepage_service_name_75eca2c7 ON public.export_readiness_countryguidepage USING btree (service_name);


--
-- Name: export_readiness_countryguidepage_service_name_75eca2c7_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_countryguidepage_service_name_75eca2c7_like ON public.export_readiness_countryguidepage USING btree (service_name varchar_pattern_ops);


--
-- Name: export_readiness_euexitd_service_name_362fca95_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_euexitd_service_name_362fca95_like ON public.export_readiness_euexitdomesticformpage USING btree (service_name varchar_pattern_ops);


--
-- Name: export_readiness_euexitdomesticformpage_service_name_362fca95; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_euexitdomesticformpage_service_name_362fca95 ON public.export_readiness_euexitdomesticformpage USING btree (service_name);


--
-- Name: export_readiness_euexitf_service_name_23f35296_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_euexitf_service_name_23f35296_like ON public.export_readiness_euexitformsuccesspage USING btree (service_name varchar_pattern_ops);


--
-- Name: export_readiness_euexitformpages_service_name_4cc5845a; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_euexitformpages_service_name_4cc5845a ON public.export_readiness_euexitformpages USING btree (service_name);


--
-- Name: export_readiness_euexitformpages_service_name_4cc5845a_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_euexitformpages_service_name_4cc5845a_like ON public.export_readiness_euexitformpages USING btree (service_name varchar_pattern_ops);


--
-- Name: export_readiness_euexitformsuccesspage_service_name_23f35296; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_euexitformsuccesspage_service_name_23f35296 ON public.export_readiness_euexitformsuccesspage USING btree (service_name);


--
-- Name: export_readiness_euexiti_service_name_655a884a_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_euexiti_service_name_655a884a_like ON public.export_readiness_euexitinternationalformpage USING btree (service_name varchar_pattern_ops);


--
-- Name: export_readiness_euexitint_service_name_655a884a; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_euexitint_service_name_655a884a ON public.export_readiness_euexitinternationalformpage USING btree (service_name);


--
-- Name: export_readiness_exportreadinessapp_service_name_545f7fca; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_exportreadinessapp_service_name_545f7fca ON public.export_readiness_exportreadinessapp USING btree (service_name);


--
-- Name: export_readiness_exportreadinessapp_service_name_545f7fca_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_exportreadinessapp_service_name_545f7fca_like ON public.export_readiness_exportreadinessapp USING btree (service_name varchar_pattern_ops);


--
-- Name: export_readiness_homepage_service_name_03ef7d15; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_homepage_service_name_03ef7d15 ON public.export_readiness_homepage USING btree (service_name);


--
-- Name: export_readiness_homepage_service_name_03ef7d15_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_homepage_service_name_03ef7d15_like ON public.export_readiness_homepage USING btree (service_name varchar_pattern_ops);


--
-- Name: export_readiness_interna_service_name_804aa4f2_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_interna_service_name_804aa4f2_like ON public.export_readiness_internationallandingpage USING btree (service_name varchar_pattern_ops);


--
-- Name: export_readiness_internationallandingpage_service_name_804aa4f2; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_internationallandingpage_service_name_804aa4f2 ON public.export_readiness_internationallandingpage USING btree (service_name);


--
-- Name: export_readiness_marketingpages_service_name_e5046b5a; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_marketingpages_service_name_e5046b5a ON public.export_readiness_marketingpages USING btree (service_name);


--
-- Name: export_readiness_marketingpages_service_name_e5046b5a_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_marketingpages_service_name_e5046b5a_like ON public.export_readiness_marketingpages USING btree (service_name varchar_pattern_ops);


--
-- Name: export_readiness_newgetfin_advantages_one_icon_id_d68b409c; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_newgetfin_advantages_one_icon_id_d68b409c ON public.export_readiness_getfinancepage USING btree (advantages_one_icon_id);


--
-- Name: export_readiness_newgetfin_advantages_three_icon_id_32d9754e; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_newgetfin_advantages_three_icon_id_32d9754e ON public.export_readiness_getfinancepage USING btree (advantages_three_icon_id);


--
-- Name: export_readiness_newgetfin_advantages_two_icon_id_20513176; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_newgetfin_advantages_two_icon_id_20513176 ON public.export_readiness_getfinancepage USING btree (advantages_two_icon_id);


--
-- Name: export_readiness_newgetfinancepage_evidence_video_id_431a261d; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_newgetfinancepage_evidence_video_id_431a261d ON public.export_readiness_getfinancepage USING btree (evidence_video_id);


--
-- Name: export_readiness_newgetfinancepage_hero_image_id_1b9d533a; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_newgetfinancepage_hero_image_id_1b9d533a ON public.export_readiness_getfinancepage USING btree (hero_image_id);


--
-- Name: export_readiness_newgetfinancepage_service_name_583406a3; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_newgetfinancepage_service_name_583406a3 ON public.export_readiness_getfinancepage USING btree (service_name);


--
-- Name: export_readiness_newgetfinancepage_service_name_583406a3_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_newgetfinancepage_service_name_583406a3_like ON public.export_readiness_getfinancepage USING btree (service_name varchar_pattern_ops);


--
-- Name: export_readiness_newgetfinancepage_ukef_logo_id_714d839d; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_newgetfinancepage_ukef_logo_id_714d839d ON public.export_readiness_getfinancepage USING btree (ukef_logo_id);


--
-- Name: export_readiness_perform_product_link_c4a8b8c6_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_perform_product_link_c4a8b8c6_like ON public.export_readiness_performancedashboardpage USING btree (product_link text_pattern_ops);


--
-- Name: export_readiness_perform_service_name_7472bd83_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_perform_service_name_7472bd83_like ON public.export_readiness_performancedashboardpage USING btree (service_name varchar_pattern_ops);


--
-- Name: export_readiness_perform_service_name_a02020fa_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_perform_service_name_a02020fa_like ON public.export_readiness_performancedashboardnotespage USING btree (service_name varchar_pattern_ops);


--
-- Name: export_readiness_performan_service_name_a02020fa; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_performan_service_name_a02020fa ON public.export_readiness_performancedashboardnotespage USING btree (service_name);


--
-- Name: export_readiness_performancedashboardpage_service_name_7472bd83; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_performancedashboardpage_service_name_7472bd83 ON public.export_readiness_performancedashboardpage USING btree (service_name);


--
-- Name: export_readiness_privacy_service_name_083b87db_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_privacy_service_name_083b87db_like ON public.export_readiness_privacyandcookiespage USING btree (service_name varchar_pattern_ops);


--
-- Name: export_readiness_privacyandcookiespage_service_name_083b87db; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_privacyandcookiespage_service_name_083b87db ON public.export_readiness_privacyandcookiespage USING btree (service_name);


--
-- Name: export_readiness_sitepolicypages_service_name_e62b9638; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_sitepolicypages_service_name_e62b9638 ON public.export_readiness_sitepolicypages USING btree (service_name);


--
-- Name: export_readiness_sitepolicypages_service_name_e62b9638_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_sitepolicypages_service_name_e62b9638_like ON public.export_readiness_sitepolicypages USING btree (service_name varchar_pattern_ops);


--
-- Name: export_readiness_termsan_service_name_20c5b33c_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_termsan_service_name_20c5b33c_like ON public.export_readiness_termsandconditionspage USING btree (service_name varchar_pattern_ops);


--
-- Name: export_readiness_termsandconditionspage_service_name_20c5b33c; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_termsandconditionspage_service_name_20c5b33c ON public.export_readiness_termsandconditionspage USING btree (service_name);


--
-- Name: export_readiness_topiclandingpage_hero_image_id_dbf67d7a; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_topiclandingpage_hero_image_id_dbf67d7a ON public.export_readiness_topiclandingpage USING btree (hero_image_id);


--
-- Name: export_readiness_topiclandingpage_service_name_6901d8f6; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_topiclandingpage_service_name_6901d8f6 ON public.export_readiness_topiclandingpage USING btree (service_name);


--
-- Name: export_readiness_topiclandingpage_service_name_6901d8f6_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX export_readiness_topiclandingpage_service_name_6901d8f6_like ON public.export_readiness_topiclandingpage USING btree (service_name varchar_pattern_ops);


--
-- Name: find_a_supplier_findasupplierapp_service_name_745f8d87; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_findasupplierapp_service_name_745f8d87 ON public.find_a_supplier_findasupplierapp USING btree (service_name);


--
-- Name: find_a_supplier_findasupplierapp_service_name_745f8d87_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_findasupplierapp_service_name_745f8d87_like ON public.find_a_supplier_findasupplierapp USING btree (service_name varchar_pattern_ops);


--
-- Name: find_a_supplier_industryarticlepage_service_name_ea4d298f; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_industryarticlepage_service_name_ea4d298f ON public.find_a_supplier_industryarticlepage USING btree (service_name);


--
-- Name: find_a_supplier_industryarticlepage_service_name_ea4d298f_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_industryarticlepage_service_name_ea4d298f_like ON public.find_a_supplier_industryarticlepage USING btree (service_name varchar_pattern_ops);


--
-- Name: find_a_supplier_industrycontactpage_service_name_3987a086; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_industrycontactpage_service_name_3987a086 ON public.find_a_supplier_industrycontactpage USING btree (service_name);


--
-- Name: find_a_supplier_industrycontactpage_service_name_3987a086_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_industrycontactpage_service_name_3987a086_like ON public.find_a_supplier_industrycontactpage USING btree (service_name varchar_pattern_ops);


--
-- Name: find_a_supplier_industryla_mobile_hero_image_id_3f4849a2; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_industryla_mobile_hero_image_id_3f4849a2 ON public.find_a_supplier_industrylandingpage USING btree (mobile_hero_image_id);


--
-- Name: find_a_supplier_industrylandingpage_hero_image_id_44beb772; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_industrylandingpage_hero_image_id_44beb772 ON public.find_a_supplier_industrylandingpage USING btree (hero_image_id);


--
-- Name: find_a_supplier_industrylandingpage_service_name_e9e17b25; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_industrylandingpage_service_name_e9e17b25 ON public.find_a_supplier_industrylandingpage USING btree (service_name);


--
-- Name: find_a_supplier_industrylandingpage_service_name_e9e17b25_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_industrylandingpage_service_name_e9e17b25_like ON public.find_a_supplier_industrylandingpage USING btree (service_name varchar_pattern_ops);


--
-- Name: find_a_supplier_industrypa_introduction_column_one_ic_10e463a0; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_industrypa_introduction_column_one_ic_10e463a0 ON public.find_a_supplier_industrypage USING btree (introduction_column_one_icon_id);


--
-- Name: find_a_supplier_industrypa_introduction_column_three__fd509d55; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_industrypa_introduction_column_three__fd509d55 ON public.find_a_supplier_industrypage USING btree (introduction_column_three_icon_id);


--
-- Name: find_a_supplier_industrypa_introduction_column_two_ic_b5f2cae1; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_industrypa_introduction_column_two_ic_b5f2cae1 ON public.find_a_supplier_industrypage USING btree (introduction_column_two_icon_id);


--
-- Name: find_a_supplier_industrypa_page_en_gb_id_1818656b; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_industrypa_page_en_gb_id_1818656b ON public.find_a_supplier_industrypagearticlesummary USING btree (page_en_gb_id);


--
-- Name: find_a_supplier_industrypa_page_pt_br_id_2e23fb1f; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_industrypa_page_pt_br_id_2e23fb1f ON public.find_a_supplier_industrypagearticlesummary USING btree (page_pt_br_id);


--
-- Name: find_a_supplier_industrypa_page_zh_hans_id_2c9fc29d; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_industrypa_page_zh_hans_id_2c9fc29d ON public.find_a_supplier_industrypagearticlesummary USING btree (page_zh_hans_id);


--
-- Name: find_a_supplier_industrypa_video_media_id_11b74530; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_industrypa_video_media_id_11b74530 ON public.find_a_supplier_industrypagearticlesummary USING btree (video_media_id);


--
-- Name: find_a_supplier_industrypage_hero_image_id_4b527995; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_industrypage_hero_image_id_4b527995 ON public.find_a_supplier_industrypage USING btree (hero_image_id);


--
-- Name: find_a_supplier_industrypage_mobile_hero_image_id_e3940be2; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_industrypage_mobile_hero_image_id_e3940be2 ON public.find_a_supplier_industrypage USING btree (mobile_hero_image_id);


--
-- Name: find_a_supplier_industrypage_service_name_8163bdee; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_industrypage_service_name_8163bdee ON public.find_a_supplier_industrypage USING btree (service_name);


--
-- Name: find_a_supplier_industrypage_service_name_8163bdee_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_industrypage_service_name_8163bdee_like ON public.find_a_supplier_industrypage USING btree (service_name varchar_pattern_ops);


--
-- Name: find_a_supplier_industrypage_summary_image_id_ec5b95f4; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_industrypage_summary_image_id_ec5b95f4 ON public.find_a_supplier_industrypage USING btree (summary_image_id);


--
-- Name: find_a_supplier_industrypagearticlesummary_image_id_346e5e98; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_industrypagearticlesummary_image_id_346e5e98 ON public.find_a_supplier_industrypagearticlesummary USING btree (image_id);


--
-- Name: find_a_supplier_industrypagearticlesummary_page_ar_id_21b6c7aa; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_industrypagearticlesummary_page_ar_id_21b6c7aa ON public.find_a_supplier_industrypagearticlesummary USING btree (page_ar_id);


--
-- Name: find_a_supplier_industrypagearticlesummary_page_de_id_0483d921; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_industrypagearticlesummary_page_de_id_0483d921 ON public.find_a_supplier_industrypagearticlesummary USING btree (page_de_id);


--
-- Name: find_a_supplier_industrypagearticlesummary_page_es_id_4a5714bc; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_industrypagearticlesummary_page_es_id_4a5714bc ON public.find_a_supplier_industrypagearticlesummary USING btree (page_es_id);


--
-- Name: find_a_supplier_industrypagearticlesummary_page_fr_id_bfd8d4b7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_industrypagearticlesummary_page_fr_id_bfd8d4b7 ON public.find_a_supplier_industrypagearticlesummary USING btree (page_fr_id);


--
-- Name: find_a_supplier_industrypagearticlesummary_page_id_beadfb32; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_industrypagearticlesummary_page_id_beadfb32 ON public.find_a_supplier_industrypagearticlesummary USING btree (page_id);


--
-- Name: find_a_supplier_industrypagearticlesummary_page_ja_id_a0834721; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_industrypagearticlesummary_page_ja_id_a0834721 ON public.find_a_supplier_industrypagearticlesummary USING btree (page_ja_id);


--
-- Name: find_a_supplier_industrypagearticlesummary_page_pt_id_a2f522f7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_industrypagearticlesummary_page_pt_id_a2f522f7 ON public.find_a_supplier_industrypagearticlesummary USING btree (page_pt_id);


--
-- Name: find_a_supplier_industrypagearticlesummary_page_ru_id_bc3a8809; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_industrypagearticlesummary_page_ru_id_bc3a8809 ON public.find_a_supplier_industrypagearticlesummary USING btree (page_ru_id);


--
-- Name: find_a_supplier_landingpag_page_en_gb_id_ad4dd2fd; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_landingpag_page_en_gb_id_ad4dd2fd ON public.find_a_supplier_landingpagearticlesummary USING btree (page_en_gb_id);


--
-- Name: find_a_supplier_landingpag_page_pt_br_id_a6ffa0f7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_landingpag_page_pt_br_id_a6ffa0f7 ON public.find_a_supplier_landingpagearticlesummary USING btree (page_pt_br_id);


--
-- Name: find_a_supplier_landingpag_page_zh_hans_id_1972a979; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_landingpag_page_zh_hans_id_1972a979 ON public.find_a_supplier_landingpagearticlesummary USING btree (page_zh_hans_id);


--
-- Name: find_a_supplier_landingpag_services_column_four_icon__072ed0b7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_landingpag_services_column_four_icon__072ed0b7 ON public.find_a_supplier_landingpage USING btree (services_column_four_icon_fr_id);


--
-- Name: find_a_supplier_landingpag_services_column_four_icon__2a144e98; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_landingpag_services_column_four_icon__2a144e98 ON public.find_a_supplier_landingpage USING btree (services_column_four_icon_ar_id);


--
-- Name: find_a_supplier_landingpag_services_column_four_icon__2d66fc19; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_landingpag_services_column_four_icon__2d66fc19 ON public.find_a_supplier_landingpage USING btree (services_column_four_icon_es_id);


--
-- Name: find_a_supplier_landingpag_services_column_four_icon__3c9f0ee0; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_landingpag_services_column_four_icon__3c9f0ee0 ON public.find_a_supplier_landingpage USING btree (services_column_four_icon_en_gb_id);


--
-- Name: find_a_supplier_landingpag_services_column_four_icon__81049aca; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_landingpag_services_column_four_icon__81049aca ON public.find_a_supplier_landingpage USING btree (services_column_four_icon_id);


--
-- Name: find_a_supplier_landingpag_services_column_four_icon__85cc6518; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_landingpag_services_column_four_icon__85cc6518 ON public.find_a_supplier_landingpage USING btree (services_column_four_icon_pt_id);


--
-- Name: find_a_supplier_landingpag_services_column_four_icon__987a4695; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_landingpag_services_column_four_icon__987a4695 ON public.find_a_supplier_landingpage USING btree (services_column_four_icon_pt_br_id);


--
-- Name: find_a_supplier_landingpag_services_column_four_icon__ad868ac2; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_landingpag_services_column_four_icon__ad868ac2 ON public.find_a_supplier_landingpage USING btree (services_column_four_icon_de_id);


--
-- Name: find_a_supplier_landingpag_services_column_four_icon__cf16e03e; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_landingpag_services_column_four_icon__cf16e03e ON public.find_a_supplier_landingpage USING btree (services_column_four_icon_ru_id);


--
-- Name: find_a_supplier_landingpag_services_column_four_icon__d12a379f; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_landingpag_services_column_four_icon__d12a379f ON public.find_a_supplier_landingpage USING btree (services_column_four_icon_ja_id);


--
-- Name: find_a_supplier_landingpag_services_column_four_icon__f5bcad12; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_landingpag_services_column_four_icon__f5bcad12 ON public.find_a_supplier_landingpage USING btree (services_column_four_icon_zh_hans_id);


--
-- Name: find_a_supplier_landingpag_services_column_one_icon_a_7e8adcef; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_landingpag_services_column_one_icon_a_7e8adcef ON public.find_a_supplier_landingpage USING btree (services_column_one_icon_ar_id);


--
-- Name: find_a_supplier_landingpag_services_column_one_icon_d_07d71f50; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_landingpag_services_column_one_icon_d_07d71f50 ON public.find_a_supplier_landingpage USING btree (services_column_one_icon_de_id);


--
-- Name: find_a_supplier_landingpag_services_column_one_icon_e_28a5c41d; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_landingpag_services_column_one_icon_e_28a5c41d ON public.find_a_supplier_landingpage USING btree (services_column_one_icon_en_gb_id);


--
-- Name: find_a_supplier_landingpag_services_column_one_icon_e_f818c154; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_landingpag_services_column_one_icon_e_f818c154 ON public.find_a_supplier_landingpage USING btree (services_column_one_icon_es_id);


--
-- Name: find_a_supplier_landingpag_services_column_one_icon_f_3d218e3f; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_landingpag_services_column_one_icon_f_3d218e3f ON public.find_a_supplier_landingpage USING btree (services_column_one_icon_fr_id);


--
-- Name: find_a_supplier_landingpag_services_column_one_icon_i_b1109e29; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_landingpag_services_column_one_icon_i_b1109e29 ON public.find_a_supplier_landingpage USING btree (services_column_one_icon_id);


--
-- Name: find_a_supplier_landingpag_services_column_one_icon_j_fdb1b3bf; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_landingpag_services_column_one_icon_j_fdb1b3bf ON public.find_a_supplier_landingpage USING btree (services_column_one_icon_ja_id);


--
-- Name: find_a_supplier_landingpag_services_column_one_icon_p_d33d9fb6; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_landingpag_services_column_one_icon_p_d33d9fb6 ON public.find_a_supplier_landingpage USING btree (services_column_one_icon_pt_br_id);


--
-- Name: find_a_supplier_landingpag_services_column_one_icon_p_db9a4d43; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_landingpag_services_column_one_icon_p_db9a4d43 ON public.find_a_supplier_landingpage USING btree (services_column_one_icon_pt_id);


--
-- Name: find_a_supplier_landingpag_services_column_one_icon_r_5b8e4485; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_landingpag_services_column_one_icon_r_5b8e4485 ON public.find_a_supplier_landingpage USING btree (services_column_one_icon_ru_id);


--
-- Name: find_a_supplier_landingpag_services_column_one_icon_z_0244324a; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_landingpag_services_column_one_icon_z_0244324a ON public.find_a_supplier_landingpage USING btree (services_column_one_icon_zh_hans_id);


--
-- Name: find_a_supplier_landingpag_services_column_three_icon_2d74f9eb; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_landingpag_services_column_three_icon_2d74f9eb ON public.find_a_supplier_landingpage USING btree (services_column_three_icon_zh_hans_id);


--
-- Name: find_a_supplier_landingpag_services_column_three_icon_3332bd7a; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_landingpag_services_column_three_icon_3332bd7a ON public.find_a_supplier_landingpage USING btree (services_column_three_icon_ar_id);


--
-- Name: find_a_supplier_landingpag_services_column_three_icon_60905b76; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_landingpag_services_column_three_icon_60905b76 ON public.find_a_supplier_landingpage USING btree (services_column_three_icon_ja_id);


--
-- Name: find_a_supplier_landingpag_services_column_three_icon_70034717; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_landingpag_services_column_three_icon_70034717 ON public.find_a_supplier_landingpage USING btree (services_column_three_icon_es_id);


--
-- Name: find_a_supplier_landingpag_services_column_three_icon_7bb2e58b; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_landingpag_services_column_three_icon_7bb2e58b ON public.find_a_supplier_landingpage USING btree (services_column_three_icon_ru_id);


--
-- Name: find_a_supplier_landingpag_services_column_three_icon_ae7ddbb5; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_landingpag_services_column_three_icon_ae7ddbb5 ON public.find_a_supplier_landingpage USING btree (services_column_three_icon_pt_br_id);


--
-- Name: find_a_supplier_landingpag_services_column_three_icon_b2bd5ecc; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_landingpag_services_column_three_icon_b2bd5ecc ON public.find_a_supplier_landingpage USING btree (services_column_three_icon_id);


--
-- Name: find_a_supplier_landingpag_services_column_three_icon_b8fe2d12; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_landingpag_services_column_three_icon_b8fe2d12 ON public.find_a_supplier_landingpage USING btree (services_column_three_icon_fr_id);


--
-- Name: find_a_supplier_landingpag_services_column_three_icon_d6066d52; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_landingpag_services_column_three_icon_d6066d52 ON public.find_a_supplier_landingpage USING btree (services_column_three_icon_pt_id);


--
-- Name: find_a_supplier_landingpag_services_column_three_icon_dbeb4fd6; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_landingpag_services_column_three_icon_dbeb4fd6 ON public.find_a_supplier_landingpage USING btree (services_column_three_icon_de_id);


--
-- Name: find_a_supplier_landingpag_services_column_three_icon_de7a7533; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_landingpag_services_column_three_icon_de7a7533 ON public.find_a_supplier_landingpage USING btree (services_column_three_icon_en_gb_id);


--
-- Name: find_a_supplier_landingpag_services_column_two_icon_a_f8e32d2f; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_landingpag_services_column_two_icon_a_f8e32d2f ON public.find_a_supplier_landingpage USING btree (services_column_two_icon_ar_id);


--
-- Name: find_a_supplier_landingpag_services_column_two_icon_d_3119d3f7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_landingpag_services_column_two_icon_d_3119d3f7 ON public.find_a_supplier_landingpage USING btree (services_column_two_icon_de_id);


--
-- Name: find_a_supplier_landingpag_services_column_two_icon_e_3e1f0de4; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_landingpag_services_column_two_icon_e_3e1f0de4 ON public.find_a_supplier_landingpage USING btree (services_column_two_icon_en_gb_id);


--
-- Name: find_a_supplier_landingpag_services_column_two_icon_e_ece32492; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_landingpag_services_column_two_icon_e_ece32492 ON public.find_a_supplier_landingpage USING btree (services_column_two_icon_es_id);


--
-- Name: find_a_supplier_landingpag_services_column_two_icon_f_f4ac7f00; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_landingpag_services_column_two_icon_f_f4ac7f00 ON public.find_a_supplier_landingpage USING btree (services_column_two_icon_fr_id);


--
-- Name: find_a_supplier_landingpag_services_column_two_icon_i_76cf917f; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_landingpag_services_column_two_icon_i_76cf917f ON public.find_a_supplier_landingpage USING btree (services_column_two_icon_id);


--
-- Name: find_a_supplier_landingpag_services_column_two_icon_j_43e311fb; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_landingpag_services_column_two_icon_j_43e311fb ON public.find_a_supplier_landingpage USING btree (services_column_two_icon_ja_id);


--
-- Name: find_a_supplier_landingpag_services_column_two_icon_p_a437d62f; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_landingpag_services_column_two_icon_p_a437d62f ON public.find_a_supplier_landingpage USING btree (services_column_two_icon_pt_br_id);


--
-- Name: find_a_supplier_landingpag_services_column_two_icon_p_bafd2caf; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_landingpag_services_column_two_icon_p_bafd2caf ON public.find_a_supplier_landingpage USING btree (services_column_two_icon_pt_id);


--
-- Name: find_a_supplier_landingpag_services_column_two_icon_r_0add801a; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_landingpag_services_column_two_icon_r_0add801a ON public.find_a_supplier_landingpage USING btree (services_column_two_icon_ru_id);


--
-- Name: find_a_supplier_landingpag_services_column_two_icon_z_7699d7e0; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_landingpag_services_column_two_icon_z_7699d7e0 ON public.find_a_supplier_landingpage USING btree (services_column_two_icon_zh_hans_id);


--
-- Name: find_a_supplier_landingpag_video_media_id_1bdc3add; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_landingpag_video_media_id_1bdc3add ON public.find_a_supplier_landingpagearticlesummary USING btree (video_media_id);


--
-- Name: find_a_supplier_landingpage_hero_image_id_76d06f77; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_landingpage_hero_image_id_76d06f77 ON public.find_a_supplier_landingpage USING btree (hero_image_id);


--
-- Name: find_a_supplier_landingpage_mobile_hero_image_id_2122ccb4; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_landingpage_mobile_hero_image_id_2122ccb4 ON public.find_a_supplier_landingpage USING btree (mobile_hero_image_id);


--
-- Name: find_a_supplier_landingpage_service_name_42d6fd2b; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_landingpage_service_name_42d6fd2b ON public.find_a_supplier_landingpage USING btree (service_name);


--
-- Name: find_a_supplier_landingpage_service_name_42d6fd2b_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_landingpage_service_name_42d6fd2b_like ON public.find_a_supplier_landingpage USING btree (service_name varchar_pattern_ops);


--
-- Name: find_a_supplier_landingpagearticlesummary_image_id_8a5fff5e; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_landingpagearticlesummary_image_id_8a5fff5e ON public.find_a_supplier_landingpagearticlesummary USING btree (image_id);


--
-- Name: find_a_supplier_landingpagearticlesummary_page_ar_id_b92c3bde; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_landingpagearticlesummary_page_ar_id_b92c3bde ON public.find_a_supplier_landingpagearticlesummary USING btree (page_ar_id);


--
-- Name: find_a_supplier_landingpagearticlesummary_page_de_id_10c841d1; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_landingpagearticlesummary_page_de_id_10c841d1 ON public.find_a_supplier_landingpagearticlesummary USING btree (page_de_id);


--
-- Name: find_a_supplier_landingpagearticlesummary_page_es_id_67b4a39b; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_landingpagearticlesummary_page_es_id_67b4a39b ON public.find_a_supplier_landingpagearticlesummary USING btree (page_es_id);


--
-- Name: find_a_supplier_landingpagearticlesummary_page_fr_id_b14ec81b; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_landingpagearticlesummary_page_fr_id_b14ec81b ON public.find_a_supplier_landingpagearticlesummary USING btree (page_fr_id);


--
-- Name: find_a_supplier_landingpagearticlesummary_page_id_18f6123b; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_landingpagearticlesummary_page_id_18f6123b ON public.find_a_supplier_landingpagearticlesummary USING btree (page_id);


--
-- Name: find_a_supplier_landingpagearticlesummary_page_ja_id_551b0c52; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_landingpagearticlesummary_page_ja_id_551b0c52 ON public.find_a_supplier_landingpagearticlesummary USING btree (page_ja_id);


--
-- Name: find_a_supplier_landingpagearticlesummary_page_pt_id_1e3fe6a9; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_landingpagearticlesummary_page_pt_id_1e3fe6a9 ON public.find_a_supplier_landingpagearticlesummary USING btree (page_pt_id);


--
-- Name: find_a_supplier_landingpagearticlesummary_page_ru_id_51fd06ed; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX find_a_supplier_landingpagearticlesummary_page_ru_id_51fd06ed ON public.find_a_supplier_landingpagearticlesummary USING btree (page_ru_id);


--
-- Name: great_international_grea_service_name_ff378121_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX great_international_grea_service_name_ff378121_like ON public.great_international_greatinternationalapp USING btree (service_name varchar_pattern_ops);


--
-- Name: great_international_greatinternationalapp_service_name_ff378121; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX great_international_greatinternationalapp_service_name_ff378121 ON public.great_international_greatinternationalapp USING btree (service_name);


--
-- Name: great_international_inte_service_name_001ec2eb_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX great_international_inte_service_name_001ec2eb_like ON public.great_international_internationalarticlelistingpage USING btree (service_name varchar_pattern_ops);


--
-- Name: great_international_inte_service_name_3d23455a_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX great_international_inte_service_name_3d23455a_like ON public.great_international_internationalregionpage USING btree (service_name varchar_pattern_ops);


--
-- Name: great_international_inte_service_name_59e6aa97_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX great_international_inte_service_name_59e6aa97_like ON public.great_international_internationaltopiclandingpage USING btree (service_name varchar_pattern_ops);


--
-- Name: great_international_inte_service_name_5f67f13e_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX great_international_inte_service_name_5f67f13e_like ON public.great_international_internationalarticlepage USING btree (service_name varchar_pattern_ops);


--
-- Name: great_international_inte_service_name_736346c0_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX great_international_inte_service_name_736346c0_like ON public.great_international_internationalcampaignpage USING btree (service_name varchar_pattern_ops);


--
-- Name: great_international_inte_service_name_86db7b04_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX great_international_inte_service_name_86db7b04_like ON public.great_international_internationalsectorpage USING btree (service_name varchar_pattern_ops);


--
-- Name: great_international_inte_service_name_a3e6c700_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX great_international_inte_service_name_a3e6c700_like ON public.great_international_internationalhomepage USING btree (service_name varchar_pattern_ops);


--
-- Name: great_international_inte_service_name_f6601488_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX great_international_inte_service_name_f6601488_like ON public.great_international_internationallocalisedfolderpage USING btree (service_name varchar_pattern_ops);


--
-- Name: great_international_intern_article_image_id_aa9240b3; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX great_international_intern_article_image_id_aa9240b3 ON public.great_international_internationalarticlepage USING btree (article_image_id);


--
-- Name: great_international_intern_campaign_hero_image_id_7170da9a; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX great_international_intern_campaign_hero_image_id_7170da9a ON public.great_international_internationalcampaignpage USING btree (campaign_hero_image_id);


--
-- Name: great_international_intern_case_study_image_id_6d174391; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX great_international_intern_case_study_image_id_6d174391 ON public.great_international_internationalsectorpage USING btree (case_study_image_id);


--
-- Name: great_international_intern_hero_image_id_2e7c0845; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX great_international_intern_hero_image_id_2e7c0845 ON public.great_international_internationaltopiclandingpage USING btree (hero_image_id);


--
-- Name: great_international_intern_hero_image_id_995757cb; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX great_international_intern_hero_image_id_995757cb ON public.great_international_internationalsectorpage USING btree (hero_image_id);


--
-- Name: great_international_intern_hero_image_id_bc57f482; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX great_international_intern_hero_image_id_bc57f482 ON public.great_international_internationalarticlelistingpage USING btree (hero_image_id);


--
-- Name: great_international_intern_internationalarticlelistin_33df4cd4; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX great_international_intern_internationalarticlelistin_33df4cd4 ON public.great_international_internationalarticlelistingpage_tags USING btree (internationalarticlelistingpage_id);


--
-- Name: great_international_intern_internationalarticlepage_i_92b154aa; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX great_international_intern_internationalarticlepage_i_92b154aa ON public.great_international_internationalarticlepage_tags USING btree (internationalarticlepage_id);


--
-- Name: great_international_intern_internationalcampaignpage__1475a34f; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX great_international_intern_internationalcampaignpage__1475a34f ON public.great_international_internationalcampaignpage_tags USING btree (internationalcampaignpage_id);


--
-- Name: great_international_intern_internationalregionpages_i_45b2ad27; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX great_international_intern_internationalregionpages_i_45b2ad27 ON public.great_international_internationalregionpage_tags USING btree (internationalregionpage_id);


--
-- Name: great_international_intern_internationaltopiclandingp_6cf777f6; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX great_international_intern_internationaltopiclandingp_6cf777f6 ON public.great_international_internationaltopiclandingpage_tags USING btree (internationaltopiclandingpage_id);


--
-- Name: great_international_intern_related_page_one_id_181b10cd; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX great_international_intern_related_page_one_id_181b10cd ON public.great_international_internationalsectorpage USING btree (related_page_one_id);


--
-- Name: great_international_intern_related_page_one_id_38d9eafc; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX great_international_intern_related_page_one_id_38d9eafc ON public.great_international_internationalhomepage USING btree (related_page_one_id);


--
-- Name: great_international_intern_related_page_one_id_a843bb9e; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX great_international_intern_related_page_one_id_a843bb9e ON public.great_international_internationalarticlepage USING btree (related_page_one_id);


--
-- Name: great_international_intern_related_page_one_id_b5973886; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX great_international_intern_related_page_one_id_b5973886 ON public.great_international_internationalcampaignpage USING btree (related_page_one_id);


--
-- Name: great_international_intern_related_page_three_id_7da7da1a; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX great_international_intern_related_page_three_id_7da7da1a ON public.great_international_internationalcampaignpage USING btree (related_page_three_id);


--
-- Name: great_international_intern_related_page_three_id_c1182ff1; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX great_international_intern_related_page_three_id_c1182ff1 ON public.great_international_internationalarticlepage USING btree (related_page_three_id);


--
-- Name: great_international_intern_related_page_three_id_c3943fa9; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX great_international_intern_related_page_three_id_c3943fa9 ON public.great_international_internationalhomepage USING btree (related_page_three_id);


--
-- Name: great_international_intern_related_page_three_id_da3ce1ef; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX great_international_intern_related_page_three_id_da3ce1ef ON public.great_international_internationalsectorpage USING btree (related_page_three_id);


--
-- Name: great_international_intern_related_page_two_id_92e5cf67; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX great_international_intern_related_page_two_id_92e5cf67 ON public.great_international_internationalarticlepage USING btree (related_page_two_id);


--
-- Name: great_international_intern_related_page_two_id_a578a749; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX great_international_intern_related_page_two_id_a578a749 ON public.great_international_internationalsectorpage USING btree (related_page_two_id);


--
-- Name: great_international_intern_related_page_two_id_ae88f175; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX great_international_intern_related_page_two_id_ae88f175 ON public.great_international_internationalcampaignpage USING btree (related_page_two_id);


--
-- Name: great_international_intern_related_page_two_id_da4f8c42; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX great_international_intern_related_page_two_id_da4f8c42 ON public.great_international_internationalhomepage USING btree (related_page_two_id);


--
-- Name: great_international_intern_section_one_image_id_6de74989; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX great_international_intern_section_one_image_id_6de74989 ON public.great_international_internationalsectorpage USING btree (section_one_image_id);


--
-- Name: great_international_intern_section_one_image_id_84c75b25; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX great_international_intern_section_one_image_id_84c75b25 ON public.great_international_internationalcampaignpage USING btree (section_one_image_id);


--
-- Name: great_international_intern_section_two_image_id_95d17c97; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX great_international_intern_section_two_image_id_95d17c97 ON public.great_international_internationalcampaignpage USING btree (section_two_image_id);


--
-- Name: great_international_intern_section_two_subsection_one_7646efd8; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX great_international_intern_section_two_subsection_one_7646efd8 ON public.great_international_internationalsectorpage USING btree (section_two_subsection_one_icon_id);


--
-- Name: great_international_intern_section_two_subsection_thr_fe5dfaf4; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX great_international_intern_section_two_subsection_thr_fe5dfaf4 ON public.great_international_internationalsectorpage USING btree (section_two_subsection_three_icon_id);


--
-- Name: great_international_intern_section_two_subsection_two_9c130204; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX great_international_intern_section_two_subsection_two_9c130204 ON public.great_international_internationalsectorpage USING btree (section_two_subsection_two_icon_id);


--
-- Name: great_international_intern_selling_point_one_icon_id_100503e1; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX great_international_intern_selling_point_one_icon_id_100503e1 ON public.great_international_internationalcampaignpage USING btree (selling_point_one_icon_id);


--
-- Name: great_international_intern_selling_point_three_icon_i_94d54bb6; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX great_international_intern_selling_point_three_icon_i_94d54bb6 ON public.great_international_internationalcampaignpage USING btree (selling_point_three_icon_id);


--
-- Name: great_international_intern_selling_point_two_icon_id_ca530800; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX great_international_intern_selling_point_two_icon_id_ca530800 ON public.great_international_internationalcampaignpage USING btree (selling_point_two_icon_id);


--
-- Name: great_international_intern_service_name_001ec2eb; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX great_international_intern_service_name_001ec2eb ON public.great_international_internationalarticlelistingpage USING btree (service_name);


--
-- Name: great_international_intern_service_name_3d23455a; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX great_international_intern_service_name_3d23455a ON public.great_international_internationalregionpage USING btree (service_name);


--
-- Name: great_international_intern_service_name_59e6aa97; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX great_international_intern_service_name_59e6aa97 ON public.great_international_internationaltopiclandingpage USING btree (service_name);


--
-- Name: great_international_intern_service_name_5f67f13e; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX great_international_intern_service_name_5f67f13e ON public.great_international_internationalarticlepage USING btree (service_name);


--
-- Name: great_international_intern_service_name_736346c0; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX great_international_intern_service_name_736346c0 ON public.great_international_internationalcampaignpage USING btree (service_name);


--
-- Name: great_international_intern_service_name_86db7b04; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX great_international_intern_service_name_86db7b04 ON public.great_international_internationalsectorpage USING btree (service_name);


--
-- Name: great_international_intern_service_name_f6601488; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX great_international_intern_service_name_f6601488 ON public.great_international_internationallocalisedfolderpage USING btree (service_name);


--
-- Name: great_international_intern_tag_id_1f99e22b; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX great_international_intern_tag_id_1f99e22b ON public.great_international_internationalcampaignpage_tags USING btree (tag_id);


--
-- Name: great_international_intern_tag_id_27c1d52c; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX great_international_intern_tag_id_27c1d52c ON public.great_international_internationalarticlelistingpage_tags USING btree (tag_id);


--
-- Name: great_international_intern_tag_id_4f3127d9; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX great_international_intern_tag_id_4f3127d9 ON public.great_international_internationaltopiclandingpage_tags USING btree (tag_id);


--
-- Name: great_international_intern_tag_id_717bde30; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX great_international_intern_tag_id_717bde30 ON public.great_international_internationalregionpage_tags USING btree (tag_id);


--
-- Name: great_international_intern_tag_id_e4984ba1; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX great_international_intern_tag_id_e4984ba1 ON public.great_international_internationalarticlepage_tags USING btree (tag_id);


--
-- Name: great_international_intern_tariffs_image_id_c84156ca; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX great_international_intern_tariffs_image_id_c84156ca ON public.great_international_internationalhomepage USING btree (tariffs_image_id);


--
-- Name: great_international_internationalhomepage_service_name_a3e6c700; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX great_international_internationalhomepage_service_name_a3e6c700 ON public.great_international_internationalhomepage USING btree (service_name);


--
-- Name: invest_highpotentialofferformpage_service_name_b36e932d; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_highpotentialofferformpage_service_name_b36e932d ON public.invest_highpotentialopportunityformpage USING btree (service_name);


--
-- Name: invest_highpotentialofferformpage_service_name_b36e932d_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_highpotentialofferformpage_service_name_b36e932d_like ON public.invest_highpotentialopportunityformpage USING btree (service_name varchar_pattern_ops);


--
-- Name: invest_highpotentialoppo_service_name_359394a4_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_highpotentialoppo_service_name_359394a4_like ON public.invest_highpotentialopportunitydetailpage USING btree (service_name varchar_pattern_ops);


--
-- Name: invest_highpotentialoppo_service_name_8c856d1c_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_highpotentialoppo_service_name_8c856d1c_like ON public.invest_highpotentialopportunityformsuccesspage USING btree (service_name varchar_pattern_ops);


--
-- Name: invest_highpotentialopport_case_study_four_image_id_7d6ba663; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_highpotentialopport_case_study_four_image_id_7d6ba663 ON public.invest_highpotentialopportunitydetailpage USING btree (case_study_four_image_id);


--
-- Name: invest_highpotentialopport_case_study_one_image_id_ba757ba9; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_highpotentialopport_case_study_one_image_id_ba757ba9 ON public.invest_highpotentialopportunitydetailpage USING btree (case_study_one_image_id);


--
-- Name: invest_highpotentialopport_case_study_three_image_id_034f8a93; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_highpotentialopport_case_study_three_image_id_034f8a93 ON public.invest_highpotentialopportunitydetailpage USING btree (case_study_three_image_id);


--
-- Name: invest_highpotentialopport_case_study_two_image_id_7765394b; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_highpotentialopport_case_study_two_image_id_7765394b ON public.invest_highpotentialopportunitydetailpage USING btree (case_study_two_image_id);


--
-- Name: invest_highpotentialopport_companies_list_item_image__24ac23e1; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_highpotentialopport_companies_list_item_image__24ac23e1 ON public.invest_highpotentialopportunitydetailpage USING btree (companies_list_item_image_seven_id);


--
-- Name: invest_highpotentialopport_companies_list_item_image__607e453f; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_highpotentialopport_companies_list_item_image__607e453f ON public.invest_highpotentialopportunitydetailpage USING btree (companies_list_item_image_five_id);


--
-- Name: invest_highpotentialopport_companies_list_item_image__689352eb; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_highpotentialopport_companies_list_item_image__689352eb ON public.invest_highpotentialopportunitydetailpage USING btree (companies_list_item_image_eight_id);


--
-- Name: invest_highpotentialopport_companies_list_item_image__69535e2d; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_highpotentialopport_companies_list_item_image__69535e2d ON public.invest_highpotentialopportunitydetailpage USING btree (companies_list_item_image_one_id);


--
-- Name: invest_highpotentialopport_companies_list_item_image__6c22af18; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_highpotentialopport_companies_list_item_image__6c22af18 ON public.invest_highpotentialopportunitydetailpage USING btree (companies_list_item_image_three_id);


--
-- Name: invest_highpotentialopport_companies_list_item_image__c4205164; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_highpotentialopport_companies_list_item_image__c4205164 ON public.invest_highpotentialopportunitydetailpage USING btree (companies_list_item_image_six_id);


--
-- Name: invest_highpotentialopport_companies_list_item_image__e511f30b; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_highpotentialopport_companies_list_item_image__e511f30b ON public.invest_highpotentialopportunitydetailpage USING btree (companies_list_item_image_two_id);


--
-- Name: invest_highpotentialopport_companies_list_item_image__f59bbf99; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_highpotentialopport_companies_list_item_image__f59bbf99 ON public.invest_highpotentialopportunitydetailpage USING btree (companies_list_item_image_four_id);


--
-- Name: invest_highpotentialopport_competitive_advantages_lis_33a2dcf6; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_highpotentialopport_competitive_advantages_lis_33a2dcf6 ON public.invest_highpotentialopportunitydetailpage USING btree (competitive_advantages_list_item_one_icon_id);


--
-- Name: invest_highpotentialopport_competitive_advantages_lis_89da55bd; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_highpotentialopport_competitive_advantages_lis_89da55bd ON public.invest_highpotentialopportunitydetailpage USING btree (competitive_advantages_list_item_two_icon_id);


--
-- Name: invest_highpotentialopport_competitive_advantages_lis_9555f962; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_highpotentialopport_competitive_advantages_lis_9555f962 ON public.invest_highpotentialopportunitydetailpage USING btree (competitive_advantages_list_item_three_icon_id);


--
-- Name: invest_highpotentialopport_hero_image_id_39933ff3; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_highpotentialopport_hero_image_id_39933ff3 ON public.invest_highpotentialopportunitydetailpage USING btree (hero_image_id);


--
-- Name: invest_highpotentialopport_opportunity_list_image_id_39bfbdee; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_highpotentialopport_opportunity_list_image_id_39bfbdee ON public.invest_highpotentialopportunitydetailpage USING btree (opportunity_list_image_id);


--
-- Name: invest_highpotentialopport_pdf_document_id_7452b06c; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_highpotentialopport_pdf_document_id_7452b06c ON public.invest_highpotentialopportunitydetailpage USING btree (pdf_document_id);


--
-- Name: invest_highpotentialopport_proposition_one_image_id_3cb62d0e; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_highpotentialopport_proposition_one_image_id_3cb62d0e ON public.invest_highpotentialopportunitydetailpage USING btree (proposition_one_image_id);


--
-- Name: invest_highpotentialopport_proposition_one_video_id_ee82eb9b; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_highpotentialopport_proposition_one_video_id_ee82eb9b ON public.invest_highpotentialopportunitydetailpage USING btree (proposition_one_video_id);


--
-- Name: invest_highpotentialopport_proposition_two_image_id_16381e09; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_highpotentialopport_proposition_two_image_id_16381e09 ON public.invest_highpotentialopportunitydetailpage USING btree (proposition_two_image_id);


--
-- Name: invest_highpotentialopport_proposition_two_video_id_81ed7649; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_highpotentialopport_proposition_two_video_id_81ed7649 ON public.invest_highpotentialopportunitydetailpage USING btree (proposition_two_video_id);


--
-- Name: invest_highpotentialopport_service_name_8c856d1c; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_highpotentialopport_service_name_8c856d1c ON public.invest_highpotentialopportunityformsuccesspage USING btree (service_name);


--
-- Name: invest_highpotentialopport_summary_image_id_2687e608; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_highpotentialopport_summary_image_id_2687e608 ON public.invest_highpotentialopportunitydetailpage USING btree (summary_image_id);


--
-- Name: invest_highpotentialopport_testimonial_background_id_438c0bf6; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_highpotentialopport_testimonial_background_id_438c0bf6 ON public.invest_highpotentialopportunitydetailpage USING btree (testimonial_background_id);


--
-- Name: invest_highpotentialopportunitydetailpage_service_name_359394a4; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_highpotentialopportunitydetailpage_service_name_359394a4 ON public.invest_highpotentialopportunitydetailpage USING btree (service_name);


--
-- Name: invest_infopage_service_name_e404a6f3; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_infopage_service_name_e404a6f3 ON public.invest_infopage USING btree (service_name);


--
-- Name: invest_infopage_service_name_e404a6f3_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_infopage_service_name_e404a6f3_like ON public.invest_infopage USING btree (service_name varchar_pattern_ops);


--
-- Name: invest_investapp_service_name_ec233209; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_investapp_service_name_ec233209 ON public.invest_investapp USING btree (service_name);


--
-- Name: invest_investapp_service_name_ec233209_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_investapp_service_name_ec233209_like ON public.invest_investapp USING btree (service_name varchar_pattern_ops);


--
-- Name: invest_investhomepage_hero_image_id_a2dbcafe; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_investhomepage_hero_image_id_a2dbcafe ON public.invest_investhomepage USING btree (hero_image_id);


--
-- Name: invest_investhomepage_how_we_help_icon_five_ar_id_8ec5c27a; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_investhomepage_how_we_help_icon_five_ar_id_8ec5c27a ON public.invest_investhomepage USING btree (how_we_help_icon_five_ar_id);


--
-- Name: invest_investhomepage_how_we_help_icon_five_de_id_b2ed9b3b; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_investhomepage_how_we_help_icon_five_de_id_b2ed9b3b ON public.invest_investhomepage USING btree (how_we_help_icon_five_de_id);


--
-- Name: invest_investhomepage_how_we_help_icon_five_en_gb_id_9e5eb318; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_investhomepage_how_we_help_icon_five_en_gb_id_9e5eb318 ON public.invest_investhomepage USING btree (how_we_help_icon_five_en_gb_id);


--
-- Name: invest_investhomepage_how_we_help_icon_five_es_id_f37325cd; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_investhomepage_how_we_help_icon_five_es_id_f37325cd ON public.invest_investhomepage USING btree (how_we_help_icon_five_es_id);


--
-- Name: invest_investhomepage_how_we_help_icon_five_fr_id_5f4b6bfe; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_investhomepage_how_we_help_icon_five_fr_id_5f4b6bfe ON public.invest_investhomepage USING btree (how_we_help_icon_five_fr_id);


--
-- Name: invest_investhomepage_how_we_help_icon_five_id_74a7d91a; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_investhomepage_how_we_help_icon_five_id_74a7d91a ON public.invest_investhomepage USING btree (how_we_help_icon_five_id);


--
-- Name: invest_investhomepage_how_we_help_icon_five_ja_id_c8f0a784; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_investhomepage_how_we_help_icon_five_ja_id_c8f0a784 ON public.invest_investhomepage USING btree (how_we_help_icon_five_ja_id);


--
-- Name: invest_investhomepage_how_we_help_icon_five_pt_br_id_f1712768; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_investhomepage_how_we_help_icon_five_pt_br_id_f1712768 ON public.invest_investhomepage USING btree (how_we_help_icon_five_pt_br_id);


--
-- Name: invest_investhomepage_how_we_help_icon_five_pt_id_f452675a; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_investhomepage_how_we_help_icon_five_pt_id_f452675a ON public.invest_investhomepage USING btree (how_we_help_icon_five_pt_id);


--
-- Name: invest_investhomepage_how_we_help_icon_five_ru_id_569e774c; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_investhomepage_how_we_help_icon_five_ru_id_569e774c ON public.invest_investhomepage USING btree (how_we_help_icon_five_ru_id);


--
-- Name: invest_investhomepage_how_we_help_icon_five_zh_hans_id_fde8f74c; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_investhomepage_how_we_help_icon_five_zh_hans_id_fde8f74c ON public.invest_investhomepage USING btree (how_we_help_icon_five_zh_hans_id);


--
-- Name: invest_investhomepage_how_we_help_icon_four_ar_id_79c301b7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_investhomepage_how_we_help_icon_four_ar_id_79c301b7 ON public.invest_investhomepage USING btree (how_we_help_icon_four_ar_id);


--
-- Name: invest_investhomepage_how_we_help_icon_four_de_id_50a9e52a; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_investhomepage_how_we_help_icon_four_de_id_50a9e52a ON public.invest_investhomepage USING btree (how_we_help_icon_four_de_id);


--
-- Name: invest_investhomepage_how_we_help_icon_four_en_gb_id_73bcef52; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_investhomepage_how_we_help_icon_four_en_gb_id_73bcef52 ON public.invest_investhomepage USING btree (how_we_help_icon_four_en_gb_id);


--
-- Name: invest_investhomepage_how_we_help_icon_four_es_id_4e58c507; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_investhomepage_how_we_help_icon_four_es_id_4e58c507 ON public.invest_investhomepage USING btree (how_we_help_icon_four_es_id);


--
-- Name: invest_investhomepage_how_we_help_icon_four_fr_id_30fc166d; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_investhomepage_how_we_help_icon_four_fr_id_30fc166d ON public.invest_investhomepage USING btree (how_we_help_icon_four_fr_id);


--
-- Name: invest_investhomepage_how_we_help_icon_four_id_15ee206d; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_investhomepage_how_we_help_icon_four_id_15ee206d ON public.invest_investhomepage USING btree (how_we_help_icon_four_id);


--
-- Name: invest_investhomepage_how_we_help_icon_four_ja_id_ddda13d6; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_investhomepage_how_we_help_icon_four_ja_id_ddda13d6 ON public.invest_investhomepage USING btree (how_we_help_icon_four_ja_id);


--
-- Name: invest_investhomepage_how_we_help_icon_four_pt_br_id_eb716ad6; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_investhomepage_how_we_help_icon_four_pt_br_id_eb716ad6 ON public.invest_investhomepage USING btree (how_we_help_icon_four_pt_br_id);


--
-- Name: invest_investhomepage_how_we_help_icon_four_pt_id_6cc9c5ef; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_investhomepage_how_we_help_icon_four_pt_id_6cc9c5ef ON public.invest_investhomepage USING btree (how_we_help_icon_four_pt_id);


--
-- Name: invest_investhomepage_how_we_help_icon_four_ru_id_cd433b63; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_investhomepage_how_we_help_icon_four_ru_id_cd433b63 ON public.invest_investhomepage USING btree (how_we_help_icon_four_ru_id);


--
-- Name: invest_investhomepage_how_we_help_icon_four_zh_hans_id_2288cb1b; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_investhomepage_how_we_help_icon_four_zh_hans_id_2288cb1b ON public.invest_investhomepage USING btree (how_we_help_icon_four_zh_hans_id);


--
-- Name: invest_investhomepage_how_we_help_icon_one_ar_id_1751478c; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_investhomepage_how_we_help_icon_one_ar_id_1751478c ON public.invest_investhomepage USING btree (how_we_help_icon_one_ar_id);


--
-- Name: invest_investhomepage_how_we_help_icon_one_de_id_e00c070c; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_investhomepage_how_we_help_icon_one_de_id_e00c070c ON public.invest_investhomepage USING btree (how_we_help_icon_one_de_id);


--
-- Name: invest_investhomepage_how_we_help_icon_one_en_gb_id_b56f7c81; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_investhomepage_how_we_help_icon_one_en_gb_id_b56f7c81 ON public.invest_investhomepage USING btree (how_we_help_icon_one_en_gb_id);


--
-- Name: invest_investhomepage_how_we_help_icon_one_es_id_933d6db7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_investhomepage_how_we_help_icon_one_es_id_933d6db7 ON public.invest_investhomepage USING btree (how_we_help_icon_one_es_id);


--
-- Name: invest_investhomepage_how_we_help_icon_one_fr_id_26bdd075; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_investhomepage_how_we_help_icon_one_fr_id_26bdd075 ON public.invest_investhomepage USING btree (how_we_help_icon_one_fr_id);


--
-- Name: invest_investhomepage_how_we_help_icon_one_id_aa76d159; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_investhomepage_how_we_help_icon_one_id_aa76d159 ON public.invest_investhomepage USING btree (how_we_help_icon_one_id);


--
-- Name: invest_investhomepage_how_we_help_icon_one_ja_id_8fdb9362; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_investhomepage_how_we_help_icon_one_ja_id_8fdb9362 ON public.invest_investhomepage USING btree (how_we_help_icon_one_ja_id);


--
-- Name: invest_investhomepage_how_we_help_icon_one_pt_br_id_a3afab67; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_investhomepage_how_we_help_icon_one_pt_br_id_a3afab67 ON public.invest_investhomepage USING btree (how_we_help_icon_one_pt_br_id);


--
-- Name: invest_investhomepage_how_we_help_icon_one_pt_id_fcfe99e1; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_investhomepage_how_we_help_icon_one_pt_id_fcfe99e1 ON public.invest_investhomepage USING btree (how_we_help_icon_one_pt_id);


--
-- Name: invest_investhomepage_how_we_help_icon_one_ru_id_4bd58fed; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_investhomepage_how_we_help_icon_one_ru_id_4bd58fed ON public.invest_investhomepage USING btree (how_we_help_icon_one_ru_id);


--
-- Name: invest_investhomepage_how_we_help_icon_one_zh_hans_id_97d549f8; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_investhomepage_how_we_help_icon_one_zh_hans_id_97d549f8 ON public.invest_investhomepage USING btree (how_we_help_icon_one_zh_hans_id);


--
-- Name: invest_investhomepage_how_we_help_icon_three_ar_id_71bb8a0b; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_investhomepage_how_we_help_icon_three_ar_id_71bb8a0b ON public.invest_investhomepage USING btree (how_we_help_icon_three_ar_id);


--
-- Name: invest_investhomepage_how_we_help_icon_three_de_id_e9e51dbe; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_investhomepage_how_we_help_icon_three_de_id_e9e51dbe ON public.invest_investhomepage USING btree (how_we_help_icon_three_de_id);


--
-- Name: invest_investhomepage_how_we_help_icon_three_en_gb_id_22772f5b; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_investhomepage_how_we_help_icon_three_en_gb_id_22772f5b ON public.invest_investhomepage USING btree (how_we_help_icon_three_en_gb_id);


--
-- Name: invest_investhomepage_how_we_help_icon_three_es_id_9e98bdfd; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_investhomepage_how_we_help_icon_three_es_id_9e98bdfd ON public.invest_investhomepage USING btree (how_we_help_icon_three_es_id);


--
-- Name: invest_investhomepage_how_we_help_icon_three_fr_id_a08f8272; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_investhomepage_how_we_help_icon_three_fr_id_a08f8272 ON public.invest_investhomepage USING btree (how_we_help_icon_three_fr_id);


--
-- Name: invest_investhomepage_how_we_help_icon_three_id_e0c8e962; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_investhomepage_how_we_help_icon_three_id_e0c8e962 ON public.invest_investhomepage USING btree (how_we_help_icon_three_id);


--
-- Name: invest_investhomepage_how_we_help_icon_three_ja_id_ee1b291e; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_investhomepage_how_we_help_icon_three_ja_id_ee1b291e ON public.invest_investhomepage USING btree (how_we_help_icon_three_ja_id);


--
-- Name: invest_investhomepage_how_we_help_icon_three_pt_br_id_e8b61047; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_investhomepage_how_we_help_icon_three_pt_br_id_e8b61047 ON public.invest_investhomepage USING btree (how_we_help_icon_three_pt_br_id);


--
-- Name: invest_investhomepage_how_we_help_icon_three_pt_id_7e9a29db; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_investhomepage_how_we_help_icon_three_pt_id_7e9a29db ON public.invest_investhomepage USING btree (how_we_help_icon_three_pt_id);


--
-- Name: invest_investhomepage_how_we_help_icon_three_ru_id_b415bb95; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_investhomepage_how_we_help_icon_three_ru_id_b415bb95 ON public.invest_investhomepage USING btree (how_we_help_icon_three_ru_id);


--
-- Name: invest_investhomepage_how_we_help_icon_three_zh__0bdefab5; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_investhomepage_how_we_help_icon_three_zh__0bdefab5 ON public.invest_investhomepage USING btree (how_we_help_icon_three_zh_hans_id);


--
-- Name: invest_investhomepage_how_we_help_icon_two_ar_id_5dfa1ff1; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_investhomepage_how_we_help_icon_two_ar_id_5dfa1ff1 ON public.invest_investhomepage USING btree (how_we_help_icon_two_ar_id);


--
-- Name: invest_investhomepage_how_we_help_icon_two_de_id_129f3373; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_investhomepage_how_we_help_icon_two_de_id_129f3373 ON public.invest_investhomepage USING btree (how_we_help_icon_two_de_id);


--
-- Name: invest_investhomepage_how_we_help_icon_two_en_gb_id_cd7f08a1; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_investhomepage_how_we_help_icon_two_en_gb_id_cd7f08a1 ON public.invest_investhomepage USING btree (how_we_help_icon_two_en_gb_id);


--
-- Name: invest_investhomepage_how_we_help_icon_two_es_id_1abb4bdd; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_investhomepage_how_we_help_icon_two_es_id_1abb4bdd ON public.invest_investhomepage USING btree (how_we_help_icon_two_es_id);


--
-- Name: invest_investhomepage_how_we_help_icon_two_fr_id_e5fd145e; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_investhomepage_how_we_help_icon_two_fr_id_e5fd145e ON public.invest_investhomepage USING btree (how_we_help_icon_two_fr_id);


--
-- Name: invest_investhomepage_how_we_help_icon_two_id_96bb49e3; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_investhomepage_how_we_help_icon_two_id_96bb49e3 ON public.invest_investhomepage USING btree (how_we_help_icon_two_id);


--
-- Name: invest_investhomepage_how_we_help_icon_two_ja_id_5fd75f90; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_investhomepage_how_we_help_icon_two_ja_id_5fd75f90 ON public.invest_investhomepage USING btree (how_we_help_icon_two_ja_id);


--
-- Name: invest_investhomepage_how_we_help_icon_two_pt_br_id_4a6e272c; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_investhomepage_how_we_help_icon_two_pt_br_id_4a6e272c ON public.invest_investhomepage USING btree (how_we_help_icon_two_pt_br_id);


--
-- Name: invest_investhomepage_how_we_help_icon_two_pt_id_3578bda4; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_investhomepage_how_we_help_icon_two_pt_id_3578bda4 ON public.invest_investhomepage USING btree (how_we_help_icon_two_pt_id);


--
-- Name: invest_investhomepage_how_we_help_icon_two_ru_id_aa9742a9; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_investhomepage_how_we_help_icon_two_ru_id_aa9742a9 ON public.invest_investhomepage USING btree (how_we_help_icon_two_ru_id);


--
-- Name: invest_investhomepage_how_we_help_icon_two_zh_hans_id_d9b9dbcf; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_investhomepage_how_we_help_icon_two_zh_hans_id_d9b9dbcf ON public.invest_investhomepage USING btree (how_we_help_icon_two_zh_hans_id);


--
-- Name: invest_investhomepage_service_name_eaa0e62a; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_investhomepage_service_name_eaa0e62a ON public.invest_investhomepage USING btree (service_name);


--
-- Name: invest_investhomepage_service_name_eaa0e62a_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_investhomepage_service_name_eaa0e62a_like ON public.invest_investhomepage USING btree (service_name varchar_pattern_ops);


--
-- Name: invest_regionlandingpage_hero_image_id_1d53b46b; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_regionlandingpage_hero_image_id_1d53b46b ON public.invest_regionlandingpage USING btree (hero_image_id);


--
-- Name: invest_regionlandingpage_service_name_d06de4e9; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_regionlandingpage_service_name_d06de4e9 ON public.invest_regionlandingpage USING btree (service_name);


--
-- Name: invest_regionlandingpage_service_name_d06de4e9_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_regionlandingpage_service_name_d06de4e9_like ON public.invest_regionlandingpage USING btree (service_name varchar_pattern_ops);


--
-- Name: invest_sectorlandingpage_hero_image_id_bb7eea33; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorlandingpage_hero_image_id_bb7eea33 ON public.invest_sectorlandingpage USING btree (hero_image_id);


--
-- Name: invest_sectorlandingpage_service_name_a3dc5f2d; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorlandingpage_service_name_a3dc5f2d ON public.invest_sectorlandingpage USING btree (service_name);


--
-- Name: invest_sectorlandingpage_service_name_a3dc5f2d_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorlandingpage_service_name_a3dc5f2d_like ON public.invest_sectorlandingpage USING btree (service_name varchar_pattern_ops);


--
-- Name: invest_sectorpage_hero_image_id_8058a47c; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_hero_image_id_8058a47c ON public.invest_sectorpage USING btree (hero_image_id);


--
-- Name: invest_sectorpage_service_name_06672cb0; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_service_name_06672cb0 ON public.invest_sectorpage USING btree (service_name);


--
-- Name: invest_sectorpage_service_name_06672cb0_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_service_name_06672cb0_like ON public.invest_sectorpage USING btree (service_name varchar_pattern_ops);


--
-- Name: invest_sectorpage_subsection_map_five_ar_id_c8719ff6; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_five_ar_id_c8719ff6 ON public.invest_sectorpage USING btree (subsection_map_five_ar_id);


--
-- Name: invest_sectorpage_subsection_map_five_de_id_ee403893; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_five_de_id_ee403893 ON public.invest_sectorpage USING btree (subsection_map_five_de_id);


--
-- Name: invest_sectorpage_subsection_map_five_en_gb_id_cd4d7920; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_five_en_gb_id_cd4d7920 ON public.invest_sectorpage USING btree (subsection_map_five_en_gb_id);


--
-- Name: invest_sectorpage_subsection_map_five_es_id_8d54aae9; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_five_es_id_8d54aae9 ON public.invest_sectorpage USING btree (subsection_map_five_es_id);


--
-- Name: invest_sectorpage_subsection_map_five_fr_id_22b85d21; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_five_fr_id_22b85d21 ON public.invest_sectorpage USING btree (subsection_map_five_fr_id);


--
-- Name: invest_sectorpage_subsection_map_five_id_0f17c849; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_five_id_0f17c849 ON public.invest_sectorpage USING btree (subsection_map_five_id);


--
-- Name: invest_sectorpage_subsection_map_five_ja_id_5dd8444c; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_five_ja_id_5dd8444c ON public.invest_sectorpage USING btree (subsection_map_five_ja_id);


--
-- Name: invest_sectorpage_subsection_map_five_pt_br_id_275133b7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_five_pt_br_id_275133b7 ON public.invest_sectorpage USING btree (subsection_map_five_pt_br_id);


--
-- Name: invest_sectorpage_subsection_map_five_pt_id_c06e94ea; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_five_pt_id_c06e94ea ON public.invest_sectorpage USING btree (subsection_map_five_pt_id);


--
-- Name: invest_sectorpage_subsection_map_five_ru_id_a267a7b3; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_five_ru_id_a267a7b3 ON public.invest_sectorpage USING btree (subsection_map_five_ru_id);


--
-- Name: invest_sectorpage_subsection_map_five_zh_hans_id_aa370701; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_five_zh_hans_id_aa370701 ON public.invest_sectorpage USING btree (subsection_map_five_zh_hans_id);


--
-- Name: invest_sectorpage_subsection_map_four_ar_id_4cf298f7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_four_ar_id_4cf298f7 ON public.invest_sectorpage USING btree (subsection_map_four_ar_id);


--
-- Name: invest_sectorpage_subsection_map_four_de_id_1b7efee2; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_four_de_id_1b7efee2 ON public.invest_sectorpage USING btree (subsection_map_four_de_id);


--
-- Name: invest_sectorpage_subsection_map_four_en_gb_id_54a181ab; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_four_en_gb_id_54a181ab ON public.invest_sectorpage USING btree (subsection_map_four_en_gb_id);


--
-- Name: invest_sectorpage_subsection_map_four_es_id_20d67a90; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_four_es_id_20d67a90 ON public.invest_sectorpage USING btree (subsection_map_four_es_id);


--
-- Name: invest_sectorpage_subsection_map_four_fr_id_85eee56b; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_four_fr_id_85eee56b ON public.invest_sectorpage USING btree (subsection_map_four_fr_id);


--
-- Name: invest_sectorpage_subsection_map_four_id_cac76cb0; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_four_id_cac76cb0 ON public.invest_sectorpage USING btree (subsection_map_four_id);


--
-- Name: invest_sectorpage_subsection_map_four_ja_id_28b40bd3; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_four_ja_id_28b40bd3 ON public.invest_sectorpage USING btree (subsection_map_four_ja_id);


--
-- Name: invest_sectorpage_subsection_map_four_pt_br_id_5750dcc0; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_four_pt_br_id_5750dcc0 ON public.invest_sectorpage USING btree (subsection_map_four_pt_br_id);


--
-- Name: invest_sectorpage_subsection_map_four_pt_id_407eb5cf; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_four_pt_id_407eb5cf ON public.invest_sectorpage USING btree (subsection_map_four_pt_id);


--
-- Name: invest_sectorpage_subsection_map_four_ru_id_b47d357c; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_four_ru_id_b47d357c ON public.invest_sectorpage USING btree (subsection_map_four_ru_id);


--
-- Name: invest_sectorpage_subsection_map_four_zh_hans_id_2c08bf7c; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_four_zh_hans_id_2c08bf7c ON public.invest_sectorpage USING btree (subsection_map_four_zh_hans_id);


--
-- Name: invest_sectorpage_subsection_map_one_ar_id_eae3734a; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_one_ar_id_eae3734a ON public.invest_sectorpage USING btree (subsection_map_one_ar_id);


--
-- Name: invest_sectorpage_subsection_map_one_de_id_e8391019; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_one_de_id_e8391019 ON public.invest_sectorpage USING btree (subsection_map_one_de_id);


--
-- Name: invest_sectorpage_subsection_map_one_en_gb_id_1a4d482b; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_one_en_gb_id_1a4d482b ON public.invest_sectorpage USING btree (subsection_map_one_en_gb_id);


--
-- Name: invest_sectorpage_subsection_map_one_es_id_5c5f38e2; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_one_es_id_5c5f38e2 ON public.invest_sectorpage USING btree (subsection_map_one_es_id);


--
-- Name: invest_sectorpage_subsection_map_one_fr_id_0a9c28e4; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_one_fr_id_0a9c28e4 ON public.invest_sectorpage USING btree (subsection_map_one_fr_id);


--
-- Name: invest_sectorpage_subsection_map_one_id_9f01edda; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_one_id_9f01edda ON public.invest_sectorpage USING btree (subsection_map_one_id);


--
-- Name: invest_sectorpage_subsection_map_one_ja_id_ff99bbbe; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_one_ja_id_ff99bbbe ON public.invest_sectorpage USING btree (subsection_map_one_ja_id);


--
-- Name: invest_sectorpage_subsection_map_one_pt_br_id_bae51dfd; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_one_pt_br_id_bae51dfd ON public.invest_sectorpage USING btree (subsection_map_one_pt_br_id);


--
-- Name: invest_sectorpage_subsection_map_one_pt_id_3704faa0; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_one_pt_id_3704faa0 ON public.invest_sectorpage USING btree (subsection_map_one_pt_id);


--
-- Name: invest_sectorpage_subsection_map_one_ru_id_5aa7df5b; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_one_ru_id_5aa7df5b ON public.invest_sectorpage USING btree (subsection_map_one_ru_id);


--
-- Name: invest_sectorpage_subsection_map_one_zh_hans_id_a4839796; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_one_zh_hans_id_a4839796 ON public.invest_sectorpage USING btree (subsection_map_one_zh_hans_id);


--
-- Name: invest_sectorpage_subsection_map_seven_ar_id_a67c2e79; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_seven_ar_id_a67c2e79 ON public.invest_sectorpage USING btree (subsection_map_seven_ar_id);


--
-- Name: invest_sectorpage_subsection_map_seven_de_id_6b4ac297; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_seven_de_id_6b4ac297 ON public.invest_sectorpage USING btree (subsection_map_seven_de_id);


--
-- Name: invest_sectorpage_subsection_map_seven_en_gb_id_c98901a8; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_seven_en_gb_id_c98901a8 ON public.invest_sectorpage USING btree (subsection_map_seven_en_gb_id);


--
-- Name: invest_sectorpage_subsection_map_seven_es_id_6127c095; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_seven_es_id_6127c095 ON public.invest_sectorpage USING btree (subsection_map_seven_es_id);


--
-- Name: invest_sectorpage_subsection_map_seven_fr_id_94308bd5; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_seven_fr_id_94308bd5 ON public.invest_sectorpage USING btree (subsection_map_seven_fr_id);


--
-- Name: invest_sectorpage_subsection_map_seven_id_410afe44; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_seven_id_410afe44 ON public.invest_sectorpage USING btree (subsection_map_seven_id);


--
-- Name: invest_sectorpage_subsection_map_seven_ja_id_5a450f7a; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_seven_ja_id_5a450f7a ON public.invest_sectorpage USING btree (subsection_map_seven_ja_id);


--
-- Name: invest_sectorpage_subsection_map_seven_pt_br_id_2a54736c; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_seven_pt_br_id_2a54736c ON public.invest_sectorpage USING btree (subsection_map_seven_pt_br_id);


--
-- Name: invest_sectorpage_subsection_map_seven_pt_id_5024f4b4; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_seven_pt_id_5024f4b4 ON public.invest_sectorpage USING btree (subsection_map_seven_pt_id);


--
-- Name: invest_sectorpage_subsection_map_seven_ru_id_bde5e042; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_seven_ru_id_bde5e042 ON public.invest_sectorpage USING btree (subsection_map_seven_ru_id);


--
-- Name: invest_sectorpage_subsection_map_seven_zh_hans_id_e60edb53; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_seven_zh_hans_id_e60edb53 ON public.invest_sectorpage USING btree (subsection_map_seven_zh_hans_id);


--
-- Name: invest_sectorpage_subsection_map_six_ar_id_44a5395c; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_six_ar_id_44a5395c ON public.invest_sectorpage USING btree (subsection_map_six_ar_id);


--
-- Name: invest_sectorpage_subsection_map_six_de_id_c9a85dcb; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_six_de_id_c9a85dcb ON public.invest_sectorpage USING btree (subsection_map_six_de_id);


--
-- Name: invest_sectorpage_subsection_map_six_en_gb_id_f128b944; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_six_en_gb_id_f128b944 ON public.invest_sectorpage USING btree (subsection_map_six_en_gb_id);


--
-- Name: invest_sectorpage_subsection_map_six_es_id_f95f752d; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_six_es_id_f95f752d ON public.invest_sectorpage USING btree (subsection_map_six_es_id);


--
-- Name: invest_sectorpage_subsection_map_six_fr_id_6857bb1c; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_six_fr_id_6857bb1c ON public.invest_sectorpage USING btree (subsection_map_six_fr_id);


--
-- Name: invest_sectorpage_subsection_map_six_id_cb1e3c3c; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_six_id_cb1e3c3c ON public.invest_sectorpage USING btree (subsection_map_six_id);


--
-- Name: invest_sectorpage_subsection_map_six_ja_id_e2bede44; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_six_ja_id_e2bede44 ON public.invest_sectorpage USING btree (subsection_map_six_ja_id);


--
-- Name: invest_sectorpage_subsection_map_six_pt_br_id_382643bc; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_six_pt_br_id_382643bc ON public.invest_sectorpage USING btree (subsection_map_six_pt_br_id);


--
-- Name: invest_sectorpage_subsection_map_six_pt_id_461ab6e9; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_six_pt_id_461ab6e9 ON public.invest_sectorpage USING btree (subsection_map_six_pt_id);


--
-- Name: invest_sectorpage_subsection_map_six_ru_id_8a62efd9; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_six_ru_id_8a62efd9 ON public.invest_sectorpage USING btree (subsection_map_six_ru_id);


--
-- Name: invest_sectorpage_subsection_map_six_zh_hans_id_d55394f2; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_six_zh_hans_id_d55394f2 ON public.invest_sectorpage USING btree (subsection_map_six_zh_hans_id);


--
-- Name: invest_sectorpage_subsection_map_three_ar_id_310ae712; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_three_ar_id_310ae712 ON public.invest_sectorpage USING btree (subsection_map_three_ar_id);


--
-- Name: invest_sectorpage_subsection_map_three_de_id_1766976a; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_three_de_id_1766976a ON public.invest_sectorpage USING btree (subsection_map_three_de_id);


--
-- Name: invest_sectorpage_subsection_map_three_en_gb_id_5fbfd4a0; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_three_en_gb_id_5fbfd4a0 ON public.invest_sectorpage USING btree (subsection_map_three_en_gb_id);


--
-- Name: invest_sectorpage_subsection_map_three_es_id_2d2a2a89; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_three_es_id_2d2a2a89 ON public.invest_sectorpage USING btree (subsection_map_three_es_id);


--
-- Name: invest_sectorpage_subsection_map_three_fr_id_b5ef10e3; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_three_fr_id_b5ef10e3 ON public.invest_sectorpage USING btree (subsection_map_three_fr_id);


--
-- Name: invest_sectorpage_subsection_map_three_id_f4e53d96; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_three_id_f4e53d96 ON public.invest_sectorpage USING btree (subsection_map_three_id);


--
-- Name: invest_sectorpage_subsection_map_three_ja_id_4a0b8e49; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_three_ja_id_4a0b8e49 ON public.invest_sectorpage USING btree (subsection_map_three_ja_id);


--
-- Name: invest_sectorpage_subsection_map_three_pt_br_id_c1bc090a; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_three_pt_br_id_c1bc090a ON public.invest_sectorpage USING btree (subsection_map_three_pt_br_id);


--
-- Name: invest_sectorpage_subsection_map_three_pt_id_3276a701; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_three_pt_id_3276a701 ON public.invest_sectorpage USING btree (subsection_map_three_pt_id);


--
-- Name: invest_sectorpage_subsection_map_three_ru_id_debe81d6; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_three_ru_id_debe81d6 ON public.invest_sectorpage USING btree (subsection_map_three_ru_id);


--
-- Name: invest_sectorpage_subsection_map_three_zh_hans_id_43a24e84; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_three_zh_hans_id_43a24e84 ON public.invest_sectorpage USING btree (subsection_map_three_zh_hans_id);


--
-- Name: invest_sectorpage_subsection_map_two_ar_id_7fe0594e; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_two_ar_id_7fe0594e ON public.invest_sectorpage USING btree (subsection_map_two_ar_id);


--
-- Name: invest_sectorpage_subsection_map_two_de_id_1d738784; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_two_de_id_1d738784 ON public.invest_sectorpage USING btree (subsection_map_two_de_id);


--
-- Name: invest_sectorpage_subsection_map_two_en_gb_id_16d9524e; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_two_en_gb_id_16d9524e ON public.invest_sectorpage USING btree (subsection_map_two_en_gb_id);


--
-- Name: invest_sectorpage_subsection_map_two_es_id_b16fbd6e; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_two_es_id_b16fbd6e ON public.invest_sectorpage USING btree (subsection_map_two_es_id);


--
-- Name: invest_sectorpage_subsection_map_two_fr_id_6e213f2d; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_two_fr_id_6e213f2d ON public.invest_sectorpage USING btree (subsection_map_two_fr_id);


--
-- Name: invest_sectorpage_subsection_map_two_id_26dd7961; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_two_id_26dd7961 ON public.invest_sectorpage USING btree (subsection_map_two_id);


--
-- Name: invest_sectorpage_subsection_map_two_ja_id_0cc7f6b9; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_two_ja_id_0cc7f6b9 ON public.invest_sectorpage USING btree (subsection_map_two_ja_id);


--
-- Name: invest_sectorpage_subsection_map_two_pt_br_id_785d41e9; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_two_pt_br_id_785d41e9 ON public.invest_sectorpage USING btree (subsection_map_two_pt_br_id);


--
-- Name: invest_sectorpage_subsection_map_two_pt_id_ddc3e9c4; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_two_pt_id_ddc3e9c4 ON public.invest_sectorpage USING btree (subsection_map_two_pt_id);


--
-- Name: invest_sectorpage_subsection_map_two_ru_id_d3c7eaa5; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_two_ru_id_d3c7eaa5 ON public.invest_sectorpage USING btree (subsection_map_two_ru_id);


--
-- Name: invest_sectorpage_subsection_map_two_zh_hans_id_f3f920d5; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_sectorpage_subsection_map_two_zh_hans_id_f3f920d5 ON public.invest_sectorpage USING btree (subsection_map_two_zh_hans_id);


--
-- Name: invest_setupguidelandingpage_service_name_c825ee7a; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_setupguidelandingpage_service_name_c825ee7a ON public.invest_setupguidelandingpage USING btree (service_name);


--
-- Name: invest_setupguidelandingpage_service_name_c825ee7a_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_setupguidelandingpage_service_name_c825ee7a_like ON public.invest_setupguidelandingpage USING btree (service_name varchar_pattern_ops);


--
-- Name: invest_setupguidepage_service_name_1ee2c367; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_setupguidepage_service_name_1ee2c367 ON public.invest_setupguidepage USING btree (service_name);


--
-- Name: invest_setupguidepage_service_name_1ee2c367_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX invest_setupguidepage_service_name_1ee2c367_like ON public.invest_setupguidepage USING btree (service_name varchar_pattern_ops);


--
-- Name: taggit_tag_name_58eb2ed9_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX taggit_tag_name_58eb2ed9_like ON public.taggit_tag USING btree (name varchar_pattern_ops);


--
-- Name: taggit_tag_slug_6be58b2c_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX taggit_tag_slug_6be58b2c_like ON public.taggit_tag USING btree (slug varchar_pattern_ops);


--
-- Name: taggit_taggeditem_content_type_id_9957a03c; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX taggit_taggeditem_content_type_id_9957a03c ON public.taggit_taggeditem USING btree (content_type_id);


--
-- Name: taggit_taggeditem_content_type_id_object_id_196cc965_idx; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX taggit_taggeditem_content_type_id_object_id_196cc965_idx ON public.taggit_taggeditem USING btree (content_type_id, object_id);


--
-- Name: taggit_taggeditem_object_id_e2d7d1df; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX taggit_taggeditem_object_id_e2d7d1df ON public.taggit_taggeditem USING btree (object_id);


--
-- Name: taggit_taggeditem_tag_id_f4f5b767; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX taggit_taggeditem_tag_id_f4f5b767 ON public.taggit_taggeditem USING btree (tag_id);


--
-- Name: wagtailcore_collection_path_d848dc19_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_collection_path_d848dc19_like ON public.wagtailcore_collection USING btree (path varchar_pattern_ops);


--
-- Name: wagtailcore_collectionview_collectionviewrestriction__47320efd; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_collectionview_collectionviewrestriction__47320efd ON public.wagtailcore_collectionviewrestriction_groups USING btree (collectionviewrestriction_id);


--
-- Name: wagtailcore_collectionviewrestriction_collection_id_761908ec; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_collectionviewrestriction_collection_id_761908ec ON public.wagtailcore_collectionviewrestriction USING btree (collection_id);


--
-- Name: wagtailcore_collectionviewrestriction_groups_group_id_1823f2a3; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_collectionviewrestriction_groups_group_id_1823f2a3 ON public.wagtailcore_collectionviewrestriction_groups USING btree (group_id);


--
-- Name: wagtailcore_groupcollectionpermission_collection_id_5423575a; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_groupcollectionpermission_collection_id_5423575a ON public.wagtailcore_groupcollectionpermission USING btree (collection_id);


--
-- Name: wagtailcore_groupcollectionpermission_group_id_05d61460; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_groupcollectionpermission_group_id_05d61460 ON public.wagtailcore_groupcollectionpermission USING btree (group_id);


--
-- Name: wagtailcore_groupcollectionpermission_permission_id_1b626275; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_groupcollectionpermission_permission_id_1b626275 ON public.wagtailcore_groupcollectionpermission USING btree (permission_id);


--
-- Name: wagtailcore_grouppagepermission_group_id_fc07e671; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_grouppagepermission_group_id_fc07e671 ON public.wagtailcore_grouppagepermission USING btree (group_id);


--
-- Name: wagtailcore_grouppagepermission_page_id_710b114a; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_grouppagepermission_page_id_710b114a ON public.wagtailcore_grouppagepermission USING btree (page_id);


--
-- Name: wagtailcore_page_content_type_id_c28424df; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_page_content_type_id_c28424df ON public.wagtailcore_page USING btree (content_type_id);


--
-- Name: wagtailcore_page_first_published_at_2b5dd637; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_page_first_published_at_2b5dd637 ON public.wagtailcore_page USING btree (first_published_at);


--
-- Name: wagtailcore_page_live_revision_id_930bd822; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_page_live_revision_id_930bd822 ON public.wagtailcore_page USING btree (live_revision_id);


--
-- Name: wagtailcore_page_owner_id_fbf7c332; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_page_owner_id_fbf7c332 ON public.wagtailcore_page USING btree (owner_id);


--
-- Name: wagtailcore_page_path_98eba2c8_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_page_path_98eba2c8_like ON public.wagtailcore_page USING btree (path varchar_pattern_ops);


--
-- Name: wagtailcore_page_slug_e7c11b8f; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_page_slug_e7c11b8f ON public.wagtailcore_page USING btree (slug);


--
-- Name: wagtailcore_page_slug_e7c11b8f_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_page_slug_e7c11b8f_like ON public.wagtailcore_page USING btree (slug varchar_pattern_ops);


--
-- Name: wagtailcore_pagerevision_created_at_66954e3b; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_pagerevision_created_at_66954e3b ON public.wagtailcore_pagerevision USING btree (created_at);


--
-- Name: wagtailcore_pagerevision_page_id_d421cc1d; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_pagerevision_page_id_d421cc1d ON public.wagtailcore_pagerevision USING btree (page_id);


--
-- Name: wagtailcore_pagerevision_submitted_for_moderation_c682e44c; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_pagerevision_submitted_for_moderation_c682e44c ON public.wagtailcore_pagerevision USING btree (submitted_for_moderation);


--
-- Name: wagtailcore_pagerevision_user_id_2409d2f4; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_pagerevision_user_id_2409d2f4 ON public.wagtailcore_pagerevision USING btree (user_id);


--
-- Name: wagtailcore_pageviewrestri_pageviewrestriction_id_f147a99a; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_pageviewrestri_pageviewrestriction_id_f147a99a ON public.wagtailcore_pageviewrestriction_groups USING btree (pageviewrestriction_id);


--
-- Name: wagtailcore_pageviewrestriction_groups_group_id_6460f223; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_pageviewrestriction_groups_group_id_6460f223 ON public.wagtailcore_pageviewrestriction_groups USING btree (group_id);


--
-- Name: wagtailcore_pageviewrestriction_page_id_15a8bea6; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_pageviewrestriction_page_id_15a8bea6 ON public.wagtailcore_pageviewrestriction USING btree (page_id);


--
-- Name: wagtailcore_site_hostname_96b20b46; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_site_hostname_96b20b46 ON public.wagtailcore_site USING btree (hostname);


--
-- Name: wagtailcore_site_hostname_96b20b46_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_site_hostname_96b20b46_like ON public.wagtailcore_site USING btree (hostname varchar_pattern_ops);


--
-- Name: wagtailcore_site_root_page_id_e02fb95c; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailcore_site_root_page_id_e02fb95c ON public.wagtailcore_site USING btree (root_page_id);


--
-- Name: wagtaildocs_document_collection_id_23881625; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtaildocs_document_collection_id_23881625 ON public.wagtaildocs_document USING btree (collection_id);


--
-- Name: wagtaildocs_document_uploaded_by_user_id_17258b41; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtaildocs_document_uploaded_by_user_id_17258b41 ON public.wagtaildocs_document USING btree (uploaded_by_user_id);


--
-- Name: wagtailforms_formsubmission_page_id_e48e93e7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailforms_formsubmission_page_id_e48e93e7 ON public.wagtailforms_formsubmission USING btree (page_id);


--
-- Name: wagtailimages_image_collection_id_c2f8af7e; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailimages_image_collection_id_c2f8af7e ON public.wagtailimages_image USING btree (collection_id);


--
-- Name: wagtailimages_image_created_at_86fa6cd4; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailimages_image_created_at_86fa6cd4 ON public.wagtailimages_image USING btree (created_at);


--
-- Name: wagtailimages_image_uploaded_by_user_id_5d73dc75; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailimages_image_uploaded_by_user_id_5d73dc75 ON public.wagtailimages_image USING btree (uploaded_by_user_id);


--
-- Name: wagtailimages_rendition_filter_spec_1cba3201; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailimages_rendition_filter_spec_1cba3201 ON public.wagtailimages_rendition USING btree (filter_spec);


--
-- Name: wagtailimages_rendition_filter_spec_1cba3201_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailimages_rendition_filter_spec_1cba3201_like ON public.wagtailimages_rendition USING btree (filter_spec varchar_pattern_ops);


--
-- Name: wagtailimages_rendition_image_id_3e1fd774; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailimages_rendition_image_id_3e1fd774 ON public.wagtailimages_rendition USING btree (image_id);


--
-- Name: wagtailmedia_media_collection_id_96a2317d; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailmedia_media_collection_id_96a2317d ON public.wagtailmedia_media USING btree (collection_id);


--
-- Name: wagtailmedia_media_uploaded_by_user_id_96e8e61b; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailmedia_media_uploaded_by_user_id_96e8e61b ON public.wagtailmedia_media USING btree (uploaded_by_user_id);


--
-- Name: wagtailsearch_editorspick_page_id_28cbc274; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailsearch_editorspick_page_id_28cbc274 ON public.wagtailsearch_editorspick USING btree (page_id);


--
-- Name: wagtailsearch_editorspick_query_id_c6eee4a0; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailsearch_editorspick_query_id_c6eee4a0 ON public.wagtailsearch_editorspick USING btree (query_id);


--
-- Name: wagtailsearch_query_query_string_e785ea07_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailsearch_query_query_string_e785ea07_like ON public.wagtailsearch_query USING btree (query_string varchar_pattern_ops);


--
-- Name: wagtailsearch_querydailyhits_query_id_2185994b; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX wagtailsearch_querydailyhits_query_id_2185994b ON public.wagtailsearch_querydailyhits USING btree (query_id);


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: components_bannercomponent components_bannercom_page_ptr_id_90b9c5d9_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.components_bannercomponent
    ADD CONSTRAINT components_bannercom_page_ptr_id_90b9c5d9_fk_wagtailco FOREIGN KEY (page_ptr_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: components_componentsapp components_component_page_ptr_id_c0d0228e_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.components_componentsapp
    ADD CONSTRAINT components_component_page_ptr_id_c0d0228e_fk_wagtailco FOREIGN KEY (page_ptr_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: core_breadcrumb core_breadcrumb_content_type_id_10fedf77_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.core_breadcrumb
    ADD CONSTRAINT core_breadcrumb_content_type_id_10fedf77_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: core_documenthash core_documenthash_document_id_6783bf52_fk_wagtaildo; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.core_documenthash
    ADD CONSTRAINT core_documenthash_document_id_6783bf52_fk_wagtaildo FOREIGN KEY (document_id) REFERENCES public.wagtaildocs_document(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: core_imagehash core_imagehash_image_id_ee947939_fk_wagtailimages_image_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.core_imagehash
    ADD CONSTRAINT core_imagehash_image_id_ee947939_fk_wagtailimages_image_id FOREIGN KEY (image_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: export_readiness_allcontactpagespage export_readiness_all_page_ptr_id_aa210107_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_allcontactpagespage
    ADD CONSTRAINT export_readiness_all_page_ptr_id_aa210107_fk_wagtailco FOREIGN KEY (page_ptr_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: export_readiness_articlepage export_readiness_art_article_image_id_89070cd3_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_articlepage
    ADD CONSTRAINT export_readiness_art_article_image_id_89070cd3_fk_wagtailim FOREIGN KEY (article_image_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: export_readiness_articlepage_tags export_readiness_art_articlepage_id_f030e54b_fk_export_re; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_articlepage_tags
    ADD CONSTRAINT export_readiness_art_articlepage_id_f030e54b_fk_export_re FOREIGN KEY (articlepage_id) REFERENCES public.export_readiness_articlepage(page_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: export_readiness_articlelistingpage export_readiness_art_hero_image_id_86c32ca9_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_articlelistingpage
    ADD CONSTRAINT export_readiness_art_hero_image_id_86c32ca9_fk_wagtailim FOREIGN KEY (hero_image_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: export_readiness_articlepage export_readiness_art_page_ptr_id_0193bdbf_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_articlepage
    ADD CONSTRAINT export_readiness_art_page_ptr_id_0193bdbf_fk_wagtailco FOREIGN KEY (page_ptr_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: export_readiness_articlelistingpage export_readiness_art_page_ptr_id_a7b8722c_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_articlelistingpage
    ADD CONSTRAINT export_readiness_art_page_ptr_id_a7b8722c_fk_wagtailco FOREIGN KEY (page_ptr_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: export_readiness_articlepage export_readiness_art_related_page_one_id_7634796a_fk_export_re; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_articlepage
    ADD CONSTRAINT export_readiness_art_related_page_one_id_7634796a_fk_export_re FOREIGN KEY (related_page_one_id) REFERENCES public.export_readiness_articlepage(page_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: export_readiness_articlepage export_readiness_art_related_page_three_i_d04918af_fk_export_re; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_articlepage
    ADD CONSTRAINT export_readiness_art_related_page_three_i_d04918af_fk_export_re FOREIGN KEY (related_page_three_id) REFERENCES public.export_readiness_articlepage(page_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: export_readiness_articlepage export_readiness_art_related_page_two_id_1173b7c9_fk_export_re; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_articlepage
    ADD CONSTRAINT export_readiness_art_related_page_two_id_1173b7c9_fk_export_re FOREIGN KEY (related_page_two_id) REFERENCES public.export_readiness_articlepage(page_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: export_readiness_articlepage_tags export_readiness_art_tag_id_5ab392b0_fk_export_re; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_articlepage_tags
    ADD CONSTRAINT export_readiness_art_tag_id_5ab392b0_fk_export_re FOREIGN KEY (tag_id) REFERENCES public.export_readiness_tag(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: export_readiness_campaignpage export_readiness_cam_campaign_hero_image__3fcd1917_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_campaignpage
    ADD CONSTRAINT export_readiness_cam_campaign_hero_image__3fcd1917_fk_wagtailim FOREIGN KEY (campaign_hero_image_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: export_readiness_campaignpage export_readiness_cam_page_ptr_id_21b1172e_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_campaignpage
    ADD CONSTRAINT export_readiness_cam_page_ptr_id_21b1172e_fk_wagtailco FOREIGN KEY (page_ptr_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: export_readiness_campaignpage export_readiness_cam_related_page_one_id_cb23b33a_fk_export_re; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_campaignpage
    ADD CONSTRAINT export_readiness_cam_related_page_one_id_cb23b33a_fk_export_re FOREIGN KEY (related_page_one_id) REFERENCES public.export_readiness_articlepage(page_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: export_readiness_campaignpage export_readiness_cam_related_page_three_i_c30330ae_fk_export_re; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_campaignpage
    ADD CONSTRAINT export_readiness_cam_related_page_three_i_c30330ae_fk_export_re FOREIGN KEY (related_page_three_id) REFERENCES public.export_readiness_articlepage(page_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: export_readiness_campaignpage export_readiness_cam_related_page_two_id_c264e13b_fk_export_re; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_campaignpage
    ADD CONSTRAINT export_readiness_cam_related_page_two_id_c264e13b_fk_export_re FOREIGN KEY (related_page_two_id) REFERENCES public.export_readiness_articlepage(page_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: export_readiness_campaignpage export_readiness_cam_section_one_image_id_b31db608_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_campaignpage
    ADD CONSTRAINT export_readiness_cam_section_one_image_id_b31db608_fk_wagtailim FOREIGN KEY (section_one_image_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: export_readiness_campaignpage export_readiness_cam_section_two_image_id_ca2e9d7d_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_campaignpage
    ADD CONSTRAINT export_readiness_cam_section_two_image_id_ca2e9d7d_fk_wagtailim FOREIGN KEY (section_two_image_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: export_readiness_campaignpage export_readiness_cam_selling_point_one_ic_fd711190_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_campaignpage
    ADD CONSTRAINT export_readiness_cam_selling_point_one_ic_fd711190_fk_wagtailim FOREIGN KEY (selling_point_one_icon_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: export_readiness_campaignpage export_readiness_cam_selling_point_three__5c85aa24_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_campaignpage
    ADD CONSTRAINT export_readiness_cam_selling_point_three__5c85aa24_fk_wagtailim FOREIGN KEY (selling_point_three_icon_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: export_readiness_campaignpage export_readiness_cam_selling_point_two_ic_c262e438_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_campaignpage
    ADD CONSTRAINT export_readiness_cam_selling_point_two_ic_c262e438_fk_wagtailim FOREIGN KEY (selling_point_two_icon_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: export_readiness_contactsuccesspages export_readiness_con_page_ptr_id_4678bdfb_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_contactsuccesspages
    ADD CONSTRAINT export_readiness_con_page_ptr_id_4678bdfb_fk_wagtailco FOREIGN KEY (page_ptr_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: export_readiness_contactusguidancepages export_readiness_con_page_ptr_id_587d2e98_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_contactusguidancepages
    ADD CONSTRAINT export_readiness_con_page_ptr_id_587d2e98_fk_wagtailco FOREIGN KEY (page_ptr_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: export_readiness_contactsuccesspage export_readiness_con_page_ptr_id_818e25f4_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_contactsuccesspage
    ADD CONSTRAINT export_readiness_con_page_ptr_id_818e25f4_fk_wagtailco FOREIGN KEY (page_ptr_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: export_readiness_contactusguidancepage export_readiness_con_page_ptr_id_d1d5bb55_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_contactusguidancepage
    ADD CONSTRAINT export_readiness_con_page_ptr_id_d1d5bb55_fk_wagtailco FOREIGN KEY (page_ptr_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: export_readiness_countryguidepage export_readiness_cou_hero_image_id_deec3fdd_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_countryguidepage
    ADD CONSTRAINT export_readiness_cou_hero_image_id_deec3fdd_fk_wagtailim FOREIGN KEY (hero_image_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: export_readiness_countryguidepage export_readiness_cou_page_ptr_id_36711733_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_countryguidepage
    ADD CONSTRAINT export_readiness_cou_page_ptr_id_36711733_fk_wagtailco FOREIGN KEY (page_ptr_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: export_readiness_countryguidepage export_readiness_cou_related_page_one_id_5ca8f131_fk_export_re; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_countryguidepage
    ADD CONSTRAINT export_readiness_cou_related_page_one_id_5ca8f131_fk_export_re FOREIGN KEY (related_page_one_id) REFERENCES public.export_readiness_articlepage(page_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: export_readiness_countryguidepage export_readiness_cou_related_page_three_i_56823dfc_fk_export_re; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_countryguidepage
    ADD CONSTRAINT export_readiness_cou_related_page_three_i_56823dfc_fk_export_re FOREIGN KEY (related_page_three_id) REFERENCES public.export_readiness_articlepage(page_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: export_readiness_countryguidepage export_readiness_cou_related_page_two_id_1ccdaa57_fk_export_re; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_countryguidepage
    ADD CONSTRAINT export_readiness_cou_related_page_two_id_1ccdaa57_fk_export_re FOREIGN KEY (related_page_two_id) REFERENCES public.export_readiness_articlepage(page_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: export_readiness_countryguidepage export_readiness_cou_selling_point_one_ic_bbe09d0e_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_countryguidepage
    ADD CONSTRAINT export_readiness_cou_selling_point_one_ic_bbe09d0e_fk_wagtailim FOREIGN KEY (selling_point_one_icon_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: export_readiness_countryguidepage export_readiness_cou_selling_point_three__b9cb720d_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_countryguidepage
    ADD CONSTRAINT export_readiness_cou_selling_point_three__b9cb720d_fk_wagtailim FOREIGN KEY (selling_point_three_icon_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: export_readiness_countryguidepage export_readiness_cou_selling_point_two_ic_8ff624b4_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_countryguidepage
    ADD CONSTRAINT export_readiness_cou_selling_point_two_ic_8ff624b4_fk_wagtailim FOREIGN KEY (selling_point_two_icon_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: export_readiness_euexitdomesticformpage export_readiness_eue_page_ptr_id_07dfb324_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_euexitdomesticformpage
    ADD CONSTRAINT export_readiness_eue_page_ptr_id_07dfb324_fk_wagtailco FOREIGN KEY (page_ptr_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: export_readiness_euexitformpages export_readiness_eue_page_ptr_id_4e2d5aba_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_euexitformpages
    ADD CONSTRAINT export_readiness_eue_page_ptr_id_4e2d5aba_fk_wagtailco FOREIGN KEY (page_ptr_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: export_readiness_euexitformsuccesspage export_readiness_eue_page_ptr_id_965be06d_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_euexitformsuccesspage
    ADD CONSTRAINT export_readiness_eue_page_ptr_id_965be06d_fk_wagtailco FOREIGN KEY (page_ptr_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: export_readiness_euexitinternationalformpage export_readiness_eue_page_ptr_id_96c5343f_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_euexitinternationalformpage
    ADD CONSTRAINT export_readiness_eue_page_ptr_id_96c5343f_fk_wagtailco FOREIGN KEY (page_ptr_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: export_readiness_exportreadinessapp export_readiness_exp_page_ptr_id_37b95a6e_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_exportreadinessapp
    ADD CONSTRAINT export_readiness_exp_page_ptr_id_37b95a6e_fk_wagtailco FOREIGN KEY (page_ptr_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: export_readiness_homepage export_readiness_hom_page_ptr_id_45b4c145_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_homepage
    ADD CONSTRAINT export_readiness_hom_page_ptr_id_45b4c145_fk_wagtailco FOREIGN KEY (page_ptr_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: export_readiness_internationallandingpage export_readiness_int_page_ptr_id_b9d90e95_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_internationallandingpage
    ADD CONSTRAINT export_readiness_int_page_ptr_id_b9d90e95_fk_wagtailco FOREIGN KEY (page_ptr_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: export_readiness_marketingpages export_readiness_mar_page_ptr_id_48d50166_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_marketingpages
    ADD CONSTRAINT export_readiness_mar_page_ptr_id_48d50166_fk_wagtailco FOREIGN KEY (page_ptr_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: export_readiness_getfinancepage export_readiness_new_advantages_one_icon__d68b409c_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_getfinancepage
    ADD CONSTRAINT export_readiness_new_advantages_one_icon__d68b409c_fk_wagtailim FOREIGN KEY (advantages_one_icon_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: export_readiness_getfinancepage export_readiness_new_advantages_three_ico_32d9754e_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_getfinancepage
    ADD CONSTRAINT export_readiness_new_advantages_three_ico_32d9754e_fk_wagtailim FOREIGN KEY (advantages_three_icon_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: export_readiness_getfinancepage export_readiness_new_advantages_two_icon__20513176_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_getfinancepage
    ADD CONSTRAINT export_readiness_new_advantages_two_icon__20513176_fk_wagtailim FOREIGN KEY (advantages_two_icon_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: export_readiness_getfinancepage export_readiness_new_evidence_video_id_431a261d_fk_wagtailme; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_getfinancepage
    ADD CONSTRAINT export_readiness_new_evidence_video_id_431a261d_fk_wagtailme FOREIGN KEY (evidence_video_id) REFERENCES public.wagtailmedia_media(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: export_readiness_getfinancepage export_readiness_new_hero_image_id_1b9d533a_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_getfinancepage
    ADD CONSTRAINT export_readiness_new_hero_image_id_1b9d533a_fk_wagtailim FOREIGN KEY (hero_image_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: export_readiness_getfinancepage export_readiness_new_page_ptr_id_9d662898_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_getfinancepage
    ADD CONSTRAINT export_readiness_new_page_ptr_id_9d662898_fk_wagtailco FOREIGN KEY (page_ptr_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: export_readiness_getfinancepage export_readiness_new_ukef_logo_id_714d839d_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_getfinancepage
    ADD CONSTRAINT export_readiness_new_ukef_logo_id_714d839d_fk_wagtailim FOREIGN KEY (ukef_logo_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: export_readiness_performancedashboardnotespage export_readiness_per_page_ptr_id_1426feef_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_performancedashboardnotespage
    ADD CONSTRAINT export_readiness_per_page_ptr_id_1426feef_fk_wagtailco FOREIGN KEY (page_ptr_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: export_readiness_performancedashboardpage export_readiness_per_page_ptr_id_9d5704e4_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_performancedashboardpage
    ADD CONSTRAINT export_readiness_per_page_ptr_id_9d5704e4_fk_wagtailco FOREIGN KEY (page_ptr_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: export_readiness_privacyandcookiespage export_readiness_pri_page_ptr_id_36e49f4f_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_privacyandcookiespage
    ADD CONSTRAINT export_readiness_pri_page_ptr_id_36e49f4f_fk_wagtailco FOREIGN KEY (page_ptr_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: export_readiness_sitepolicypages export_readiness_sit_page_ptr_id_4f9754c4_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_sitepolicypages
    ADD CONSTRAINT export_readiness_sit_page_ptr_id_4f9754c4_fk_wagtailco FOREIGN KEY (page_ptr_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: export_readiness_superregionpage export_readiness_sup_topiclandingpage_ptr_f68fce83_fk_export_re; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_superregionpage
    ADD CONSTRAINT export_readiness_sup_topiclandingpage_ptr_f68fce83_fk_export_re FOREIGN KEY (topiclandingpage_ptr_id) REFERENCES public.export_readiness_topiclandingpage(page_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: export_readiness_termsandconditionspage export_readiness_ter_page_ptr_id_bfc6d184_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_termsandconditionspage
    ADD CONSTRAINT export_readiness_ter_page_ptr_id_bfc6d184_fk_wagtailco FOREIGN KEY (page_ptr_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: export_readiness_topiclandingpage export_readiness_top_hero_image_id_dbf67d7a_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_topiclandingpage
    ADD CONSTRAINT export_readiness_top_hero_image_id_dbf67d7a_fk_wagtailim FOREIGN KEY (hero_image_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: export_readiness_topiclandingpage export_readiness_top_page_ptr_id_9f77ba9c_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.export_readiness_topiclandingpage
    ADD CONSTRAINT export_readiness_top_page_ptr_id_9f77ba9c_fk_wagtailco FOREIGN KEY (page_ptr_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_findasupplierapp find_a_supplier_find_page_ptr_id_54416533_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_findasupplierapp
    ADD CONSTRAINT find_a_supplier_find_page_ptr_id_54416533_fk_wagtailco FOREIGN KEY (page_ptr_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_industrylandingpage find_a_supplier_indu_hero_image_id_44beb772_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_industrylandingpage
    ADD CONSTRAINT find_a_supplier_indu_hero_image_id_44beb772_fk_wagtailim FOREIGN KEY (hero_image_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_industrypage find_a_supplier_indu_hero_image_id_4b527995_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_industrypage
    ADD CONSTRAINT find_a_supplier_indu_hero_image_id_4b527995_fk_wagtailim FOREIGN KEY (hero_image_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_industrypagearticlesummary find_a_supplier_indu_image_id_346e5e98_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_industrypagearticlesummary
    ADD CONSTRAINT find_a_supplier_indu_image_id_346e5e98_fk_wagtailim FOREIGN KEY (image_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_industrypage find_a_supplier_indu_introduction_column__10e463a0_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_industrypage
    ADD CONSTRAINT find_a_supplier_indu_introduction_column__10e463a0_fk_wagtailim FOREIGN KEY (introduction_column_one_icon_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_industrypage find_a_supplier_indu_introduction_column__b5f2cae1_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_industrypage
    ADD CONSTRAINT find_a_supplier_indu_introduction_column__b5f2cae1_fk_wagtailim FOREIGN KEY (introduction_column_two_icon_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_industrypage find_a_supplier_indu_introduction_column__fd509d55_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_industrypage
    ADD CONSTRAINT find_a_supplier_indu_introduction_column__fd509d55_fk_wagtailim FOREIGN KEY (introduction_column_three_icon_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_industrylandingpage find_a_supplier_indu_mobile_hero_image_id_3f4849a2_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_industrylandingpage
    ADD CONSTRAINT find_a_supplier_indu_mobile_hero_image_id_3f4849a2_fk_wagtailim FOREIGN KEY (mobile_hero_image_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_industrypage find_a_supplier_indu_mobile_hero_image_id_e3940be2_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_industrypage
    ADD CONSTRAINT find_a_supplier_indu_mobile_hero_image_id_e3940be2_fk_wagtailim FOREIGN KEY (mobile_hero_image_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_industrypagearticlesummary find_a_supplier_indu_page_ar_id_21b6c7aa_fk_find_a_su; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_industrypagearticlesummary
    ADD CONSTRAINT find_a_supplier_indu_page_ar_id_21b6c7aa_fk_find_a_su FOREIGN KEY (page_ar_id) REFERENCES public.find_a_supplier_industrypage(page_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_industrypagearticlesummary find_a_supplier_indu_page_de_id_0483d921_fk_find_a_su; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_industrypagearticlesummary
    ADD CONSTRAINT find_a_supplier_indu_page_de_id_0483d921_fk_find_a_su FOREIGN KEY (page_de_id) REFERENCES public.find_a_supplier_industrypage(page_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_industrypagearticlesummary find_a_supplier_indu_page_en_gb_id_1818656b_fk_find_a_su; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_industrypagearticlesummary
    ADD CONSTRAINT find_a_supplier_indu_page_en_gb_id_1818656b_fk_find_a_su FOREIGN KEY (page_en_gb_id) REFERENCES public.find_a_supplier_industrypage(page_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_industrypagearticlesummary find_a_supplier_indu_page_es_id_4a5714bc_fk_find_a_su; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_industrypagearticlesummary
    ADD CONSTRAINT find_a_supplier_indu_page_es_id_4a5714bc_fk_find_a_su FOREIGN KEY (page_es_id) REFERENCES public.find_a_supplier_industrypage(page_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_industrypagearticlesummary find_a_supplier_indu_page_fr_id_bfd8d4b7_fk_find_a_su; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_industrypagearticlesummary
    ADD CONSTRAINT find_a_supplier_indu_page_fr_id_bfd8d4b7_fk_find_a_su FOREIGN KEY (page_fr_id) REFERENCES public.find_a_supplier_industrypage(page_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_industrypagearticlesummary find_a_supplier_indu_page_id_beadfb32_fk_find_a_su; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_industrypagearticlesummary
    ADD CONSTRAINT find_a_supplier_indu_page_id_beadfb32_fk_find_a_su FOREIGN KEY (page_id) REFERENCES public.find_a_supplier_industrypage(page_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_industrypagearticlesummary find_a_supplier_indu_page_ja_id_a0834721_fk_find_a_su; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_industrypagearticlesummary
    ADD CONSTRAINT find_a_supplier_indu_page_ja_id_a0834721_fk_find_a_su FOREIGN KEY (page_ja_id) REFERENCES public.find_a_supplier_industrypage(page_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_industrypagearticlesummary find_a_supplier_indu_page_pt_br_id_2e23fb1f_fk_find_a_su; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_industrypagearticlesummary
    ADD CONSTRAINT find_a_supplier_indu_page_pt_br_id_2e23fb1f_fk_find_a_su FOREIGN KEY (page_pt_br_id) REFERENCES public.find_a_supplier_industrypage(page_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_industrypagearticlesummary find_a_supplier_indu_page_pt_id_a2f522f7_fk_find_a_su; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_industrypagearticlesummary
    ADD CONSTRAINT find_a_supplier_indu_page_pt_id_a2f522f7_fk_find_a_su FOREIGN KEY (page_pt_id) REFERENCES public.find_a_supplier_industrypage(page_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_industrypage find_a_supplier_indu_page_ptr_id_5f39b625_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_industrypage
    ADD CONSTRAINT find_a_supplier_indu_page_ptr_id_5f39b625_fk_wagtailco FOREIGN KEY (page_ptr_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_industrycontactpage find_a_supplier_indu_page_ptr_id_7536ce81_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_industrycontactpage
    ADD CONSTRAINT find_a_supplier_indu_page_ptr_id_7536ce81_fk_wagtailco FOREIGN KEY (page_ptr_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_industrylandingpage find_a_supplier_indu_page_ptr_id_7bec7615_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_industrylandingpage
    ADD CONSTRAINT find_a_supplier_indu_page_ptr_id_7bec7615_fk_wagtailco FOREIGN KEY (page_ptr_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_industryarticlepage find_a_supplier_indu_page_ptr_id_dfe5af72_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_industryarticlepage
    ADD CONSTRAINT find_a_supplier_indu_page_ptr_id_dfe5af72_fk_wagtailco FOREIGN KEY (page_ptr_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_industrypagearticlesummary find_a_supplier_indu_page_ru_id_bc3a8809_fk_find_a_su; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_industrypagearticlesummary
    ADD CONSTRAINT find_a_supplier_indu_page_ru_id_bc3a8809_fk_find_a_su FOREIGN KEY (page_ru_id) REFERENCES public.find_a_supplier_industrypage(page_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_industrypagearticlesummary find_a_supplier_indu_page_zh_hans_id_2c9fc29d_fk_find_a_su; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_industrypagearticlesummary
    ADD CONSTRAINT find_a_supplier_indu_page_zh_hans_id_2c9fc29d_fk_find_a_su FOREIGN KEY (page_zh_hans_id) REFERENCES public.find_a_supplier_industrypage(page_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_industrypage find_a_supplier_indu_summary_image_id_ec5b95f4_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_industrypage
    ADD CONSTRAINT find_a_supplier_indu_summary_image_id_ec5b95f4_fk_wagtailim FOREIGN KEY (summary_image_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_industrypagearticlesummary find_a_supplier_indu_video_media_id_11b74530_fk_wagtailme; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_industrypagearticlesummary
    ADD CONSTRAINT find_a_supplier_indu_video_media_id_11b74530_fk_wagtailme FOREIGN KEY (video_media_id) REFERENCES public.wagtailmedia_media(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_landingpage find_a_supplier_land_hero_image_id_76d06f77_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_landingpage
    ADD CONSTRAINT find_a_supplier_land_hero_image_id_76d06f77_fk_wagtailim FOREIGN KEY (hero_image_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_landingpagearticlesummary find_a_supplier_land_image_id_8a5fff5e_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_landingpagearticlesummary
    ADD CONSTRAINT find_a_supplier_land_image_id_8a5fff5e_fk_wagtailim FOREIGN KEY (image_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_landingpage find_a_supplier_land_mobile_hero_image_id_2122ccb4_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_landingpage
    ADD CONSTRAINT find_a_supplier_land_mobile_hero_image_id_2122ccb4_fk_wagtailim FOREIGN KEY (mobile_hero_image_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_landingpagearticlesummary find_a_supplier_land_page_ar_id_b92c3bde_fk_find_a_su; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_landingpagearticlesummary
    ADD CONSTRAINT find_a_supplier_land_page_ar_id_b92c3bde_fk_find_a_su FOREIGN KEY (page_ar_id) REFERENCES public.find_a_supplier_landingpage(page_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_landingpagearticlesummary find_a_supplier_land_page_de_id_10c841d1_fk_find_a_su; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_landingpagearticlesummary
    ADD CONSTRAINT find_a_supplier_land_page_de_id_10c841d1_fk_find_a_su FOREIGN KEY (page_de_id) REFERENCES public.find_a_supplier_landingpage(page_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_landingpagearticlesummary find_a_supplier_land_page_en_gb_id_ad4dd2fd_fk_find_a_su; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_landingpagearticlesummary
    ADD CONSTRAINT find_a_supplier_land_page_en_gb_id_ad4dd2fd_fk_find_a_su FOREIGN KEY (page_en_gb_id) REFERENCES public.find_a_supplier_landingpage(page_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_landingpagearticlesummary find_a_supplier_land_page_es_id_67b4a39b_fk_find_a_su; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_landingpagearticlesummary
    ADD CONSTRAINT find_a_supplier_land_page_es_id_67b4a39b_fk_find_a_su FOREIGN KEY (page_es_id) REFERENCES public.find_a_supplier_landingpage(page_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_landingpagearticlesummary find_a_supplier_land_page_fr_id_b14ec81b_fk_find_a_su; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_landingpagearticlesummary
    ADD CONSTRAINT find_a_supplier_land_page_fr_id_b14ec81b_fk_find_a_su FOREIGN KEY (page_fr_id) REFERENCES public.find_a_supplier_landingpage(page_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_landingpagearticlesummary find_a_supplier_land_page_id_18f6123b_fk_find_a_su; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_landingpagearticlesummary
    ADD CONSTRAINT find_a_supplier_land_page_id_18f6123b_fk_find_a_su FOREIGN KEY (page_id) REFERENCES public.find_a_supplier_landingpage(page_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_landingpagearticlesummary find_a_supplier_land_page_ja_id_551b0c52_fk_find_a_su; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_landingpagearticlesummary
    ADD CONSTRAINT find_a_supplier_land_page_ja_id_551b0c52_fk_find_a_su FOREIGN KEY (page_ja_id) REFERENCES public.find_a_supplier_landingpage(page_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_landingpagearticlesummary find_a_supplier_land_page_pt_br_id_a6ffa0f7_fk_find_a_su; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_landingpagearticlesummary
    ADD CONSTRAINT find_a_supplier_land_page_pt_br_id_a6ffa0f7_fk_find_a_su FOREIGN KEY (page_pt_br_id) REFERENCES public.find_a_supplier_landingpage(page_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_landingpagearticlesummary find_a_supplier_land_page_pt_id_1e3fe6a9_fk_find_a_su; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_landingpagearticlesummary
    ADD CONSTRAINT find_a_supplier_land_page_pt_id_1e3fe6a9_fk_find_a_su FOREIGN KEY (page_pt_id) REFERENCES public.find_a_supplier_landingpage(page_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_landingpage find_a_supplier_land_page_ptr_id_1fb2205e_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_landingpage
    ADD CONSTRAINT find_a_supplier_land_page_ptr_id_1fb2205e_fk_wagtailco FOREIGN KEY (page_ptr_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_landingpagearticlesummary find_a_supplier_land_page_ru_id_51fd06ed_fk_find_a_su; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_landingpagearticlesummary
    ADD CONSTRAINT find_a_supplier_land_page_ru_id_51fd06ed_fk_find_a_su FOREIGN KEY (page_ru_id) REFERENCES public.find_a_supplier_landingpage(page_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_landingpagearticlesummary find_a_supplier_land_page_zh_hans_id_1972a979_fk_find_a_su; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_landingpagearticlesummary
    ADD CONSTRAINT find_a_supplier_land_page_zh_hans_id_1972a979_fk_find_a_su FOREIGN KEY (page_zh_hans_id) REFERENCES public.find_a_supplier_landingpage(page_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_landingpage find_a_supplier_land_services_column_four_072ed0b7_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_landingpage
    ADD CONSTRAINT find_a_supplier_land_services_column_four_072ed0b7_fk_wagtailim FOREIGN KEY (services_column_four_icon_fr_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_landingpage find_a_supplier_land_services_column_four_2a144e98_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_landingpage
    ADD CONSTRAINT find_a_supplier_land_services_column_four_2a144e98_fk_wagtailim FOREIGN KEY (services_column_four_icon_ar_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_landingpage find_a_supplier_land_services_column_four_2d66fc19_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_landingpage
    ADD CONSTRAINT find_a_supplier_land_services_column_four_2d66fc19_fk_wagtailim FOREIGN KEY (services_column_four_icon_es_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_landingpage find_a_supplier_land_services_column_four_3c9f0ee0_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_landingpage
    ADD CONSTRAINT find_a_supplier_land_services_column_four_3c9f0ee0_fk_wagtailim FOREIGN KEY (services_column_four_icon_en_gb_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_landingpage find_a_supplier_land_services_column_four_81049aca_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_landingpage
    ADD CONSTRAINT find_a_supplier_land_services_column_four_81049aca_fk_wagtailim FOREIGN KEY (services_column_four_icon_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_landingpage find_a_supplier_land_services_column_four_85cc6518_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_landingpage
    ADD CONSTRAINT find_a_supplier_land_services_column_four_85cc6518_fk_wagtailim FOREIGN KEY (services_column_four_icon_pt_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_landingpage find_a_supplier_land_services_column_four_987a4695_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_landingpage
    ADD CONSTRAINT find_a_supplier_land_services_column_four_987a4695_fk_wagtailim FOREIGN KEY (services_column_four_icon_pt_br_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_landingpage find_a_supplier_land_services_column_four_ad868ac2_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_landingpage
    ADD CONSTRAINT find_a_supplier_land_services_column_four_ad868ac2_fk_wagtailim FOREIGN KEY (services_column_four_icon_de_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_landingpage find_a_supplier_land_services_column_four_cf16e03e_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_landingpage
    ADD CONSTRAINT find_a_supplier_land_services_column_four_cf16e03e_fk_wagtailim FOREIGN KEY (services_column_four_icon_ru_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_landingpage find_a_supplier_land_services_column_four_d12a379f_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_landingpage
    ADD CONSTRAINT find_a_supplier_land_services_column_four_d12a379f_fk_wagtailim FOREIGN KEY (services_column_four_icon_ja_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_landingpage find_a_supplier_land_services_column_four_f5bcad12_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_landingpage
    ADD CONSTRAINT find_a_supplier_land_services_column_four_f5bcad12_fk_wagtailim FOREIGN KEY (services_column_four_icon_zh_hans_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_landingpage find_a_supplier_land_services_column_one__0244324a_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_landingpage
    ADD CONSTRAINT find_a_supplier_land_services_column_one__0244324a_fk_wagtailim FOREIGN KEY (services_column_one_icon_zh_hans_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_landingpage find_a_supplier_land_services_column_one__07d71f50_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_landingpage
    ADD CONSTRAINT find_a_supplier_land_services_column_one__07d71f50_fk_wagtailim FOREIGN KEY (services_column_one_icon_de_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_landingpage find_a_supplier_land_services_column_one__28a5c41d_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_landingpage
    ADD CONSTRAINT find_a_supplier_land_services_column_one__28a5c41d_fk_wagtailim FOREIGN KEY (services_column_one_icon_en_gb_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_landingpage find_a_supplier_land_services_column_one__3d218e3f_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_landingpage
    ADD CONSTRAINT find_a_supplier_land_services_column_one__3d218e3f_fk_wagtailim FOREIGN KEY (services_column_one_icon_fr_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_landingpage find_a_supplier_land_services_column_one__5b8e4485_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_landingpage
    ADD CONSTRAINT find_a_supplier_land_services_column_one__5b8e4485_fk_wagtailim FOREIGN KEY (services_column_one_icon_ru_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_landingpage find_a_supplier_land_services_column_one__7e8adcef_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_landingpage
    ADD CONSTRAINT find_a_supplier_land_services_column_one__7e8adcef_fk_wagtailim FOREIGN KEY (services_column_one_icon_ar_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_landingpage find_a_supplier_land_services_column_one__b1109e29_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_landingpage
    ADD CONSTRAINT find_a_supplier_land_services_column_one__b1109e29_fk_wagtailim FOREIGN KEY (services_column_one_icon_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_landingpage find_a_supplier_land_services_column_one__d33d9fb6_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_landingpage
    ADD CONSTRAINT find_a_supplier_land_services_column_one__d33d9fb6_fk_wagtailim FOREIGN KEY (services_column_one_icon_pt_br_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_landingpage find_a_supplier_land_services_column_one__db9a4d43_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_landingpage
    ADD CONSTRAINT find_a_supplier_land_services_column_one__db9a4d43_fk_wagtailim FOREIGN KEY (services_column_one_icon_pt_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_landingpage find_a_supplier_land_services_column_one__f818c154_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_landingpage
    ADD CONSTRAINT find_a_supplier_land_services_column_one__f818c154_fk_wagtailim FOREIGN KEY (services_column_one_icon_es_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_landingpage find_a_supplier_land_services_column_one__fdb1b3bf_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_landingpage
    ADD CONSTRAINT find_a_supplier_land_services_column_one__fdb1b3bf_fk_wagtailim FOREIGN KEY (services_column_one_icon_ja_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_landingpage find_a_supplier_land_services_column_thre_2d74f9eb_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_landingpage
    ADD CONSTRAINT find_a_supplier_land_services_column_thre_2d74f9eb_fk_wagtailim FOREIGN KEY (services_column_three_icon_zh_hans_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_landingpage find_a_supplier_land_services_column_thre_3332bd7a_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_landingpage
    ADD CONSTRAINT find_a_supplier_land_services_column_thre_3332bd7a_fk_wagtailim FOREIGN KEY (services_column_three_icon_ar_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_landingpage find_a_supplier_land_services_column_thre_60905b76_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_landingpage
    ADD CONSTRAINT find_a_supplier_land_services_column_thre_60905b76_fk_wagtailim FOREIGN KEY (services_column_three_icon_ja_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_landingpage find_a_supplier_land_services_column_thre_70034717_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_landingpage
    ADD CONSTRAINT find_a_supplier_land_services_column_thre_70034717_fk_wagtailim FOREIGN KEY (services_column_three_icon_es_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_landingpage find_a_supplier_land_services_column_thre_7bb2e58b_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_landingpage
    ADD CONSTRAINT find_a_supplier_land_services_column_thre_7bb2e58b_fk_wagtailim FOREIGN KEY (services_column_three_icon_ru_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_landingpage find_a_supplier_land_services_column_thre_ae7ddbb5_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_landingpage
    ADD CONSTRAINT find_a_supplier_land_services_column_thre_ae7ddbb5_fk_wagtailim FOREIGN KEY (services_column_three_icon_pt_br_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_landingpage find_a_supplier_land_services_column_thre_b2bd5ecc_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_landingpage
    ADD CONSTRAINT find_a_supplier_land_services_column_thre_b2bd5ecc_fk_wagtailim FOREIGN KEY (services_column_three_icon_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_landingpage find_a_supplier_land_services_column_thre_b8fe2d12_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_landingpage
    ADD CONSTRAINT find_a_supplier_land_services_column_thre_b8fe2d12_fk_wagtailim FOREIGN KEY (services_column_three_icon_fr_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_landingpage find_a_supplier_land_services_column_thre_d6066d52_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_landingpage
    ADD CONSTRAINT find_a_supplier_land_services_column_thre_d6066d52_fk_wagtailim FOREIGN KEY (services_column_three_icon_pt_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_landingpage find_a_supplier_land_services_column_thre_dbeb4fd6_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_landingpage
    ADD CONSTRAINT find_a_supplier_land_services_column_thre_dbeb4fd6_fk_wagtailim FOREIGN KEY (services_column_three_icon_de_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_landingpage find_a_supplier_land_services_column_thre_de7a7533_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_landingpage
    ADD CONSTRAINT find_a_supplier_land_services_column_thre_de7a7533_fk_wagtailim FOREIGN KEY (services_column_three_icon_en_gb_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_landingpage find_a_supplier_land_services_column_two__0add801a_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_landingpage
    ADD CONSTRAINT find_a_supplier_land_services_column_two__0add801a_fk_wagtailim FOREIGN KEY (services_column_two_icon_ru_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_landingpage find_a_supplier_land_services_column_two__3119d3f7_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_landingpage
    ADD CONSTRAINT find_a_supplier_land_services_column_two__3119d3f7_fk_wagtailim FOREIGN KEY (services_column_two_icon_de_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_landingpage find_a_supplier_land_services_column_two__3e1f0de4_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_landingpage
    ADD CONSTRAINT find_a_supplier_land_services_column_two__3e1f0de4_fk_wagtailim FOREIGN KEY (services_column_two_icon_en_gb_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_landingpage find_a_supplier_land_services_column_two__43e311fb_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_landingpage
    ADD CONSTRAINT find_a_supplier_land_services_column_two__43e311fb_fk_wagtailim FOREIGN KEY (services_column_two_icon_ja_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_landingpage find_a_supplier_land_services_column_two__7699d7e0_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_landingpage
    ADD CONSTRAINT find_a_supplier_land_services_column_two__7699d7e0_fk_wagtailim FOREIGN KEY (services_column_two_icon_zh_hans_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_landingpage find_a_supplier_land_services_column_two__76cf917f_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_landingpage
    ADD CONSTRAINT find_a_supplier_land_services_column_two__76cf917f_fk_wagtailim FOREIGN KEY (services_column_two_icon_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_landingpage find_a_supplier_land_services_column_two__a437d62f_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_landingpage
    ADD CONSTRAINT find_a_supplier_land_services_column_two__a437d62f_fk_wagtailim FOREIGN KEY (services_column_two_icon_pt_br_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_landingpage find_a_supplier_land_services_column_two__bafd2caf_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_landingpage
    ADD CONSTRAINT find_a_supplier_land_services_column_two__bafd2caf_fk_wagtailim FOREIGN KEY (services_column_two_icon_pt_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_landingpage find_a_supplier_land_services_column_two__ece32492_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_landingpage
    ADD CONSTRAINT find_a_supplier_land_services_column_two__ece32492_fk_wagtailim FOREIGN KEY (services_column_two_icon_es_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_landingpage find_a_supplier_land_services_column_two__f4ac7f00_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_landingpage
    ADD CONSTRAINT find_a_supplier_land_services_column_two__f4ac7f00_fk_wagtailim FOREIGN KEY (services_column_two_icon_fr_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_landingpage find_a_supplier_land_services_column_two__f8e32d2f_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_landingpage
    ADD CONSTRAINT find_a_supplier_land_services_column_two__f8e32d2f_fk_wagtailim FOREIGN KEY (services_column_two_icon_ar_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: find_a_supplier_landingpagearticlesummary find_a_supplier_land_video_media_id_1bdc3add_fk_wagtailme; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.find_a_supplier_landingpagearticlesummary
    ADD CONSTRAINT find_a_supplier_land_video_media_id_1bdc3add_fk_wagtailme FOREIGN KEY (video_media_id) REFERENCES public.wagtailmedia_media(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: great_international_internationalarticlepage great_international__article_image_id_aa9240b3_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.great_international_internationalarticlepage
    ADD CONSTRAINT great_international__article_image_id_aa9240b3_fk_wagtailim FOREIGN KEY (article_image_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: great_international_internationalcampaignpage great_international__campaign_hero_image__7170da9a_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.great_international_internationalcampaignpage
    ADD CONSTRAINT great_international__campaign_hero_image__7170da9a_fk_wagtailim FOREIGN KEY (campaign_hero_image_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: great_international_internationalsectorpage great_international__case_study_image_id_6d174391_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.great_international_internationalsectorpage
    ADD CONSTRAINT great_international__case_study_image_id_6d174391_fk_wagtailim FOREIGN KEY (case_study_image_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: great_international_internationaltopiclandingpage great_international__hero_image_id_2e7c0845_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.great_international_internationaltopiclandingpage
    ADD CONSTRAINT great_international__hero_image_id_2e7c0845_fk_wagtailim FOREIGN KEY (hero_image_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: great_international_internationalsectorpage great_international__hero_image_id_995757cb_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.great_international_internationalsectorpage
    ADD CONSTRAINT great_international__hero_image_id_995757cb_fk_wagtailim FOREIGN KEY (hero_image_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: great_international_internationalarticlelistingpage great_international__hero_image_id_bc57f482_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.great_international_internationalarticlelistingpage
    ADD CONSTRAINT great_international__hero_image_id_bc57f482_fk_wagtailim FOREIGN KEY (hero_image_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: great_international_internationalarticlelistingpage_tags great_international__internationalarticle_33df4cd4_fk_great_int; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.great_international_internationalarticlelistingpage_tags
    ADD CONSTRAINT great_international__internationalarticle_33df4cd4_fk_great_int FOREIGN KEY (internationalarticlelistingpage_id) REFERENCES public.great_international_internationalarticlelistingpage(page_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: great_international_internationalarticlepage_tags great_international__internationalarticle_92b154aa_fk_great_int; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.great_international_internationalarticlepage_tags
    ADD CONSTRAINT great_international__internationalarticle_92b154aa_fk_great_int FOREIGN KEY (internationalarticlepage_id) REFERENCES public.great_international_internationalarticlepage(page_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: great_international_internationalcampaignpage_tags great_international__internationalcampaig_1475a34f_fk_great_int; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.great_international_internationalcampaignpage_tags
    ADD CONSTRAINT great_international__internationalcampaig_1475a34f_fk_great_int FOREIGN KEY (internationalcampaignpage_id) REFERENCES public.great_international_internationalcampaignpage(page_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: great_international_internationalregionpage_tags great_international__internationalregionp_f86f9b1a_fk_great_int; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.great_international_internationalregionpage_tags
    ADD CONSTRAINT great_international__internationalregionp_f86f9b1a_fk_great_int FOREIGN KEY (internationalregionpage_id) REFERENCES public.great_international_internationalregionpage(page_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: great_international_internationaltopiclandingpage_tags great_international__internationaltopicla_6cf777f6_fk_great_int; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.great_international_internationaltopiclandingpage_tags
    ADD CONSTRAINT great_international__internationaltopicla_6cf777f6_fk_great_int FOREIGN KEY (internationaltopiclandingpage_id) REFERENCES public.great_international_internationaltopiclandingpage(page_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: great_international_internationalarticlepage great_international__page_ptr_id_07743492_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.great_international_internationalarticlepage
    ADD CONSTRAINT great_international__page_ptr_id_07743492_fk_wagtailco FOREIGN KEY (page_ptr_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: great_international_internationalsectorpage great_international__page_ptr_id_4ad0f5a9_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.great_international_internationalsectorpage
    ADD CONSTRAINT great_international__page_ptr_id_4ad0f5a9_fk_wagtailco FOREIGN KEY (page_ptr_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: great_international_internationalarticlelistingpage great_international__page_ptr_id_6df7ff9c_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.great_international_internationalarticlelistingpage
    ADD CONSTRAINT great_international__page_ptr_id_6df7ff9c_fk_wagtailco FOREIGN KEY (page_ptr_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: great_international_internationalcampaignpage great_international__page_ptr_id_813d1aab_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.great_international_internationalcampaignpage
    ADD CONSTRAINT great_international__page_ptr_id_813d1aab_fk_wagtailco FOREIGN KEY (page_ptr_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: great_international_internationaltopiclandingpage great_international__page_ptr_id_af82f41c_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.great_international_internationaltopiclandingpage
    ADD CONSTRAINT great_international__page_ptr_id_af82f41c_fk_wagtailco FOREIGN KEY (page_ptr_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: great_international_internationalhomepage great_international__page_ptr_id_d432b23c_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.great_international_internationalhomepage
    ADD CONSTRAINT great_international__page_ptr_id_d432b23c_fk_wagtailco FOREIGN KEY (page_ptr_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: great_international_internationallocalisedfolderpage great_international__page_ptr_id_e4cce4ec_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.great_international_internationallocalisedfolderpage
    ADD CONSTRAINT great_international__page_ptr_id_e4cce4ec_fk_wagtailco FOREIGN KEY (page_ptr_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: great_international_greatinternationalapp great_international__page_ptr_id_e94f663f_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.great_international_greatinternationalapp
    ADD CONSTRAINT great_international__page_ptr_id_e94f663f_fk_wagtailco FOREIGN KEY (page_ptr_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: great_international_internationalregionpage great_international__page_ptr_id_f44a3e2a_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.great_international_internationalregionpage
    ADD CONSTRAINT great_international__page_ptr_id_f44a3e2a_fk_wagtailco FOREIGN KEY (page_ptr_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: great_international_internationalsectorpage great_international__related_page_one_id_181b10cd_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.great_international_internationalsectorpage
    ADD CONSTRAINT great_international__related_page_one_id_181b10cd_fk_wagtailco FOREIGN KEY (related_page_one_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: great_international_internationalhomepage great_international__related_page_one_id_38d9eafc_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.great_international_internationalhomepage
    ADD CONSTRAINT great_international__related_page_one_id_38d9eafc_fk_wagtailco FOREIGN KEY (related_page_one_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: great_international_internationalarticlepage great_international__related_page_one_id_a843bb9e_fk_great_int; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.great_international_internationalarticlepage
    ADD CONSTRAINT great_international__related_page_one_id_a843bb9e_fk_great_int FOREIGN KEY (related_page_one_id) REFERENCES public.great_international_internationalarticlepage(page_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: great_international_internationalcampaignpage great_international__related_page_one_id_b5973886_fk_great_int; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.great_international_internationalcampaignpage
    ADD CONSTRAINT great_international__related_page_one_id_b5973886_fk_great_int FOREIGN KEY (related_page_one_id) REFERENCES public.great_international_internationalarticlepage(page_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: great_international_internationalcampaignpage great_international__related_page_three_i_7da7da1a_fk_great_int; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.great_international_internationalcampaignpage
    ADD CONSTRAINT great_international__related_page_three_i_7da7da1a_fk_great_int FOREIGN KEY (related_page_three_id) REFERENCES public.great_international_internationalarticlepage(page_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: great_international_internationalarticlepage great_international__related_page_three_i_c1182ff1_fk_great_int; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.great_international_internationalarticlepage
    ADD CONSTRAINT great_international__related_page_three_i_c1182ff1_fk_great_int FOREIGN KEY (related_page_three_id) REFERENCES public.great_international_internationalarticlepage(page_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: great_international_internationalhomepage great_international__related_page_three_i_c3943fa9_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.great_international_internationalhomepage
    ADD CONSTRAINT great_international__related_page_three_i_c3943fa9_fk_wagtailco FOREIGN KEY (related_page_three_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: great_international_internationalsectorpage great_international__related_page_three_i_da3ce1ef_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.great_international_internationalsectorpage
    ADD CONSTRAINT great_international__related_page_three_i_da3ce1ef_fk_wagtailco FOREIGN KEY (related_page_three_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: great_international_internationalarticlepage great_international__related_page_two_id_92e5cf67_fk_great_int; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.great_international_internationalarticlepage
    ADD CONSTRAINT great_international__related_page_two_id_92e5cf67_fk_great_int FOREIGN KEY (related_page_two_id) REFERENCES public.great_international_internationalarticlepage(page_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: great_international_internationalsectorpage great_international__related_page_two_id_a578a749_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.great_international_internationalsectorpage
    ADD CONSTRAINT great_international__related_page_two_id_a578a749_fk_wagtailco FOREIGN KEY (related_page_two_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: great_international_internationalcampaignpage great_international__related_page_two_id_ae88f175_fk_great_int; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.great_international_internationalcampaignpage
    ADD CONSTRAINT great_international__related_page_two_id_ae88f175_fk_great_int FOREIGN KEY (related_page_two_id) REFERENCES public.great_international_internationalarticlepage(page_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: great_international_internationalhomepage great_international__related_page_two_id_da4f8c42_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.great_international_internationalhomepage
    ADD CONSTRAINT great_international__related_page_two_id_da4f8c42_fk_wagtailco FOREIGN KEY (related_page_two_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: great_international_internationalsectorpage great_international__section_one_image_id_6de74989_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.great_international_internationalsectorpage
    ADD CONSTRAINT great_international__section_one_image_id_6de74989_fk_wagtailim FOREIGN KEY (section_one_image_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: great_international_internationalcampaignpage great_international__section_one_image_id_84c75b25_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.great_international_internationalcampaignpage
    ADD CONSTRAINT great_international__section_one_image_id_84c75b25_fk_wagtailim FOREIGN KEY (section_one_image_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: great_international_internationalcampaignpage great_international__section_two_image_id_95d17c97_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.great_international_internationalcampaignpage
    ADD CONSTRAINT great_international__section_two_image_id_95d17c97_fk_wagtailim FOREIGN KEY (section_two_image_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: great_international_internationalsectorpage great_international__section_two_subsecti_7646efd8_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.great_international_internationalsectorpage
    ADD CONSTRAINT great_international__section_two_subsecti_7646efd8_fk_wagtailim FOREIGN KEY (section_two_subsection_one_icon_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: great_international_internationalsectorpage great_international__section_two_subsecti_9c130204_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.great_international_internationalsectorpage
    ADD CONSTRAINT great_international__section_two_subsecti_9c130204_fk_wagtailim FOREIGN KEY (section_two_subsection_two_icon_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: great_international_internationalsectorpage great_international__section_two_subsecti_fe5dfaf4_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.great_international_internationalsectorpage
    ADD CONSTRAINT great_international__section_two_subsecti_fe5dfaf4_fk_wagtailim FOREIGN KEY (section_two_subsection_three_icon_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: great_international_internationalcampaignpage great_international__selling_point_one_ic_100503e1_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.great_international_internationalcampaignpage
    ADD CONSTRAINT great_international__selling_point_one_ic_100503e1_fk_wagtailim FOREIGN KEY (selling_point_one_icon_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: great_international_internationalcampaignpage great_international__selling_point_three__94d54bb6_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.great_international_internationalcampaignpage
    ADD CONSTRAINT great_international__selling_point_three__94d54bb6_fk_wagtailim FOREIGN KEY (selling_point_three_icon_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: great_international_internationalcampaignpage great_international__selling_point_two_ic_ca530800_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.great_international_internationalcampaignpage
    ADD CONSTRAINT great_international__selling_point_two_ic_ca530800_fk_wagtailim FOREIGN KEY (selling_point_two_icon_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: great_international_internationalcampaignpage_tags great_international__tag_id_1f99e22b_fk_export_re; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.great_international_internationalcampaignpage_tags
    ADD CONSTRAINT great_international__tag_id_1f99e22b_fk_export_re FOREIGN KEY (tag_id) REFERENCES public.export_readiness_tag(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: great_international_internationalarticlelistingpage_tags great_international__tag_id_27c1d52c_fk_export_re; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.great_international_internationalarticlelistingpage_tags
    ADD CONSTRAINT great_international__tag_id_27c1d52c_fk_export_re FOREIGN KEY (tag_id) REFERENCES public.export_readiness_tag(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: great_international_internationaltopiclandingpage_tags great_international__tag_id_4f3127d9_fk_export_re; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.great_international_internationaltopiclandingpage_tags
    ADD CONSTRAINT great_international__tag_id_4f3127d9_fk_export_re FOREIGN KEY (tag_id) REFERENCES public.export_readiness_tag(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: great_international_internationalregionpage_tags great_international__tag_id_717bde30_fk_export_re; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.great_international_internationalregionpage_tags
    ADD CONSTRAINT great_international__tag_id_717bde30_fk_export_re FOREIGN KEY (tag_id) REFERENCES public.export_readiness_tag(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: great_international_internationalarticlepage_tags great_international__tag_id_e4984ba1_fk_export_re; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.great_international_internationalarticlepage_tags
    ADD CONSTRAINT great_international__tag_id_e4984ba1_fk_export_re FOREIGN KEY (tag_id) REFERENCES public.export_readiness_tag(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: great_international_internationalhomepage great_international__tariffs_image_id_c84156ca_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.great_international_internationalhomepage
    ADD CONSTRAINT great_international__tariffs_image_id_c84156ca_fk_wagtailim FOREIGN KEY (tariffs_image_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_highpotentialopportunitydetailpage invest_highpotential_case_study_four_imag_7d6ba663_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_highpotentialopportunitydetailpage
    ADD CONSTRAINT invest_highpotential_case_study_four_imag_7d6ba663_fk_wagtailim FOREIGN KEY (case_study_four_image_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_highpotentialopportunitydetailpage invest_highpotential_case_study_one_image_ba757ba9_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_highpotentialopportunitydetailpage
    ADD CONSTRAINT invest_highpotential_case_study_one_image_ba757ba9_fk_wagtailim FOREIGN KEY (case_study_one_image_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_highpotentialopportunitydetailpage invest_highpotential_case_study_three_ima_034f8a93_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_highpotentialopportunitydetailpage
    ADD CONSTRAINT invest_highpotential_case_study_three_ima_034f8a93_fk_wagtailim FOREIGN KEY (case_study_three_image_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_highpotentialopportunitydetailpage invest_highpotential_case_study_two_image_7765394b_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_highpotentialopportunitydetailpage
    ADD CONSTRAINT invest_highpotential_case_study_two_image_7765394b_fk_wagtailim FOREIGN KEY (case_study_two_image_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_highpotentialopportunitydetailpage invest_highpotential_companies_list_item__24ac23e1_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_highpotentialopportunitydetailpage
    ADD CONSTRAINT invest_highpotential_companies_list_item__24ac23e1_fk_wagtailim FOREIGN KEY (companies_list_item_image_seven_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_highpotentialopportunitydetailpage invest_highpotential_companies_list_item__607e453f_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_highpotentialopportunitydetailpage
    ADD CONSTRAINT invest_highpotential_companies_list_item__607e453f_fk_wagtailim FOREIGN KEY (companies_list_item_image_five_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_highpotentialopportunitydetailpage invest_highpotential_companies_list_item__689352eb_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_highpotentialopportunitydetailpage
    ADD CONSTRAINT invest_highpotential_companies_list_item__689352eb_fk_wagtailim FOREIGN KEY (companies_list_item_image_eight_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_highpotentialopportunitydetailpage invest_highpotential_companies_list_item__69535e2d_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_highpotentialopportunitydetailpage
    ADD CONSTRAINT invest_highpotential_companies_list_item__69535e2d_fk_wagtailim FOREIGN KEY (companies_list_item_image_one_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_highpotentialopportunitydetailpage invest_highpotential_companies_list_item__6c22af18_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_highpotentialopportunitydetailpage
    ADD CONSTRAINT invest_highpotential_companies_list_item__6c22af18_fk_wagtailim FOREIGN KEY (companies_list_item_image_three_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_highpotentialopportunitydetailpage invest_highpotential_companies_list_item__c4205164_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_highpotentialopportunitydetailpage
    ADD CONSTRAINT invest_highpotential_companies_list_item__c4205164_fk_wagtailim FOREIGN KEY (companies_list_item_image_six_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_highpotentialopportunitydetailpage invest_highpotential_companies_list_item__e511f30b_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_highpotentialopportunitydetailpage
    ADD CONSTRAINT invest_highpotential_companies_list_item__e511f30b_fk_wagtailim FOREIGN KEY (companies_list_item_image_two_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_highpotentialopportunitydetailpage invest_highpotential_companies_list_item__f59bbf99_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_highpotentialopportunitydetailpage
    ADD CONSTRAINT invest_highpotential_companies_list_item__f59bbf99_fk_wagtailim FOREIGN KEY (companies_list_item_image_four_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_highpotentialopportunitydetailpage invest_highpotential_competitive_advantag_33a2dcf6_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_highpotentialopportunitydetailpage
    ADD CONSTRAINT invest_highpotential_competitive_advantag_33a2dcf6_fk_wagtailim FOREIGN KEY (competitive_advantages_list_item_one_icon_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_highpotentialopportunitydetailpage invest_highpotential_competitive_advantag_89da55bd_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_highpotentialopportunitydetailpage
    ADD CONSTRAINT invest_highpotential_competitive_advantag_89da55bd_fk_wagtailim FOREIGN KEY (competitive_advantages_list_item_two_icon_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_highpotentialopportunitydetailpage invest_highpotential_competitive_advantag_9555f962_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_highpotentialopportunitydetailpage
    ADD CONSTRAINT invest_highpotential_competitive_advantag_9555f962_fk_wagtailim FOREIGN KEY (competitive_advantages_list_item_three_icon_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_highpotentialopportunitydetailpage invest_highpotential_hero_image_id_39933ff3_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_highpotentialopportunitydetailpage
    ADD CONSTRAINT invest_highpotential_hero_image_id_39933ff3_fk_wagtailim FOREIGN KEY (hero_image_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_highpotentialopportunitydetailpage invest_highpotential_opportunity_list_ima_39bfbdee_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_highpotentialopportunitydetailpage
    ADD CONSTRAINT invest_highpotential_opportunity_list_ima_39bfbdee_fk_wagtailim FOREIGN KEY (opportunity_list_image_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_highpotentialopportunityformsuccesspage invest_highpotential_page_ptr_id_a7ad4949_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_highpotentialopportunityformsuccesspage
    ADD CONSTRAINT invest_highpotential_page_ptr_id_a7ad4949_fk_wagtailco FOREIGN KEY (page_ptr_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_highpotentialopportunityformpage invest_highpotential_page_ptr_id_a8398cf4_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_highpotentialopportunityformpage
    ADD CONSTRAINT invest_highpotential_page_ptr_id_a8398cf4_fk_wagtailco FOREIGN KEY (page_ptr_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_highpotentialopportunitydetailpage invest_highpotential_page_ptr_id_e9139d8d_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_highpotentialopportunitydetailpage
    ADD CONSTRAINT invest_highpotential_page_ptr_id_e9139d8d_fk_wagtailco FOREIGN KEY (page_ptr_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_highpotentialopportunitydetailpage invest_highpotential_pdf_document_id_7452b06c_fk_wagtaildo; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_highpotentialopportunitydetailpage
    ADD CONSTRAINT invest_highpotential_pdf_document_id_7452b06c_fk_wagtaildo FOREIGN KEY (pdf_document_id) REFERENCES public.wagtaildocs_document(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_highpotentialopportunitydetailpage invest_highpotential_proposition_one_imag_3cb62d0e_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_highpotentialopportunitydetailpage
    ADD CONSTRAINT invest_highpotential_proposition_one_imag_3cb62d0e_fk_wagtailim FOREIGN KEY (proposition_one_image_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_highpotentialopportunitydetailpage invest_highpotential_proposition_one_vide_ee82eb9b_fk_wagtailme; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_highpotentialopportunitydetailpage
    ADD CONSTRAINT invest_highpotential_proposition_one_vide_ee82eb9b_fk_wagtailme FOREIGN KEY (proposition_one_video_id) REFERENCES public.wagtailmedia_media(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_highpotentialopportunitydetailpage invest_highpotential_proposition_two_imag_16381e09_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_highpotentialopportunitydetailpage
    ADD CONSTRAINT invest_highpotential_proposition_two_imag_16381e09_fk_wagtailim FOREIGN KEY (proposition_two_image_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_highpotentialopportunitydetailpage invest_highpotential_proposition_two_vide_81ed7649_fk_wagtailme; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_highpotentialopportunitydetailpage
    ADD CONSTRAINT invest_highpotential_proposition_two_vide_81ed7649_fk_wagtailme FOREIGN KEY (proposition_two_video_id) REFERENCES public.wagtailmedia_media(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_highpotentialopportunitydetailpage invest_highpotential_summary_image_id_2687e608_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_highpotentialopportunitydetailpage
    ADD CONSTRAINT invest_highpotential_summary_image_id_2687e608_fk_wagtailim FOREIGN KEY (summary_image_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_highpotentialopportunitydetailpage invest_highpotential_testimonial_backgrou_438c0bf6_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_highpotentialopportunitydetailpage
    ADD CONSTRAINT invest_highpotential_testimonial_backgrou_438c0bf6_fk_wagtailim FOREIGN KEY (testimonial_background_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_infopage invest_infopage_page_ptr_id_159e58b0_fk_wagtailcore_page_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_infopage
    ADD CONSTRAINT invest_infopage_page_ptr_id_159e58b0_fk_wagtailcore_page_id FOREIGN KEY (page_ptr_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_investapp invest_investapp_page_ptr_id_53fe18ed_fk_wagtailcore_page_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_investapp
    ADD CONSTRAINT invest_investapp_page_ptr_id_53fe18ed_fk_wagtailcore_page_id FOREIGN KEY (page_ptr_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_investhomepage invest_investhomepag_hero_image_id_a2dbcafe_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_investhomepage
    ADD CONSTRAINT invest_investhomepag_hero_image_id_a2dbcafe_fk_wagtailim FOREIGN KEY (hero_image_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_investhomepage invest_investhomepag_how_we_help_icon_fiv_569e774c_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_investhomepage
    ADD CONSTRAINT invest_investhomepag_how_we_help_icon_fiv_569e774c_fk_wagtailim FOREIGN KEY (how_we_help_icon_five_ru_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_investhomepage invest_investhomepag_how_we_help_icon_fiv_5f4b6bfe_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_investhomepage
    ADD CONSTRAINT invest_investhomepag_how_we_help_icon_fiv_5f4b6bfe_fk_wagtailim FOREIGN KEY (how_we_help_icon_five_fr_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_investhomepage invest_investhomepag_how_we_help_icon_fiv_74a7d91a_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_investhomepage
    ADD CONSTRAINT invest_investhomepag_how_we_help_icon_fiv_74a7d91a_fk_wagtailim FOREIGN KEY (how_we_help_icon_five_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_investhomepage invest_investhomepag_how_we_help_icon_fiv_8ec5c27a_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_investhomepage
    ADD CONSTRAINT invest_investhomepag_how_we_help_icon_fiv_8ec5c27a_fk_wagtailim FOREIGN KEY (how_we_help_icon_five_ar_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_investhomepage invest_investhomepag_how_we_help_icon_fiv_9e5eb318_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_investhomepage
    ADD CONSTRAINT invest_investhomepag_how_we_help_icon_fiv_9e5eb318_fk_wagtailim FOREIGN KEY (how_we_help_icon_five_en_gb_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_investhomepage invest_investhomepag_how_we_help_icon_fiv_b2ed9b3b_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_investhomepage
    ADD CONSTRAINT invest_investhomepag_how_we_help_icon_fiv_b2ed9b3b_fk_wagtailim FOREIGN KEY (how_we_help_icon_five_de_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_investhomepage invest_investhomepag_how_we_help_icon_fiv_c8f0a784_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_investhomepage
    ADD CONSTRAINT invest_investhomepag_how_we_help_icon_fiv_c8f0a784_fk_wagtailim FOREIGN KEY (how_we_help_icon_five_ja_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_investhomepage invest_investhomepag_how_we_help_icon_fiv_f1712768_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_investhomepage
    ADD CONSTRAINT invest_investhomepag_how_we_help_icon_fiv_f1712768_fk_wagtailim FOREIGN KEY (how_we_help_icon_five_pt_br_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_investhomepage invest_investhomepag_how_we_help_icon_fiv_f37325cd_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_investhomepage
    ADD CONSTRAINT invest_investhomepag_how_we_help_icon_fiv_f37325cd_fk_wagtailim FOREIGN KEY (how_we_help_icon_five_es_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_investhomepage invest_investhomepag_how_we_help_icon_fiv_f452675a_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_investhomepage
    ADD CONSTRAINT invest_investhomepag_how_we_help_icon_fiv_f452675a_fk_wagtailim FOREIGN KEY (how_we_help_icon_five_pt_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_investhomepage invest_investhomepag_how_we_help_icon_fiv_fde8f74c_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_investhomepage
    ADD CONSTRAINT invest_investhomepag_how_we_help_icon_fiv_fde8f74c_fk_wagtailim FOREIGN KEY (how_we_help_icon_five_zh_hans_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_investhomepage invest_investhomepag_how_we_help_icon_fou_15ee206d_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_investhomepage
    ADD CONSTRAINT invest_investhomepag_how_we_help_icon_fou_15ee206d_fk_wagtailim FOREIGN KEY (how_we_help_icon_four_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_investhomepage invest_investhomepag_how_we_help_icon_fou_2288cb1b_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_investhomepage
    ADD CONSTRAINT invest_investhomepag_how_we_help_icon_fou_2288cb1b_fk_wagtailim FOREIGN KEY (how_we_help_icon_four_zh_hans_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_investhomepage invest_investhomepag_how_we_help_icon_fou_30fc166d_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_investhomepage
    ADD CONSTRAINT invest_investhomepag_how_we_help_icon_fou_30fc166d_fk_wagtailim FOREIGN KEY (how_we_help_icon_four_fr_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_investhomepage invest_investhomepag_how_we_help_icon_fou_4e58c507_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_investhomepage
    ADD CONSTRAINT invest_investhomepag_how_we_help_icon_fou_4e58c507_fk_wagtailim FOREIGN KEY (how_we_help_icon_four_es_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_investhomepage invest_investhomepag_how_we_help_icon_fou_50a9e52a_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_investhomepage
    ADD CONSTRAINT invest_investhomepag_how_we_help_icon_fou_50a9e52a_fk_wagtailim FOREIGN KEY (how_we_help_icon_four_de_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_investhomepage invest_investhomepag_how_we_help_icon_fou_6cc9c5ef_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_investhomepage
    ADD CONSTRAINT invest_investhomepag_how_we_help_icon_fou_6cc9c5ef_fk_wagtailim FOREIGN KEY (how_we_help_icon_four_pt_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_investhomepage invest_investhomepag_how_we_help_icon_fou_73bcef52_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_investhomepage
    ADD CONSTRAINT invest_investhomepag_how_we_help_icon_fou_73bcef52_fk_wagtailim FOREIGN KEY (how_we_help_icon_four_en_gb_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_investhomepage invest_investhomepag_how_we_help_icon_fou_79c301b7_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_investhomepage
    ADD CONSTRAINT invest_investhomepag_how_we_help_icon_fou_79c301b7_fk_wagtailim FOREIGN KEY (how_we_help_icon_four_ar_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_investhomepage invest_investhomepag_how_we_help_icon_fou_cd433b63_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_investhomepage
    ADD CONSTRAINT invest_investhomepag_how_we_help_icon_fou_cd433b63_fk_wagtailim FOREIGN KEY (how_we_help_icon_four_ru_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_investhomepage invest_investhomepag_how_we_help_icon_fou_ddda13d6_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_investhomepage
    ADD CONSTRAINT invest_investhomepag_how_we_help_icon_fou_ddda13d6_fk_wagtailim FOREIGN KEY (how_we_help_icon_four_ja_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_investhomepage invest_investhomepag_how_we_help_icon_fou_eb716ad6_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_investhomepage
    ADD CONSTRAINT invest_investhomepag_how_we_help_icon_fou_eb716ad6_fk_wagtailim FOREIGN KEY (how_we_help_icon_four_pt_br_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_investhomepage invest_investhomepag_how_we_help_icon_one_1751478c_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_investhomepage
    ADD CONSTRAINT invest_investhomepag_how_we_help_icon_one_1751478c_fk_wagtailim FOREIGN KEY (how_we_help_icon_one_ar_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_investhomepage invest_investhomepag_how_we_help_icon_one_26bdd075_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_investhomepage
    ADD CONSTRAINT invest_investhomepag_how_we_help_icon_one_26bdd075_fk_wagtailim FOREIGN KEY (how_we_help_icon_one_fr_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_investhomepage invest_investhomepag_how_we_help_icon_one_4bd58fed_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_investhomepage
    ADD CONSTRAINT invest_investhomepag_how_we_help_icon_one_4bd58fed_fk_wagtailim FOREIGN KEY (how_we_help_icon_one_ru_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_investhomepage invest_investhomepag_how_we_help_icon_one_8fdb9362_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_investhomepage
    ADD CONSTRAINT invest_investhomepag_how_we_help_icon_one_8fdb9362_fk_wagtailim FOREIGN KEY (how_we_help_icon_one_ja_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_investhomepage invest_investhomepag_how_we_help_icon_one_933d6db7_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_investhomepage
    ADD CONSTRAINT invest_investhomepag_how_we_help_icon_one_933d6db7_fk_wagtailim FOREIGN KEY (how_we_help_icon_one_es_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_investhomepage invest_investhomepag_how_we_help_icon_one_97d549f8_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_investhomepage
    ADD CONSTRAINT invest_investhomepag_how_we_help_icon_one_97d549f8_fk_wagtailim FOREIGN KEY (how_we_help_icon_one_zh_hans_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_investhomepage invest_investhomepag_how_we_help_icon_one_a3afab67_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_investhomepage
    ADD CONSTRAINT invest_investhomepag_how_we_help_icon_one_a3afab67_fk_wagtailim FOREIGN KEY (how_we_help_icon_one_pt_br_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_investhomepage invest_investhomepag_how_we_help_icon_one_aa76d159_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_investhomepage
    ADD CONSTRAINT invest_investhomepag_how_we_help_icon_one_aa76d159_fk_wagtailim FOREIGN KEY (how_we_help_icon_one_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_investhomepage invest_investhomepag_how_we_help_icon_one_b56f7c81_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_investhomepage
    ADD CONSTRAINT invest_investhomepag_how_we_help_icon_one_b56f7c81_fk_wagtailim FOREIGN KEY (how_we_help_icon_one_en_gb_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_investhomepage invest_investhomepag_how_we_help_icon_one_e00c070c_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_investhomepage
    ADD CONSTRAINT invest_investhomepag_how_we_help_icon_one_e00c070c_fk_wagtailim FOREIGN KEY (how_we_help_icon_one_de_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_investhomepage invest_investhomepag_how_we_help_icon_one_fcfe99e1_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_investhomepage
    ADD CONSTRAINT invest_investhomepag_how_we_help_icon_one_fcfe99e1_fk_wagtailim FOREIGN KEY (how_we_help_icon_one_pt_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_investhomepage invest_investhomepag_how_we_help_icon_thr_0bdefab5_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_investhomepage
    ADD CONSTRAINT invest_investhomepag_how_we_help_icon_thr_0bdefab5_fk_wagtailim FOREIGN KEY (how_we_help_icon_three_zh_hans_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_investhomepage invest_investhomepag_how_we_help_icon_thr_22772f5b_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_investhomepage
    ADD CONSTRAINT invest_investhomepag_how_we_help_icon_thr_22772f5b_fk_wagtailim FOREIGN KEY (how_we_help_icon_three_en_gb_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_investhomepage invest_investhomepag_how_we_help_icon_thr_71bb8a0b_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_investhomepage
    ADD CONSTRAINT invest_investhomepag_how_we_help_icon_thr_71bb8a0b_fk_wagtailim FOREIGN KEY (how_we_help_icon_three_ar_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_investhomepage invest_investhomepag_how_we_help_icon_thr_7e9a29db_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_investhomepage
    ADD CONSTRAINT invest_investhomepag_how_we_help_icon_thr_7e9a29db_fk_wagtailim FOREIGN KEY (how_we_help_icon_three_pt_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_investhomepage invest_investhomepag_how_we_help_icon_thr_9e98bdfd_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_investhomepage
    ADD CONSTRAINT invest_investhomepag_how_we_help_icon_thr_9e98bdfd_fk_wagtailim FOREIGN KEY (how_we_help_icon_three_es_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_investhomepage invest_investhomepag_how_we_help_icon_thr_a08f8272_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_investhomepage
    ADD CONSTRAINT invest_investhomepag_how_we_help_icon_thr_a08f8272_fk_wagtailim FOREIGN KEY (how_we_help_icon_three_fr_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_investhomepage invest_investhomepag_how_we_help_icon_thr_b415bb95_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_investhomepage
    ADD CONSTRAINT invest_investhomepag_how_we_help_icon_thr_b415bb95_fk_wagtailim FOREIGN KEY (how_we_help_icon_three_ru_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_investhomepage invest_investhomepag_how_we_help_icon_thr_e0c8e962_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_investhomepage
    ADD CONSTRAINT invest_investhomepag_how_we_help_icon_thr_e0c8e962_fk_wagtailim FOREIGN KEY (how_we_help_icon_three_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_investhomepage invest_investhomepag_how_we_help_icon_thr_e8b61047_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_investhomepage
    ADD CONSTRAINT invest_investhomepag_how_we_help_icon_thr_e8b61047_fk_wagtailim FOREIGN KEY (how_we_help_icon_three_pt_br_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_investhomepage invest_investhomepag_how_we_help_icon_thr_e9e51dbe_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_investhomepage
    ADD CONSTRAINT invest_investhomepag_how_we_help_icon_thr_e9e51dbe_fk_wagtailim FOREIGN KEY (how_we_help_icon_three_de_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_investhomepage invest_investhomepag_how_we_help_icon_thr_ee1b291e_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_investhomepage
    ADD CONSTRAINT invest_investhomepag_how_we_help_icon_thr_ee1b291e_fk_wagtailim FOREIGN KEY (how_we_help_icon_three_ja_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_investhomepage invest_investhomepag_how_we_help_icon_two_129f3373_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_investhomepage
    ADD CONSTRAINT invest_investhomepag_how_we_help_icon_two_129f3373_fk_wagtailim FOREIGN KEY (how_we_help_icon_two_de_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_investhomepage invest_investhomepag_how_we_help_icon_two_1abb4bdd_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_investhomepage
    ADD CONSTRAINT invest_investhomepag_how_we_help_icon_two_1abb4bdd_fk_wagtailim FOREIGN KEY (how_we_help_icon_two_es_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_investhomepage invest_investhomepag_how_we_help_icon_two_3578bda4_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_investhomepage
    ADD CONSTRAINT invest_investhomepag_how_we_help_icon_two_3578bda4_fk_wagtailim FOREIGN KEY (how_we_help_icon_two_pt_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_investhomepage invest_investhomepag_how_we_help_icon_two_4a6e272c_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_investhomepage
    ADD CONSTRAINT invest_investhomepag_how_we_help_icon_two_4a6e272c_fk_wagtailim FOREIGN KEY (how_we_help_icon_two_pt_br_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_investhomepage invest_investhomepag_how_we_help_icon_two_5dfa1ff1_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_investhomepage
    ADD CONSTRAINT invest_investhomepag_how_we_help_icon_two_5dfa1ff1_fk_wagtailim FOREIGN KEY (how_we_help_icon_two_ar_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_investhomepage invest_investhomepag_how_we_help_icon_two_5fd75f90_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_investhomepage
    ADD CONSTRAINT invest_investhomepag_how_we_help_icon_two_5fd75f90_fk_wagtailim FOREIGN KEY (how_we_help_icon_two_ja_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_investhomepage invest_investhomepag_how_we_help_icon_two_96bb49e3_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_investhomepage
    ADD CONSTRAINT invest_investhomepag_how_we_help_icon_two_96bb49e3_fk_wagtailim FOREIGN KEY (how_we_help_icon_two_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_investhomepage invest_investhomepag_how_we_help_icon_two_aa9742a9_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_investhomepage
    ADD CONSTRAINT invest_investhomepag_how_we_help_icon_two_aa9742a9_fk_wagtailim FOREIGN KEY (how_we_help_icon_two_ru_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_investhomepage invest_investhomepag_how_we_help_icon_two_cd7f08a1_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_investhomepage
    ADD CONSTRAINT invest_investhomepag_how_we_help_icon_two_cd7f08a1_fk_wagtailim FOREIGN KEY (how_we_help_icon_two_en_gb_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_investhomepage invest_investhomepag_how_we_help_icon_two_d9b9dbcf_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_investhomepage
    ADD CONSTRAINT invest_investhomepag_how_we_help_icon_two_d9b9dbcf_fk_wagtailim FOREIGN KEY (how_we_help_icon_two_zh_hans_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_investhomepage invest_investhomepag_how_we_help_icon_two_e5fd145e_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_investhomepage
    ADD CONSTRAINT invest_investhomepag_how_we_help_icon_two_e5fd145e_fk_wagtailim FOREIGN KEY (how_we_help_icon_two_fr_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_investhomepage invest_investhomepag_page_ptr_id_de1ae3d7_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_investhomepage
    ADD CONSTRAINT invest_investhomepag_page_ptr_id_de1ae3d7_fk_wagtailco FOREIGN KEY (page_ptr_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_regionlandingpage invest_regionlanding_hero_image_id_1d53b46b_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_regionlandingpage
    ADD CONSTRAINT invest_regionlanding_hero_image_id_1d53b46b_fk_wagtailim FOREIGN KEY (hero_image_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_regionlandingpage invest_regionlanding_page_ptr_id_d6a9186a_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_regionlandingpage
    ADD CONSTRAINT invest_regionlanding_page_ptr_id_d6a9186a_fk_wagtailco FOREIGN KEY (page_ptr_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorlandingpage invest_sectorlanding_hero_image_id_bb7eea33_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorlandingpage
    ADD CONSTRAINT invest_sectorlanding_hero_image_id_bb7eea33_fk_wagtailim FOREIGN KEY (hero_image_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorlandingpage invest_sectorlanding_page_ptr_id_73ed820f_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorlandingpage
    ADD CONSTRAINT invest_sectorlanding_page_ptr_id_73ed820f_fk_wagtailco FOREIGN KEY (page_ptr_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_hero_image_id_8058a47c_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_hero_image_id_8058a47c_fk_wagtailim FOREIGN KEY (hero_image_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_page_ptr_id_32b7192a_fk_wagtailcore_page_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_page_ptr_id_32b7192a_fk_wagtailcore_page_id FOREIGN KEY (page_ptr_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_five__0f17c849_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_five__0f17c849_fk_wagtailim FOREIGN KEY (subsection_map_five_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_five__22b85d21_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_five__22b85d21_fk_wagtailim FOREIGN KEY (subsection_map_five_fr_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_five__275133b7_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_five__275133b7_fk_wagtailim FOREIGN KEY (subsection_map_five_pt_br_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_five__5dd8444c_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_five__5dd8444c_fk_wagtailim FOREIGN KEY (subsection_map_five_ja_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_five__8d54aae9_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_five__8d54aae9_fk_wagtailim FOREIGN KEY (subsection_map_five_es_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_five__a267a7b3_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_five__a267a7b3_fk_wagtailim FOREIGN KEY (subsection_map_five_ru_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_five__aa370701_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_five__aa370701_fk_wagtailim FOREIGN KEY (subsection_map_five_zh_hans_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_five__c06e94ea_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_five__c06e94ea_fk_wagtailim FOREIGN KEY (subsection_map_five_pt_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_five__c8719ff6_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_five__c8719ff6_fk_wagtailim FOREIGN KEY (subsection_map_five_ar_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_five__cd4d7920_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_five__cd4d7920_fk_wagtailim FOREIGN KEY (subsection_map_five_en_gb_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_five__ee403893_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_five__ee403893_fk_wagtailim FOREIGN KEY (subsection_map_five_de_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_four__1b7efee2_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_four__1b7efee2_fk_wagtailim FOREIGN KEY (subsection_map_four_de_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_four__20d67a90_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_four__20d67a90_fk_wagtailim FOREIGN KEY (subsection_map_four_es_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_four__28b40bd3_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_four__28b40bd3_fk_wagtailim FOREIGN KEY (subsection_map_four_ja_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_four__2c08bf7c_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_four__2c08bf7c_fk_wagtailim FOREIGN KEY (subsection_map_four_zh_hans_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_four__407eb5cf_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_four__407eb5cf_fk_wagtailim FOREIGN KEY (subsection_map_four_pt_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_four__4cf298f7_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_four__4cf298f7_fk_wagtailim FOREIGN KEY (subsection_map_four_ar_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_four__54a181ab_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_four__54a181ab_fk_wagtailim FOREIGN KEY (subsection_map_four_en_gb_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_four__5750dcc0_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_four__5750dcc0_fk_wagtailim FOREIGN KEY (subsection_map_four_pt_br_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_four__85eee56b_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_four__85eee56b_fk_wagtailim FOREIGN KEY (subsection_map_four_fr_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_four__b47d357c_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_four__b47d357c_fk_wagtailim FOREIGN KEY (subsection_map_four_ru_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_four__cac76cb0_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_four__cac76cb0_fk_wagtailim FOREIGN KEY (subsection_map_four_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_one_a_eae3734a_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_one_a_eae3734a_fk_wagtailim FOREIGN KEY (subsection_map_one_ar_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_one_d_e8391019_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_one_d_e8391019_fk_wagtailim FOREIGN KEY (subsection_map_one_de_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_one_e_1a4d482b_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_one_e_1a4d482b_fk_wagtailim FOREIGN KEY (subsection_map_one_en_gb_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_one_e_5c5f38e2_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_one_e_5c5f38e2_fk_wagtailim FOREIGN KEY (subsection_map_one_es_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_one_f_0a9c28e4_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_one_f_0a9c28e4_fk_wagtailim FOREIGN KEY (subsection_map_one_fr_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_one_i_9f01edda_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_one_i_9f01edda_fk_wagtailim FOREIGN KEY (subsection_map_one_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_one_j_ff99bbbe_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_one_j_ff99bbbe_fk_wagtailim FOREIGN KEY (subsection_map_one_ja_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_one_p_3704faa0_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_one_p_3704faa0_fk_wagtailim FOREIGN KEY (subsection_map_one_pt_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_one_p_bae51dfd_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_one_p_bae51dfd_fk_wagtailim FOREIGN KEY (subsection_map_one_pt_br_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_one_r_5aa7df5b_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_one_r_5aa7df5b_fk_wagtailim FOREIGN KEY (subsection_map_one_ru_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_one_z_a4839796_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_one_z_a4839796_fk_wagtailim FOREIGN KEY (subsection_map_one_zh_hans_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_seven_2a54736c_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_seven_2a54736c_fk_wagtailim FOREIGN KEY (subsection_map_seven_pt_br_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_seven_410afe44_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_seven_410afe44_fk_wagtailim FOREIGN KEY (subsection_map_seven_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_seven_5024f4b4_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_seven_5024f4b4_fk_wagtailim FOREIGN KEY (subsection_map_seven_pt_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_seven_5a450f7a_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_seven_5a450f7a_fk_wagtailim FOREIGN KEY (subsection_map_seven_ja_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_seven_6127c095_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_seven_6127c095_fk_wagtailim FOREIGN KEY (subsection_map_seven_es_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_seven_6b4ac297_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_seven_6b4ac297_fk_wagtailim FOREIGN KEY (subsection_map_seven_de_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_seven_94308bd5_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_seven_94308bd5_fk_wagtailim FOREIGN KEY (subsection_map_seven_fr_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_seven_a67c2e79_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_seven_a67c2e79_fk_wagtailim FOREIGN KEY (subsection_map_seven_ar_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_seven_bde5e042_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_seven_bde5e042_fk_wagtailim FOREIGN KEY (subsection_map_seven_ru_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_seven_c98901a8_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_seven_c98901a8_fk_wagtailim FOREIGN KEY (subsection_map_seven_en_gb_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_seven_e60edb53_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_seven_e60edb53_fk_wagtailim FOREIGN KEY (subsection_map_seven_zh_hans_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_six_a_44a5395c_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_six_a_44a5395c_fk_wagtailim FOREIGN KEY (subsection_map_six_ar_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_six_d_c9a85dcb_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_six_d_c9a85dcb_fk_wagtailim FOREIGN KEY (subsection_map_six_de_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_six_e_f128b944_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_six_e_f128b944_fk_wagtailim FOREIGN KEY (subsection_map_six_en_gb_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_six_e_f95f752d_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_six_e_f95f752d_fk_wagtailim FOREIGN KEY (subsection_map_six_es_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_six_f_6857bb1c_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_six_f_6857bb1c_fk_wagtailim FOREIGN KEY (subsection_map_six_fr_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_six_i_cb1e3c3c_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_six_i_cb1e3c3c_fk_wagtailim FOREIGN KEY (subsection_map_six_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_six_j_e2bede44_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_six_j_e2bede44_fk_wagtailim FOREIGN KEY (subsection_map_six_ja_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_six_p_382643bc_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_six_p_382643bc_fk_wagtailim FOREIGN KEY (subsection_map_six_pt_br_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_six_p_461ab6e9_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_six_p_461ab6e9_fk_wagtailim FOREIGN KEY (subsection_map_six_pt_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_six_r_8a62efd9_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_six_r_8a62efd9_fk_wagtailim FOREIGN KEY (subsection_map_six_ru_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_six_z_d55394f2_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_six_z_d55394f2_fk_wagtailim FOREIGN KEY (subsection_map_six_zh_hans_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_three_1766976a_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_three_1766976a_fk_wagtailim FOREIGN KEY (subsection_map_three_de_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_three_2d2a2a89_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_three_2d2a2a89_fk_wagtailim FOREIGN KEY (subsection_map_three_es_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_three_310ae712_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_three_310ae712_fk_wagtailim FOREIGN KEY (subsection_map_three_ar_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_three_3276a701_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_three_3276a701_fk_wagtailim FOREIGN KEY (subsection_map_three_pt_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_three_43a24e84_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_three_43a24e84_fk_wagtailim FOREIGN KEY (subsection_map_three_zh_hans_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_three_4a0b8e49_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_three_4a0b8e49_fk_wagtailim FOREIGN KEY (subsection_map_three_ja_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_three_5fbfd4a0_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_three_5fbfd4a0_fk_wagtailim FOREIGN KEY (subsection_map_three_en_gb_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_three_b5ef10e3_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_three_b5ef10e3_fk_wagtailim FOREIGN KEY (subsection_map_three_fr_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_three_c1bc090a_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_three_c1bc090a_fk_wagtailim FOREIGN KEY (subsection_map_three_pt_br_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_three_debe81d6_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_three_debe81d6_fk_wagtailim FOREIGN KEY (subsection_map_three_ru_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_three_f4e53d96_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_three_f4e53d96_fk_wagtailim FOREIGN KEY (subsection_map_three_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_two_a_7fe0594e_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_two_a_7fe0594e_fk_wagtailim FOREIGN KEY (subsection_map_two_ar_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_two_d_1d738784_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_two_d_1d738784_fk_wagtailim FOREIGN KEY (subsection_map_two_de_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_two_e_16d9524e_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_two_e_16d9524e_fk_wagtailim FOREIGN KEY (subsection_map_two_en_gb_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_two_e_b16fbd6e_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_two_e_b16fbd6e_fk_wagtailim FOREIGN KEY (subsection_map_two_es_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_two_f_6e213f2d_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_two_f_6e213f2d_fk_wagtailim FOREIGN KEY (subsection_map_two_fr_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_two_i_26dd7961_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_two_i_26dd7961_fk_wagtailim FOREIGN KEY (subsection_map_two_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_two_j_0cc7f6b9_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_two_j_0cc7f6b9_fk_wagtailim FOREIGN KEY (subsection_map_two_ja_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_two_p_785d41e9_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_two_p_785d41e9_fk_wagtailim FOREIGN KEY (subsection_map_two_pt_br_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_two_p_ddc3e9c4_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_two_p_ddc3e9c4_fk_wagtailim FOREIGN KEY (subsection_map_two_pt_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_two_r_d3c7eaa5_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_two_r_d3c7eaa5_fk_wagtailim FOREIGN KEY (subsection_map_two_ru_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_sectorpage invest_sectorpage_subsection_map_two_z_f3f920d5_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_sectorpage
    ADD CONSTRAINT invest_sectorpage_subsection_map_two_z_f3f920d5_fk_wagtailim FOREIGN KEY (subsection_map_two_zh_hans_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_setupguidelandingpage invest_setupguidelan_page_ptr_id_6728f726_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_setupguidelandingpage
    ADD CONSTRAINT invest_setupguidelan_page_ptr_id_6728f726_fk_wagtailco FOREIGN KEY (page_ptr_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: invest_setupguidepage invest_setupguidepag_page_ptr_id_07b60be6_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.invest_setupguidepage
    ADD CONSTRAINT invest_setupguidepag_page_ptr_id_07b60be6_fk_wagtailco FOREIGN KEY (page_ptr_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: taggit_taggeditem taggit_taggeditem_content_type_id_9957a03c_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.taggit_taggeditem
    ADD CONSTRAINT taggit_taggeditem_content_type_id_9957a03c_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: taggit_taggeditem taggit_taggeditem_tag_id_f4f5b767_fk_taggit_tag_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.taggit_taggeditem
    ADD CONSTRAINT taggit_taggeditem_tag_id_f4f5b767_fk_taggit_tag_id FOREIGN KEY (tag_id) REFERENCES public.taggit_tag(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: wagtailcore_collectionviewrestriction wagtailcore_collecti_collection_id_761908ec_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_collectionviewrestriction
    ADD CONSTRAINT wagtailcore_collecti_collection_id_761908ec_fk_wagtailco FOREIGN KEY (collection_id) REFERENCES public.wagtailcore_collection(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: wagtailcore_collectionviewrestriction_groups wagtailcore_collecti_collectionviewrestri_47320efd_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_collectionviewrestriction_groups
    ADD CONSTRAINT wagtailcore_collecti_collectionviewrestri_47320efd_fk_wagtailco FOREIGN KEY (collectionviewrestriction_id) REFERENCES public.wagtailcore_collectionviewrestriction(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: wagtailcore_collectionviewrestriction_groups wagtailcore_collecti_group_id_1823f2a3_fk_auth_grou; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_collectionviewrestriction_groups
    ADD CONSTRAINT wagtailcore_collecti_group_id_1823f2a3_fk_auth_grou FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: wagtailcore_groupcollectionpermission wagtailcore_groupcol_collection_id_5423575a_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_groupcollectionpermission
    ADD CONSTRAINT wagtailcore_groupcol_collection_id_5423575a_fk_wagtailco FOREIGN KEY (collection_id) REFERENCES public.wagtailcore_collection(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: wagtailcore_groupcollectionpermission wagtailcore_groupcol_group_id_05d61460_fk_auth_grou; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_groupcollectionpermission
    ADD CONSTRAINT wagtailcore_groupcol_group_id_05d61460_fk_auth_grou FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: wagtailcore_groupcollectionpermission wagtailcore_groupcol_permission_id_1b626275_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_groupcollectionpermission
    ADD CONSTRAINT wagtailcore_groupcol_permission_id_1b626275_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: wagtailcore_grouppagepermission wagtailcore_grouppag_group_id_fc07e671_fk_auth_grou; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_grouppagepermission
    ADD CONSTRAINT wagtailcore_grouppag_group_id_fc07e671_fk_auth_grou FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: wagtailcore_grouppagepermission wagtailcore_grouppag_page_id_710b114a_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_grouppagepermission
    ADD CONSTRAINT wagtailcore_grouppag_page_id_710b114a_fk_wagtailco FOREIGN KEY (page_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: wagtailcore_page wagtailcore_page_content_type_id_c28424df_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_page
    ADD CONSTRAINT wagtailcore_page_content_type_id_c28424df_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: wagtailcore_page wagtailcore_page_live_revision_id_930bd822_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_page
    ADD CONSTRAINT wagtailcore_page_live_revision_id_930bd822_fk_wagtailco FOREIGN KEY (live_revision_id) REFERENCES public.wagtailcore_pagerevision(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: wagtailcore_page wagtailcore_page_owner_id_fbf7c332_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_page
    ADD CONSTRAINT wagtailcore_page_owner_id_fbf7c332_fk_auth_user_id FOREIGN KEY (owner_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: wagtailcore_pagerevision wagtailcore_pagerevi_page_id_d421cc1d_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_pagerevision
    ADD CONSTRAINT wagtailcore_pagerevi_page_id_d421cc1d_fk_wagtailco FOREIGN KEY (page_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: wagtailcore_pagerevision wagtailcore_pagerevision_user_id_2409d2f4_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_pagerevision
    ADD CONSTRAINT wagtailcore_pagerevision_user_id_2409d2f4_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: wagtailcore_pageviewrestriction_groups wagtailcore_pageview_group_id_6460f223_fk_auth_grou; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_pageviewrestriction_groups
    ADD CONSTRAINT wagtailcore_pageview_group_id_6460f223_fk_auth_grou FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: wagtailcore_pageviewrestriction wagtailcore_pageview_page_id_15a8bea6_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_pageviewrestriction
    ADD CONSTRAINT wagtailcore_pageview_page_id_15a8bea6_fk_wagtailco FOREIGN KEY (page_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: wagtailcore_pageviewrestriction_groups wagtailcore_pageview_pageviewrestriction__f147a99a_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_pageviewrestriction_groups
    ADD CONSTRAINT wagtailcore_pageview_pageviewrestriction__f147a99a_fk_wagtailco FOREIGN KEY (pageviewrestriction_id) REFERENCES public.wagtailcore_pageviewrestriction(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: wagtailcore_site wagtailcore_site_root_page_id_e02fb95c_fk_wagtailcore_page_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailcore_site
    ADD CONSTRAINT wagtailcore_site_root_page_id_e02fb95c_fk_wagtailcore_page_id FOREIGN KEY (root_page_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: wagtaildocs_document wagtaildocs_document_collection_id_23881625_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtaildocs_document
    ADD CONSTRAINT wagtaildocs_document_collection_id_23881625_fk_wagtailco FOREIGN KEY (collection_id) REFERENCES public.wagtailcore_collection(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: wagtaildocs_document wagtaildocs_document_uploaded_by_user_id_17258b41_fk_auth_user; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtaildocs_document
    ADD CONSTRAINT wagtaildocs_document_uploaded_by_user_id_17258b41_fk_auth_user FOREIGN KEY (uploaded_by_user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: wagtailforms_formsubmission wagtailforms_formsub_page_id_e48e93e7_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailforms_formsubmission
    ADD CONSTRAINT wagtailforms_formsub_page_id_e48e93e7_fk_wagtailco FOREIGN KEY (page_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: wagtailimages_image wagtailimages_image_collection_id_c2f8af7e_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailimages_image
    ADD CONSTRAINT wagtailimages_image_collection_id_c2f8af7e_fk_wagtailco FOREIGN KEY (collection_id) REFERENCES public.wagtailcore_collection(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: wagtailimages_image wagtailimages_image_uploaded_by_user_id_5d73dc75_fk_auth_user; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailimages_image
    ADD CONSTRAINT wagtailimages_image_uploaded_by_user_id_5d73dc75_fk_auth_user FOREIGN KEY (uploaded_by_user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: wagtailimages_rendition wagtailimages_rendit_image_id_3e1fd774_fk_wagtailim; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailimages_rendition
    ADD CONSTRAINT wagtailimages_rendit_image_id_3e1fd774_fk_wagtailim FOREIGN KEY (image_id) REFERENCES public.wagtailimages_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: wagtailmedia_media wagtailmedia_media_collection_id_96a2317d_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailmedia_media
    ADD CONSTRAINT wagtailmedia_media_collection_id_96a2317d_fk_wagtailco FOREIGN KEY (collection_id) REFERENCES public.wagtailcore_collection(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: wagtailmedia_media wagtailmedia_media_uploaded_by_user_id_96e8e61b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailmedia_media
    ADD CONSTRAINT wagtailmedia_media_uploaded_by_user_id_96e8e61b_fk_auth_user_id FOREIGN KEY (uploaded_by_user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: wagtailsearch_editorspick wagtailsearch_editor_page_id_28cbc274_fk_wagtailco; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailsearch_editorspick
    ADD CONSTRAINT wagtailsearch_editor_page_id_28cbc274_fk_wagtailco FOREIGN KEY (page_id) REFERENCES public.wagtailcore_page(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: wagtailsearch_editorspick wagtailsearch_editor_query_id_c6eee4a0_fk_wagtailse; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailsearch_editorspick
    ADD CONSTRAINT wagtailsearch_editor_query_id_c6eee4a0_fk_wagtailse FOREIGN KEY (query_id) REFERENCES public.wagtailsearch_query(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: wagtailsearch_querydailyhits wagtailsearch_queryd_query_id_2185994b_fk_wagtailse; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailsearch_querydailyhits
    ADD CONSTRAINT wagtailsearch_queryd_query_id_2185994b_fk_wagtailse FOREIGN KEY (query_id) REFERENCES public.wagtailsearch_query(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: wagtailusers_userprofile wagtailusers_userprofile_user_id_59c92331_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.wagtailusers_userprofile
    ADD CONSTRAINT wagtailusers_userprofile_user_id_59c92331_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--


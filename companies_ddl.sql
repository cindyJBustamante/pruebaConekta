-- Table: public.companies

-- DROP TABLE public.companies;

CREATE TABLE public.companies
(
    company_id character varying(24) COLLATE pg_catalog."default" NOT NULL,
    company_name character varying(130) COLLATE pg_catalog."default",
    CONSTRAINT pk_companies PRIMARY KEY (company_id)
)

TABLESPACE pg_default;

ALTER TABLE public.companies
    OWNER to postgres;
-- Table: public.charges

-- DROP TABLE public.charges;

CREATE TABLE public.charges
(
    id character varying(24) COLLATE pg_catalog."default" NOT NULL,
    company_id character varying(24) COLLATE pg_catalog."default" NOT NULL,
    amount numeric(16,2) NOT NULL,
    status character varying(30) COLLATE pg_catalog."default" NOT NULL,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone,
    CONSTRAINT pk_charges PRIMARY KEY (id),
    CONSTRAINT fk_charges_companies FOREIGN KEY (company_id)
        REFERENCES public.companies (company_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE public.charges
    OWNER to postgres;


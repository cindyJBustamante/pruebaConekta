-- View: public.dly_trans_vw

-- DROP VIEW public.dly_trans_vw;

CREATE OR REPLACE VIEW public.dly_trans_vw
 AS
 SELECT c1.company_id,
    c2.created_at,
    sum(c2.amount) AS transaccinado
   FROM (companies c1
     JOIN charges c2 ON (((c1.company_id)::text = (c2.company_id)::text)))
  GROUP BY c1.company_id, c2.created_at
  ORDER BY c1.company_id, c2.created_at;

ALTER TABLE public.dly_trans_vw
    OWNER TO postgres;
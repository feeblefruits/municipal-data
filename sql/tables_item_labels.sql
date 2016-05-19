-- drop table bsheet_labels;
-- drop table aged_creditors_labels;
-- drop table aged_debtors_labels;
-- drop table capital_labels;
-- drop table cflow_labels;
-- drop table incexp_labels;
-- drop table repmaint_labels;

CREATE TABLE public.bsheet_items
(
  code text NOT NULL,
  label text,
  position_in_return_form integer,
  return_form_structure text,
  composition text,
  CONSTRAINT bsheet_items_primary_key PRIMARY KEY (code)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.bsheet_items
  OWNER TO municipal_finance;



CREATE TABLE public.aged_creditors_items
(
  code text NOT NULL,
  label text,
  position_in_return_form integer,
  return_form_structure text,
  composition text,
  CONSTRAINT aged_creditors_items_primary_key PRIMARY KEY (code)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.aged_creditors_items
  OWNER TO municipal_finance;



CREATE TABLE public.aged_debtors_items
(
  code text NOT NULL,
  label text,
  position_in_return_form integer,
  return_form_structure text,
  composition text,
  CONSTRAINT aged_debtors_items_primary_key PRIMARY KEY (code)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.aged_debtors_items
  OWNER TO municipal_finance;



CREATE TABLE public.capital_items
(
  code text NOT NULL,
  label text,
  position_in_return_form integer,
  return_form_structure text,
  composition text,
  CONSTRAINT capital_items_primary_key PRIMARY KEY (code)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.capital_items
  OWNER TO municipal_finance;



CREATE TABLE public.cflow_items
(
  code text NOT NULL,
  label text,
  position_in_return_form integer,
  return_form_structure text,
  composition text,
  CONSTRAINT cflow_items_primary_key PRIMARY KEY (code)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.cflow_items
  OWNER TO municipal_finance;


CREATE TABLE public.incexp_items
(
  code text NOT NULL,
  label text,
  position_in_return_form integer,
  return_form_structure text,
  composition text,
  CONSTRAINT incexp_items_primary_key PRIMARY KEY (code)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.incexp_items
  OWNER TO municipal_finance;



CREATE TABLE public.repmaint_items
(
  code text NOT NULL,
  label text,
  position_in_return_form integer,
  return_form_structure text,
  composition text,
  CONSTRAINT repmaint_items_primary_key PRIMARY KEY (code)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.repmaint_items
  OWNER TO municipal_finance;

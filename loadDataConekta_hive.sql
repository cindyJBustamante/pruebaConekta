CREATE TABLE data_prueba_tecnica(
id	 STRING,
name STRING,	
company_id STRING,
amount DECIMAL(18,5),
status STRING,	
created_at DATE,
paid_at DATE)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ","
tblproperties("skip.header.line.count"="1"); 



load data local inpath '/u/users/vn0nv6j/pruebaConekta/data_prueba_tecnica.csv' into table data_prueba_tecnica;
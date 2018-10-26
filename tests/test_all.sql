CREATE OR REPLACE FUNCTION gisbase.test_all()
RETURNS void AS $$
DECLARE
    proc pg_catalog.pg_proc%rowtype;
BEGIN
    for proc in select p.* from 
                pg_catalog.pg_proc p 
                join 
                pg_catalog.pg_namespace n 
                on p.pronamespace = n.oid 
                where 
                nspname = 'gisbase' and
                proname like 'test_%'and
                proname <> 'test_all'
                order by proname
    loop
        execute format('select %s.%s();', test_schema_name, proc.proname);
    end loop;    
end;
$$ LANGUAGE plpgsql;
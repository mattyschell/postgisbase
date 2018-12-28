CREATE OR REPLACE FUNCTION gisbase.escapecharstab (
   p_tablename VARCHAR
) RETURNS VOID AS $$
DECLARE
   refc refcursor;
   dsql varchar(200);
   acol varchar(64);
BEGIN
    dsql = 'select column_name from '
        || 'information_schema.columns '
        || 'where table_name = $1 '
        || 'and table_schema = current_schema() '
        || 'and data_type = ''character varying''';
    OPEN refc FOR EXECUTE dsql USING p_tablename; 
    FETCH NEXT FROM refc INTO acol;
    WHILE FOUND 
    LOOP
        EXECUTE 'UPDATE ' || p_tablename || ' ' 
             || 'SET ' 
             || acol || ' = gisbase.escapechars(' || acol || ')';
        FETCH NEXT FROM refc INTO acol; 
    END LOOP;
    CLOSE refc; 
END;
$$ LANGUAGE plpgsql VOLATILE;

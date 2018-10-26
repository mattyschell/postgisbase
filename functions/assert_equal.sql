CREATE OR REPLACE FUNCTION gisbase.assert_equals(expected anyelement, actual anyelement) 
RETURNS void AS $$
BEGIN
    IF expected = actual OR (expected IS NULL AND actual IS NULL) 
    THEN
            --do nothing
    ELSE
       raise exception 'Assertion Error. Expected <%> but was <%>', expected, actual;
    END IF;
end;
$$ LANGUAGE plpgsql;
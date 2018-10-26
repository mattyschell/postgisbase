CREATE OR REPLACE FUNCTION gisbase.test_dummy()
RETURNS VOID AS $$
BEGIN
    perform gisbase.assert_equals('X', gisbase.dummy());
END;
$$ LANGUAGE plpgsql;
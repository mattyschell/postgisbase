CREATE OR REPLACE FUNCTION gisbase.escapechars (
   chars VARCHAR
) RETURNS VARCHAR AS $$
BEGIN
    -- legacy apps can create a mess when
    -- displaying special chars like e-acute and n-tilde 
    -- may also want to throw in ampersand, <, and > but not doing it yet
    RETURN unaccent('unaccent', chars);
END;
$$ LANGUAGE plpgsql STABLE;
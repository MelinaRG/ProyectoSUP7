CREATE PROCEDURE carga_ta(
    in_nombre VARCHAR(45),
    in_apellido VARCHAR(45),
    in_email VARCHAR(45),
	in_pw INTEGER,
	in_carrera VARCHAR(20),
	in_cohorte INTEGER,
	in_grupo INTEGER)
LANGUAGE plpgsql
AS $$
DECLARE
    ta_existe ta%rowtype;
	sup_existe sup_test%rowtype;
    id_x VARCHAR(20):= '';
	BEGIN
        SELECT id_ta FROM ta
        INTO ta_existe
        WHERE email = in_email;
        IF NOT FOUND THEN
            IF in_carrera = 'fullstack' THEN
                    id_x:= CONCAT('FT-',in_cohorte,'_',in_grupo);
                ELSIF in_carrera = 'data' THEN
                    id_x:= CONCAT('DTS-',in_cohorte,'_',in_grupo);
            END IF;        
			SELECT * FROM sup_test
            INTO sup_existe
            WHERE id_sup = id_x;
            IF NOT FOUND THEN
                INSERT INTO sup_test
                VALUES(id_x,in_grupo,in_cohorte,in_carrera);
            END IF;
            INSERT INTO ta(nombre,apellido,email,pw,id_sup)
            VALUES(in_nombre,in_apellido,in_email,in_pw,id_x);
			RAISE notice'Usuario creado correctamente.';
		ELSE
			RAISE notice'email ya registrado.';
	END IF;
END; $$


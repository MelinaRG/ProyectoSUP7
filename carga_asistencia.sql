CREATE OR REPLACE PROCEDURE carga_asistencia(in_id_alumno INTEGER,in_semana INTEGER,in_modulo INTEGER,in_lunes BOOLEAN,in_martes BOOLEAN,in_miercoles BOOLEAN,in_jueves BOOLEAN)
LANGUAGE plpgsql
AS $$
DECLARE
	idx_asistencia VARCHAR(20):= CONCAT(id_alumno,'__m', in_modulo,'-',in_semana);
	asistencia_existe Asistencia_test%rowtype;
BEGIN
	SELECT id_asistencia FROM Asistencia_test
	INTO asistencia_existe
	WHERE id_asistencia = idx_asistencia;
	IF NOT FOUND THEN
		INSERT INTO Asistencia_test(id_asistencia,id_alumno,lunes,martes,miercoles,jueves,semana,modulo)
		VALUES(idx_asistencia,in_id_alumno,in_lunes,in_martes,in_miercoles,in_jueves,in_semana,in_modulo);
	ELSE
		UPDATE Asistencia_test
		SET lunes = in_lunes, martes = in_martes, miercoles = in_miercoles, jueves = in_jueves
		WHERE id_asistencia = idx_asistencia;
	END IF;
END; $$
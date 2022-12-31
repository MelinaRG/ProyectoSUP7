DROP TABLE IF EXISTS Alumnos;
CREATE TABLE Alumnos (
	IDAlumno				SERIAL PRIMARY KEY,
	Nombre_y_apellido		VARCHAR(50) NOT NULL,
	Carrera					VARCHAR(50) NOT NULL,
	Cohorte					VARCHAR(10) NOT NULL,
	Mail					VARCHAR(70)
);

INSERT INTO Alumnos VALUES(0,'Emmanuel Corral','DS','05','emmanuel.ac@hotmail.com');
INSERT INTO Alumnos VALUES(1,'Melina Griffo','DS','05','meli.griffo@hotmail.com');
INSERT INTO Alumnos VALUES(2,'Federico Olivieri','DS','03','fede.olivieri@hotmail.com');

SELECT * FROM Alumnos;
insert into alumno values(0,'Emmanuel','Corral',35,'mail@mail.com',01,True,True,'Notebook','Argentina','Juegos');
insert into alumno values(1,'Melina','Griffo',28,'mail@mail.com',01,False,True,'Celular','Argentina','Charlar');
insert into alumno values(2,'Ronal','Cabrera',27,'mail@mail.com',01,True,False,'Notebook','Argentina','Juegos');
insert into alumno values(3,'Emmanuel','Fernandez',29,'mail@mail.com',01,False,False,'PC','Uruguay','Código');
insert into alumno values(4,'Luciano','Asencio',31,'mail@mail.com',01,True,False,'PC','Chile','Juegos');
insert into alumno values(5,'Matias','Martínez',26,'mail@mail.com',01,True,True,'Celular','Chile','Charlar');
insert into alumno values(6,'Valentín','Fogliatti',37,'mail@mail.com',01,False,True,'Notebook','Argentina','Juegos');
insert into alumno values(7,'Leonel','Balleis',30,'mail@mail.com',01,False,False,'Celular','Argentina','Charlar');
insert into alumno values(8,'Maciela','Ortiz',31,'mail@mail.com',01,True,False,'PC','Argentina','Código');
insert into alumno values(9,'Julio','Postigo',27,'mail@mail.com',01,False,True,'Celular','Uruguay','Juegos');
insert into alumno values(10,'Matías','Saez',25,'mail@mail.com',01,False,True,'Notebook','Chile','Dudas Henry');
insert into alumno values(11,'Nicolás','Mulet',26,'mail@mail.com',01,True,False,'Celular','Chile','Juegos');

delete from "Alumno";

insert into "Ta" values(01,'Fede','Olivieri','fede.olivieri@lagorra.com','8811225');

insert into "Sup" values(01,07,05,01,null,'Data');

select * from alumno;
select * from sup;
select * from ta;

SELECT ROUND(AVG(edad),0) FROM Alumno;

SELECT nombre,apellido,edad FROM alumno;

SELECT ROUND(AVG(edad),0) FROM alumno;

ALTER TABLE "Alumno" RENAME TO "alumno";
ALTER TABLE "Sup" RENAME TO "sup";
ALTER TABLE "Ta" RENAME TO "ta";

SELECT nombre,apellido,dispositivo,mic_y_cam FROM alumno;

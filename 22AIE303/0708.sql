create table department(Name varchar(20) primary key,
                        building varchar(15),
                        Budget numeric(12,2)); -- 22AIE303/0708.sql
DESC department;
INSERT INTO department VALUES('CSE','Taylor',100);
INSERT INTO department VALUES('Biology','Watson',200);
INSERT INTO department VALUES('Electrical','Taylor',300);
INSERT INTO department VALUES('Music','Packard',400);
INSERT INTO department VALUES('Finance','Painter',500);
INSERT INTO department VALUES('History','Painter',600);
INSERT INTO department VALUES('Physics','Watson',700);
SELECT * FROM department;

delete from department where name = 'Music';
delete from department where Budget between 300 and 500;
update department set Budget = Budget + 100 where Budget<700; 
update department set Budget = 1000 where name ='CSE';
SELECT * FROM department;

ALTER TABLE department ADD classrooms numeric(1);
ALTER TABLE department DROP COLUMN building;
UPDATE department SET classrooms = 7 where name = 'CSE';
UPDATE department SET classrooms = 6 where name = 'Biology';
UPDATE department SET classrooms = 3 where name = 'Electrical';
UPDATE department SET classrooms = 4 where name = 'Music';
UPDATE department SET classrooms = 5 where name = 'Finance';
UPDATE department SET classrooms = 3 where name = 'History';
UPDATE department SET classrooms = 2 where name = 'Physics';
SELECT * FROM department;

drop table department;
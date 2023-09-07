PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE books (
	id INTEGER NOT NULL, 
	name VARCHAR NOT NULL, 
	type VARCHAR NOT NULL, 
	author VARCHAR NOT NULL, 
	borrowed_date DATE, 
	return_date DATE, status VARCHAR(255) DEFAULT "not borrowed", 
	PRIMARY KEY (id)
);
INSERT INTO books VALUES(1,'The Big Bad Wolf','Fiction','James Patterson','2023-09-07','2023-09-21','not borrowed');
INSERT INTO books VALUES(2,'Pride and Prejudice','Romance','Jane Austen','2023-09-07','2023-09-21','borrowed');
INSERT INTO books VALUES(3,'The Shining','Horror','Stephen King','2023-09-07','2023-09-21','borrowed');
INSERT INTO books VALUES(4,'Dracula','Horror','Bram Stoker','2023-09-07','2023-09-21','borrowed');
INSERT INTO books VALUES(5,'Dune','Science Fiction','Frank Herbert','2023-09-07','2023-09-21','borrowed');
INSERT INTO books VALUES(6,'Brave New World','Science Fiction','Aldous Huxley','2023-09-07','2023-09-21','borrowed');
INSERT INTO books VALUES(7,'The Hobbit','Fantasy','J.R.R. Tolkien','2023-09-07','2023-09-21','borrowed');
INSERT INTO books VALUES(8,'A Song of Ice and Fire','Fantasy','George R.R. Martin','2023-09-07','2023-09-21','borrowed');
INSERT INTO books VALUES(9,'The Hound of the Baskervilles','Mystery','Arthur Conan Doyle',NULL,NULL,'not borrowed');
INSERT INTO books VALUES(10,'Murder on the Orient Express','Mystery','Agatha Christie',NULL,NULL,'not borrowed');
INSERT INTO books VALUES(11,'The Book Thief','Historical Fiction','Markus Zusak',NULL,NULL,'not borrowed');
INSERT INTO books VALUES(12,'The Book Thief','Historical Fiction','Markus Zusak','2023-09-07','2023-09-21','not borrowed');
INSERT INTO books VALUES(13,'Dune','Science Fiction','Frank Herbert','2023-09-07','2023-09-21','not borrowed');
INSERT INTO books VALUES(14,'The Catcher in the Rye','Classic Fiction','J.D. Salinger','2023-09-07','2023-09-21','not borrowed');
INSERT INTO books VALUES(15,'A Brief History of Time','Non-fiction','Stephen Hawking',NULL,NULL,'not borrowed');
INSERT INTO books VALUES(16,'American Gods','Fantasy','Neil Gaiman',NULL,NULL,'not borrowed');
CREATE TABLE mentors (
	id INTEGER NOT NULL, 
	f_name VARCHAR NOT NULL, 
	surname VARCHAR NOT NULL, 
	book_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(book_id) REFERENCES books (id)
);
INSERT INTO mentors VALUES(1,'Julius','Wafula',14);
INSERT INTO mentors VALUES(2,'Michael','Omondi',NULL);
INSERT INTO mentors VALUES(3,'Sarah','Achieng',12);
INSERT INTO mentors VALUES(4,'Benjamin','Mutuku',NULL);
INSERT INTO mentors VALUES(5,'Florence','Kemunto',NULL);
INSERT INTO mentors VALUES(6,'Geoffrey','Koech',NULL);
CREATE TABLE students (
	id INTEGER NOT NULL, 
	f_name VARCHAR NOT NULL, 
	l_name VARCHAR NOT NULL, 
	surname VARCHAR NOT NULL, 
	class_ VARCHAR NOT NULL, 
	book_id INTEGER NOT NULL, 
	mentor_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(book_id) REFERENCES books (id), 
	FOREIGN KEY(mentor_id) REFERENCES mentors (id)
);
INSERT INTO students VALUES(1,'Peter','Frank','Smith','6',5,1);
INSERT INTO students VALUES(2,'James','Mwangi','Kamau','1',3,4);
INSERT INTO students VALUES(3,'Ruth','Nyambura','Wairimu','8',2,5);
INSERT INTO students VALUES(4,'Peter','Omondi','Otieno','7',7,6);
INSERT INTO students VALUES(5,'Esther','Akinyi','Adhiambo','6',7,5);
INSERT INTO students VALUES(6,'Joyce','Cherono','Adhiambo','7',8,4);
INSERT INTO students VALUES(7,'Mary','Wanjiru','Njoki','8',2,3);
INSERT INTO students VALUES(8,'John','Kipchoge','Keino','6',3,3);
INSERT INTO students VALUES(9,'Grace','Wambui','Muthoni','7',4,2);
INSERT INTO students VALUES(10,'Daniel','Kiptoo','Rono','8',9,1);
INSERT INTO students VALUES(11,'Samuel','Kamau','Mbugua','7',5,2);
COMMIT;

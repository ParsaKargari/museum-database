DROP DATABASE IF EXISTS MUSEUM_DB;
CREATE DATABASE MUSEUM_DB;
USE MUSEUM_DB;



CREATE TABLE ARTIST
(   ANAME CHAR(50) NOT NULL,
    DateBorn DATE,
    DateDied DATE,
    Country_Origin CHAR(15),
    EPOCH CHAR(15),
    Descriptions CHAR(50),
    Main_Style CHAR(15),

    

CONSTRAINT ARPK PRIMARY KEY (ANAME));



CREATE TABLE OBJECTS
(   Year  INT,
    Descriptions CHAR(100),
    Artist CHAR(50),
    IDno INT    NOT NULL,
    Title CHAR(50),
    Atype CHAR(50),
CONSTRAINT OBPK PRIMARY KEY (IDno),
FOREIGN KEY (Atype) REFERENCES ARTIST(ANAME));



CREATE TABLE COLLECTIONS
(   CNAME CHAR(50)  NOT NULL,
    CAddress CHAR(50),
    CType CHAR(25),
    Descriptions CHAR(50),
    Phone CHAR(20),
    C_Person CHAR(50),
    CONSTRAINT COPK PRIMARY KEY (CNAME));



CREATE TABLE EXHIBITION
(  	ENAME CHAR(50)  NOT NULL,
    Start_D DATE,
    End_D DATE,
    CONSTRAINT EXPK PRIMARY KEY (ENAME));



CREATE TABLE PAINTING
(   IDno INT    NOT NULL,
    Style CHAR(15),
    PType CHAR(15),
    Material CHAR(15),
    CONSTRAINT PAPK PRIMARY KEY (IDno),
    FOREIGN KEY (IDno) REFERENCES OBJECTS(IDno));



CREATE TABLE OTHER
(   IDno INT    NOT NULL,
    Style CHAR(15),
    PType CHAR(15),
    CONSTRAINT OTPK PRIMARY KEY (IDno),
    FOREIGN KEY (IDno) REFERENCES OBJECTS(IDno));



CREATE TABLE SCULPTURE
(   IDno INT    NOT NULL,
    Style CHAR(15),
    Material CHAR(15),
    SWEIGHT INT,
    SHEIGHT INT,
    CONSTRAINT SCPK PRIMARY KEY (IDno),
    FOREIGN KEY (IDno) REFERENCES OBJECTS(IDno));



CREATE TABLE STATUE
(   IDno INT    NOT NULL,
    Style CHAR(15),
    Material CHAR(15),
    SWEIGHT INT,
    SHEIGHT INT,
    CONSTRAINT STPK PRIMARY KEY (IDno),
    FOREIGN KEY (IDno) REFERENCES OBJECTS(IDno));




CREATE TABLE PERMENANT
(   IDno INT   NOT NULL,
    Cost INT,
    PStatus CHAR(15),
    Pdate DATE,
    CONSTRAINT PEPK PRIMARY KEY (IDno),
    FOREIGN KEY (IDno) REFERENCES OBJECTS(IDno));



CREATE TABLE BORROWED
(   IDno INT    NOT NULL,
    Cname CHAR(50),
    Date_B DATE,
    Date_R DATE,
    CONSTRAINT BOPK PRIMARY KEY(IDno),
    FOREIGN KEY (IDno) REFERENCES OBJECTS(IDno),
    FOREIGN KEY (CNAME) REFERENCES COLLECTIONS(CNAME));




CREATE TABLE SHOWS
(   EName CHAR(50)	NOT NULL,
    IDno INT	 NOT NULL,
    CONSTRAINT SHOWPK PRIMARY KEY (IDno, EName),
    FOREIGN KEY (IDno) REFERENCES OBJECTS(IDno),
    FOREIGN KEY (EName) REFERENCES EXHIBITION(Ename));




-- ROLES AND PERMISIONS
DROP ROLE IF EXISTS db_admin@localhost, read_access@localhost;

CREATE ROLE db_admin@localhost, read_access@localhost;

GRANT ALL PRIVILEGES ON MUSEUM_DB.* TO db_admin@localhost;
GRANT SELECT ON MUSEUM_DB.* TO read_access@localhost;

drop user if exists pk@localhost;
drop user if exists guest@localhost;

CREATE USER pk@localhost identified with mysql_native_password by 'password';
CREATE USER guest@localhost;
GRANT db_admin@localhost to pk@localhost;
GRANT read_access@localhost to guest@localhost;

SET DEFAULT ROLE ALL TO pk@localhost;
SET DEFAULT ROLE ALL TO guest@localhost;
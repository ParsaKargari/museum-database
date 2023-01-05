-- Inserting the Objects and Artists --

USE MUSEUM_DB;


INSERT INTO ARTIST
VALUES      ('Marcus Gheeraerts the Younger','1561-01-06','1636-01-19','Belgium','Baroque','Realism Potrait','Still Life'),
            ('Hans Eworth','1520-11-01','1574-11-03','Belgium','Baroque','Allegorical Reflection','Stil Life'),
            ('Hans Holbein the Younger','1497-01-01','1543-01-08','Germany','Renaissance','Preserving History','Potraits'),
            ('Jean Antoine','1699-06-01','1781-05-03','Croatia','Renaissance','Nature and beauty','Landscape'),
			('Sanek','1760-06-01','1859-05-09','London','Bascillica','Pottery','Handcrafting'),
			('Nivon','1769-09-01','186-01-01','Macedonia','Ancient','Pottery','Handcrafting'),
			('Simone Leigh','1996-05-01','2022-05-05','United States','Modern','History','Absract'),
			('Adebunmi','2000-11-01','2022-08-03','United States','Modern','Arborignal','Sculpting'),
			('kant','1770-05-01','1860-05-03','Estonia','Renaissance','Preserving Hisotry','Statues'),
			('Picasso','1889-05-01','1950-09-03','England','Renaissance','Abstract Expressionism','Self Potraits'),
			('various artists','1769-06-01','1874-05-03','Italy','Renaissance','Pottery','Sculpting'),
			('Jamberone','1769-05-01','1851-05-03','France','Renaissance','Preserving Hisotry','Potraits'),
			('romaine','1779-05-06','1883-05-19','France','Renaissance','Abstract','Expressionism'),
			('Jan Van','1669-07-07','1723-06-18','Romania','Abstract','Encaustic','Expressionism'),
			('Passe','1799-11-23','1886-07-03','Slovakia','Renaissance','Pottery','Handcrafting'),
			('Limosin','1589-09-22','1703-01-01','Italy','Ancient','Pottery','Handcrafting'),
			('Micheal Stittow','1448-01-01','1567-09-09','Sweden','Renaissance','Realism Potrait','Still life');


-- Fixing errors in row 6 with double hyphen in data -- 

INSERT INTO OBJECTS
VALUES		(1537,'Potrait of King Henry VIII','Hans Holbein the Younger',123344,'Henry VIII','Hans Holbein the Younger'),
            (1514,'Potrait of Queen of France','Micheal Stittow',123345,'Mary Tudor','Micheal Stittow'),
            (1554,'Potrait of Majesty Mary I','Hans Eworth',123346,'Mary I','Hans Eworth'),
            (1597,'Potrait of Ellen Maurice','Marcus Gheeraerts the Younger',123347,'Ellen Maurice','Marcus Gheeraerts the Younger'),
			(1700,'Water Landscape','Jean Antoine',9935,'La Chute','Jean Antoine'),
			(1850,'Mug with faces','Sanek',124401,'Untitled','Sanek'),
			(1854,'Mug with faces 2','Nivon',124402,'Untitled','Nivon'),
			(2021,'Large Jug','Simone Leigh',124403,'Large Jug','Simone Leigh'),
			(2021,'A memorabilia','Adebunmi',124404,'K.S.','Adebunmi'),
			(1850,'A metallic figurine','kant',125501,'Vili','kant'),
			(1914,'An abstract figure','Picasso',125505,'The Absinthe Glass','Picasso'),
			(1850,'An artefact','various artists',125502,'Circular mug','various artists'),
			(1850,'A metallic figurine','Jamberone',125503,'White fragment','Jamberone'),
			(1800,'Tablet of wood','romaine',9931,'Tableau','romaine'),
			(1700,'A fabric','Jan Van',9932,'Shroud','Jan Van'),
			(1810,'A broken tablet','Passe',9933,'Tablet','Passe'),
			(1690,'Painted plate','Limosin',9934,'Renaissance Plate','Limosin');

INSERT INTO EXHIBITION
VALUES		('The Tudors','2022-10-10','2023-01-08'),
            ('Hear Me Now: The Black Potters of Old Edgefield','2022-09-09','2023-02-05'),
            ('Cubism and the Trompe l’Oeil Tradition','2022-10-20','2023-01-22'),
			('Louvre Themed Collection','2021-08-20','2023-01-16');


-- All the types of Artists work


INSERT INTO PAINTING
VALUES		(123344,'Realism','Oil','Canvas'),
            (123345,'Allegorical','Oil','Paper'),
			(123346,'Realism','Encaustic','Wood'),
			(123347,'Realism','Encaustic','Canvas'),
			(9935,'Landscape','Oil','Paper');
			
			
			
INSERT INTO SCULPTURE
VALUES		(124401,'Full Round','Stone',18,389),
            (124402,'Full Round','Composite',23,255),
			(124403,'Carved','Wood',15,109),
			(124404,'Carved','Wood',11,190);
			
			
INSERT INTO STATUE
VALUES 		(125501,'Cast','Bronze',24,600),
            (125502,'Carved','Stone',17,290),
			(125503,'Carved','Stone',15,311);
			
			
			
INSERT INTO OTHER
VALUES 		(9931,'Tablet','Baroque'),
            (9932,'Painted Fabric','Abstract'),
			(9934,'Plate','Renaissance'),
			(9933,'Tablet','Abstract');


INSERT INTO PERMENANT
VALUES 		(123344,1500000,'on loan','2022-10-10'),
            (123345,1900000,'on loan','2022-11-09'),
			(123346,2300000,'on display','2022-10-10'),
			(123347,1898000,'on loan','2022-10-10'),
			(124401,49000,'stored','2022-09-09'),
            (124402,19000,'on display','2022-09-09'),
			(124403,29000,'on loan','2022-09-21'),
			(124404,29000,'on loan','2022-09-17'),
			(125501,190000,'on loan','2022-09-09'),
			(125502,190000,'on display','2022-09-09'),
			(125503,190000,'on loan','2022-10-20');




INSERT INTO COLLECTIONS
VALUES 		('Departement des Objets...','18 Sussex Blvd, France','Museum','Private Museum','789-777-123','Kaleb Antoine'),
            ('Departement des Antiquites...','2258 Wellignton Street, The avenue, Italy','Museum','Private Museum collection','989-456-333','Luka Modric'),
			('Service de lHistoire','19 Fargo, Slovakia','Private Collector','Collection of artefact organization','111-697-696','Sir Jacob III'),
            ('Departement des Peintures','Louvre Museum, Rue de Rivoli, 75001 Paris, France','Museum','Federal Museum','189-189-001','John Van Parsa');
			
INSERT INTO BORROWED 
VALUES		(9931,'Departement des Antiquites...','2020-02-12','2020-02-29'),
			(9932,'Service de lHistoire','2020-03-10','2020-07-14'),
			(9933,'Departement des Objets...','2020-05-14','2021-05-14'),
			(9934,'Departement des Objets...','2020-09-28','2020-10-14');




INSERT INTO SHOWS
VALUES		('The Tudors',123344),
			('The Tudors',123345),
			('The Tudors',123346),
			('The Tudors',123347);


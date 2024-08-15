CREATE TABLE Worker (
    Worker_ID BIGINT PRIMARY KEY,
    Surname VARCHAR(30),
	Name varchar(30),
    position VARCHAR(30)
);

CREATE TABLE Purchase (
    Purchase_ID INT PRIMARY KEY,
    price DECIMAL(10, 2),
    date DATE,
    sellerPhoneNumber VARCHAR(20)
);

CREATE TABLE Who_supervise (
    Worker_ID BIGINT,
    Purchase_ID INT,
    PRIMARY KEY (Worker_ID, Purchase_ID),
    FOREIGN KEY (Worker_ID) REFERENCES Worker(Worker_ID),
    FOREIGN KEY (Purchase_ID) REFERENCES Purchase(Purchase_ID)
);

CREATE TABLE Renovation (
    Renovation_ID INT PRIMARY KEY,
    startDate DATE,
    endDate DATE,
    price DECIMAL(10, 2),
    deadline DATE,
    Worker_ID BIGINT,
    FOREIGN KEY (Worker_ID) REFERENCES Worker(Worker_ID)
);

CREATE TABLE RenovationTeam (
    Renovation_ID INT,
    contructionManager VARCHAR(30),
    companyName VARCHAR(30),
    NIP VARCHAR(20),
    PRIMARY KEY (Renovation_ID),
    FOREIGN KEY (Renovation_ID) REFERENCES Renovation(Renovation_ID)
);
CREATE TABLE Location (
    Location_ID INT PRIMARY KEY,
    City VARCHAR(30),
    District VARCHAR(30),
    ResidentialArea VARCHAR(30),
);

CREATE TABLE RealEstate (
    estate_ID INT PRIMARY KEY,
    area INT,
    numberOfFloors INT,
    whichFloor INT,
    typeOfProperty VARCHAR(30),
    developer VARCHAR(30),
    productionYear VARCHAR(30),
    street VARCHAR(30),
    flatNumber INT,
	Location_ID INT,
    FOREIGN KEY (Location_ID) REFERENCES Location(Location_ID),
    Renovation_ID INT,
    FOREIGN KEY (Renovation_ID) REFERENCES Renovation(Renovation_ID)
);




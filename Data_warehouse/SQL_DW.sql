
CREATE TABLE DimRenovationTeam (
    RenovationTeamID INT PRIMARY KEY IDENTITY(1,1),
	RT_ID INT not null,
    NIP varchar(20) UNIQUE NOT NULL,
    companyName VARCHAR(30) NOT NULL,
    constructionManager VARCHAR(30) NOT NULL,
    companyEmail VARCHAR(70) NOT NULL,
    Specializations VARCHAR(30) NOT NULL,
    establishYearRange VARCHAR(30) NOT NULL,
    workersRange VARCHAR(30) NOT NULL,
    licensesAndCertifications VARCHAR(70) NOT NULL,
    licensesRange VARCHAR(30) NOT NULL,
    finishedRenovationRange VARCHAR(30) NOT NULL,
	CONSTRAINT chk_establishYearRange CHECK ( establishYearRange in (' between 1900-1950', ' between 1951-1980',' between 1981-2000', ' between 2001-2024')),
	CONSTRAINT chk_Specializations CHECK (Specializations IN (' Interior Design', ' Painting', ' Flooring', ' Electrical', ' Renovation', ' Plumbing', ' Carpentry', ' Landscaping', ' HVAC', ' Masonry')),
	CONSTRAINT chk_workersRange CHECK (workersRange IN (' between 1-5', ' between 6-15',' between 16-50',' between 50-200', ' over 200')),
	CONSTRAINT chk_licenses CHECK (licensesRange IN (' between 0-5', ' between 6-15',' between 16-50',' over 50')),
    CONSTRAINT chk_finished CHECK (finishedRenovationRange IN(' between 0-5', ' between 6-20', ' between 21-100', ' between 101-500', ' more than 500')),
	CONSTRAINT chk_licensesAndCertifications CHECK( licensesAndCertifications IN (' LEED Certification', ' PMP Certification', ' OSHA 30-Hour Certification', ' EPA Lead-Safe Certification', ' First Aid Certification', ' Six Sigma Certification', ' AWS Certified Solutions Architect', ' CompTIA Security+', ' Certified ScrumMaster', ' Cisco Certified Network Associate'))

);



CREATE TABLE DimRealEstate (
    estate_ID INT PRIMARY KEY IDENTITY(1,1),
	RE_ID INT not null,
    street VARCHAR(30) NOT NULL,
    typeOfProperty VARCHAR(30) NOT NULL,
    developer VARCHAR(30) NOT NULL,
    productionYearRange VARCHAR(30) NOT NULL, 
	CONSTRAINT chk_type CHECK ( Typeofproperty IN ( ' flat', ' apartment', ' house', ' twin')),
	CONSTRAINT chk_production CHECK ( productionYearRange IN (' between 1900-1950',' between 1951-1980',' between 1981-2000',' between 2001-2010',' between 2011-2020',' between 2021-2024'))
);

CREATE TABLE DimLocation (
    Location_ID INT PRIMARY KEY IDENTITY(1,1),
	L_ID INT not null,
    City VARCHAR(30) NOT NULL,
    District VARCHAR(30) NOT NULL,
    ResidentialArea VARCHAR(30) NOT NULL
);

CREATE TABLE DimWorker (
	Worker_ID INT Primary key IDENTITY(1,1),
	W_ID INT not null, 
    Pesel BIGINT UNIQUE NOT NULL,
    name VARCHAR(30) NOT NULL,
    surname VARCHAR(30) NOT NULL,
    isCurrent varchar(5) NOT NULL,
    position VARCHAR(30) NOT NULL,
	CONSTRAINT chk_isCurrent CHECK (isCurrent IN ('yes', 'no')),
	CONSTRAINT chk_position CHECK (position IN ('researcher', 'analyst', 'CEO', 'supervisor'))
);


CREATE TABLE DimDate (
    dateID INT PRIMARY KEY IDENTITY(1,1),
    Date DATE UNIQUE,
    Year VARCHAR(4),
    Month VARCHAR(10),
    season VARCHAR(30),
    monthNo TINYINT,
    seasonNo TINYINT,
	CONSTRAINT chk_Month CHECK ([Month] IN ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')),
    CONSTRAINT chk_season CHECK ([season] in ('Winter', 'Spring', 'Summer', 'Autumn'))
);


CREATE TABLE DimJunk (
    JunkID INT PRIMARY KEY IDENTITY(1,1),
	J_ID INT not null,
    reasonforDelay VARCHAR(30) NOT NULL,
	CONSTRAINT chk_reason CHECK( reasonforDelay IN(' No delay', ' Material shortages', ' Unexpected structural issues' , ' Weather-related setbacks', ' Changes in project scope', ' Labor shortages', ' Budgetary constraints'))
);

CREATE TABLE DimRenovation (
	Area INT NOT NULL,
    renovationPrice NUMERIC NOT NULL,
    Delay NUMERIC,
    NumberOfRenovatedRooms NUMERIC NOT NULL,
    RenovationTeamID INT FOREIGN KEY REFERENCES DimRenovationTeam,
    estateID INT FOREIGN KEY REFERENCES DimRealEstate,
    startDateID INT FOREIGN KEY REFERENCES DimDate,
    endDateID INT FOREIGN KEY REFERENCES DimDate,
    deadlineID INT FOREIGN KEY REFERENCES DimDate,
    JunkID INT FOREIGN KEY REFERENCES DimJunk,
    LocationID INT FOREIGN KEY REFERENCES DimLocation,
    workerID INT FOREIGN KEY REFERENCES DimWorker,

	Constraint composite_renovation Primary key(
	RenovationTeamID,
	estateID,
	startDateID,
	endDateID,
	deadlineID,
	junkID,
	LocationID,
	workerID
	)
);





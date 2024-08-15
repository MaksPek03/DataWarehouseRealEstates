USE DW
GO

If (object_id('dbo.RealEstate') is not null) DROP TABLE dbo.RealEstate;
CREATE TABLE dbo.RealEstate(estate_ID INT, street varchar(30), area INT, typeOfProperty varchar(30),  productionYearRange varchar(30), flatNumber int, developer varchar(30), numberOfFloors INT, 
whichFloor INT, Location_ID int, Renovation_ID int);
go
BULK INSERT dbo.RealEstate
    FROM 'C:\Users\maksp\OneDrive\Pulpit\semestr IV\warehouse\etl\DataWarehousesGeneratorDW\first_real_estates.txt'
    WITH
    (
    FIRSTROW = 1,
    FIELDTERMINATOR = ',',  
    ROWTERMINATOR = '\n',   
    TABLOCK
    )

CREATE VIEW vETLDimRealEstate
AS
SELECT DISTINCT
	estate_ID,
	street, 
	area,
	typeOfProperty,
	productionYearRange,
	flatNumber,
	developer,
	numberOfFloors,
	whichFloor,
	Location_ID,
	Renovation_ID
FROM dbo.RealEstate;
go

MERGE INTO dbo.DimRealEstate AS TT
	USING vETLDimRealEstate AS ST
		ON TT.RE_ID = ST.estate_ID
			WHEN Not Matched
				THEN
					INSERT
					Values (
					ST.estate_ID,
					ST.street,
					ST.typeOfProperty,
					ST.developer,
					ST.productionYearRange)
			WHEN Not Matched By Source
				Then
					DELETE
			;

DROP VIEW vETLDimRealEstate



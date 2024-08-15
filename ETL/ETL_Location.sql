USE DW
GO

If (object_id('dbo.Location') is not null) DROP TABLE dbo.Location;
CREATE TABLE dbo.Location(Location_ID INT, City varchar(30), District varchar(30), ResidentialArea varchar(30));
go

BULK INSERT dbo.Location
    FROM 'C:\Users\maksp\OneDrive\Pulpit\semestr IV\warehouse\etl\DataWarehousesGeneratorDW\first_locations.txt'
    WITH
    (
    FIRSTROW = 1,
    FIELDTERMINATOR = ',',  
    ROWTERMINATOR = '\n',   
    TABLOCK
    )
go
CREATE VIEW vETLDimLocation
AS
SELECT DISTINCT
	[Location_ID],
	[City],
	[District],
	[ResidentialArea]
FROM dbo.Location;
go



MERGE INTO dbo.DimLocation AS TT
	USING vETLDimLocation AS ST
		ON TT.L_ID = ST.Location_ID
			WHEN NOT Matched
				THEN
					INSERT
					Values (
					ST.Location_ID,
					ST.City,
					ST.District,
					ST.ResidentialArea)
			WHEN NOT Matched By Source
				Then
					DELETE
			;


DROP VIEW vETLDimLocation



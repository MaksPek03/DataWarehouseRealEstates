USE DW
go

If (object_id('dbo.JunkTemp') is not null) DROP TABLE dbo.JunkTemp;
CREATE TABLE dbo.JunkTemp(Renovation_ID INT, RenovationTeamID varchar(30), Delay numeric, renovationPrice numeric, SupervisorName varchar(30), DelayReason varchar(30), DelayID INT, NumberOfRenovatedRooms numeric);
go

BULK INSERT dbo.JunkTemp
    FROM 'C:\Users\maksp\OneDrive\Pulpit\semestr IV\warehouse\etl\DataWarehousesGeneratorDW\renovation_info.csv'
    WITH
    (
    FIRSTROW = 1,
    FIELDTERMINATOR = ',',  
    ROWTERMINATOR = '\n',   
    TABLOCK
    )

If (object_id('vETLDimJunk') is not null) Drop View vETLDimJunk;
go
CREATE VIEW vETLDimJunk
AS
SELECT DISTINCT
	Renovation_ID,
	RenovationTeamID,
	Delay,
	renovationPrice,
	SupervisorName,
	DelayReason,
	DelayID, 
	NumberOfRenovatedRooms
FROM dbo.JunkTemp;
go

MERGE INTO dbo.DimJunk AS TT
	USING vETLDimJunk AS ST
		ON TT.J_ID = ST.DelayID
			WHEN Not Matched
				THEN
					INSERT
					Values (
					ST.DelayID,
					ST.DelayReason
					)
			WHEN Not Matched By Source
				Then
					DELETE;
Drop view vETLDimJunk;

Drop view vETLDimJunk;


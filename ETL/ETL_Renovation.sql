use DW;
go

If (object_id('dbo.RenovationTemp') is not null) DROP TABLE dbo.RenovationTemo;
CREATE TABLE dbo.RenovationTemp(Renovation_ID INT, RenovationTeamID varchar(30), Delay numeric, renovationPrice numeric, SupervisorName varchar(30), DelayReason varchar(30), DelayID INT, NumberOfRenovatedRooms numeric);
go

BULK INSERT dbo.RenovationTemp
	FROM 'C:\Users\maksp\OneDrive\Pulpit\semestr IV\warehouse\etl\DataWarehousesGeneratorDW\renovation_info.csv'
    WITH
    (
    FIRSTROW = 1,
    FIELDTERMINATOR = ',',  
    ROWTERMINATOR = '\n',   
    TABLOCK
    )
CREATE VIEW vETLFRenovation
AS
SELECT 
	Area,
	RenovationPrice,
	Delay,
	NumberOfRenovatedRooms,
	RenovationTeamID,
	estate_ID,
	startDateID,
	endDateID,
	deadlineID,
	JunkID,
	LocationID,
	WorkerID
FROM
	(SELECT 
		  Area = dbo.RealEstate.area,
		  RenovationPrice = ST1.price,
		  Delay = dbo.RenovationTemp.Delay,
		  NumberOfRenovatedRooms = RenovationTemp.NumberOfRenovatedRooms,
		  RenovationTeamID = ST3.Renovation_ID,
		  estate_ID = ST4.estate_ID,
		  startDateID = SD.dateID,
		  endDateID = ED.dateID,
		  deadlineID = DD.dateID,
		  JunkID = dbo.RenovationTemp.DelayID,
		  LocationID = ST2.LocationID,
		  WorkerID = ST5.Worker_ID
					
	FROM DB.dbo.Renovation AS ST1
	JOIN DB.dbo.Location AS ST2 ON ST1.LocationID = ST2.LocationID
	JOIN DB.dbo.RenovationTeam AS ST3 ON ST1.RenovationTeamID = ST3.RenovationTeamID
	JOIN DB.dbo.RealEstate AS ST4 ON ST1.estate_ID = ST4.estate_ID
	JOIN DB.dbo.Worker AS ST5 ON ST1.WorkerID = ST5.WorkerID
	JOIN dbo.DimDate as SD ON CONVERT(VARCHAR(10), SD.Date, 111) = CONVERT(VARCHAR(10), ST1.startDate, 111)
	JOIN dbo.DimDate as ED ON CONVERT(VARCHAR(10), ED.Date, 111) = CONVERT(VARCHAR(10), ST1.endDate, 111)
	JOIN dbo.DimDate as DD ON CONVERT(VARCHAR(10), DD.Date, 111) = CONVERT(VARCHAR(10), ST1.deadline, 111)
	) AS Subquery;
	

MERGE INTO dbo.DimRenovation as TT
	USING vETLFRenovation as ST
		ON 	
		TT.estateID = ST.estate_ID
			WHEN Not Matched
				THEN
					INSERT Values (
						  ST.Area,
						  ST.RenovationPrice,
						  ST.Delay,
						  ST.NumberOfRenovatedRooms,
						  ST.RenovationTeamID,
						  ST.estate_ID,
						  ST.startDateID,
						  ST.endDateID,
						  ST.deadlineID
						  ST.JunkID,
						  ST.LocationID,
						  ST.WorkerID,
					)
			;

Drop view vETLFRenovation;

-- select * from FBookSales;
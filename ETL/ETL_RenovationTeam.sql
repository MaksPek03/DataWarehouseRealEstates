use DW;
go

If (object_id('dbo.RenovationTemp') is not null) DROP TABLE dbo.RenovationTemp;
CREATE TABLE dbo.RenovationTemp(Renovation_ID INT, RenovationTeamID varchar(30), Delay numeric, renovationPrice numeric, SupervisorName varchar(30), DelayReason varchar(30), DelayID INT, NumberOfRenovatedRooms numeric);
go

BULK INSERT dbo.RenovationTemp
    FROM 'C:\Users\maksp\OneDrive\Pulpit\semestr IV\warehouse\etl\DataWarehousesGeneratorDW\renovation_team.csv'
    WITH
    (
    FIRSTROW = 1,
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    TABLOCK
    )
go

If (object_id('vETLFRenovation') is not null) Drop View vETLFRenovation;
go
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
          Area = ST3.area,
          RenovationPrice = ST1.price,
          Delay = ST7.Delay,
          NumberOfRenovatedRooms = ST7.NumberOfRenovatedRooms,
          RenovationTeamID = ST2.Renovation_ID,
          estate_ID = ST3.estate_ID,
          startDateID = SD.dateID,
          endDateID = ED.dateID,
          deadlineID = DD.dateID,
          JunkID = ST7.DelayID,
          LocationID = ST4.Location_ID,
          WorkerID = ST5.Worker_ID

    FROM DB.dbo.Renovation AS ST1
    JOIN DB.dbo.RenovationTeam AS ST2 ON ST1.RenovationTeam = ST2.Renovation_ID
    JOIN DB.dbo.RealEstate AS ST3 ON ST1.RealEstate = ST3.estate_ID
    JOIN DB.dbo.Location AS ST4 ON ST3.Location_ID = ST4.Location_ID
    JOIN DB.dbo.Worker AS ST5 ON ST1.Worker_ID = ST5.Worker_ID
    JOIN DW.dbo.RenovationTemp AS ST7 on ST1.Renovation_ID = ST7.Renovation_ID
    JOIN dbo.DimDate as SD ON CONVERT(VARCHAR(10), SD.Date, 111) = CONVERT(VARCHAR(10), ST1.startDate, 111)
    JOIN dbo.DimDate as ED ON CONVERT(VARCHAR(10), ED.Date, 111) = CONVERT(VARCHAR(10), ST1.endDate, 111)
    JOIN dbo.DimDate as DD ON CONVERT(VARCHAR(10), DD.Date, 111) = CONVERT(VARCHAR(10), ST1.deadline, 111)
    ) AS Subquery;




go


MERGE INTO dbo.FRenovation as TT
    USING vETLFRenovation as ST
        ON
        TT.estateID = ST.estate_ID AND
        TT.startDateID = ST.startDateID AND
        TT.endDateID = ST.endDateID AND
        TT.RenovationTeamID = ST.RenovationTeamID AND
        TT.LocationID = ST.LocationID AND
        TT.workerID = ST.WorkerID AND
        TT.deadlineID = ST.deadlineID AND
        TT.JunkID = ST.JunkID
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
                          ST.deadlineID,
                          ST.JunkID,
                          ST.LocationID,
                          ST.WorkerID
                    )
            ;

SELECT * FROM FRenovation
-- select * from FBookSales;
DROP VIEW vETLFRenovation;
select * from vETLFRenovation;
select * from dbo.FRenovation
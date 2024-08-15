USE DW
GO

If (object_id('dbo.Worker') is not null) DROP TABLE dbo.Worker;
CREATE TABLE dbo.Worker(Worker_ID INT, Pesel BIGINT, name varchar(30), surname varchar(30), position varchar(30) );
go

BULK INSERT dbo.Worker
    FROM 'C:\Users\maksp\OneDrive\Pulpit\semestr IV\warehouse\etl\DataWarehousesGeneratorDW\first_workers.txt'
    WITH
    (
    FIRSTROW = 1,
    FIELDTERMINATOR = ',',  
    ROWTERMINATOR = '\n',   
    TABLOCK
    )
go

CREATE VIEW vETLDimWorker
AS
SELECT DISTINCT
	Worker_ID,
	Pesel,
	name,
	surname,
	position
FROM dbo.Worker;
go


MERGE INTO DimWorker AS TT
	USING vETLDimWorker AS ST
		ON TT.W_ID = ST.Worker_ID
			WHEN Not Matched
				THEN
					INSERT
					Values (
					ST.Worker_ID,
					ST.Pesel,
					ST.name,
					ST.surname,
					ST.position
					)
			WHEN Not Matched By Source
				Then
					DELETE
			;

DROP VIEW vETLDimWorker

If (object_id('vETLDimWorker') is not null) Drop View vETLDimWorker;
go
CREATE VIEW vETLDimWorker
AS
SELECT DISTINCT
    Worker_ID,
    Pesel,
    name,
    surname,
    position
FROM DB.dbo.Worker;
go

MERGE INTO DimWorker AS TT
    USING vETLDimWorker AS ST
        ON TT.Pesel = ST.Pesel
            WHEN Not Matched
                THEN
                    INSERT
                    Values (
                    ST.Worker_ID,
                    ST.Pesel,
                    ST.name,
                    ST.surname,
                    1,
                    ST.position
                    )
            WHEN Matched
                AND TT.position <> ST.position
                    THEN
                        UPDATE
                            SET TT.IsCurrent = 0
            WHEN Not Matched By Source
                Then
                    DELETE
            ;



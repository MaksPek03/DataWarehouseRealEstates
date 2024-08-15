USE DW;
GO

DECLARE @StartDate DATE; 
DECLARE @EndDate DATE;

SELECT @StartDate = '2000-01-01', @EndDate = '2024-04-30';

DECLARE @DateInProcess DATETIME = @StartDate;

WHILE @DateInProcess <= @EndDate
BEGIN

    INSERT INTO DimDate
        ( 
            [Date], 
            [Year],
            [Month], 
            [monthNo],
            [season],  -- Season name
            [seasonNo] -- Season number
        )
    VALUES ( 
            @DateInProcess, 
            CAST(YEAR(@DateInProcess) AS VARCHAR(4)), 
            CAST(DATENAME(MONTH, @DateInProcess) AS VARCHAR(10)), 
            CAST(MONTH(@DateInProcess) AS INT),
            CASE 
                WHEN MONTH(@DateInProcess) IN (12, 1, 2) THEN 'Winter'
                WHEN MONTH(@DateInProcess) IN (3, 4, 5) THEN 'Spring'
                WHEN MONTH(@DateInProcess) IN (6, 7, 8) THEN 'Summer'
                WHEN MONTH(@DateInProcess) IN (9, 10, 11) THEN 'Autumn'
            END,
            CASE 
                WHEN MONTH(@DateInProcess) IN (12, 1, 2) THEN 1
                WHEN MONTH(@DateInProcess) IN (3, 4, 5) THEN 2
                WHEN MONTH(@DateInProcess) IN (6, 7, 8) THEN 3
                WHEN MONTH(@DateInProcess) IN (9, 10, 11) THEN 4
            END
        );  

    SET @DateInProcess = DATEADD(DAY, 1, @DateInProcess);
END;
GO
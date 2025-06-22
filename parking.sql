-- Create the database if it doesn't exist
IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = 'ParkingSystem')
BEGIN
    CREATE DATABASE ParkingSystem;
    PRINT 'Database Created';
END
ELSE
BEGIN
    PRINT 'Database Already Exists';
END
GO

-- Switch to the ParkingSystem database
USE ParkingSystem;
GO

-- Create the parking_records table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'parking_records')
BEGIN
    CREATE TABLE parking_records (
        plate_number VARCHAR(20) NOT NULL,
        entry_time FLOAT,
        exit_time FLOAT,
        duration FLOAT,
        payment FLOAT,
        PRIMARY KEY (plate_number, entry_time)
    );
    PRINT 'Parking Records Table Created';
END
ELSE
BEGIN
    PRINT 'Parking Records Table Already Exists';
END
GO

-- Create the sensor_data table with 6 fixed sensors
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'sensor_data')
BEGIN
    CREATE TABLE sensor_data (
        sensor_name VARCHAR(20) PRIMARY KEY,
        distance FLOAT,
        status VARCHAR(10),
        timestamp FLOAT
    );
    PRINT 'Sensor Data Table Created';
    
    -- Insert 6 sensor rows if they don't exist
    INSERT INTO sensor_data (sensor_name, distance, status, timestamp)
    VALUES 
        ('parking_sensor_1', 0.0, 'Free', 0),
        ('parking_sensor_2', 0.0, 'Free', 0),
        ('parking_sensor_3', 0.0, 'Free', 0),
        ('parking_sensor_4', 0.0, 'Free', 0),
        ('parking_sensor_5', 0.0, 'Free', 0),
        ('parking_sensor_6', 0.0, 'Free', 0);
    PRINT 'Sensor Data Initialized';
END
ELSE
BEGIN
    PRINT 'Sensor Data Table Already Exists';
END
GO

DROP TABLE IF EXISTS `META_BILLS`;

CREATE TABLE `META_BILLS` {
    `BILL_ID` VARCHAR(100) PRIMARY KEY,
    `TITLE` VARCHAR(500) DEFAULT NULL,
    `CONGRESS_SESSION` INT DEFAULT 0,
    `INTRODUCED_DATE` INT DEFAULT 0,
    `ACTIVE` BOOLEAN DEFAULT FALSE
};

DROP TABLE IF EXISTS `BILLS_CACHE`

CREATE TABLE `BILLS_CACHE`{
    `BILL_ID` VARCHAR(100) PRIMARY KEY,
    `SPONSER` VARCHAR(50) DEFAULT NULL,
    `STATE` VARCHAR(5) DEFAULT NULL,
    `PARTY` VARCHAR(1) DEFAULT NULL,
    `ENACTED` BOOLEAN DEFAULT FALSE,
    `VETOED` BOOLEAN DEFAULT FALSE,
    `SUMMARY` VARCHAR(500) DEFAULT NULL,
    `LATEST_MAJOR_ACTION` VARCHAR(500) DEFAULT NULL
};
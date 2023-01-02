CREATE USER 'admin_GenServices'@'localhost' IDENTIFIED BY 'admin@password@GenServices';
DROP DATABASE IF EXISTS GenServices;
CREATE DATABASE GenServices;
GRANT ALL PRIVILEGES ON GenServices.* TO 'admin_GenServices'@'localhost';
FLUSH PRIVILEGES;


USE GenServices;
CREATE TABLE login_details(
    username VARCHAR(50),
    password VARCHAR(100),
    email_or_fcbk VARCHAR(100),
    phone_number VARCHAR(10),
    PRIMARY KEY(username)
);

CREATE TABLE net_banking(
    username VARCHAR(50),
    cost INT,
    account_number INT,
    CIF_number INT,
    branch_code INT,
    flat_number INT,
    PRIMARY KEY(username)
);

CREATE TABLE upi(
    username VARCHAR(50),
    cost INT,
    UPI_ID INT,
    flat_number INT,
    PRIMARY KEY(username)
);

CREATE TABLE paytm(
    username VARCHAR(50),
    cost INT,
    paytm_ID INT,
    flat_number INT,
    PRIMARY KEY(username)
);

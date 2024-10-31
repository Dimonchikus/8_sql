USE testdb;

-- Create a table for users with a date of birth column
CREATE TABLE users (
                       id BIGINT PRIMARY KEY AUTO_INCREMENT,
                       name VARCHAR(255),
                       email VARCHAR(255),
                       date_of_birth DATE
) ENGINE=InnoDB;
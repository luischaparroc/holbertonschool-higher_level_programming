-- Script that creates an user in MySQL server
-- Query to create the user 'user_0d_1' in MySQL server
CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON * . * TO 'user_0d_1'@'localhost';

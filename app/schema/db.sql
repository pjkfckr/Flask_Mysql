CREATE DATABASE test_db DEFAULT CHARACTER SET UTF8;

use test_db;

CREATE TABLE testTable(
    idx INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    test VARCHAR(200) NOT NULL
) CHARSET=utf8;
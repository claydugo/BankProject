use narayanFall2020group3;
drop table IF EXISTS loan;
drop table IF EXISTS customer;
drop table IF EXISTS account;
drop table IF EXISTS employee;
drop table IF EXISTS branch;
CREATE TABLE employee (emp_id INT NOT NULL,
                      emp_name VARCHAR(30),
                      emp_city VARCHAR(20),
                      pho_num INT NOT NULL,
                      PRIMARY KEY(emp_id)) ENGINE=INNODB;
CREATE TABLE account (acc_id INT NOT NULL,
                      balance INT NOT NULL,
                      acc_type VARCHAR(10),
                      PRIMARY KEY (acc_id)) ENGINE=INNODB;
CREATE TABLE customer (cust_id INT NOT NULL,
                      cust_name VARCHAR(20),
                      cust_city VARCHAR(20),
                      acc_id INT NOT NULL,
                      PRIMARY KEY (cust_id),
                      FOREIGN KEY (acc_id) REFERENCES account(acc_id))  ENGINE=INNODB;
CREATE TABLE branch (branch_name VARCHAR(20),
                      branch_city VARCHAR(20),
                      PRIMARY KEY (branch_name)) ENGINE=INNODB;
CREATE TABLE loan (loan_id INT NOT NULL,
                      loan_amt INT NOT NULL,
                      loan_rate INT NOT NULL,
                      monthly INT NOT NULL,
                      loan_length INT NOT NULL,
                      acc_id INT NOT NULL,
                      PRIMARY KEY (loan_id),
                      FOREIGN KEY (acc_id) REFERENCES account(acc_id))  ENGINE=INNODB;
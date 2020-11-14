select avg(balance) from account;

 select avg(balance) from account where acc_type = 'User' and balance < 100000;


create view balancesheet as select cust_name, balance from account a, customer c where a.acc_id = c.acc_id;


# for open account function
select max(acc_id) from account where acc_type = 'User'

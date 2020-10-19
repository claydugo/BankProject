SET FOREIGN_KEY_CHECKS=0;
insert into account values(1337 , 100000, 'Admin');
insert into account values(1 , 0, 'test');
insert into account values(123 , 100, 'User');

insert into customer values(3, 'John Doe', 'Wilmington', 123);
insert into customer values(1, 'Admin User', 'Nowhere', 1337);

insert into employee values(1201 , 'Joel Barish', 'Montauk', '7045558896');
insert into employee values(1202 , 'Clementime Kruczynski', 'Montauk', '7045557432');
insert into employee values(1203 , 'Louis Bloom', 'Los Angeles', '3015550201');
insert into employee values(1204 , 'Nina Romina', 'Los Angeles', '3015553381');
insert into employee values(1205 , 'Wilson Joel', 'Covington', '9855555492');

insert into branch values('Alpha', 'Wilmington');
insert into branch values('Bravo', 'Covington');
insert into branch values('Charlie', 'Los Angeles');

insert into loan values(101, 150000, 10, 1000, 30, 123);
insert into loan values(102, 1000000, 25, 10000, 15, 1337);
SET FOREIGN_KEY_CHECKS=1;

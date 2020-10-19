SET FOREIGN_KEY_CHECKS=0;
insert into account values(1337, 100000, 'Admin');
insert into account values(201, 30212, 'User');
insert into account values(202, 4002, 'User');
insert into account values(204, 875, 'User');
insert into account values(205, 320, 'User');
insert into account values(206, 7832, 'User');
insert into account values(207, 60, 'User');
insert into account values(208, 621435, 'User');
insert into account values(209, 2217, 'User');

insert into customer values(301, 'Truman Burbank', 'Montauk', 201);
insert into customer values(302, 'Hannah Burbank', 'Montauk', 202);
insert into customer values(303, 'Cherita Chen', 'Los Angeles', 203);
insert into customer values(304, 'Jim Cunningham', 'Los Angeles', 204);
insert into customer values(305, 'Nathan Young', 'Los Angeles', 205);
insert into customer values(306, 'Curtis Donovan', 'Los Angeles', 206);
insert into customer values(307, 'Lawrence Gordon', 'Covington', 207);
insert into customer values(308, 'Amy Dunne', 'Covington', 208);
insert into customer values(309, 'Annie Wilkes', 'Covington', 209);

insert into employee values(1201 , 'Joel Barish', 'Montauk', '7045558896');
insert into employee values(1202 , 'Clementime Kruczynski', 'Montauk', '7045557432');
insert into employee values(1203 , 'Louis Bloom', 'Los Angeles', '3015550201');
insert into employee values(1204 , 'Nina Romina', 'Los Angeles', '3015553381');
insert into employee values(1205 , 'Wilson Joel', 'Covington', '9855555492');

insert into branch values('Alpha', 'Wilmington');
insert into branch values('Bravo', 'Covington');
insert into branch values('Charlie', 'Los Angeles');

insert into loan values(101, 150000, 10, 1000, 30, 201);
insert into loan values(102, 10000, 12, 833, 1, 202);
insert into loan values(103, 3000, 40, 250, 30, 203);
insert into loan values(104, 1000000, 5, 50000, 2, 208);
SET FOREIGN_KEY_CHECKS=1;

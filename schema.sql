create database subscription_tracker;

use subscription_tracker;

create table subscriptions (
id int auto_increment primary key,
name varchar(100) not null,
category varchar(50),
cost decimal(5, 2) not null,
billing_cycle enum("Monthly", "Yearly") not null,
start_date date not null,
next_renewal date not null,
status enum("Active", "Cancelled") default "Active"
);
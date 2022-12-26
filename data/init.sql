SET NAMES 'utf8mb4';
SET CHARACTER SET utf8mb4;

drop table if exists `city`;

drop table if exists `county`;

drop table if exists `country`;

DROP TABLE IF EXISTS `places`;

DROP TABLE IF EXISTS `raw_places`;

DROP TABLE IF EXISTS `people`;

DROP TABLE IF EXISTS `raw_people`;

drop table if exists `examples`;

CREATE TABLE `city`
(
   
`Name` nvarchar(500) not null,
`createdate` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
primary key (`Name`)
);

CREATE TABLE `county`
(
 
`Name` nvarchar(500) not null,
`createdate` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
primary key (`Name`)
);


CREATE TABLE  `country`
(
 
`Name` nvarchar(500) not null,
`createdate` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
primary key (`Name`)
);


CREATE TABLE  `raw_places`
(
`id` int not null auto_increment,
`city` nvarchar(500) not null,
`county` nvarchar(500) not null,
`country`nvarchar(500) not null,
`createdate` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
primary key (`id`)
);

CREATE TABLE  `places`
(
`id` int not null auto_increment,
`city` nvarchar(500)  null,
`county` nvarchar(500)  null,
`country` nvarchar(500)  null,
`createdate` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
primary key (`id`),
FOREIGN KEY (`city`) REFERENCES city(`Name`),
FOREIGN KEY (`county`) REFERENCES county(`Name`),
FOREIGN KEY (`country`) REFERENCES country(`Name`)
);

CREATE TABLE  `people`
(
`id` int not null auto_increment,
`given_name` nvarchar(500) default null,
`family_name` nvarchar(500) default null,
`date_of_birth` nvarchar(500) default null,
`place_of_birth` nvarchar(500) default null,
`createdate` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
primary key (`id`)

);


create table `examples` (
  `id` int not null auto_increment,
  `name` nvarchar(80) default null,
  `createdate` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  primary key (`id`)
);


CREATE INDEX `index_places_city` ON `places` (`city`);

CREATE INDEX `index_people_place_of_birth` ON `people` (`place_of_birth`);


 
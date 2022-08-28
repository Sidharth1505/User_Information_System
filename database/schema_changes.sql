CREATE DATABASE  IF NOT EXISTS user_info_system ;
USE user_info_system;

CREATE TABLE  IF NOT EXISTS profession(
  `id` int NOT NULL AUTO_INCREMENT,
  `profession_name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ;

CREATE TABLE  IF NOT EXISTS role(
  `id` int NOT NULL AUTO_INCREMENT,
  `role_name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;



CREATE TABLE IF NOT EXISTS user(
  `id` int NOT NULL AUTO_INCREMENT,
  `user_name` varchar(45) NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `date_of_birth` date DEFAULT NULL,
  `contact_no` varchar(45) DEFAULT NULL,
  `address` varchar(300) DEFAULT NULL,
  `password` varchar(300) DEFAULT NULL,
  `gender` varchar(45) DEFAULT NULL,
  `is_approved` tinyint DEFAULT NULL,
  `timestamp` datetime DEFAULT NULL, 
  `modified_by` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;



CREATE TABLE  IF NOT EXISTS user_profession_map(
  `user_id` int NOT NULL ,
  `profession_id` int NOT NULL,
  KEY `profession_id_idx` (`profession_id`),
  CONSTRAINT `profession_id` FOREIGN KEY (`profession_id`) REFERENCES `profession` (`id`),
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;



CREATE TABLE IF NOT EXISTS user_role_map(
  `userid` int NOT NULL ,
  `roleid` int NOT NULL,
  PRIMARY KEY (`userid`),
  KEY `roleid_idx` (`roleid`),
  CONSTRAINT `roleid` FOREIGN KEY (`roleid`) REFERENCES `role` (`id`),
  CONSTRAINT `userid` FOREIGN KEY (`userid`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;



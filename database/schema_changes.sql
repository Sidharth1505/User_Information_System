CREATE DATABASE  IF NOT EXISTS tmp ;
USE tmp;

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
  `name` varchar(45) DEFAULT NULL,
  `date_of_birth` datetime DEFAULT NULL,
  `contact_no` varchar(45) DEFAULT NULL,
  `address` varchar(45) DEFAULT NULL,
  `password` varchar(45) DEFAULT NULL,
  `gender` varchar(45) DEFAULT NULL,
  `is_approved` tinyint DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;



CREATE TABLE  IF NOT EXISTS user_profession_map(
  `user_id` int NOT NULL AUTO_INCREMENT,
  `profession_id` int NOT NULL,
  PRIMARY KEY (`user_id`),
  KEY `profession_id_idx` (`profession_id`),
  CONSTRAINT `profession_id` FOREIGN KEY (`profession_id`) REFERENCES `profession` (`id`),
  CONSTRAINT `user_id` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;



CREATE TABLE IF NOT EXISTS user_role_map(
  `userid` int NOT NULL AUTO_INCREMENT,
  `roleid` int NOT NULL,
  PRIMARY KEY (`userid`),
  KEY `roleid_idx` (`roleid`),
  CONSTRAINT `roleid` FOREIGN KEY (`roleid`) REFERENCES `role` (`id`),
  CONSTRAINT `userid` FOREIGN KEY (`userid`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;



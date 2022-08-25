INSERT INTO user_info_system.user Values(101,'Sidharth Jain', 15/05/2001, 9729066397,'Jagadhri','password','Male',1);

INSERT INTO user_info_system.role Values(101, 'admin');
INSERT INTO user_info_system.role(role_name) values('user');

ALTER TABLE `user_info_system`.`user` 
CHANGE COLUMN `date_of_birth` `date_of_birth` DATE NULL DEFAULT NULL ;
INSERT INTO user_info_system.user_role_map values(1001,102);
INSERT INTO user_info_system.profession values(1, 'businessman');
INSERT INTO user_info_system.profession(profession_name) values('singer');
INSERT INTO user_info_system.profession(profession_name) values('poet');
INSERT INTO user_info_system.profession(profession_name) values('teacher');
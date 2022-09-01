DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `getUserNames`()
BEGIN
	SELECT user_name from user_info_system.user;
END$$
DELIMITER ;


DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `checkApproval`(IN username varchar(45))
BEGIN
	SELECT is_approved FROM user_info_system.user where user_name = username;
END$$
DELIMITER ;

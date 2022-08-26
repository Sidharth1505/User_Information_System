queries = {

    'insert_user' : "INSERT INTO user_info_system.user values({},'{}','{}','{}','{}','{}','{}','{}',{},sysdate(),'{}')",
    'insert_user_map' : 'INSERT INTO user_info_system.user_role_map values({},{})', 
    'check_password' : "SELECT password from user_info_system.user where user_name = '{}'",
    'is_user' : "select role_name from user_info_system.user_role_map t JOIN user_info_system.user u ON u.id = t.userid JOIN user_info_system.role r ON r.id = t.roleid  where user_name = '{}'",
    'if_exists' : "SELECT COUNT(name) from user_info_system.user where name = '{}'",
    'get_id_counter': "SELECT COUNT(id) from user_info_system.user",
    'is_allowed' : "SELECT is_approved FROM user_info_system.user where user_name = '{}'",
    'unapproved' : "SELECT user_name,name FROM user_info_system.user where is_approved =0",
    'approve': "UPDATE user_info_system.user SET is_approved = 1, modified_by = '{}' WHERE user_name = '{}'",
    'insert_profession_map' : ["INSERT INTO user_info_system.user_profession_map(user_id,profession_id) values({},{}),({},{})", "INSERT INTO user_info_system.user_profession_map values({},{})"],
    'display_all_details' :"select user_id,user_name,name,year(sysdate())-year(date_of_birth) as age,address,gender,is_approved,modified_by,profession_name,role_name from user_info_system.user_profession_map t JOIN user_info_system.user u ON u.id = t.user_id JOIN user_info_system.profession r ON r.id = t.profession_id JOIN user_info_system.user_role_map m ON m.userid = t.user_id JOIN user_info_system.role l ON l.id = m.roleid ",
    'display_specific_user' : "select user_id,user_name,name,year(sysdate())-year(date_of_birth) as age,address,gender,is_approved,modified_by,profession_name,role_name from user_info_system.user_profession_map t JOIN user_info_system.user u ON u.id = t.user_id JOIN user_info_system.profession r ON r.id = t.profession_id JOIN user_info_system.user_role_map m ON m.userid = t.user_id JOIN user_info_system.role l ON l.id = m.roleid where user_name ='{}'",
    'fetch_username': "select user_name from user_info_system.user",
    'display_filter' : "select user_id,user_name,name,year(sysdate())-year(date_of_birth)as age ,address,gender,is_approved,modified_by,profession_name,role_name from user_info_system.user_profession_map t JOIN user_info_system.user u ON u.id = t.user_id JOIN user_info_system.profession r ON r.id = t.profession_id JOIN user_info_system.user_role_map m ON m.userid = t.user_id JOIN user_info_system.role l ON l.id = m.roleid where {} = '{}'",
    'display_all_username': 'select user_name from user_info_system.user',
    'delete_user': "DELETE FROM user_info_system.user where user_name = '{}'",
    'edit_user' : "UPDATE schema.user SET {} ='{}', modified_by = '{}' where user_name = '{}'",
    'display_my_details' : "select user_name, name,year(sysdate())-year(date_of_birth) as age , contact_no, address, gender from user_info_system.user where user_name = '{}'",
    'display_other' : "select name, contact_no,address from user_info_system.user"
}
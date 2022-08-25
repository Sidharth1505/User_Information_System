queries = {

    'insert_user' : "INSERT INTO user_info_system.user values({},'{}','{}','{}','{}','{}','{}','{}',{},sysdate(),'{}')",
    'insert_user_map' : 'INSERT INTO user_info_system.user_role_map values({},{})', 
    'check_password' : "SELECT password from user_info_system.user where user_name = '{}'",
    'is_user' : "select role_name from user_info_system.user_role_map t JOIN user_info_system.user u ON u.id = t.userid JOIN user_info_system.role r ON r.id = t.roleid  where user_name = '{}'",
    'if_exists' : "SELECT COUNT(name) from user_info_system.user where name = '{}'",
    'get_id_counter': "SELECT COUNT(id) from user_info_system.user",
    'is_allowed' : "SELECT is_approved FROM user_info_system.user where user_name = '{}'",
    'unapproved' : "SELECT user_name,name FROM user_info_system.user where is_approved =0",
    'approve': "UPDATE user_info_system.user SET is_approved = 1, modified_by = '{}' WHERE user_name = '{}'"
}
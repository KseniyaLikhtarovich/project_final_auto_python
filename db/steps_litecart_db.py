def changes_in_db(cursor, test_case_1_data):
    cursor.execute("SELECT `firstname`, `lastname` FROM `lc_customers` "
                   "WHERE id=2")
    result = cursor.fetchall()
    assert test_case_1_data["input"]["name"] in result[0][0]

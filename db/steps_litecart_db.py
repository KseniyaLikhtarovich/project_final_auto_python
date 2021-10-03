def changes_in_db(cursor, tc_1_data):
    cursor.execute("SELECT `firstname`, `lastname` FROM `lc_customers` "
                   "WHERE id=2")
    result = cursor.fetchall()
    print(result)
    assert tc_1_data["input"]["name"] in result[0][0]

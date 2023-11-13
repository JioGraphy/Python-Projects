# # import mysql.connector


# try: 
        
#     # Establish a connection
#         connection = mysql.connector.connect(
#         host="your_host",
#         user="your_username",
#         password="your_password",
#         database="your_database"
#     )
        
# except ConnectionError as err:
#       print('Connection Error timed out', err)

# # Create a cursor
# cursor = connection.cursor()

# # Execute a SQL query
# cursor.execute("SELECT * FROM your_table")

# # Fetch and print the results
# result = cursor.fetchall()
# for row in result:
#     print(row)

# # Close the cursor and the connection
# cursor.close()
# connection.close()

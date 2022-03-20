from Data.database_handler import DatabaseHandler

database_handler = DatabaseHandler("database.db")

cmd = input("izupass>")

if(cmd == "addpass"):
    website = input("website: ")
    email = input("email: ")
    username = input("username: ")
    password = input("password: ")

    database_handler.add_account(website, email, username, password)
if(cmd == "delpass"):
    website = input("website: ")
    
    database_handler.del_account(website)
if(cmd == "listpass"):
    website = input("website: ")

    database_handler.list_account(website)
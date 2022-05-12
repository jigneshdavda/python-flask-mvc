from app import mysql

class AuthModel():
    def __init__(self):
        try:
            self.conn = mysql.connection.cursor()
            print('Database Connected')
        except:
            print('Database connection problem')
    
    def user_login(self):
        userResults = [{"id":"1"},{"id":"2"}]
        return userResults
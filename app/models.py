from flask_login import UserMixin
from .sql_service2 import Connection

class UserData:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class UserModel(UserMixin):
    def __init__(self,user_data):
        """
        :param user_data: USerData
        """
        self.id = user_data.username
        self.password = user_data.password
    
    @staticmethod
    def query(user_id):
        user_doc = Connection.get_userc(connection=Connection.connection,user_id=user_id)
        user_data = UserData(
            username=((user_doc[0])['user_name']),
            password=((user_doc[0])['password'])
        )

        return UserModel(user_data)
# repositories/repository.py

class Repository:
    def __init__(self):
        self.users = {}


    def save(self, user_id, user_data):
        self.users[user_id] = user_data
        return user_data

    def delete(self, user_id):
        return self.users.pop(user_id, None)

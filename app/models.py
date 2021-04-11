import pyrebase
from config import dbConfig
class database:
  def __init__(self):
    print("config")
    self.firebase = pyrebase.initialize_app(dbConfig) 
    self._auth = self.auth
    self._db = self.db
  def auth(self):
    return self.firebase.auth()
  def db(self):
    return self.firebase.database()  




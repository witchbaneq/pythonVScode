class Database:
    __instanse = None

    def __new__(cls, *args, **kwargs):
        if cls.__instanse is None:
            cls.__instanse = super().__new__(cls)
        return cls.__instanse
    
    def __del__(self):
        Database.__instanse = None

    def __init__(self, user, psw, port):
        if not hasattr(self, "_initialized"):
            self.user = user
            self.psw = psw
            self.port = port
            self._initialized = True

    def connect(self):
        print(f"соединение с БД {self.user} {self.psw} {self.port}")

    def close(self):
        print("соединение с БД закрыто")

    def read(self):
        return "данные из БД"
    
    def write(self, data):
        print(f"запись в БД: {data}")

        
db = Database("root", "1234", 80)
db = Database("root", "1234", 81)
db2 = Database("root", "1234", 82)

db.connect()
db2.connect()

print(db is db2)  # True, все ссылки на один объект

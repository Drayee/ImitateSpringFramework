@get_controller("/login")
def login():
     LoginService()

@Service
class LoginService:
    def login(self):
        print("登录")

@Method()
def logino(service_title: str):
    print(service_title)
    print("登录")

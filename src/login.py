from framework import Service, auto_inject, controller


@controller("/login")
def login():
    print("登录")

@Service
class LoginService:
    @auto_inject()
    def main(self):
        print(123)

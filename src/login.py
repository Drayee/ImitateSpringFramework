import peewee


@Mapper(table_name="users")
class User:
    id = peewee.AutoField()
    username = peewee.CharField(unique=True)
    password = peewee.CharField()
    email = peewee.CharField(null=True)
    created_at = peewee.DateTimeField(constraints=[peewee.SQL('DEFAULT CURRENT_TIMESTAMP')])


@Service
class UserService:
    
    @auto_inject()
    def __init__(self, service_title: str):
        import framework.library as library
        print("UserService 初始化")
        print(f"服务标题: {service_title}")
        # 从 library.dependencies 中获取 User 模型
        if "model" in library.dependencies and "Mapper_User" in library.dependencies["model"]:
            self.User = library.dependencies["model"]["Mapper_User"]
        elif "Mapper" in library.dependencies and "User" in library.dependencies["Mapper"]:
            self.User = library.dependencies["Mapper"]["User"]
        else:
            raise ValueError("User 模型未找到")
    
    def add_user(self, username, password, email=None):
        """添加用户 - 类似 MyBatis Plus 的 save"""
        user = self.User.create(
            username=username,
            password=password,
            email=email
        )
        print(f"添加用户成功: {username}")
        return user
    
    def list_all_users(self):
        """查询所有用户"""
        return list(self.User.select())
    
    def count_users(self):
        """统计用户数量 - 类似 MyBatis Plus 的 count"""
        return self.User.select().count()


@Method()
def test_mybatis_plus(service_title: str):
    """测试 MyBatis Plus 功能"""
    print("\n=== MyBatis Plus 功能测试 ===")
    print(f"服务标题: {service_title}")
    
    # 获取 UserService
    import framework.library as library
    user_service = library.resource_dependencies["UserService"]
    
    # 测试 1: 添加用户
    print("\n--- 测试 1: 添加用户 ---")
    user1 = user_service.add_user("admin", "123456", "admin@example.com")
    user2 = user_service.add_user("user1", "password1", "user1@example.com")
    user3 = user_service.add_user("user2", "password2")
    
    # 测试 2: 查询所有用户
    print("\n--- 测试 2: 查询所有用户 ---")
    all_users = user_service.list_all_users()
    print(f"共有 {len(all_users)} 个用户:")
    for user in all_users:
        print(f"  - {getattr(user, 'username', 'N/A')} ({getattr(user, 'email', 'N/A')})")
    
    # 测试 3: 统计用户数量
    print("\n--- 测试 3: 统计用户数量 ---")
    user_count = user_service.count_users()
    print(f"当前用户总数: {user_count}")
    
    print("\n=== MyBatis Plus 功能测试完成 ===")

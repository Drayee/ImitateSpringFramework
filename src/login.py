from peewee import *
from framework.public_modules import Service, auto_inject, Method


@Mapper(table_name="users")
class User:
    id = AutoField()
    username = CharField(unique=True)
    password = CharField()
    email = CharField(null=True)
    created_at = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')])


@Service
class UserService:
    
    @auto_inject()
    def __init__(self, service_title: str):
        print("UserService 初始化")
        print(f"服务标题: {service_title}")
        self.User = Mapper_User
    
    def add_user(self, username, password, email=None):
        """添加用户 - 类似 MyBatis Plus 的 save"""
        user = self.User.create(
            username=username,
            password=password,
            email=email
        )
        print(f"添加用户成功: {username}")
        return user
    
    def get_user_by_id(self, user_id):
        """根据 ID 查询用户 - 类似 MyBatis Plus 的 getById"""
        try:
            return self.User.get(self.User.id == user_id)
        except self.User.DoesNotExist:
            return None
    
    def get_user_by_username(self, username):
        """根据用户名查询用户 - 使用 QueryWrapper"""
        return query_wrapper(self.User).eq("username", username).one()
    
    def list_all_users(self):
        """查询所有用户"""
        return list(self.User.select())
    
    def update_user(self, user_id, **kwargs):
        """更新用户 - 类似 MyBatis Plus 的 updateById"""
        query = self.User.update(**kwargs).where(self.User.id == user_id)
        return query.execute()
    
    def delete_user(self, user_id):
        """删除用户 - 类似 MyBatis Plus 的 removeById"""
        query = self.User.delete().where(self.User.id == user_id)
        return query.execute()
    
    def search_users(self, keyword):
        """模糊查询用户 - 使用 QueryWrapper 的 like"""
        return query_wrapper(self.User).like("username", keyword).list()
    
    def count_users(self):
        """统计用户数量 - 类似 MyBatis Plus 的 count"""
        return self.User.select().count()


@Method()
def test_mybatis_plus(service_title: str):
    """测试 MyBatis Plus 功能"""
    print("\n=== MyBatis Plus 功能测试 ===")
    print(f"服务标题: {service_title}")
    
    # 获取 UserService
    user_service = library.resource_dependencies["UserService"]
    
    # 测试 1: 添加用户
    print("\n--- 测试 1: 添加用户 ---")
    user1 = user_service.add_user("admin", "123456", "admin@example.com")
    user2 = user_service.add_user("user1", "password1", "user1@example.com")
    user3 = user_service.add_user("user2", "password2")
    
    # 测试 2: 查询单个用户
    print("\n--- 测试 2: 查询单个用户 ---")
    found_user = user_service.get_user_by_id(user1.id)
    if found_user:
        print(f"找到用户: {found_user.username}")
    
    # 测试 3: 使用 QueryWrapper 查询
    print("\n--- 测试 3: QueryWrapper 查询 ---")
    user_by_name = user_service.get_user_by_username("admin")
    if user_by_name:
        print(f"通过用户名查询到: {user_by_name.username}")
    
    # 测试 4: 查询所有用户
    print("\n--- 测试 4: 查询所有用户 ---")
    all_users = user_service.list_all_users()
    print(f"共有 {len(all_users)} 个用户:")
    for user in all_users:
        print(f"  - {user.username} ({user.email})")
    
    # 测试 5: 模糊查询
    print("\n--- 测试 5: 模糊查询 ---")
    search_results = user_service.search_users("user")
    print(f"模糊搜索 'user' 找到 {len(search_results)} 个用户")
    
    # 测试 6: 更新用户
    print("\n--- 测试 6: 更新用户 ---")
    update_count = user_service.update_user(user2.id, email="new_email@example.com")
    print(f"更新了 {update_count} 条记录")
    updated_user = user_service.get_user_by_id(user2.id)
    print(f"更新后的邮箱: {updated_user.email}")
    
    # 测试 7: 统计用户数量
    print("\n--- 测试 7: 统计用户数量 ---")
    user_count = user_service.count_users()
    print(f"当前用户总数: {user_count}")
    
    # 测试 8: 删除用户
    print("\n--- 测试 8: 删除用户 ---")
    delete_count = user_service.delete_user(user3.id)
    print(f"删除了 {delete_count} 条记录")
    user_count = user_service.count_users()
    print(f"删除后用户总数: {user_count}")
    
    print("\n=== MyBatis Plus 功能测试完成 ===")

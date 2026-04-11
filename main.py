from framework import run
import framework.library as library

# 运行框架
print("=== 启动 Python Spring Framework ===")
run.run()

print("\n=== 框架启动完成，开始测试 ===")

# 测试 MyBatis Plus 功能
try:
    # 先打印 library.dependencies 的内容，以便调试
    print("\n--- 调试信息 ---")
    print("library.dependencies 键:", list(library.dependencies.keys()))
    if "Service" in library.dependencies:
        print("library.dependencies['Service'] 键:", list(library.dependencies["Service"].keys()))
    if "Method" in library.dependencies:
        print("library.dependencies['Method'] 键:", list(library.dependencies["Method"].keys()))
    print("library.resource_dependencies 键:", list(library.resource_dependencies.keys()))

    # 自己构建 UserService
    if "Service" in library.dependencies and "UserService" in library.dependencies["Service"]:
        print("\n--- 正在构建 UserService ---")
        user_service = library.dependencies["Service"]["UserService"].build()
        library.resource_dependencies["UserService"] = user_service
        print("UserService 构建成功并添加到 library.resource_dependencies")

    # 调用测试方法
    test_func = library.dependencies["Method"]["test_mybatis_plus"]
    test_func()
except Exception as e:
    print(f"测试过程中发生错误: {e}")
    import traceback
    traceback.print_exc()

print("\n=== 所有测试完成 ===")

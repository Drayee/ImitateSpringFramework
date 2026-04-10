from framework import run

# 运行框架
print("=== 启动 Python Spring Framework ===")
run.run()

print("\n=== 框架启动完成，开始测试 ===")

# 测试 MyBatis Plus 功能
try:
    # 调用测试方法
    Methodtest_mybatis_plus()
except Exception as e:
    print(f"测试过程中发生错误: {e}")
    import traceback
    traceback.print_exc()

print("\n=== 所有测试完成 ===")

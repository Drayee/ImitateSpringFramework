"""
    # Web 服务 插件
    提供 Web 服务的构建和运行功能

"""


from fastapi import FastAPI
import uvicorn



# 检查服务配置文件是否存在
def _check():
    import os
    if not os.path.exists("resource\\yaml\\service.yaml") and not os.path.exists("resource\\yaml\\service.yml"):
        raise FileNotFoundError("service.yaml 或 service.yml 文件不存在")

"""
     Web 服务 主类
"""
class Main(BaseMain):

    def __init__(self):
        _check()
        library.dependencies["Controller"] = {}

        self.service_title = library.resource_yaml["service.title"]
        self.service_version = library.resource_yaml["service.version"]
        self.service_host = library.resource_yaml["service.host"]
        self.service_port = library.resource_yaml["service.port"]
        # 构建所有控制器实例
        self.app = FastAPI(title=self.service_title, version=self.service_version)

    def build(self):
        pass

    def loop_method(self):
        uvicorn.run(self.app, host=self.service_host, port=self.service_port)

"""
    控制器装饰器
"""
def controller(path, name= None):
    def decorator(func):
        nonlocal name
        if name is None:
            name = func.__name__
        library.resource["path"][name] = path
        library.dependencies["Controller"][name] = func
        logger.info(f"Controller {name} 已加入库")
        return func
    return decorator
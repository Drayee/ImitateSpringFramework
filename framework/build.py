from PyQt5.QtNfc import title

import library
from fastapi import FastAPI
import uvicorn

def build():

    # 构建所有服务实例
    for classes in library.dependencies["Service"]:
        library.resource_dependencies[str(classes)] = library.dependencies["Service"][classes].build()


    service_title = library.resource_yaml["service.title"]
    service_version = library.resource_yaml["service.version"]
    service_host = library.resource_yaml["service.host"]
    service_port = library.resource_yaml["service.port"]
    # 构建所有控制器实例
    app = FastAPI(title=service_title, version=service_version)

    for classes in library.dependencies["Controller"]:
        path = library.resource["path"][str(classes)]

        @app.get(path)
        def read_root():
            return library.dependencies["Controller"][classes]()

    uvicorn.run(app, host=service_host, port=service_port)


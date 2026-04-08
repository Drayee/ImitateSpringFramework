"""
    # 嵌入 插件
    提供嵌入功能，将所有依赖项和装饰器加载到全局命名空间中
"""

class Main(BaseMain):

    def __init__(self):
        pass

    def build(self):
        __builtins__["library"] = library

        for classes in library.dependencies.keys():
            for module in library.dependencies[classes].keys():
                __builtins__[classes+module] = library.dependencies[classes][module]

        for decorator in library.decorator.keys():
            __builtins__[decorator] = library.decorator[decorator]

        for yml in library.resource_yaml.keys():
            __builtins__[yml] = library.resource_yaml[yml]

        for json in library.resource_json.keys():
            __builtins__[json] = library.resource_json[json]

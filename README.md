# Python Spring Framework

一个模仿 Spring 框架风格设计的 Python 轻量级开发框架，提供依赖注入、注解开发、资源管理和插件扩展等功能。

## 快速开始

### 项目启动

使用 `main.py` 启动项目。

### 项目结构

```
text/
├── main.py                # 项目启动文件
├── framework/             # 框架核心目录
│   ├── __init__.py        # 框架初始化
│   ├── run.py            # 框架运行主入口
│   ├── build.py          # 服务构建
│   ├── library.py        # 核心库管理
│   ├── check.py          # 环境检查
│   ├── load_src.py       # 源文件加载
│   ├── load_dlc.py       # DLC插件加载
│   ├── public_modules.py # 公共模块
│   ├── dlc/              # DLC插件目录
│   │   ├── web.py        # Web服务插件
│   │   ├── embed.py      # 嵌入插件
│   │   └── langgraph.py  # LangGraph插件
│   └── resource/         # 资源管理目录
│       ├── config.py     # 环境变量配置
│       ├── json.py       # JSON资源加载
│       ├── logging.py    # 日志配置
│       └── yml.py        # YAML资源加载
└── src/                   # 用户代码目录
    └── resource/         # 资源文件目录
        ├── json/         # JSON资源文件
        └── yaml/         # YAML资源文件
```

## 核心功能

### 1. 服务注册 (@Service)

使用 `@Service` 装饰器将类注册为服务：

```python
@Service
class MyService:
    def __init__(self):
        self.value = "Hello World"
    
    def do_something(self):
        return self.value
```

### 2. 依赖注入 (@auto_inject)

使用 `@auto_inject` 装饰器自动注入依赖：

```python
@auto_inject()
def my_function(service: MyService, config: str):
    return service.do_something() + config
```

支持两种参数注入方式：
- **同名参数注入**：`@auto_inject("param1", "param2")`
- **自定义参数注入**：`@auto_inject(custom_name="original_name")`

### 3. 资源管理

框架支持多种资源加载方式：

#### YAML 配置

在 `src/resource/yaml/` 目录下放置 YAML 文件，支持 `${key}` 占位符引用。

```python
# 获取 YAML 配置
from framework.library import get_resource_yaml
value = get_resource_yaml("config.key")
```

#### JSON 配置

在 `src/resource/json/` 目录下放置 JSON 文件。

```python
# 获取 JSON 配置
from framework.library import get_resource_json
data = get_resource_json("filename")
```

#### 环境变量

```python
# 获取环境变量
from framework.library import get_resource_config
value = get_resource_config("ENV_VAR")
```

#### 自定义资源

```python
# 设置资源
from framework.library import set_resource, get_resource
set_resource("my_key", "my_value")
value = get_resource("my_key")
```

## DLC 插件系统

框架支持通过 DLC（Downloadable Content）插件扩展功能。

### Web 插件 (web.py)

提供 FastAPI Web 服务功能。

#### 配置文件

在 `src/resource/yaml/` 下创建 `service.yaml`：

```yaml
service:
  title: "My Service"
  version: "1.0.0"
  host: "0.0.0.0"
  port: 8000
```

#### 控制器定义

```python
@controller(path="/api", name="my_controller")
def my_controller():
    return {"message": "Hello"}
```

### 嵌入插件 (embed.py)

将所有依赖项、装饰器和配置嵌入到全局命名空间中，便于直接使用。

### LangGraph 插件 (langgraph.py)

集成 LangGraph 用于构建复杂的 LLM 应用工作流。

```python
@langgraph_node(name="my_node")
def my_node(state):
    # 处理状态
    return state
```

## 核心模块说明

### framework/__init__.py
框架初始化模块，负责：
- 初始化环境
- 检查并创建必要目录
- 配置日志系统

### framework/run.py
框架运行主入口，流程：
1. 加载 DLC 插件
2. 加载用户源文件
3. 构建服务
4. 运行主循环

### framework/build.py
服务构建模块，负责：
- 实例化所有服务
- 执行构建器方法
- 启动主循环

### framework/library.py
核心库管理，维护：
- `dependencies`: 依赖库
- `decorator`: 装饰器
- `builder`: 构建器
- `loop_method`: 主循环方法
- `resource`: 用户资源
- `resource_yaml`: YAML 配置
- `resource_json`: JSON 配置
- `resource_dependencies`: 服务实例

### framework/load_src.py
源文件加载器，使用 AST 解析用户代码，安全加载带有装饰器的类和函数。

### framework/load_dlc.py
DLC 插件加载器，扫描并加载 `framework/dlc/` 目录下的插件。

## 开发示例

### 完整服务示例

```python
from framework.public_modules import Service, auto_inject

@Service
class DatabaseService:
    def __init__(self):
        self.connection = "database_connection"
    
    def query(self, sql):
        return f"Executing: {sql}"

@Service
class UserService:
    @auto_inject()
    def __init__(self, db: DatabaseService):
        self.db = db
    
    def get_user(self, user_id):
        return self.db.query(f"SELECT * FROM users WHERE id = {user_id}")

@auto_inject()
def main(user_service: UserService):
    print(user_service.get_user(1))
```

## 注意事项

1. 所有用户代码应放在 `src/` 目录下
2. 资源文件应放在 `src/resource/` 对应的子目录中
3. 使用 `@Service` 装饰器的类会被自动实例化
4. `@auto_inject` 需要配合类型注解使用

## 依赖库

- `pyyaml`: YAML 配置文件解析
- `python-dotenv`: 环境变量加载
- `fastapi`: Web 服务（可选）
- `uvicorn`: ASGI 服务器（可选）
- `langgraph`: 工作流编排（可选）

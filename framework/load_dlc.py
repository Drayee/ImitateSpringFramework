import library
import public_modules

def run():
    import importlib
    import inspect
    import os

    dlc_dir = os.path.join(os.path.dirname(__file__), "dlc")  # dlc 文件夹路径
    plugin_files = [f[:-3] for f in os.listdir(dlc_dir) if f.endswith(".py") and f not in ["__init__.py"]]

    for plugin_name in plugin_files:
        plugin = importlib.import_module(f"dlc.{plugin_name}")
        all_items = {}
        for name, member in inspect.getmembers(plugin):
            if (
                (not name.startswith("_"))
                and (inspect.isclass(member) or inspect.isfunction(member))
                and member.__module__ == plugin.__name__
            ):
                all_items[name] = member

        # 加载 all_items 中的所有 修饰器和 main 类
        for decorator in all_items.keys():
            if not decorator.startswith("_"):
                if decorator == "Main":

                    # 加载 Main 类
                    new_main = all_items[decorator]()
                    library.builder[decorator] = new_main.build

                    # 尝试获取 loop_method，check_method
                    try:
                        library.loop_method = new_main.loop_method
                    except:
                        pass
                    try:
                        library.dependencies["Check"] = new_main.check
                    except:
                        pass
                    continue
                library.decorator[decorator] = all_items[decorator]
                setattr(public_modules, decorator, all_items[decorator])

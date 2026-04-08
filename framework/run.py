import build
import load_dlc
import load_src
import library

def run():

    # 加载 扩展插件 并 执行服务发现
    load_dlc.run()
    load_src.run()

    # 构建 服务
    build.build()

    if library.loop_method is not None:
        # 运行 loop_method
        library.loop_method()


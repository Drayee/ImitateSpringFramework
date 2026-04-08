import library


def build():

    # 构建所有服务实例
    for classes in library.dependencies["Service"]:
        library.resource_dependencies[str(classes)] = library.dependencies["Service"][classes].build()


    for build_method in library.builder.values():
        build_method()

    if library.loop_method is not None:
        library.loop_method()




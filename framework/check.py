import os
import logging

logger = logging.getLogger(__name__)

def check():
    if not os.path.exists("src"):
        os.mkdir("src")
        logger.info("src 目录已创建")

    if not os.path.exists("src\\resource"):
        os.mkdir("src\\resource")
        logger.info("src\\resource 目录已创建")

    if not os.path.exists("src\\resource\\json"):
        os.mkdir("src\\resource\\json")
        logger.info("src\\resource\\json 目录已创建")

    if not os.path.exists("src\\resource\\yaml"):
        os.mkdir("src\\resource\\yaml")
        logger.info("src\\resource\\yaml 目录已创建")

def dependency_check(check_method):
    try:
        check_method()
    except ValueError as e:
        logger.error(e)
        raise e

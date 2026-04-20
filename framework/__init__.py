import sys
import os


current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

import check
os.chdir(os.sep.join(current_dir.split(os.sep)[:-1]))
check.check()
os.chdir(os.sep.join(current_dir.split(os.sep)[:-1]+["src"]))

# 资源库(系统) - env
from resource import config
from resource import logging

logger = logging.getLogger(__name__)
logger.info("框架初始化")
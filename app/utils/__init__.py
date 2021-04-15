import subprocess
import shlex
import random
import string

import os
import colorlog
import re
import hashlib
from celery.utils.log import get_task_logger
import logging


def load_file(path):
    with open(path, "r+", encoding="utf-8") as f:
        return f.readlines()

def exec_system(cmd, **kwargs):
    cmd = " ".join(cmd)
    timeout = 4 * 60 * 60

    if kwargs.get('timeout'):
        timeout = kwargs['timeout']

    completed = subprocess.run(shlex.split(cmd), timeout=timeout, check=False, close_fds=True, **kwargs)

    return completed


def check_output(cmd, **kwargs):
    cmd = " ".join(cmd)
    timeout = 4 * 60 * 60

    if kwargs.get('timeout'):
        timeout = kwargs.pop('timeout')

    if 'stdout' in kwargs:
        raise ValueError('stdout argument not allowed, it will be overridden.')


    output = subprocess.run(shlex.split(cmd), stdout=subprocess.PIPE, timeout=timeout, check=False,
               **kwargs).stdout
    return output

def random_choices(k = 6):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=k))


def gen_md5(s):
    return hashlib.md5(s.encode()).hexdigest()


def init_logger():
    handler = colorlog.StreamHandler()
    handler.setFormatter(colorlog.ColoredFormatter(
        fmt = '%(log_color)s[%(asctime)s] [%(levelname)s] '
              '[%(threadName)s] [%(filename)s:%(lineno)d] %(message)s', datefmt = "%Y-%m-%d %H:%M:%S"))

    logger = colorlog.getLogger('arlv2')

    logger.setLevel(logging.INFO)
    logger.addHandler(handler)
    logger.propagate = False


import sys

def get_logger():
    if 'celery' in sys.argv[0]:
        task_logger = get_task_logger(__name__)
        return task_logger

    logger = logging.getLogger('arlv2')
    if not logger.handlers:
        init_logger()

    return  logging.getLogger('arlv2')



def gen_filename(site):
    filename = site.replace('://', '_')

    return re.sub('[^\w\-_\. ]', '_', filename)


def build_ret(error, data):
    if isinstance(error, str):
        error = {
            "message": error,
            "code": 999,
        }

    ret = {}
    ret.update(error)
    ret["data"] = data
    msg = error["message"]

    if error["code"] != 200:
        for k in data:
            if k.endswith("id"):
                continue
            if not data[k]:
                continue
            if isinstance(data[k], str):
                msg += " {}:{}".format(k, data[k])

    ret["message"] = msg
    return ret


def conn_db(collection, db_name = None):
    """
    连接DB
    :param collection:
    :param db_name:
    :return:
    """
    return
from datetime import datetime
import os
from . import conn_db
from app.config import Config


def update_task_tag():
    """更新task任务tag信息"""

    try:
        table = "task"
        items = conn_db(table).find({})
        for item in items:
            task_tag = item.get("task_tag")
            query = {"_id": item["_id"]}
            if not task_tag:
                item["task_tag"] = "task"
                conn_db(table).find_one_and_replace(query, item)
    except Exception as e:
        print(e)


def arl_update():
    update_lock = os.path.join(Config.TMP_PATH, 'arl_update.lock')
    if os.path.exists(update_lock):
        return

    update_task_tag()

    open(update_lock, 'a').close()
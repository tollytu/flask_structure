from .ipInfo import PortInfo, IPInfo
from .baseInfo import BaseInfo
from .domainInfo import DomainInfo
from .pageInfo import PageInfo
from app.config import Config


class ScanPortType:
    TEST = Config.TOP_10
    TOP100 = Config.TOP_100
    TOP1000 = Config.TOP_1000
    ALL = "0-65535"


class DomainDictType:
    TEST = Config.DOMAIN_DICT_TEST
    BIG = Config.DOMAIN_DICT_2W


class CollectSource:
    DOMAIN_BRUTE = "domain_brute"
    BAIDU = "baidu"
    RISKIQ = "riskIQ"
    ALTDNS = "altdns"
    ARL = "arl"
    SITESPIDER = "site_spider"
    SEARCHENGINE = "search_engine"
    MONITOR = "monitor"

class TaskStatus:
    WAITING = "waiting"
    DONE = "done"
    ERROR = "error"
    STOP = "stop"


class TaskTag:
    """任务标签"""

    """带资产发现的任务"""
    TASK = "task"

    """域名监控任务"""
    MONITOR = "monitor"

    """风险巡航任务"""
    RISK_CRUISING = "risk_cruising"


class TaskSyncStatus:
    WAITING = "waiting"
    RUNNING = "running"
    ERROR = "error"
    DEFAULT = "default"


class SchedulerStatus:
    RUNNING = "running"
    STOP = "stop"


class PoCCategory:
    POC = "漏洞PoC"
    SNIFFER = "协议识别"
    SYSTEM_BRUTE = "服务弱口令"
    WEBB_RUTE = "应用弱口令"


class CeleryAction:
    """celery任务celery_action字段"""

    """常规IP任务"""
    IP_TASK = "ip_task"

    """常规域名任务"""
    DOMAIN_TASK = "domain_task"

    """域名监测任务"""
    DOMAIN_EXEC_TASK = "domain_exec_task"

    """同步已有任务"""
    DOMAIN_TASK_SYNC_TASK = "domain_task_sync_task"

    """添加任务到资产组中"""
    ADD_DOMAIN_TO_SCOPE = "add_domain_to_scope"

    """PoC运行任务"""
    RUN_RISK_CRUISING = "run_risk_cruising"

error_map = {
    'CeleryIdNotFound': {
        "message": "没有找到Celery id",
        "code": 102,
    },
    'NotFoundTask': {
        "message": "没有找到任务",
        "code": 103,
    },
    "TaskIsRunning": {
        "message": "任务运行中",
        "code": 104,
    },
    "TaskIsDone": {
        "message": "任务已经完成",
        "code": 105,
    },
    "Success": {
        "message": "success",
        "code": 200,
    },
    "NotLogin": {
        "message": "未登录",
        "code": 401,
    },
    "NotFoundScopeID": {
        "message": "没有找到资产范围ID",
        "code": 601,
    },
    "NotFoundScope": {
        "message": "没有找到对应的资产范围",
        "code": 602,
    },
    "ExistScope": {
        "message": "已存在对应的资产范围",
        "code": 603,
    },
    "IntervalLessThan3600": {
        "message": "监控任务时间间隔不能小于6小时（21600s）",
        "code": 700,
    },
    "DomainNotFoundViaScope": {
        "message": "域名不在给定的资产范围中",
        "code": 701,
    },
    "DomainViaJob": {
        "message": "给定资产范围中的域名已经存在监控任务",
        "code": 701,
    },
    "DomainNotViaJob": {
        "message": "给定资产范围中的域名不存在监控任务",
        "code": 702,
    },
    "JobNotFound": {
        "message": "监控任务未找到",
        "code": 702,
    },
    "DomainInvalid": {
        "message": "域名无效",
        "code": 703,
    },
    "TargetInvalid": {
        "message": "任务目标无效",
        "code": 704,
    },
    "IPInBlackIps": {
        "message": "目标IP不允许下发",
        "code": 705,
    },
    "TaskTargetIsEmpty": {
        "message": "任务目标为空",
        "code": 706,
    },
    "TaskSyncDealing": {
        "message": "任务资产同步处理中",
        "code": 801,
    },
    "TaskTypeIsNotDomain": {
        "message": "不是域名发现任务",
        "code": 802,
    },
    "TaskTargetNotInScope": {
        "message": "任务目标不在资产组中",
        "code": 802,
    },
    "DomainInScope": {
        "message": "域名已经存在指定资产组中",
        "code": 803,
    },
    "URLInvalid": {
        "message": "URL无效",
        "code": 804,
    },
    "SiteURLNotDomain": {
        "message": "非域名类型URL",
        "code": 805,
    },
    "SiteInScope": {
        "message": "站点已在指定资产中",
        "code": 806,
    },
    "DomainNotFoundNotInScope": {
            "message": "没有发现可以添加的域名",
            "code": 807,
    },
    "SchedulerStatusNotRunning": {
        "message": "监控任务非运行状态",
        "code": 901,
    },
    "SchedulerStatusNotStop": {
        "message": "监控任务非停止状态",
        "code": 902,
    },
    "ResultSetIDNotFound": {
        "message": "结果集 ID 没有找到",
        "code": 1001,
    },
    "ResultSetIsEmpty": {
        "message": "结果集中目标为空",
        "code": 1002,
    },
    "PoCTargetIsEmpty": {
        "message": "PoC 任务目标为空",
        "code": 1003,
    },
    "QueryResultIsEmpty": {
        "message": "查询结果为空",
        "code": 1004,
    },
    "PolicyIDNotFound": {
        "message": "策略不存在",
        "code": 1100,
    },
    "RiskCruisingPoCConfigIsEmpty": {
        "message": "风险巡航任务选择的策略PoC配置字段不能为空",
        "code": 1101,
    },
    "BruteTaskBruteConfigIsEmpty": {
        "message": "弱口令任务选择的策略爆破配置字段不能为空",
        "code": 1102,
    },
    "PolicyDataIsEmpty": {
        "message": "策略数据为空",
        "code": 1103,
    }
}


class ErrorMsg:
    CeleryIdNotFound = error_map["CeleryIdNotFound"]
    NotFoundTask = error_map["NotFoundTask"]
    TaskIsRunning = error_map["TaskIsRunning"]
    TaskIsDone = error_map["TaskIsDone"]
    Success = error_map["Success"]
    NotLogin = error_map["NotLogin"]
    NotFoundScopeID = error_map["NotFoundScopeID"]
    NotFoundScope = error_map["NotFoundScope"]
    ExistScope = error_map["ExistScope"]
    IntervalLessThan3600 = error_map["IntervalLessThan3600"]
    DomainNotFoundViaScope = error_map["DomainNotFoundViaScope"]
    DomainViaJob = error_map["DomainViaJob"]
    DomainNotViaJob = error_map["DomainNotViaJob"]
    JobNotFound = error_map["JobNotFound"]
    DomainInvalid = error_map["DomainInvalid"]
    TargetInvalid = error_map["TargetInvalid"]
    IPInBlackIps = error_map["IPInBlackIps"]
    TaskSyncDealing = error_map["TaskSyncDealing"]
    TaskTypeIsNotDomain = error_map["TaskTypeIsNotDomain"]
    TaskTargetNotInScope = error_map["TaskTargetNotInScope"]
    DomainInScope = error_map["DomainInScope"]
    SiteInScope = error_map["SiteInScope"]
    URLInvalid = error_map["URLInvalid"]
    SiteURLNotDomain = error_map["SiteURLNotDomain"]
    SchedulerStatusNotRunning = error_map["SchedulerStatusNotRunning"]
    SchedulerStatusNotStop = error_map["SchedulerStatusNotStop"]
    DomainNotFoundNotInScope = error_map["DomainNotFoundNotInScope"]
    ResultSetIDNotFound = error_map["ResultSetIDNotFound"]
    ResultSetIsEmpty = error_map["ResultSetIsEmpty"]
    PoCTargetIsEmpty = error_map["PoCTargetIsEmpty"]
    QueryResultIsEmpty = error_map["QueryResultIsEmpty"]
    TaskTargetIsEmpty = error_map["TaskTargetIsEmpty"]
    PolicyIDNotFound = error_map["PolicyIDNotFound"]
    PolicyDataIsEmpty = error_map["PolicyDataIsEmpty"]
    RiskCruisingPoCConfigIsEmpty = error_map["RiskCruisingPoCConfigIsEmpty"]
    BruteTaskBruteConfigIsEmpty = error_map["BruteTaskBruteConfigIsEmpty"]




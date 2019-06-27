__author__ = 'singo'
__datetime__ = '2019/5/7 11:03 AM'

__all__ = ['D_UNREVIEWED', 'ONLINE', 'D_PENDING', 'ROLLBACK', 'D_RUNNING', 'D_FAILED',
           'REONLONE', 'D_SUCCESSFUL', 'D_REJECTED', 'H_FAILED', 'H_CANCELED', 'S_UNKNOW',
           'H_UNKNOWN', 'H_SUCCESSFUL', 'CACHE_TIMEOUT', 'S_RUNNING', 'S_FAILED', 'S_SUCCESSFUL',
           'DOCKER', 'PACKAGE']

# 部署方式
ONLINE  = 0
ROLLBACK  = 1
REONLONE  = 2

# 发布方式
DOCKER = 0
PACKAGE = 1

CACHE_TIMEOUT = 24*3600

# DeploymentOrder 的状态
D_UNREVIEWED = 0
D_PENDING = 1
D_RUNNING = 2
D_SUCCESSFUL = 3
D_REJECTED = 4
D_FAILED = 5

# History 的状态
H_UNKNOWN = 0
H_CANCELED = 1
H_SUCCESSFUL = 2
H_FAILED = 3

# 部署环境
# PRO = 0
# PRE = 1
# TEST = 2
# DEV = 3

S_RUNNING = 'running'
S_FAILED = 'failed'
S_SUCCESSFUL = 'successful'
S_UNKNOW = 'unknown'






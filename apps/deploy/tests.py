# {'id': 1,
#  'description': '',
#  'name': 'devops-server',
#  'name_with_namespace': 'cainanjie / devops-server',
#  'path': 'devops-server',
#  'path_with_namespace': 'cainanjie/devops-server',
#  'created_at': '2019-03-27T01:34:48.895Z',
#  'default_branch': 'master', 'tag_list': [],
#  'ssh_url_to_repo': 'git@git.ops.com:cainanjie/devops-server.git',
#  'http_url_to_repo': 'http://git.ops.com/cainanjie/devops-server.git',
#  'web_url': 'http://git.ops.com/cainanjie/devops-server',
#  'readme_url': 'http://git.ops.com/cainanjie/devops-server/blob/master/README.md',
#  'avatar_url': None, 'star_count': 0, 'forks_count': 0,
#  'last_activity_at': '2019-04-24T04:52:13.721Z',
#  'namespace': {'id': 4, 'name': 'cainanjie', 'path': 'cainanjie', 'kind': 'user', 'full_path': 'cainanjie', 'parent_id': None}, '_links': {'self': 'http://git.ops.com/api/v4/projects/1', 'issues': 'http://git.ops.com/api/v4/projects/1/issues', 'merge_requests': 'http://git.ops.com/api/v4/projects/1/merge_requests', 'repo_branches': 'http://git.ops.com/api/v4/projects/1/repository/branches', 'labels': 'http://git.ops.com/api/v4/projects/1/labels', 'events': 'http://git.ops.com/api/v4/projects/1/events', 'members': 'http://git.ops.com/api/v4/projects/1/members'}, 'archived': False, 'visibility': 'private', 'owner': {'id': 3, 'name': 'cainanjie', 'username': 'cainanjie', 'state': 'active', 'avatar_url': 'https://www.gravatar.com/avatar/49b5c2f2f9b051d268581e9f055beb42?s=80&d=identicon', 'web_url': 'http://git.ops.com/cainanjie'}, 'resolve_outdated_diff_discussions': False, 'container_registry_enabled': True, 'issues_enabled': True, 'merge_requests_enabled': True, 'wiki_enabled': True, 'jobs_enabled': True, 'snippets_enabled': True, 'shared_runners_enabled': True, 'lfs_enabled': True, 'creator_id': 3, 'import_status': 'none', 'import_error': None, 'open_issues_count': 0, 'runners_token': 'DPZhiduYGoWbssVGhaJk', 'public_jobs': True, 'ci_config_path': None, 'shared_with_groups': [], 'only_allow_merge_if_pipeline_succeeds': False, 'request_access_enabled': False, 'only_allow_merge_if_all_discussions_are_resolved': False, 'printing_merge_request_link_enabled': True, 'merge_method': 'merge', 'permissions': {'project_access': {'access_level': 40, 'notification_level': 3}, 'group_access': None}}

#############get_job_info()###############
{'_class': 'hudson.model.FreeStyleProject',
 'actions': [{'_class': 'hudson.model.ParametersDefinitionProperty',
              'parameterDefinitions': [{'_class': 'net.uaznia.lukanus.hudson.plugins.gitparameter.GitParameterDefinition',
                                        'defaultParameterValue': None,
                                        'description': '', 'name': 'BRANCH', 'type': 'PT_BRANCH'}]}, {}, {}, {},
             {'_class': 'com.cloudbees.plugins.credentials.ViewCredentialsAction'}],
 'description': '不要再删我了',
 'displayName': 'devops',
 'displayNameOrNull': None,
 'fullDisplayName': 'devops',
 'fullName': 'devops',
 'name': 'devops',
 'url': 'http://172.16.102.16:8080/job/devops/',
 'buildable': True,
 'builds': [{'_class': 'hudson.model.FreeStyleBuild',
             'number': 1, 'url': 'http://172.16.102.16:8080/job/devops/1/'}],
 'color': 'blue',
 'firstBuild': {'_class': 'hudson.model.FreeStyleBuild',
                'number': 1,
                'url': 'http://172.16.102.16:8080/job/devops/1/'},
 'healthReport': [{'description': 'Build stability: No recent builds failed.',
                   'iconClassName': 'icon-health-80plus',
                   'iconUrl': 'health-80plus.png', 'score': 100}],
 'inQueue': False,
 'keepDependencies': False,
 'lastBuild': {'_class': 'hudson.model.FreeStyleBuild', 'number': 1,
               'url': 'http://172.16.102.16:8080/job/devops/1/'},
 'lastCompletedBuild': {'_class': 'hudson.model.FreeStyleBuild',
                        'number': 1, 'url': 'http://172.16.102.16:8080/job/devops/1/'},
 'lastFailedBuild': None, 'lastStableBuild':
     {'_class': 'hudson.model.FreeStyleBuild', 'number': 1,
      'url': 'http://172.16.102.16:8080/job/devops/1/'},
 'lastSuccessfulBuild': {'_class': 'hudson.model.FreeStyleBuild', 'number': 1,
                         'url': 'http://172.16.102.16:8080/job/devops/1/'},
 'lastUnstableBuild': None,
 'lastUnsuccessfulBuild': None,
 'nextBuildNumber': 2,
 'property': [{'_class': 'jenkins.model.BuildDiscarderProperty'},
              {'_class': 'hudson.model.ParametersDefinitionProperty',
               'parameterDefinitions': [{'_class': 'net.uaznia.lukanus.hudson.plugins.gitparameter.GitParameterDefinition',
                                         'defaultParameterValue': None, 'description': '',
                                         'name': 'BRANCH', 'type': 'PT_BRANCH'}]}],
 'queueItem': None,
 'concurrentBuild': False,
 'downstreamProjects': [],
 'labelExpression': 'jenkins_node01',
 'scm': {'_class': 'hudson.plugins.git.GitSCM'},
 'upstreamProjects': []}

##########build_info################
{'_class': 'hudson.model.FreeStyleBuild',
 'actions': [{'_class': 'hudson.model.ParametersAction',
              'parameters': [{'_class': 'net.uaznia.lukanus.hudson.plugins.gitparameter.GitParameterValue',
                              'name': 'BRANCH', 'value': 'master'}]},
             {'_class': 'hudson.model.CauseAction',
              'causes': [{'_class': 'hudson.model.Cause$UserIdCause',
                          'shortDescription': 'Started by user 周金亮',
                          'userId': 'zhoujinliang', 'userName': '周金亮'}]},
             {'_class': 'hudson.plugins.git.util.BuildData',
              'buildsByBranchName': {'origin/master': {'_class': 'hudson.plugins.git.util.Build',
                                                       'buildNumber': 4, 'buildResult': None,
                                                       'marked': {'SHA1': '88d4ddf20e0cf6e24acf199e96b1f54b0454a0b4',
                                                                  'branch': [{'SHA1': '88d4ddf20e0cf6e24acf199e96b1f54b0454a0b4', 'name': 'origin/master'}]},
                                                       'revision': {'SHA1': '88d4ddf20e0cf6e24acf199e96b1f54b0454a0b4',
                                                                    'branch': [{'SHA1': '88d4ddf20e0cf6e24acf199e96b1f54b0454a0b4', 'name': 'origin/master'}]}},
                                     'refs/remotes/origin/master': {'_class': 'hudson.plugins.git.util.Build', 'buildNumber': 2, 'buildResult': None,
                                                                    'marked': {'SHA1': '88d4ddf20e0cf6e24acf199e96b1f54b0454a0b4',
                                                                               'branch': [{'SHA1': '88d4ddf20e0cf6e24acf199e96b1f54b0454a0b4',
                                                                                           'name': 'refs/remotes/origin/master'}]},
                                                                    'revision': {'SHA1': '88d4ddf20e0cf6e24acf199e96b1f54b0454a0b4',
                                                                                 'branch': [{'SHA1': '88d4ddf20e0cf6e24acf199e96b1f54b0454a0b4',
                                                                                             'name': 'refs/remotes/origin/master'}]}}},
              'lastBuiltRevision': {'SHA1': '88d4ddf20e0cf6e24acf199e96b1f54b0454a0b4',
                                    'branch': [{'SHA1': '88d4ddf20e0cf6e24acf199e96b1f54b0454a0b4', 'name': 'origin/master'}]},
              'remoteUrls': ['http://172.16.100.189/ztocwst-wms/express.git'], 'scmName': ''},
             {'_class': 'hudson.plugins.git.GitTagAction'}, {}, {}, {}],
 'artifacts': [],
 'building': True,
 'description': None,
 'displayName': '#4',
 'duration': 0,
 'estimatedDuration': 152438, 'executor': {},
 'fullDisplayName': 'devops #4',
 'id': '4',
 'keepLog': False,
 'number': 4,
 'queueId': 3229,
 'result': None,
 'timestamp': 1556442130930,
 'url': 'http://172.16.102.16:8080/job/devops/4/',
 'builtOn': 'jenkins_node01',
 'changeSet': {'_class': 'hudson.plugins.git.GitChangeSetList', 'items': [], 'kind': 'git'},
 'culprits': []}


######queue info###############
[{'_class': 'hudson.model.Queue$WaitingItem',
  'actions': [{'_class': 'hudson.model.ParametersAction',
               'parameters': [{'_class': 'net.uaznia.lukanus.hudson.plugins.gitparameter.GitParameterValue',
                               'name': 'BRANCH', 'value': 'master'}]},
              {'_class': 'hudson.model.CauseAction', 'causes': [{'_class': 'hudson.model.Cause$UserIdCause',
                                                                 'shortDescription': 'Started by user 周金亮',
                                                                 'userId': 'zhoujinliang', 'userName': '周金亮'}]}],
  'blocked': False,
  'buildable': False,
  'id': 3258, 'inQueueSince': 1556502928109, 'params': '\nBRANCH=master', 'stuck': False, 'task': {'_class': 'hudson.model.FreeStyleProject', 'name': 'devops', 'url': 'http://172.16.102.16:8080/job/devops/', 'color': 'aborted'}, 'url': 'queue/item/3258/', 'why': 'In the quiet period. Expires in 4.9 sec', 'timestamp': 1556502933109}]

######get_queue_item()
{'_class': 'hudson.model.Queue$LeftItem',
 'actions': [{'_class': 'hudson.model.ParametersAction',
              'parameters': [{'_class': 'net.uaznia.lukanus.hudson.plugins.gitparameter.GitParameterValue',
                              'name': 'BRANCH', 'value': 'master'}]},
             {'_class': 'hudson.model.CauseAction',
              'causes': [{'_class': 'hudson.model.Cause$UserIdCause',
                          'shortDescription': 'Started by user 周金亮',
                          'userId': 'zhoujinliang', 'userName': '周金亮'}]}],
 'blocked': False,
 'buildable': False,
 'id': 3260,
 'inQueueSince': 1556503319759,
 'params': '\nBRANCH=master',
 'stuck': False,
 'task': {'_class': 'hudson.model.FreeStyleProject',
          'name': 'devops', 'url': 'http://172.16.102.16:8080/job/devops/',
          'color': 'aborted'},
 'url': 'queue/item/3260/',
 'why': None,
 'cancelled': False,
 'executable': {'_class': 'hudson.model.FreeStyleBuild',
                'number': 9, 'url': 'http://172.16.102.16:8080/job/devops/9/'}}



{'_class': 'hudson.model.Queue$WaitingItem', 'actions': [{'_class': 'hudson.model.ParametersAction', 'parameters': [{'_class': 'net.uaznia.lukanus.hudson.plugins.gitparameter.GitParameterValue', 'name': 'BRANCH', 'value': 'master'}]}, {'_class': 'hudson.model.CauseAction', 'causes': [{'_class': 'hudson.model.Cause$UserIdCause', 'shortDescription': 'Started by user 周金亮', 'userId': 'zhoujinliang', 'userName': '周金亮'}]}], 'blocked': False, 'buildable': False, 'id': 3261, 'inQueueSince': 1556504393600, 'params': '\nBRANCH=master', 'stuck': False, 'task': {'_class': 'hudson.model.FreeStyleProject', 'name': 'devops', 'url': 'http://172.16.102.16:8080/job/devops/', 'color': 'aborted'},
 'url': 'queue/item/3261/',
 'why': 'In the quiet period. Expires in 4.9 sec', 'timestamp': 1556504398599}


#单台回调错误
{'return': [
    {'minion-1': {
        'http_|-alert_code_|-http://127.0.0.1:8418/api/deploy/v1/deploy/ba74e384513f4f63b6643727444a8172/webhook/_|-query':
            {'comment': 'An exception occurred in this state: Traceback (most recent call last):\n  File "/usr/lib/python2.7/site-packages/salt/state.py", line 1913, in call\n    **cdata[\'kwargs\'])\n  File "/usr/lib/python2.7/site-packages/salt/loader.py", line 1898, in wrapper\n    return f(*args, **kwargs)\n  File "/usr/lib/python2.7/site-packages/salt/states/http.py", line 92, in query\n    data = __salt__[\'http.query\'](name, **kwargs)\n  File "/usr/lib/python2.7/site-packages/salt/modules/http.py", line 38, in query\n    return salt.utils.http.query(url=url, opts=opts, **kwargs)\n  File "/usr/lib/python2.7/site-packages/salt/utils/http.py", line 555, in query\n    **req_kwargs\n  File "/usr/lib64/python2.7/site-packages/tornado/httpclient.py", line 102, in fetch\n    self._async_client.fetch, request, **kwargs))\n  File "/usr/lib64/python2.7/site-packages/tornado/ioloop.py", line 444, in run_sync\n    return future_cell[0].result()\n  File "/usr/lib64/python2.7/site-packages/tornado/concurrent.py", line 214, in result\n    raise_exc_info(self._exc_info)\n  File "<string>", line 3, in raise_exc_info\nerror: [Errno 111] Connection refused\n',
             'name': 'http://127.0.0.1:8418/api/deploy/v1/deploy/ba74e384513f4f63b6643727444a8172/webhook/',
             'start_time': '04:05:07.701100',
             'result': False,'duration': 10.771,'__run_num__': 1,'__sls__': 'devops-server','changes': {},
             '__id__': 'alert_code'},
        "cmd_|-finally_|-echo 'successful'_|-run":
            {'comment': 'Command "echo \'successful\'" run',
             'name': "echo 'successful'",
             'start_time': '04:05:08.482114',
             'result': True, 'duration': 7.273,
             '__run_num__': 4,
             '__sls__': 'devops-server',
             'changes': {'pid': 5161, 'retcode': 0, 'stderr': '', 'stdout': 'successful'},
             '__id__': 'finally'},
        'service_|-web_service_|-httpd_|-running':
            {'comment': 'The service httpd is already running', 'name': 'httpd', 'start_time': '04:05:08.441249',
             'result': True, 'duration': 34.109, '__run_num__': 2, '__sls__': 'devops-server', 'changes': {},
             '__id__': 'web_service'},
        'file_|-lemon_|-/opt/devops/edi-express-1.3.0.war_|-managed':
            {'comment': 'File /opt/devops/edi-express-1.3.0.war is in the correct state', 'pchanges': {}, 'name': '/opt/devops/edi-express-1.3.0.war', 'start_time': '04:05:06.691312',
             'result': True, 'duration': 1007.795, '__run_num__': 0, '__sls__': 'devops-server', 'changes': {},
             '__id__': 'lemon'},
        'http_|-alert_web_|-http://127.0.0.1:8418/api/deploy/v1/deploy/ba74e384513f4f63b6643727444a8172/webhook/_|-query':
            {'comment': 'An exception occurred in this state: Traceback (most recent call last):\n  File "/usr/lib/python2.7/site-packages/salt/state.py", line 1913, in call\n    **cdata[\'kwargs\'])\n  File "/usr/lib/python2.7/site-packages/salt/loader.py", line 1898, in wrapper\n    return f(*args, **kwargs)\n  File "/usr/lib/python2.7/site-packages/salt/states/http.py", line 92, in query\n    data = __salt__[\'http.query\'](name, **kwargs)\n  File "/usr/lib/python2.7/site-packages/salt/modules/http.py", line 38, in query\n    return salt.utils.http.query(url=url, opts=opts, **kwargs)\n  File "/usr/lib/python2.7/site-packages/salt/utils/http.py", line 555, in query\n    **req_kwargs\n  File "/usr/lib64/python2.7/site-packages/tornado/httpclient.py", line 102, in fetch\n    self._async_client.fetch, request, **kwargs))\n  File "/usr/lib64/python2.7/site-packages/tornado/ioloop.py", line 444, in run_sync\n    return future_cell[0].result()\n  File "/usr/lib64/python2.7/site-packages/tornado/concurrent.py", line 214, in result\n    raise_exc_info(self._exc_info)\n  File "<string>", line 3, in raise_exc_info\nerror: [Errno 111] Connection refused\n', 'name': 'http://127.0.0.1:8418/api/deploy/v1/deploy/ba74e384513f4f63b6643727444a8172/webhook/', 'start_time': '04:05:08.476145',
             'result': False, 'duration': 3.895, '__run_num__': 3, '__sls__': 'devops-server', 'changes': {},
             '__id__': 'alert_web'}}}]}


#单台某一必须步骤出错(貌似当必须步骤出错后就不会反回后面步骤的__id__了)
{'return': [
    {'minion-1':
         {'http_|-alert_code_|-http://127.0.0.1:8418/api/deploy/v1/deploy/ba74e384513f4f63b6643727444a8172/webhook/_|-query':
              {'comment': 'An exception occurred in this state: Traceback (most recent call last):\n  File "/usr/lib/python2.7/site-packages/salt/state.py", line 1913, in call\n    **cdata[\'kwargs\'])\n  File "/usr/lib/python2.7/site-packages/salt/loader.py", line 1898, in wrapper\n    return f(*args, **kwargs)\n  File "/usr/lib/python2.7/site-packages/salt/states/http.py", line 92, in query\n    data = __salt__[\'http.query\'](name, **kwargs)\n  File "/usr/lib/python2.7/site-packages/salt/modules/http.py", line 38, in query\n    return salt.utils.http.query(url=url, opts=opts, **kwargs)\n  File "/usr/lib/python2.7/site-packages/salt/utils/http.py", line 555, in query\n    **req_kwargs\n  File "/usr/lib64/python2.7/site-packages/tornado/httpclient.py", line 102, in fetch\n    self._async_client.fetch, request, **kwargs))\n  File "/usr/lib64/python2.7/site-packages/tornado/ioloop.py", line 444, in run_sync\n    return future_cell[0].result()\n  File "/usr/lib64/python2.7/site-packages/tornado/concurrent.py", line 214, in result\n    raise_exc_info(self._exc_info)\n  File "<string>", line 3, in raise_exc_info\nerror: [Errno 111] Connection refused\n', 'name': 'http://127.0.0.1:8418/api/deploy/v1/deploy/ba74e384513f4f63b6643727444a8172/webhook/', 'start_time': '04:12:06.837035',
               'result': False, 'duration': 8.051, '__run_num__': 1, '__sls__': 'devops-server', 'changes': {},
               '__id__': 'alert_code'},
          "cmd_|-finally_|-echo 'successful'_|-run":
              {'comment': 'One or more requisite failed: devops-server.web_service', 'start_time': '04:12:07.253626',
               'result': False, 'duration': 0.012, '__run_num__': 4, '__sls__': 'devops-server', 'changes': {}},
          'service_|-web_service_|-httpd_|-running':
              {'comment': 'The named service httpd is not available', 'name': 'httpd', 'start_time': '04:12:07.236787',
                'result': False, 'duration': 14.993, '__run_num__': 2, '__sls__': 'devops-server', 'changes': {},
               '__id__': 'web_service'},
          'file_|-lemon_|-/opt/devops/edi-express-1.3.0.war_|-managed':
              {'comment': 'File /opt/devops/edi-express-1.3.0.war is in the correct state', 'pchanges': {}, 'name': '/opt/devops/edi-express-1.3.0.war', 'start_time': '04:12:05.872551',
               'result': True, 'duration': 963.485, '__run_num__': 0, '__sls__': 'devops-server', 'changes': {},
               '__id__': 'lemon'},
          'http_|-alert_web_|-http://127.0.0.1:8418/api/deploy/v1/deploy/ba74e384513f4f63b6643727444a8172/webhook/_|-query':
              {'comment': 'One or more requisite failed: devops-server.web_service', 'start_time': '04:12:07.252419',
               'result': False, 'duration': 0.012, '__run_num__': 3, '__sls__': 'devops-server', 'changes': {}}}}]}

{'return': [
    {'minion-1': {'file_|-lemon_|-/opt/devops/edi-express-1.3.0.war_|-managed':
                      {'comment': 'File /opt/devops/edi-express-1.3.0.war updated', 'pchanges': {}, 'name': '/opt/devops/edi-express-1.3.0.war', 'start_time': '02:34:28.967491',
                       'result': True, 'duration': 4325.627, '__run_num__': 0, '__sls__': 'devops-server', 'changes': {'diff': 'Replace binary file'},
                       '__id__': 'lemon'},
                  'service_|-web_service_|-httpd_|-running':
                      {'comment': 'The named service httpd is not available', 'name': 'httpd', 'start_time': '02:34:34.965798',
                       'result': False, 'duration': 39.207, '__run_num__': 2, '__sls__': 'devops-server', 'changes': {},
                       '__id__': 'web_service'},
                  'cmd_|-finally_|-sleep 10_|-run':
                      {'comment': 'One or more requisite failed: devops-server.web_service', 'start_time': '02:34:35.033297',
                       'result': False, 'duration': 0.172, '__run_num__': 4,
                       '__sls__': 'devops-server', 'changes': {}},
                  'http_|-alert_code_|-http://192.168.33.20:8418/api/deploy/v1/deploy/ba74e384513f4f63b6643727444a8172/webhook/_|-query':
                      {'comment': 'Status 200 was found, as specified.', 'name': 'http://192.168.33.20:8418/api/deploy/v1/deploy/ba74e384513f4f63b6643727444a8172/webhook/', 'data': {'body': '"lemon"', 'status': 200, 'text': '"lemon"'}, 'start_time': '02:34:33.294225',
                       'result': True, 'duration': 22.352, '__run_num__': 1, '__sls__': 'devops-server', 'changes': {},
                       '__id__': 'alert_code'},
                  'http_|-alert_finally_|-http://192.168.33.20:8418/api/deploy/v1/deploy/ba74e384513f4f63b6643727444a8172/webhook/_|-query':
                      {'comment': 'One or more requisite failed: devops-server.finally', 'start_time': '02:34:35.034036',
                        'result': False, 'duration': 0.024, '__run_num__': 5, '__sls__': 'devops-server', 'changes': {}},
                  'http_|-alert_web_|-http://192.168.33.20:8418/api/deploy/v1/deploy/ba74e384513f4f63b6643727444a8172/webhook/_|-query':
                      {'comment': 'One or more requisite failed: devops-server.web_service', 'start_time': '02:34:35.005807',
                       'result': False, 'duration': 0.014, '__run_num__': 3, '__sls__': 'devops-server', 'changes': {}}}}]}


# 单台saltID出错
{'return': [{}]}

# 单台某一台还在运行sls,再次运行sls输出
{'return': [
    {'minion-1': ['The function "state.sls" is running as PID 5657 and was started at 2019, May 15 14:40:08.624416 with jid 20190515144008624416']}]}

# 多台某一台还在运行sls,再次运行sls输出
{'return': [
    {'minion-1':
         {'file_|-lemon_|-/opt/devops/edi-express-1.3.0.war_|-managed':
              {'comment': 'File /opt/devops/edi-express-1.3.0.war is in the correct state', 'pchanges': {}, 'name': '/opt/devops/edi-express-1.3.0.war', 'start_time': '09:00:42.781066',
               'result': True, 'duration': 934.122, '__run_num__': 0, '__sls__': 'devops-server', 'changes': {},
               '__id__': 'lemon'},
          'service_|-web_service_|-httpd_|-running':
              {'comment': 'The service httpd is already running', 'name': 'httpd', 'start_time': '09:00:44.151209',
               'result': True, 'duration': 33.432, '__run_num__': 2, '__sls__': 'devops-server', 'changes': {},
               '__id__': 'web_service'},
          'cmd_|-finally_|-sleep 10_|-run':
              {'comment': 'Command "sleep 10" run', 'name': 'sleep 10', 'start_time': '09:00:44.198474',
               'result': True, 'duration': 10008.931, '__run_num__': 4, '__sls__': 'devops-server', 'changes': {'pid': 5940, 'retcode': 0, 'stderr': '', 'stdout': ''},
               '__id__': 'finally'},
          'http_|-alert_code_|-http://192.168.33.20:8418/api/deploy/v1/deploy/ba74e384513f4f63b6643727444a8172/webhook/_|-query':
              {'comment': 'Status 200 was found, as specified.', 'name': 'http://192.168.33.20:8418/api/deploy/v1/deploy/ba74e384513f4f63b6643727444a8172/webhook/', 'data': {'body': '"lemon"', 'status': 200, 'text': '"lemon"'}, 'start_time': '09:00:43.716306',
               'result': True, 'duration': 16.551, '__run_num__': 1, '__sls__': 'devops-server', 'changes': {},
               '__id__': 'alert_code'},
          'http_|-alert_finally_|-http://192.168.33.20:8418/api/deploy/v1/deploy/ba74e384513f4f63b6643727444a8172/webhook/_|-query':
              {'comment': 'Status 200 was found, as specified.', 'name': 'http://192.168.33.20:8418/api/deploy/v1/deploy/ba74e384513f4f63b6643727444a8172/webhook/', 'data': {'body': '"lemon"', 'status': 200, 'text': '"lemon"'},
               'start_time': '09:00:54.208149', 'result': True, 'duration': 11.609, '__run_num__': 5, '__sls__': 'devops-server', 'changes': {}, '__id__': 'alert_finally'},
          'http_|-alert_web_|-http://192.168.33.20:8418/api/deploy/v1/deploy/ba74e384513f4f63b6643727444a8172/webhook/_|-query':
              {'comment': 'Status 200 was found, as specified.', 'name': 'http://192.168.33.20:8418/api/deploy/v1/deploy/ba74e384513f4f63b6643727444a8172/webhook/', 'data': {'body': '"lemon"', 'status': 200, 'text': '"lemon"'}, 'start_time': '09:00:44.185612',
               'result': True, 'duration': 11.105, '__run_num__': 3, '__sls__': 'devops-server', 'changes': {},
               '__id__': 'alert_web'}},
     'devops': ['The function "state.sls" is running as PID 598 and was started at 2019, May 15 16:00:41.396583 with jid 20190515160041396583']}]}

# 单台不存在minion
{'return': [{}]}
# 多台其中有不在的minion
a={'return': [
    {'devops': {'file_|-lemon_|-/opt/devops/edi-express-1.3.0.war_|-managed':
                    {'comment': 'File /opt/devops/edi-express-1.3.0.war updated', 'pchanges': {}, 'name': '/opt/devops/edi-express-1.3.0.war', 'start_time': '08:53:09.466476',
                     'result': True, 'duration': 2890.885, '__run_num__': 0, '__sls__': 'devops-server', 'changes': {'diff': 'Replace binary file'},
                     '__id__': 'lemon'},
            'service_|-web_service_|-httpd_|-running':
                {'comment': 'The service httpd is already running', 'name': 'httpd', 'start_time': '08:53:13.242459',
                    'result': True, 'duration': 105.314, '__run_num__': 2, '__sls__': 'devops-server', 'changes': {},
                     '__id__': 'web_service'},
            'cmd_|-finally_|-sleep 10_|-run':
                {'comment': 'Command "sleep 10" run', 'name': 'sleep 10', 'start_time': '08:53:13.367637',
                 'result': True, 'duration': 10031.501, '__run_num__': 4, '__sls__': 'devops-server', 'changes': {'pid': 11342, 'retcode': 0, 'stderr': '', 'stdout': ''},
                 '__id__': 'finally'},
                'http_|-alert_code_|-http://192.168.33.20:8418/api/deploy/v1/deploy/ba74e384513f4f63b6643727444a8172/webhook/_|-query':
                    {'comment': 'Status 200 was found, as specified.', 'name': 'http://192.168.33.20:8418/api/deploy/v1/deploy/ba74e384513f4f63b6643727444a8172/webhook/', 'data': {'body': '"lemon"', 'status': 200, 'text': '"lemon"'}, 'start_time': '08:53:12.359145',
                     'result': True, 'duration': 29.033, '__run_num__': 1, '__sls__': 'devops-server', 'changes': {},
                     '__id__': 'alert_code'},
                'http_|-alert_finally_|-http://192.168.33.20:8418/api/deploy/v1/deploy/ba74e384513f4f63b6643727444a8172/webhook/_|-query':
                    {'comment': 'Status 200 was found, as specified.', 'name': 'http://192.168.33.20:8418/api/deploy/v1/deploy/ba74e384513f4f63b6643727444a8172/webhook/', 'data': {'body': '"lemon"', 'status': 200, 'text': '"lemon"'}, 'start_time': '08:53:23.399680',
                     'result': True, 'duration': 14.531, '__run_num__': 5, '__sls__': 'devops-server', 'changes': {},
                     '__id__': 'alert_finally'},
                'http_|-alert_web_|-http://192.168.33.20:8418/api/deploy/v1/deploy/ba74e384513f4f63b6643727444a8172/webhook/_|-query':
                    {'comment': 'Status 200 was found, as specified.', 'name': 'http://192.168.33.20:8418/api/deploy/v1/deploy/ba74e384513f4f63b6643727444a8172/webhook/', 'data': {'body': '"lemon"', 'status': 200, 'text': '"lemon"'}, 'start_time': '08:53:13.348341',
                     'result': True, 'duration': 10.864, '__run_num__': 3, '__sls__': 'devops-server', 'changes': {},
                     '__id__': 'alert_web'}},
     'minion-22': 'Minion did not return. [No response]'}]}

# import requests
# session = requests.Session()
#
#
# data =  {'os_username': 'singo', 'os_password': 'nj532680'}
# url = 'http://doc.ops.com/login.action'
# r = session.post(url, data=data)
# print(session.cookies)
{'return': [
    {'hz01-dev-ops-akama-01':
         {'archive_|-extract_app_|-/var/www/html_|-extracted':
              {'comment': 'salt://packages/devops-web.tar.gz extracted to /var/www/html/', 'name': '/var/www/html', 'start_time': '14:17:13.857030',
               'result': True, 'duration': 766.979, '__run_num__': 0, '__sls__': 'devops-web', 'changes': {'updated ownership': True, 'extracted_files': 'no tar output so far'}, '__id__': 'extract_app'},
          'http_|-alert_code_|-http://172.16.102.28:8418/api/deploy/v1/deploy/b200965b-5f92-499b-86fc-bd24511e9ac2/webhook/_|-query':
              {'comment': 'The following requisites were not found:\n                   require:\n                       cmd: extract_app\n', 'start_time': '14:17:14.627225',
               'result': False, 'duration': 0.045, '__run_num__': 1, '__sls__': 'devops-web', 'changes': {}},
          'cmd_|-finally_|-echo successful_|-run':
              {'comment': 'The following requisites were not found:\n                   require:\n                       cmd: extract_app\n', 'start_time': '14:17:14.629778',
               'result': False, 'duration': 0.046, '__run_num__': 2, '__sls__': 'devops-web', 'changes': {}},
          'http_|-alert_finally_|-http://172.16.102.28:8418/api/deploy/v1/deploy/b200965b-5f92-499b-86fc-bd24511e9ac2/webhook/_|-query':
              {'comment': 'One or more requisite failed: devops-web.finally', 'start_time': '14:17:14.630549',
               'result': False, 'duration': 0.04, '__run_num__': 3, '__sls__': 'devops-web', 'changes': {}}}}]}
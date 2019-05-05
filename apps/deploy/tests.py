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

# import jenkins
# from requests.exceptions import ConnectionError
#
#
#
# try:
#     server = jenkins.Jenkins("http://cainanjie:119c8e97980559a91210458a8a9e8864f31@ci.ops.com")
#
#     # print(server.get_all_jobs())
# except ConnectionError:
#     print('无法连接jenkins')
# except jenkins.JenkinsException:
#     print('====')



try:
    raise Exception('赵永强曹尼玛')
except Exception as e:
    print(e)


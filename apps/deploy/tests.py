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


import jenkins
from requests.exceptions import ConnectionError



try:
    server = jenkins.Jenkins("http://cainanjie:119c8e97980559a91210458a8a9e8864f31@ci.ops.com")

    # print(server.get_all_jobs())
except ConnectionError:
    print('无法连接jenkins')
except jenkins.JenkinsException:
    print('====')

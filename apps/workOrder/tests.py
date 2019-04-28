from ldap3 import Connection,Server,ALL,SUBTREE,MODIFY_REPLACE,LEVEL, BASE
import time

try:
    server = Server(host='172.16.102.18:389',
                    use_ssl=False,
                    connect_timeout=5)
    conn = Connection(server,
                   user='cn=root,dc=ztyc,dc=net',
                   password='ztyc1234', auto_bind=True)

    # conn.search('dc=ztyc,dc=net','(objectclass=person)')
    # conn.search('dc=ztyc,dc=net','(objectclass=dcObject)')
    conn.search(search_base='dc=ztyc,dc=net',
                search_filter='(objectClass=top)',
                search_scope=LEVEL
                )
    print(len(conn.entries))
    print(conn.entries)

    # conn.add('cn=zhaoguocai,ou=people,dc=ztyc,dc=net',
    #          attributes={'objectClass':  ['shadowAccount', 'person', 'organizationalPerson', 'inetOrgPerson'],
    #                      'sn': 'cai', 'givenName': 'zhao', 'displayName': '赵国才',
    #                      'uid': 'zhaoguocai', 'userPassword':'hello1234',
    #                      'mobile':'181586854555', 'mail': 'zgc@ztocwst.com', 'postalAddress': 'hangzhou'})

    # conn.modify('cn=zhaoguocai,ou=people,dc=ztyc,dc=net',
    #             {'displayName': [(MODIFY_REPLACE, ['赵国才'])]}
    # )
    # print(conn.result)

    # conn.search(search_base='ou=people,dc=ztyc,dc=net',
    #             search_filter='(uid=zhaoguocai)',
    #             attributes=['sn', 'givenName', 'displayName', 'uid',
    #                         'userPassword', 'mobile', 'mail', 'postalAddress']
    #             )
    # print(conn.entries[0].entry_to_json())
except Exception as e:
    print('======')
    print(e)




{'biosversion': 'VirtualBox',
 'kernel': 'Linux',
 'domain': '',
 'uid': 0, 'zmqversion': '3.2.5',
 'kernelrelease': '3.10.0-327.4.5.el7.x86_64',
 'selinux': {'enforced': 'Disabled', 'enabled': False},
 'serialnumber': '0', 'pid': 3839,
 'ip_interfaces': {'lo': ['127.0.0.1', '::1'],
                   'enp0s3': ['10.0.2.15', 'fe80::a00:27ff:fe6c:3e95'],
                   'enp0s8': ['192.168.33.20', 'fe80::a00:27ff:feaf:7437']},
 'groupname': 'root', 'fqdn_ip6': [],
 'mem_total': 237, 'saltversioninfo': [2018, 3, 3, 0],
 'zfs_support': False, 'SSDs': [], 'mdadm': [],
 'id': 'devops', 'osrelease': '7.2.1511',
 'ps': 'ps -efHww',
 'systemd': {'version': '219',
             'features': '+PAM +AUDIT +SELINUX +IMA -APPARMOR +SMACK +SYSVINIT +UTMP +LIBCRYPTSETUP +GCRYPT +GNUTLS +ACL +XZ +LZ4 -SECCOMP +BLKID +ELFUTILS +KMOD +IDN'},
 'fqdn': 'devops', 'ip_gw': True,
 'ip6_interfaces': {'lo': ['::1'], 'enp0s3': ['fe80::a00:27ff:fe6c:3e95'],
                    'enp0s8': ['fe80::a00:27ff:feaf:7437']},
 'num_cpus': 2,
 'hwaddr_interfaces': {
     'lo': '00:00:00:00:00:00',
     'enp0s3': '08:00:27:6c:3e:95',
     'enp0s8': '08:00:27:af:74:37'},
 'osfullname': 'CentOS Linux',
 'ip4_interfaces': {'lo': ['127.0.0.1'], 'enp0s3': ['10.0.2.15'],
                    'enp0s8': ['192.168.33.20']},
 'init': 'systemd', 'gid': 0,
 'master': '10.0.2.15',
 'ipv4': ['10.0.2.15', '127.0.0.1', '192.168.33.20'],
 'dns': {'domain': '', 'sortlist': [],
         'nameservers': ['10.0.2.3'],
         'ip4_nameservers': ['10.0.2.3'],
         'search': [], 'ip6_nameservers': [], 'options': []},
 'ipv6': ['::1', 'fe80::a00:27ff:fe6c:3e95', 'fe80::a00:27ff:feaf:7437'],
 'virtual': 'VirtualBox', 'cpu_flags': ['fpu', 'vme', 'de', 'pse', 'tsc', 'msr', 'pae', 'mce', 'cx8', 'apic', 'sep', 'mtrr', 'pge', 'mca', 'cmov', 'pat', 'pse36', 'clflush', 'mmx', 'fxsr', 'sse', 'sse2', 'ht', 'syscall', 'nx', 'rdtscp', 'lm', 'constant_tsc', 'rep_good', 'nopl', 'xtopology', 'nonstop_tsc', 'pni', 'pclmulqdq', 'ssse3', 'cx16', 'pcid', 'sse4_1', 'sse4_2', 'movbe', 'popcnt', 'aes', 'xsave', 'avx', 'rdrand', 'lahf_lm', 'abm', '3dnowprefetch', 'fsgsbase', 'avx2', 'invpcid', 'rdseed', 'clflushopt'], 'localhost': 'devops', 'lsb_distrib_id': 'CentOS Linux',
 'username': 'root', 'fqdn_ip4': ['127.0.0.1'],
 'shell': '/bin/sh', 'nodename': 'devops',
 'saltversion': '2018.3.3', 'ip6_gw': False,
 'pythonpath': ['/usr/bin', '/usr/lib64/python27.zip', '/usr/lib64/python2.7', '/usr/lib64/python2.7/plat-linux2', '/usr/lib64/python2.7/lib-tk', '/usr/lib64/python2.7/lib-old', '/usr/lib64/python2.7/lib-dynload', '/usr/lib64/python2.7/site-packages', '/usr/lib/python2.7/site-packages'],
 'server_id': 1360107821,
 'saltpath': '/usr/lib/python2.7/site-packages/salt',
 'zfs_feature_flags': False, 'osmajorrelease': 7,
 'swap_total': 999, 'os_family': 'RedHat',
 'oscodename': 'CentOS Linux 7 (Core)',
 'osfinger': 'CentOS Linux-7', 'pythonversion': [2, 7, 5, 'final', 0],
 'manufacturer': 'innotek GmbH',
 'mygrain': 'grain ttest value',
 'ip4_gw': '10.0.2.2', 'num_gpus': 1,
 'kernelversion': '#1 SMP Mon Jan 25 22:07:14 UTC 2016',
 'host': 'devops',
 'disks': ['sda', 'dm-0', 'dm-1'],
 'cpu_model': 'Intel(R) Core(TM) i5-8259U CPU @ 2.30GHz',
 'uuid': '9d20bd59-85b4-47d0-83bb-6d9fac6cbba3',
 'biosreleasedate': '12/01/2006',
 'productname': 'VirtualBox',
 'osarch': 'x86_64',
 'cpuarch': 'x86_64',
 'lsb_distrib_codename': 'CentOS Linux 7 (Core)',
 'osrelease_info': [7, 2, 1511], 'locale_info': {'detectedencoding': 'UTF-8', 'defaultlanguage':
    'en_GB', 'defaultencoding': 'UTF-8'},
 'gpus': [{'model': 'VirtualBox Graphics Adapter', 'vendor': 'unknown'}],
 'path': '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin',
 'machine_id': 'e147b422673549a3b4fda77127bd4bcd',
 'os': 'CentOS', 'pythonexecutable': '/usr/bin/python', 'code': 200}


{'return': [{'hz01-dev-ops-akama-01': {'biosversion': '6.00', 'kernel': 'Linux', 'domain': 'test.ops.com', 'uid': 0, 'zmqversion': '4.2.5', 'kernelrelease': '4.15.0-46-generic', 'pythonpath': ['/usr/lib/python2.7/dist-packages/git/ext/gitdb', '/usr/bin', '/usr/lib/python2.7', '/usr/lib/python2.7/plat-x86_64-linux-gnu', '/usr/lib/python2.7/lib-tk', '/usr/lib/python2.7/lib-old', '/usr/lib/python2.7/lib-dynload', '/usr/local/lib/python2.7/dist-packages', '/usr/lib/python2.7/dist-packages', '/usr/lib/python2.7/dist-packages/gitdb/ext/smmap'], 'serialnumber': 'VMware-56 4d 22 19 d6 ed 81 99-7a 82 81 f7 a4 89 b4 c1', 'pid': 13522, 'fqdns': [], 'ip_interfaces': {'lo': ['127.0.0.1', '::1'], 'ens160': ['172.16.102.28', 'fe80::eaa1:61ed:b9c3:dacd']}, 'groupname': 'root', 'fqdn_ip6': [], 'mem_total': 16040, 'saltversioninfo': [2019, 2, 0, 0], 'zfs_support': False, 'SSDs': [], 'mdadm': [], 'id': 'hz01-dev-ops-akama-01', 'manufacturer': 'VMware, Inc.', 'osrelease': '18.04', 'ps': 'ps -efHww', 'systemd': {'version': '237', 'features': '+PAM +AUDIT +SELINUX +IMA +APPARMOR +SMACK +SYSVINIT +UTMP +LIBCRYPTSETUP +GCRYPT +GNUTLS +ACL +XZ +LZ4 +SECCOMP +BLKID +ELFUTILS +KMOD -IDN2 +IDN -PCRE2 default-hierarchy=hybrid'}, 'fqdn': 'akama.test.ops.com', 'ip_gw': True, 'ip6_interfaces': {'lo': ['::1'], 'ens160': ['fe80::eaa1:61ed:b9c3:dacd']}, 'num_cpus': 8, 'hwaddr_interfaces': {'lo': '00:00:00:00:00:00', 'ens160': '00:0c:29:89:b4:c1'}, 'osfullname': 'Ubuntu', 'ip4_interfaces': {'lo': ['127.0.0.1'], 'ens160': ['172.16.102.28']}, 'init': 'systemd', 'gid': 0, 'master': 'salt', 'ipv4': ['127.0.0.1', '172.16.102.28'], 'dns': {'domain': '', 'sortlist': [], 'nameservers': ['127.0.0.53'], 'ip4_nameservers': ['127.0.0.53'], 'search': [], 'ip6_nameservers': [], 'options': ['edns0']}, 'ipv6': ['::1', 'fe80::eaa1:61ed:b9c3:dacd'], 'cpu_flags': ['fpu', 'vme', 'de', 'pse', 'tsc', 'msr', 'pae', 'mce', 'cx8', 'apic', 'sep', 'mtrr', 'pge', 'mca', 'cmov', 'pat', 'pse36', 'clflush', 'dts', 'mmx', 'fxsr', 'sse', 'sse2', 'ss', 'syscall', 'nx', 'rdtscp', 'lm', 'constant_tsc', 'arch_perfmon', 'pebs', 'bts', 'nopl', 'xtopology', 'tsc_reliable', 'nonstop_tsc', 'cpuid', 'pni', 'pclmulqdq', 'ssse3', 'cx16', 'pcid', 'sse4_1', 'sse4_2', 'x2apic', 'popcnt', 'tsc_deadline_timer', 'aes', 'xsave', 'avx', 'hypervisor', 'lahf_lm', 'pti', 'ssbd', 'ibrs', 'ibpb', 'stibp', 'tsc_adjust', 'arat', 'flush_l1d', 'arch_capabilities'], 'localhost': 'hz01-dev-ops-akama-01', 'lsb_distrib_id': 'Ubuntu', 'username': 'root', 'fqdn_ip4': ['172.16.102.28'], 'shell': '/bin/sh', 'nodename': 'hz01-dev-ops-akama-01', 'saltversion': '2019.2.0', 'lsb_distrib_release': '18.04', 'ip6_gw': False, 'server_id': 214569799, 'saltpath': '/usr/lib/python2.7/dist-packages/salt', 'zfs_feature_flags': False, 'osmajorrelease': 18, 'swap_total': 2047, 'os_family': 'Debian', 'oscodename': 'bionic', 'osfinger': 'Ubuntu-18.04', 'pythonversion': [2, 7, 15, 'candidate', 1], 'lsb_distrib_description': 'Ubuntu 18.04.2 LTS', 'kernelversion': '#49-Ubuntu SMP Wed Feb 6 09:33:07 UTC 2019', 'ip4_gw': '172.16.102.1', 'num_gpus': 1, 'virtual': 'VMware', 'host': 'akama', 'disks': ['loop1', 'loop19', 'loop17', 'loop8', 'loop25', 'loop15', 'loop6', 'loop23', 'loop13', 'loop4', 'loop21', 'loop11', 'sr0', 'loop2', 'loop0', 'loop18', 'loop9', 'loop16', 'loop7', 'loop24', 'sda', 'loop14', 'loop5', 'loop22', 'loop12', 'loop3', 'loop20', 'loop10'], 'cpu_model': 'Intel(R) Xeon(R) CPU E5-2670 0 @ 2.60GHz', 'uuid': '19224d56-edd6-9981-7a82-81f7a489b4c1', 'biosreleasedate': '04/05/2016', 'productname': 'VMware Virtual Platform', 'osarch': 'amd64', 'cpuarch': 'x86_64', 'lsb_distrib_codename': 'bionic', 'osrelease_info': [18, 4], 'locale_info': {'timezone': 'CST', 'detectedencoding': 'UTF-8', 'defaultlanguage': 'en_US', 'defaultencoding': 'UTF-8'}, 'gpus': [{'model': 'SVGA II Adapter', 'vendor': 'vmware'}], 'path': '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin', 'machine_id': '327f66f15765446683dff95f9aff43a5', 'os': 'Ubuntu', 'pythonexecutable': '/usr/bin/python2'}}]}

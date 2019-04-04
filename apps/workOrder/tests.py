from ldap3 import Connection,Server,ALL,SUBTREE,MODIFY_REPLACE,SUBTREE,LEVEL, BASE

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
    # search_scope = SUBTREE
    # print(conn.entries[0].entry_to_json())
    print(len(conn.entries))
    print(conn.entries)
except Exception as e:
    print('======')
    print(e)

# import time
# while True:
#     conn.search(search_base='dc=ztyc,dc=net',
#                 search_filter='(objectClass=top)',
#                 search_scope=LEVEL
#                 )
#     print(conn.entries)
#     print(len(conn.entries))
#     print((time.time()))
#     time.sleep(600)




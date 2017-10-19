# master_python
python codes from master
```bash
# Setup the HOBBIT Platform user
/opt/virtuoso/bin/isql 1111 dba dba exec="DB.DBA.USER_CREATE ('HobbitPlatform', 'Password'); GRANT SPARQL_UPDATE TO "HobbitPlatform";"
...
# Finally, change the 'dba' password
/opt/virtuoso/bin/isql 1111 dba dba exec="user_set_password ('dba', 'Password');"
```
'''bash
test
'''

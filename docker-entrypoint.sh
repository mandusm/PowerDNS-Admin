#!/bin/bash

echo "Configuring APP"
cd $PDNSADMIN_DIR
cp config_template.py config.py
sed "s,BIND_ADDRESS = '127.0.0.1',BIND_ADDRESS = '0.0.0.0',g" -i $PDNSADMIN_DIR/config.py
sed "s,PDNS_STATS_URL = 'http://172.16.214.131:8081/',PDNS_STATS_URL = '$PDNSADMIN_APIURL',g" -i $PDNSADMIN_DIR/config.py
sed "s,PDNS_API_KEY = 'you never know',PDNS_API_KEY = '$PDNSADMIN_APIKEY',g" -i $PDNSADMIN_DIR/config.py
sed "s,SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@192.168.59.103/pdns',SQLALCHEMY_DATABASE_URI = 'mysql://$PDNSADMIN_DBUSER:$PDNSADMIN_DBPASS@$PDNSADMIN_DBHOST/$PDNSADMIN_DBNAME',g" -i $PDNSADMIN_DIR/config.py
sed "s,PORT = 9393,PORT = $PDNSADMIN_PORT,g" -i $PDNSADMIN_DIR/config.py

echo "Starting APP"
/opt/PowerDNS-Admin/run.py

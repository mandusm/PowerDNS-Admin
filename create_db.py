#!flask/bin/python
from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO
from app import db
from app.models import Role, Setting
import os.path
db.create_all()
# create initial user roles and turn off maintenance mode
admin_role = Role('Administrator', 'Administrator')
user_role = Role('User', 'User')
maintenance_setting = Setting('maintenance', 'False')
fullscreen_layout_setting = Setting('fullscreen_layout', 'True')
record_helper_setting = Setting('record_helper', 'True')
default_table_size_setting = Setting('default_record_table_size', '15')
db.session.add(admin_role)
db.session.add(user_role)
db.session.add(maintenance_setting)
db.session.add(fullscreen_layout_setting)
db.session.add(record_helper_setting)
db.session.add(default_table_size_setting)
db.session.commit()
if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
    api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
else:
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, api.version(SQLALCHEMY_MIGRATE_REPO))

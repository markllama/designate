# Copyright 2014 Hewlett-Packard Development Company, L.P.
#
# Author: Kiall Mac Innes <kiall@hp.com>
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
import os

from migrate.versioning import api as versioning_api
from oslo.config import cfg
from oslo.db.sqlalchemy.migration_cli import manager as migration_manager

from designate.openstack.common import log as logging
from designate.manage import base


LOG = logging.getLogger(__name__)

REPOSITORY = os.path.abspath(os.path.join(os.path.dirname(__file__), '..',
                                          'backend', 'impl_powerdns',
                                          'migrate_repo'))
cfg.CONF.import_opt('connection', 'designate.backend.impl_powerdns_mdns',
                    group='backend:powerdns_mdns')

CONF = cfg.CONF


def get_manager():
    migration_config = {
        'migration_repo_path': REPOSITORY,
        'db_url': CONF['backend:powerdns_mdns'].connection}
    return migration_manager.MigrationManager(migration_config)


class DatabaseCommands(base.Commands):
    def version(self):
        current = get_manager().version()
        latest = versioning_api.version(repository=REPOSITORY).value
        print("Current: %s Latest: %s" % (current, latest))

    def sync(self):
        get_manager().upgrade(None)

    @base.args('revision', nargs='?')
    def upgrade(self, revision):
        get_manager().upgrade(revision)

    @base.args('revision', nargs='?')
    def downgrade(self, revision):
        get_manager().downgrade(revision)

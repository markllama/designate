# Copyright 2015 Hewlett-Packard Development Company, L.P.
#
# Author: Endre Karlson <endre.karlson@hpe.com>
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
from oslo_config import cfg

PRODUCER_GROUP = cfg.OptGroup(
    name='service:producer',
    title='Configuration for Producer Service'
)

ZONE_MANAGER_GROUP = cfg.OptGroup(
    name='service:zone_manager',
    title='Configuration for Zone Manager Service'
)

PRODUCER_TASK_DELAYED_NOTIFY_GROUP = cfg.OptGroup(
    name='producer_task:delayed_notify',
    title='Configuration for Producer Task: Delayed Notify'
)

PRODUCER_TASK_PERIODIC_EXISTS_GROUP = cfg.OptGroup(
    name='producer_task:periodic_exists',
    title='Configuration for Producer Task: Periodic Exists'
)

PRODUCER_TASK_PERIODIC_SECONDARY_REFRESH_GROUP = cfg.OptGroup(
    name='producer_task:periodic_secondary_refresh',
    title='Configuration for Producer Task: Periodic Secondary Refresh'
)

PRODUCER_TASK_WORKER_PERIODIC_RECOVERY_GROUP = cfg.OptGroup(
    name='producer_task:worker_periodic_recovery',
    title='Configuration for Producer Task: Worker Periodic Recovery'
)

PRODUCER_TASK_ZONE_PURGE_GROUP = cfg.OptGroup(
    name='producer_task:zone_purge',
    title='Configuration for Producer Task: Zone Purge'
)

PRODUCER_OPTS = [
    cfg.IntOpt('workers',
               help='Number of Producer worker processes to spawn'),
    cfg.IntOpt('threads', default=1000,
               help='Number of Producer greenthreads to spawn'),
    cfg.ListOpt('enabled_tasks',
                help='Enabled tasks to run'),
    cfg.StrOpt('storage_driver', default='sqlalchemy',
               help='The storage driver to use'),
    cfg.BoolOpt('export_synchronous', default=True,
                help='Whether to allow synchronous zone exports',
                deprecated_for_removal=True,
                deprecated_reason='Migrated to designate-worker'),
    cfg.StrOpt('topic', default='producer',
               help='RPC topic name for producer'),
]

ZONE_MANAGER_OPTS = [
    cfg.IntOpt('workers',
               help='Number of Zone Manager worker processes to spawn',
               deprecated_for_removal=True,
               deprecated_reason='Migrated to designate-worker'),
    cfg.IntOpt('threads', default=1000,
               help='Number of Zone Manager greenthreads to spawn',
               deprecated_for_removal=True,
               deprecated_reason='Migrated to designate-worker'),
    cfg.ListOpt('enabled_tasks',
                help='Enabled tasks to run',
                deprecated_for_removal=True,
                deprecated_reason='Migrated to designate-worker'),
    cfg.StrOpt('storage_driver', default='sqlalchemy',
               help='The storage driver to use',
               deprecated_for_removal=True,
               deprecated_reason='Migrated to designate-worker'),
    cfg.BoolOpt('export_synchronous', default=True,
                help='Whether to allow synchronous zone exports',
                deprecated_for_removal=True,
                deprecated_reason='Migrated to designate-worker'),
]

PRODUCER_TASK_DELAYED_NOTIFY_OPTS = [
    cfg.IntOpt('interval', default=5,
               help='Run interval in seconds'),
    cfg.IntOpt('per_page', default=100,
               help='Default amount of results returned per page'),
    cfg.IntOpt('batch_size', default=100,
               help='How many zones to receive NOTIFY on each run'),
]

PRODUCER_TASK_PERIODIC_EXISTS_OPTS = [
    cfg.IntOpt('interval', default=3600,
               help='Run interval in seconds'),
    cfg.IntOpt('per_page', default=100,
               help='Default amount of results returned per page'),
]

PRODUCER_TASK_PERIODIC_SECONDARY_REFRESH_OPTS = [
    cfg.IntOpt('interval', default=3600,
               help='Run interval in seconds'),
    cfg.IntOpt('per_page', default=100,
               help='Default amount of results returned per page'),
]

PRODUCER_TASK_WORKER_PERIODIC_RECOVERY_OPTS = [
    cfg.IntOpt('interval', default=120,
               help='Run interval in seconds'),
    cfg.IntOpt('per_page', default=100,
               help='Default amount of results returned per page'),
]

PRODUCER_TASK_ZONE_PURGE_OPTS = [
    cfg.IntOpt('interval', default=3600,
               help='Run interval in seconds'),
    cfg.IntOpt('per_page', default=100,
               help='Default amount of results returned per page'),
    cfg.IntOpt('time_threshold', default=604800,
               help='How old deleted zones should be (deleted_at) to be '
                    'purged, in seconds'),
    cfg.IntOpt('batch_size', default=100,
               help='How many zones to be purged on each run'),
]


def register_opts(conf):
    conf.register_group(PRODUCER_GROUP)
    conf.register_opts(PRODUCER_OPTS, group=PRODUCER_GROUP)
    conf.register_group(ZONE_MANAGER_GROUP)
    conf.register_opts(ZONE_MANAGER_OPTS, group=ZONE_MANAGER_GROUP)
    conf.register_group(PRODUCER_TASK_DELAYED_NOTIFY_GROUP)
    conf.register_opts(PRODUCER_TASK_DELAYED_NOTIFY_OPTS,
                       group=PRODUCER_TASK_DELAYED_NOTIFY_GROUP)
    conf.register_group(PRODUCER_TASK_PERIODIC_EXISTS_GROUP)
    conf.register_opts(PRODUCER_TASK_PERIODIC_EXISTS_OPTS,
                       group=PRODUCER_TASK_PERIODIC_EXISTS_GROUP)
    conf.register_group(PRODUCER_TASK_PERIODIC_SECONDARY_REFRESH_GROUP)
    conf.register_opts(PRODUCER_TASK_PERIODIC_SECONDARY_REFRESH_OPTS,
                       group=PRODUCER_TASK_PERIODIC_SECONDARY_REFRESH_GROUP)
    conf.register_group(PRODUCER_TASK_WORKER_PERIODIC_RECOVERY_GROUP)
    conf.register_opts(PRODUCER_TASK_WORKER_PERIODIC_RECOVERY_OPTS,
                       group=PRODUCER_TASK_WORKER_PERIODIC_RECOVERY_GROUP)
    conf.register_group(PRODUCER_TASK_ZONE_PURGE_GROUP)
    conf.register_opts(PRODUCER_TASK_ZONE_PURGE_OPTS,
                       group=PRODUCER_TASK_ZONE_PURGE_GROUP)


def list_opts():
    return {
        PRODUCER_GROUP: PRODUCER_OPTS,
        ZONE_MANAGER_GROUP: ZONE_MANAGER_OPTS,
        PRODUCER_TASK_DELAYED_NOTIFY_GROUP:
            PRODUCER_TASK_DELAYED_NOTIFY_OPTS,
        PRODUCER_TASK_PERIODIC_EXISTS_GROUP:
            PRODUCER_TASK_PERIODIC_EXISTS_OPTS,
        PRODUCER_TASK_PERIODIC_SECONDARY_REFRESH_GROUP:
            PRODUCER_TASK_PERIODIC_SECONDARY_REFRESH_OPTS,
        PRODUCER_TASK_WORKER_PERIODIC_RECOVERY_GROUP:
            PRODUCER_TASK_WORKER_PERIODIC_RECOVERY_OPTS,
        PRODUCER_TASK_ZONE_PURGE_GROUP: PRODUCER_TASK_ZONE_PURGE_OPTS,
    }

import os

PUPPETDB_HOST = 'puppetdb.local'
PUPPETDB_PORT = 8081
PUPPETDB_SSL_VERIFY = '/etc/puppetlabs/puppet/ssl/certs/ca.pem'
PUPPETDB_KEY = '/etc/puppetlabs/puppet/ssl/private_keys/puppetboard.local.pem'
PUPPETDB_CERT = '/etc/puppetlabs/puppet/ssl/certs/puppetboard.local.pem'
PUPPETDB_TIMEOUT = 20
DEFAULT_ENVIRONMENT = 'production'
SECRET_KEY = 'VAYidkkpI0+xmWBR6QSUFnsgIvWJHXG4'
DEV_LISTEN_HOST = '127.0.0.1'
DEV_LISTEN_PORT = 5000
DEV_COFFEE_LOCATION = 'coffee'
UNRESPONSIVE_HOURS = 2
ENABLE_QUERY = True
LOCALISE_TIMESTAMP = True
LOGLEVEL = 'info'
NORMAL_TABLE_COUNT = 100
LITTLE_TABLE_COUNT = 10
TABLE_COUNT_SELECTOR = [10, 20, 50, 100, 500]
OFFLINE_MODE = False
ENABLE_CATALOG = False
OVERVIEW_FILTER = None
GRAPH_TYPE = 'pie'
GRAPH_FACTS = ['architecture',
               'clientversion',
               'domain',
               'lsbcodename',
               'lsbdistcodename',
               'lsbdistid',
               'lsbdistrelease',
               'lsbmajdistrelease',
               'netmask',
               'osfamily',
               'puppetversion',
               'processorcount']
INVENTORY_FACTS = [('Hostname', 'fqdn'),
                   ('IP Address', 'ipaddress'),
                   ('OS', 'lsbdistdescription'),
                   ('Architecture', 'hardwaremodel'),
                   ('Kernel Version', 'kernelrelease'),
                   ('Puppet Version', 'puppetversion'), ]
REFRESH_RATE = 30
DAILY_REPORTS_CHART_ENABLED = True
DAILY_REPORTS_CHART_DAYS = 8

import os

import urllib.parse as up
from flask_script import Manager
from flask import url_for

from src import api, create_app, dc, configs, admin, elastic_store, mail, security, bp, limiter, redis

config = os.environ.get('PYTH_SRVR')

config = configs.get(config, 'default')

extensions = [dc, mail, api, admin, elastic_store, security, limiter, redis]

app = create_app(__name__, config, blueprints=[bp], extensions=extensions)

manager = Manager(app)
# migrate = Migrate(app, dc)
# manager.add_command('db', MigrateCommand)


@manager.shell
def _shell_context():
    return dict(
        app=app,
        config=config
        )


@manager.command
def list_routes():
    import urllib
    output = []
    for rule in app.url_map.iter_rules():

        options = {}
        for arg in rule.arguments:
            options[arg] = "[{0}]".format(arg)

        methods = ','.join(rule.methods)
        url = url_for(rule.endpoint, **options)
        line = up.unquote("{:50s} {:20s} {}".format(rule.endpoint, methods, url))
        output.append(line)

    for line in sorted(output):
        print(line)

if __name__ == "__main__":
    # app.run(host='0.0.0.0', debug=True)
    manager.run()

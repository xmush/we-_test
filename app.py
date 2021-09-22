from flask import Flask, request
from flask_restful import Resource, Api
import json, logging, sys
from logging.handlers import RotatingFileHandler

from blueprints import app, db


api = Api(app, catch_all_404s=True)

if __name__ == '__main__' :
    
    if len(sys.argv) > 1 :
        db.cli.run()
    # print(len(sys.argv))

    formatter = logging.Formatter("[%(asctime)s]{%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
    log_handler = RotatingFileHandler("%s/%s" % (app.root_path, '../storage/log/app.log'), maxBytes=10000, backupCount=10)
    log_handler.setLevel(logging.INFO)
    log_handler.setFormatter(formatter)
    app.logger.addHandler(log_handler)

    app.run(debug=app.config['DEBUG'], host=app.config['HOST'], port=app.config['PORT'])
    # try :
    #     if sys.argv[1] == 'db' :
    #         # manager.run()
    # except Exception as e :
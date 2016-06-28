VERSION_STR = 'v1.0.0'


from flask import Blueprint
blueprint = Blueprint(VERSION_STR, __name__)


@blueprint.route('/')
def root():
    return VERSION_STR


@blueprint.route('/info')
def info():
    return VERSION_STR + '/info'


from app import app
app.register_blueprint(blueprint, url_prefix='/'+VERSION_STR)
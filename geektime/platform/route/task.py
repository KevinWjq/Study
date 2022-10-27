from flask import Blueprint

task_bp = Blueprint("task", __name__)


@task_bp.route('/task', methods=['POST'])
def task_post():
    ...

import json
from flask import request, abort, Flask
from flask_restplus import Namespace, Resource, fields
from v1.database.models import Task
from mongoengine import DoesNotExist
from celery import Celery
import subprocess

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

tasks = Namespace('v1/tasks', description='Shell background queue')

task_fields = tasks.model('Resource', {
    'cmd': fields.String,
})


@tasks.route('/new_task')
class Tasks(Resource):
    @tasks.expect(task_fields, validate=True)
    def post(self):
        data = request.json
        cmd = data['cmd']
        task_id = Task.objects.count() + 1
        task = Task(task_id= task_id, cmd=cmd, output='').save()
        execute_async_command(cmd,task_id)
        return {'id':task_id}, 200

@tasks.route('/get_output/<id>')
@tasks.response(404, 'Todo not found')
@tasks.param('id', 'The task identifier')
class TaskGet(Resource):
    def get(self, id):
        '''Fetch a given Task'''
        try:
            task = Task.objects.get(task_id=id)
            return json.loads(task.to_json()), 200
        except(DoesNotExist):
            abort(404)
        except:
            abort(500)

@celery.task
def execute_async_command(cmd,task_id):
    '''Background task to execute commands.'''
    result = subprocess.getoutput(cmd)
    task = Task.objects.get(task_id=task_id)
    task.output=result
    task.save()
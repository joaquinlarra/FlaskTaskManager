import json
from flask import abort
from flask_restplus import Namespace, Resource
from v1.database.models import Task
from mongoengine import DoesNotExist

tasks = Namespace('v1/tasks', description='Tasks Manager')


@tasks.route('/new_task')
class TaskCreate(Resource):
    def put(self):
        '''Create a task'''
        tasks = Task.objects.all()
        return json.loads(todos.to_json()), 200


@tasks.route('/get_output/<id>')
@tasks.response(404, 'Todo not found')
@tasks.param('id', 'The task identifier')
class TaskGet(Resource):
    def get(self, id):
        '''Fetch a given Task'''
        try:
            task = Task.objects.get(id=id)
            return json.loads(task.to_json()), 200
        except(DoesNotExist):
            abort(404)
        except:
            abort(500)

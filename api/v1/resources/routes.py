from v1.resources.tasks import tasks


def initialize_routes(api):
    api.add_namespace(tasks)

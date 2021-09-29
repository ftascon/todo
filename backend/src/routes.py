from flask import Blueprint, request, jsonify

from .Infra.taskRepository import TaskRepository

main = Blueprint('main', __name__)

@main.route('/tasks', methods=['POST'])
def taskCreate():
    request_data = request.get_json()
    taskId = TaskRepository.persist(request_data['content'])
    return {"taskId": taskId}, 200

@main.route('/tasks/<taskId>', methods=['GET'])
def taskById(taskId):
    response = TaskRepository.getById(taskId)
    return jsonify(response)


@main.route('/tasks/<taskId>', methods=['PUT'])
def taskEdit(taskId):
    request_data = request.get_json()

    completed = (False, True) [int(request_data['completed']) == 0]

    response = TaskRepository.persist(
        request_data['content'],
        completed,
        taskId
    )
    return {"taskId": response}, 200


@main.route('/tasks/<taskId>', methods=['DELETE'])
def taskDelete(taskId):
    response = TaskRepository.deleteById(taskId)
    return "{}", 200


@main.route('/tasks', methods=['GET'])
def tasksList():
    response = TaskRepository.getAll()
    return jsonify(response)


@main.route('/tasks/complete', methods=['POST'])
def tasksComplete():
    request_data = request.get_json()
    taskId = TaskRepository.complete(
        request_data["id"]
    )
    return {"taskId": taskId}, 200


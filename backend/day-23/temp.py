from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data (list of tasks)

tasks = []

# Route for home page
@app.route('/')
def home():
    return "Welcome to the Task Manager!"

# Route to get all tasks
@app.route('/api/tasks', methods=['GET'])
def get_task():
    return jsonify({'task': tasks}), 200

# Route to create a new task
@app.route('/api/tasks/', methods=['POST'])
def create_task():
    data = request.get_json()
    if 'title' in data:
        task = {'title': data['title']}
        tasks.append(task)
        return jsonify({'message': 'Task created successfully'}, 201)
    else:
        return jsonify({'message': 'Title is required'}, 400)



# Route to update a task
@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    if task_id < len(tasks):
        data = request.get_json()
        if 'title' in data:
            tasks[task_id]['title'] = data['title']
            return jsonify({'message': 'Task updated successfully'})
        else:
            return jsonify({'message': 'Title is required'}, 400)
    else:
        return jsonify({'message': 'Task not found'}, 404)
    

# Route to delete a task
@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    if task_id < len(tasks):
        del tasks[task_id] 
        return jsonify({'message': 'Task deleted successfully'}) 
    else:
        return jsonify({'message': 'Task not found'}, 404)

if __name__ == '__main__':
    app.run()
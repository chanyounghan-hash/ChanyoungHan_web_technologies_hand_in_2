from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

# Helper function to read/write JSON data
def load_data(filename):
    if not os.path.exists(filename):
        return [] if 'todos' in filename else {}
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_data(filename, data):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# Page Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/memo')
def memo_page():
    return render_template('memo.html')

@app.route('/info')
def info_page():
    return render_template('info.html')

# Data Routes for Todos
@app.route('/todos', methods=['GET', 'POST'])
def handle_todos():
    todos = load_data('todos.json')
    if request.method == 'POST':
        new_todo = request.json.get('task')
        if new_todo:
            todos.append(new_todo)
            save_data('todos.json', todos)
        return jsonify(todos)
    return jsonify(todos)

@app.route('/todos/<int:index>', methods=['DELETE'])
def delete_todo(index):
    todos = load_data('todos.json')
    if 0 <= index < len(todos):
        todos.pop(index)
        save_data('todos.json', todos)
    return jsonify(todos)

# Data Routes for Memo
@app.route('/memo-data', methods=['GET', 'POST'])
def handle_memo():
    memo = load_data('memo.json')
    if request.method == 'POST':
        memo['content'] = request.json.get('content', '')
        save_data('memo.json', memo)
        return jsonify({"status": "success", "message": "Saved successfully"})
    return jsonify(memo)

# Data Routes for Info
@app.route('/info-data', methods=['GET', 'POST'])
def handle_info():
    info = load_data('info.json')
    if request.method == 'POST':
        info['name'] = request.json.get('name', info.get('name', ''))
        info['email'] = request.json.get('email', info.get('email', ''))
        save_data('info.json', info)
        return jsonify({"status": "success", "message": "Saved successfully"})
    return jsonify(info)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

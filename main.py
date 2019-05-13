from flask import Flask, render_template, request
from database import connection
from database import todo_list_dao
from datetime import datetime

app = Flask(__name__)

@app.context_processor
def inject_now():
    return {'now' : datetime.today()}
    

@app.route('/')
def index():

    content_list=todo_list_dao.get_todolist()

    html = render_template('index.html', data_list=content_list)
    return html

@app.route('/write_pro', methods=['post'])
def write_pro() :

    element = request.values.get('todoItem')

    todo_list_dao.write_todo(element)

    return '''
            <script>
                alert("저장되었습니다")
                location.href="."
            </script>
           ''' 

@app.route('/delete', methods=['post'])
def delete() :
    
    idx = request.values.get('idx')
    todo_list_dao.delete(idx)
    return '''
            <script>
                alert("삭제되었습니다")
                location.href="."
            </script>
           ''' 

if __name__ == '__main__' :
    app.run(debug=True)


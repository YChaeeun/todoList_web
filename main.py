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

@app.route('/modify', defaults={'idx':1})
@app.route('/modify/<idx>')
def modify(idx) :
    content_list = todo_list_dao.get_todolist()
    modify_content = todo_list_dao.get_modify_content(idx)
    modify_dic = {
        'modify_idx' : idx,
        'modify_content' : modify_content
    }
    html = render_template('modify.html', data_list=content_list, data_dic=modify_dic)
    return html


@app.route('/modify_pro', methods=['post'])
def modify_pro() :
    
    content = request.values.get('modifyItem')
    idx = request.values.get('modifyIdx')
    todo_list_dao.modify(content,idx)

    return '''
            <script>
                alert("수정되었습니다")
                location.href="."
            </script>
           ''' 

if __name__ == '__main__' :
    app.run(debug=True)


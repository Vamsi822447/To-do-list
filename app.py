from flask import *
from flask_sqlalchemy import SQLAlchemy
from flask_scss import Scss
from datetime import datetime
app = Flask(__name__)
app.secret_key = 'dev-key'
Scss(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db = SQLAlchemy(app)
class MyTask(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    content = db.Column(db.String(100),nullable = False)
    complete = db.Column(db.Integer,default=0)
    created = db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"Task{self.id}"
@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        content = request.form['content'].strip()
        if not content:
            flash('Task cannot be empty','error')
            return redirect('/')
        new_task = MyTask(content=content)
        try:
            db.session.add(new_task)
            db.session.commit()
            flash('Task added successfully','success')
            return redirect('/')
        except Exception as e:
            flash('Error in adding the task','error')
            print(f"ERROR:{e}")
            return f"ERROR:{e}"   
    else:
        tasks = MyTask.query.order_by(MyTask.created).all()
        return render_template('index.html',tasks = tasks)         


@app.route('/delete/<int:id>')
def delete(id:int):
    delete_task = MyTask.query.get_or_404(id)
    try:
        db.session.delete(delete_task)
        db.session.commit()
        flash('Task deleted sucessfully','success')
        return redirect('/')
    except Exception as e:
        flash('Error in deleting the task','error')
        return f"ERROR:{e}"    

@app.route('/update/<int:id>',methods=['POST','GET'])
def update(id:int):
    task = MyTask.query.get_or_404(id)
    if request.method == 'POST':
        task.content = request.form['content']
        try:
            db.session.commit()
            flash('Task updated successfully','success')
            return redirect('/')
        except Exception as e:
            flash('Error in updating task')
            return f"ERROR:{e}"     
    else:
        return render_template('update.html',task=task)
   
      

if __name__ == '__main__':
    with app.app_context():
       db.create_all() 
    app.run(debug=True)
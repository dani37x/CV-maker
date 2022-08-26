from project_files import app
from flask import render_template, url_for, redirect, request, session, flash
# from project_files.forms import Informations
# from project_files.database import User
from project_files import db
from project_files.database import Informations
from project_files.functions import file_check
import os




# def index():
#     return render_template('index.html')

@app.route('/' , methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['name'] = request.form['name']
        session['profession'] = request.form['profession']
        session['e_mail'] = request.form['e_mail']
        session['city'] = request.form['city']
        session['birthday'] = request.form['birthday']
        session['phone'] = request.form['phone']
        session['color'] = request.form['color']
        session['second_color'] = request.form['second_color']
        session['info'] = request.form['info']
        session['second_info'] = request.form['second_info']
        file = request.files['file']
        file_name = file.filename
        if file_check( file_name=file_name):
            session['file'] = file_name
            destination = 'C:/projekty/CV/myproject/project_files/static/' + file_name
            session['destination'] = destination
            file.save(destination)     
            return redirect( url_for('page'))
        else:
            flash('[ERROR] SELECT YOUR PHOTO. REMEMBER ABOUT FILE EXTENSION')
            return redirect('/')
    return render_template('login.html')



@app.route('/page', methods=['GET', 'POST'])
def page():
    return render_template('page.html')


@app.route('/more', methods=['GET', 'POST'])
def more():
    if request.method == 'POST':    
        form_content = request.form['form_content']
        content_type = str(request.form.get('membership'))
        if len(form_content) > int(0):
            new_row = Informations( name=form_content, information_type=content_type)
            try:
                db.session.add( new_row)
                db.session.commit()
                return redirect('/more')
            except:
                flash('[ERROR] ROW CAN NOT BE ADDED')
        else:
            flash('[ERROR] EMPTY FIELD. WRITE SOMETHING BEFORE SEND')
            return redirect('/more')   
    else:
        expirences = Informations.query.filter_by(information_type='expirence').all()  
        skills = Informations.query.filter_by(information_type='skill').all()  
        interests = Informations.query.filter_by(information_type='interest').all()  
        languages = Informations.query.filter_by(information_type='language').all()  
        return render_template('more.html', expirences=expirences, skills=skills, interests=interests, languages=languages)
    
@app.route('/logout', methods=['GET', 'POST'])
def logout():
    try:
        db.session.query( Informations).delete()
        db.session.commit()
        file_name = session.get('destination')
        os.remove( file_name)
        for key in list(session.keys()):
            session.pop(key)
        return redirect('/')
    except:
        flash('[ERROR] THERE IS PROBLEM WITH DATA DELETE')
        return redirect('/more')
    
    return render_template('login.html')


@app.route('/delete/<int:id>')
def delete(id):
  row_to_delete = Informations.query.get_or_404(id)
  
  try:
    db.session.delete( row_to_delete)
    db.session.commit()
    return redirect('/more')
  except:
    'Problem with delete'

@app.before_first_request
def before_first_request():
    db.create_all()

@app.errorhandler(404)
def handle_404(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def handle_500(e):
    return render_template('500.html'), 500



#store standard routes for website
from flask import Blueprint, flash, render_template,request

from flask_login import login_required, current_user

views = Blueprint('views',__name__)

@views.route('/',methods=['GET','POST'])
@login_required
def home():
    if request.method == 'POST':
        noteText = request.form.get('note')

        if len(noteText)<1:
            flash('Note is too short',category='error')
        else:
            flash('Note added!',category='success')
            #add note to database
    return render_template("home.html", user=current_user)
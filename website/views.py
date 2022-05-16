#store standard routes for website
from flask import Blueprint, flash, render_template,request,jsonify
import json
from flask_login import login_required, current_user
from .models import User, Note
from . import db

views = Blueprint('views',__name__)

@views.route('/',methods=['GET','POST'])
@login_required
def home():
    if request.method == 'POST':
        noteText = request.form.get('note')

        if len(noteText)<1:
            flash('Note is too short',category='error')
        else:
            
            #add note to database
            new_note = Note(data=noteText, userID = current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!',category='success')
    return render_template("home.html", user=current_user)

@views.route('delete-note', methods=['POST'])
def delete_note():
    data = json.loads(request.data)
    noteId = data['noteID']
    note = Note.query.get(noteId)
    if note:
        if note.userID == current_user.id:
            db.session.delete(note)
            db.session.commit()
    
    return jsonify({})
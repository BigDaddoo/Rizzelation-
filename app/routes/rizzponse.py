# Some of this may not be necessary
from app import app
import mongoengine.errors
from flask import render_template, flash, redirect, url_for
from flask_login import current_user
from app.classes.data import Blog, Comment
from app.classes.forms import BlogForm, CommentForm
from flask_login import login_required
import datetime as dt

@app.route('/rizzponse/new/<rizzponseID>', methods=['GET', 'POST'])
@login_required
def rizzponseNew(rizzponseID):
    rizzponse = Rizzponse.objects.get(id=rizzponseID)
    form = RizzponseForm()
    if form.validate_on_submit():
        newRizzponse = Rizzponse(
            author = current_user.id,
            rizzponse = rizzponseID, 
            commentary = form.content.data 
            #! not sure if we should add more things but ehh
        )
        newRizzponse.save()
        return redirect(url_for('rizzponse',rizzponseID=blogID))
    return render_template('rizzponseform.html',form=form,rizzponse=rizzponse) #! this is weird, might work
#   return render_template('rizzponseform.html',form=form,blog=blog) 






from app import app
import mongoengine.errors
from flask import render_template, flash, redirect, url_for
from flask_login import current_user
from app.classes.data import GrandQuestion, Comment
from app.classes.forms import GrandQuestionForm, CommentForm
from flask_login import login_required
import datetime as dt

@app.route('/grandQuestion/list')
@app.route('/grandQuestions')
@login_required
def grandQuestionList():
    grandQuestions = GrandQuestion.objects()
    return render_template('grandQuestions.html',grandQuestions=grandQuestions)


@app.route('/grandQuestion/<grandQuestionID>')
@login_required
def grandQuestion(grandQuestionID):
    thisGrandQuestion = GrandQuestion.objects.get(id=grandQuestionID) #EVAN
    #theseComments = Comment.objects(grandQuestion=thisGrandQuestion)
    return render_template('grandQuestion.html',grandQuestion=thisGrandQuestion,comments=None)

# TODO add the ability for an administrator to delete blogs. 
@app.route('/grandQuestion/delete/<grandQuestionID>')
@login_required
def grandQuestionDelete(grandQuestionID):
    deleteGrandQuestion = GrandQuestion.objects.get(id=grandQuestionID) #EVAN
    if current_user == deleteGrandQuestion.author or current_user.email == "s_ahmed.alowmari@ousd.org":
        deleteGrandQuestion.delete()
        flash('The Grand Question was deleted.')
    else:
        flash("You can't delete a Grand Question you don't own.")
    grandQuestions = GrandQuestion.objects()  
    return render_template('grandQuestions.html',grandQuestions=grandQuestions)

@app.route('/grandQuestion/new', methods=['GET', 'POST'])
@login_required
def grandQuestionNew():
    form = GrandQuestionForm() #EVAN
    if form.validate_on_submit():
        newGrandQuestion = GrandQuestion( #EVAN
            gQuestion = form.gQuestion.data,
            author = current_user.id,
            modify_date = dt.datetime.utcnow
        )
        newGrandQuestion.save()
        return redirect(url_for('grandQuestion',grandQuestionID=newGrandQuestion.id))
    return render_template('grandQuestionform.html',form=form)

@app.route('/grandQuestion/edit/<grandQuestionID>', methods=['GET', 'POST'])
@login_required
def grandQuestionEdit(grandQuestionID):
    editGrandQuestion = GrandQuestion.objects.get(id=grandQuestionID)
    if current_user != editGrandQuestion.author:
        flash("You can't edit a Grand Question you don't own.")
        return redirect(url_for('grandQuestion',grandQuestionID=grandQuestionID))
    form = GrandQuestionForm()
    if form.validate_on_submit():
        editGrandQuestion.update(
            gQuestion = form.gQuestion.data,
            modify_date = dt.datetime.utcnow
        )
        return redirect(url_for('grandQuestion',grandQuestionID=grandQuestionID))
    #form.subject.data = editGrandQuestion.subject
    #form.content.data = editGrandQuestion.content
    #form.tag.data = editGrandQuestion.tag
    return render_template('grandQuestionform.html',form=form)

@app.route('/comment/new/<grandQuestionID>', methods=['GET', 'POST'])
@login_required
def commentNew(grandQuestionID):
    grandQuestion = GrandQuestion.objects.get(id=grandQuestionID)
    form = CommentForm()
    if form.validate_on_submit():
        newComment = Comment(
            author = current_user.id,
            grandQuestion = grandQuestionID,
            content = form.content.data
        )
        newComment.save()
        return redirect(url_for('grandQuestion',grandQuestionID=grandQuestionID))
    return render_template('commentform.html',form=form,grandQuestion=grandQuestion)

@app.route('/comment/edit/<commentID>', methods=['GET', 'POST'])
@login_required
def commentEdit(commentID):
    editComment = Comment.objects.get(id=commentID)
    if current_user != editComment.author:
        flash("You can't edit a comment you didn't write.")
        return redirect(url_for('grandQuestion',grandQuestionID=editComment.grandQuestion.id))
    grandQuestion = grandQuestion.objects.get(id=editComment.grandQuestion.id)
    form = CommentForm()
    if form.validate_on_submit():
        editComment.update(
            content = form.content.data,
            modifydate = dt.datetime.utcnow
        )
        return redirect(url_for('grandQuestion',grandQuestionID=editComment.grandQuestion.id))

    form.content.data = editComment.content

    return render_template('commentform.html',form=form,grandQuestion=grandQuestion)   

@app.route('/comment/delete/<commentID>')
@login_required
def commentDelete(commentID): 
    deleteComment = Comment.objects.get(id=commentID)
    deleteComment.delete()
    flash('The comments was deleted.')
    return redirect(url_for('grandQuestion',grandQuestionID=deleteComment.grandQuestion.id))

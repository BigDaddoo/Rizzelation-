from app import app
from flask_login.utils import login_required
from flask import render_template, redirect, flash, url_for
from app.classes.data import User
from app.classes.forms import ProfileForm
from app.classes.forms import TheirProfileForm

from flask_login import current_user

# These routes and functions are for accessing and editing user profiles.

# The first line is what listens for the user to type 'myprofile'
@app.route('/myprofile')
# This line tells the user that they cannot access this without being loggedin
@login_required
# This is the function that is run when the route is triggered
def myProfile(): 
    # This sends the user to their profile page which renders the 'profilemy.html' template
    return render_template('profilemy.html')

# This is the route for editing a profile
# the methods part is required if you are using a form 
@app.route('/myprofile/edit', methods=['GET','POST'])
# This requires the user to be loggedin 
@login_required
# This is the function that goes with the route
def profileEdit():
    # This gets an object that is an instance of the form class from the forms.pyin classes
    form = ProfileForm()
    # This asks if the form was valid when it was submitted
    if form.validate_on_submit():
        # if the form was valid then this gets an object that represents the currUser's data
        currUser = User.objects.get(id=current_user.id)
        # This updates the data on the user record that was collected from the form
        currUser.update(
            lname = form.lname.data,
            fname = form.fname.data,
            username = form.username.data,
            role = form.role.data,
            purpose = form.purpose.data,
            qRizztriction = form.qRizztriction.data,
            cRizztriction = form.cRizztriction.data
        )
        # This updates the profile image
        if form.image.data:
            if currUser.image:
                currUser.image.delete()
            currUser.image.put(form.image.data, content_type = 'image/jpeg')
            # This saves all the updates
            currUser.save()
        # Then sends the user to their profle page
        return redirect(url_for('myProfile'))

    # If the form was not submitted this prepopulates a few fields
    # then sends the user to the page with the edit profile form
    form.fname.data = current_user.fname
    form.lname.data = current_user.lname
    form.username.data = current_user.username
    form.role.data = current_user.role
    form.purpose.data = current_user.purpose

    form.qRizztriction.data = current_user.qRizztriction
    form.cRizztriction.data = current_user.cRizztriction

    return render_template('profileform.html', form=form)

@app.route('/users')
def users():
    users = User.objects()
    return render_template('users.html',users=users)

@app.route('/user/<uid>')
def user(uid):
    thisUser = User.objects.get(id=uid)
    return render_template("profile.html",user=thisUser)

# Time to make some mistakes _____________________________________________________

@app.route('/editUser/<uid>', methods=['GET','POST'])
# This requires the user to be loggedin 
@login_required
# This is the function that goes with the route
def editProfile(uid):
    # This gets an object that is an instance of the form class from the forms.pyin classes
    form = TheirProfileForm()
    # This asks if the form was valid when it was submitted
    if form.validate_on_submit():
        # if the form was valid then this gets an object that represents the currUser's data
        thisUser = User.objects.get(id=uid)
        # This updates the data on the user record that was collected from the form
        thisUser.update(
            lname = form.lname.data,
            fname = form.fname.data,
            username = form.username.data,
            role = form.role.data,
            purpose = form.purpose.data,
            qRizztriction = form.qRizztriction.data,
            cRizztriction = form.cRizztriction.data
        )
        # This updates the profile image
        if form.image.data:
            if thisUser.image:
                thisUser.image.delete()
            thisUser.image.put(form.image.data, content_type = 'image/jpeg')
            # This saves all the updates
            thisUser.save()
        # Then sends the user to their profle page
        return redirect(url_for('user')) # hmm

    # If the form was not submitted this prepopulates a few fields
    # then sends the user to the page with the edit profile form
    form.lname.data = user.lname
    form.fname.data = user.fname
    form.username.data = user.username
    form.role.data = user.role
    form.purpose.data = user.purpose

    form.qRizztriction.data = user.qRizztriction
    form.cRizztriction.data = user.cRizztriction

    return render_template('theirprofileform.html', form=form)
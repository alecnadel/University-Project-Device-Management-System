from flask import Blueprint, render_template, session, abort, request, url_for, redirect
from service.user_service import get_user_by_username, update_user_by_username, get_overdue_by_username,get_currently_devices_by_username,get_cursor

user_app = Blueprint('user_app', __name__)


@user_app.route("/user/home")
def member_home():
    """Creates the user home"""
    user = session.get('user')
    if user:
        overdue = get_overdue_by_username(user[0])
        borrowed = get_currently_devices_by_username(user[0])
        empty = len(overdue) == 0 and len(borrowed) == 0
        return render_template('user/home.html', overdue=overdue, borrowed=borrowed, empty=empty)
    else:
        abort(404)


@user_app.route("/user/profile", methods=['GET', 'POST'])
def user_profile():
    """creates the users profile page"""
    username = session.get('user')[0]
    user = get_user_by_username(username)
    if user:
        if request.method == 'POST':
            print("request.form",request.form)
            update_user_by_username(username, request.form)
            return redirect(url_for('user_app.user_profile'))
        if request.method == 'GET':
            cur = get_cursor()
            cur.execute("SELECT DISTINCT Location FROM users")
            locations = cur.fetchall()
            cur.execute("select * from users where Users_name=%s;",(username,))
            userdetails = cur.fetchone()
            return render_template('user/profile.html', user=user,
                                                        locations=locations,
                                                        userdetails=userdetails)
    else:
        abort(404)

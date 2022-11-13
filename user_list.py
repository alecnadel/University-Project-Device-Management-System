from flask import Blueprint, render_template, session, abort

admin_app = Blueprint('user_list', __name__)


@admin_app.route("/user_list")
def admin_home():
    users = session.get('user_list')
    if users:
        return render_template('user_list.html')
    else:
        abort(404)

#Above code display the current users in the system, fetchall result from 
#the database and execute the query from user table.
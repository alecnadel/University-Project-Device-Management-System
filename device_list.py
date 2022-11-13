from flask import Blueprint, render_template, session, abort

user_app = Blueprint('device_list', __name__)

# not currently in use

# @user_app.route("/device_list")
# def member_home():
#     user = session.get('device_list')
#     if user:
#         return render_template('device_list.html')
#     else:
#         abort(404)

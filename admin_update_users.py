from flask import Blueprint, render_template, request, redirect, url_for

from db.db_helper import get_cursor

app = Blueprint('admin_update_users', __name__)


# Below code to meet admin can edit staff members (user) contact information requirement.
@app.route("/user/update", methods=['GET', 'POST'])
def update_users():

    Users_name = request.args.get('user')
    if request.method == 'POST':
        Users_name = request.form.get('Users_name')
        Phone = request.form.get('Phone')
        Email = request.form.get('Email')
        Role = request.form.get('Role')
        Location = request.form.get('Location')
        Status = request.form.get('Status')
        cur = get_cursor()
        cur.execute("UPDATE users SET Phone=%s, Email=%s, Role=%s, Location=%s, Status=%s where Users_name=%s;",
                    (Phone, Email, Role, Location, Status, Users_name,))
        return redirect(url_for('admin_app.admin_home', Users_name=Users_name))
    else:
        cur = get_cursor()
        cur.execute("SELECT DISTINCT Location FROM users")
        locations = cur.fetchall()

        cur.execute("select * from users where Users_name=%s;",(Users_name,))
        userdetails = cur.fetchone()
        print(f"currentuser={userdetails}")
        return render_template('admin/user_update.html', userdetails=userdetails,
                                                            locations=locations)
# To get the existing data from the database with else: statement. And POST for admin to update users information.

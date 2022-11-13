from flask import Blueprint, render_template, session, abort, request, url_for, redirect
from db.db_helper import get_cursor
from service.user_service import get_user_by_username, update_user_by_username, get_overdue_by_username, \
    get_currently_devices_by_username, create_user

from service.device_service import get_popular_devices

admin_app = Blueprint('admin_app', __name__)


# admin home page
@admin_app.route("/admin/home")
def admin_home():
    """creates the admins home page"""
    messages = request.args.get('alertMessage')
    username = session.get('user')[0]
    overdue = get_overdue_by_username(username)
    borrowed = get_currently_devices_by_username(username)
    empty = len(overdue) == 0 and len(borrowed) == 0
    return render_template('admin/home.html', alertMessage=messages, overdue=overdue, borrowed=borrowed, empty=empty)


@admin_app.route("/admin/profile", methods=['GET', 'POST'])
def user_profile():
    """creates the admins user profile page"""
    username = session.get('user')[0]
    user = get_user_by_username(username)
    if user:
        if request.method == 'POST':
            print("request.form",request.form)
            update_user_by_username(username, request.form)
            return redirect(url_for('admin_app.user_profile'))
        if request.method == 'GET':
            cur = get_cursor()
            cur.execute("SELECT DISTINCT Location FROM users")
            locations = cur.fetchall()
            cur.execute("select * from users where Users_name=%s;",(username,))
            userdetails = cur.fetchone()
            return render_template('admin/profile.html', user=user,
                                                        locations=locations,
                                                        userdetails=userdetails)
    else:
        abort(404)


@admin_app.route("/admin/newUser", methods=['GET', 'POST'])
def new_user_profile():
    """Creates the newUser form pages"""
    if request.method == 'POST':
        username = request.form.get('username')
        user = get_user_by_username(username)
        if user:
            return render_template('admin/newUser.html',
                                   user=[None, request.form.get('email'), request.form.get('phone'), request.form.get('Role'), request.form.get('Location'), request.form.get('Status')])
        else:
            create_user(username, request.form)
            return redirect(url_for('admin_app.admin_home', alertMessage='Create user success'))
    if request.method == 'GET':
        cur = get_cursor()
        cur.execute("SELECT DISTINCT Location FROM users")
        locations = cur.fetchall()
        
        return render_template('admin/newUser.html',locations=locations)


@admin_app.route("/admin/popular", methods=['GET'])
def get_popular_device():
    """Creates the popular device list page sorted by most borrowed over last month"""
    popular_devices = get_popular_devices()
    return render_template('admin/popular.html', popular_devices=popular_devices)


# Alec part of code here: for admin to add new devices to the existing device list. So that the users can borrow the new added device from the list.

#@admin_app.route("/admin/addnewdevice", methods=['GET', 'POST'])
def get_user_by_DeviceName(DeviceName):
    """gets device info based on the device name"""
    cursor = get_cursor()
    cursor.execute('SELECT * FROM devices WHERE Device_Name=%s;', (DeviceName,))
    users = cursor.fetchall()
    return users[0] if len(users) else None

def add_device():
    """Creates the add new device form page and controls the submission 
    of the that form and prevents the admin from submitting a form with
    a device name that already exists"""
    Device_Name = request.args.get('Device_Name')
    select_options = [['Windows', 'Android', 'IOS', 'VR', 'XV'],
                        ['32','64'],
                        ['High','Medium','Low - Mid','Low','Obsolete']]

    if request.method == 'POST': # add device form submit
            Device_name1 = request.form.get('Device_Name')
            cur = get_cursor()
            Device = get_user_by_DeviceName(Device_name1)
            
            
            if Device: # Checking if device already exits
                cur.execute("select * from devices;")
                device = cur.fetchall()
                name = [desc[0] for desc in cur.description]

                return render_template('admin/addnewdevice2.html',
                device=[None, 
                request.form.get('Device_Type'),
                request.form.get('OS_Type'),
                request.form.get('OS_Version'),
                request.form.get('Ram'),
                request.form.get('CPU'),
                request.form.get('Bits'),
                request.form.get('Screen_Resolution'),
                request.form.get('Grade'),
                request.form.get('UUID'),
                request.form.get('Available')],
                name=name,
                select_options=select_options)
            else: # creates new device
                Device_Type = request.form.get('Device_Type')
                OS_Type = request.form.get('OS_Type')
                OS_Version = request.form.get('OS_Version')
                Ram = request.form.get('Ram')
                CPU = request.form.get('CPU')
                Bits = request.form.get('Bits')
                Screen_Resolution = request.form.get('Screen_Resolution')
                Grade = request.form.get('Grade')
                UUID = request.form.get('UUID')
                Available = request.form.get('Available')
                cur = get_cursor()
                cur.execute("""insert into devices(Device_Name, Device_Type, OS_Type, OS_Version, Ram, CPU, Bits, Screen_Resolution, Grade, UUID, Available,Activity)
                    values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,1);""", (
                    Device_name1, Device_Type, OS_Type, OS_Version, Ram, CPU, Bits, Screen_Resolution, Grade, UUID, Available,))
                cur.execute("select * from devices;")
                Device_Name = cur.fetchall()
                Device = [desc[0] for desc in cur.description]
                return redirect(url_for('admin_app.admin_home', alertMessage='New device added!'))
                

        
            
    else: # creates the add new device form page 
            cur = get_cursor()
            cur.execute("select * from devices;")
            device = cur.fetchall()
            name = [desc[0] for desc in cur.description]
            return render_template('admin/addnewdevice2.html', device=None,
                                                            name=name,
                                                            select_options=select_options) 

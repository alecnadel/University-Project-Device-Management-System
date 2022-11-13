from datetime import datetime
from flask import Flask, render_template, session, request, redirect, abort, url_for, flash
from db.db_helper import get_cursor
from controller.user_app import user_app
from controller.admin_app import admin_app
from controller.admin_update_users import app as admin_update_app
from service.user_service import get_devices, get_dev_headers #get_borrower_info
from service.user_service import get_users, get_user_by_username,get_currently_devices_by_username,get_overdue_by_username,get_overdue
from controller.device_search import Sevice_Search
from controller.admin_update_users import update_users
from controller.admin_app import add_device
import uuid

# setting up variables for the app
connection = None
dbconn = None

app = Flask(__name__)
app.register_blueprint(admin_app)
app.register_blueprint(user_app)
app.register_blueprint(admin_update_app)
app.secret_key = "super secret key"

ADMIN = 1
MEMBER = 0

def genID():
    """Creates a unique ID"""
    return uuid.uuid3().field[1]

@app.route("/")
def root():
    """sets up the Login page"""
    users = get_users()
    return render_template('login.html', users=users)


@app.route("/login", methods=['POST'])
def login():
    """Log the user in when they select their username on 
    the login page"""
    username = request.form.get('username')
    user = get_user_by_username(username)
    if user: # check a valid user is selected then confirms users role admin or user
        session['user'] = user
        if user[3] == 1:
            return redirect("/admin/home")
        if user[3] == 0:
            return redirect("/user/home")
    else:
        abort(404)

@app.route("/Search", methods=['GET','POST'])
def Search():
    """controls creation of the device list searchable table
    and if the edit device features is present based on users role"""
    return Sevice_Search()

# Sohaib Qadir original device list no longer in use.

# @app.route("/DevList", methods=['GET','POST'])
# def DevList(): 
#     """creates a list of devices showing then in html file"""
#     if request.method == 'POST':#The post method is called when the member submits the form
#         # The following are the fields that we get from the form
#         browerinfo = get_borrower_info(request.form.get('MemberID'))
#         return browerinfo
#     else:
#         devices = get_devices()
#         dev_headers = get_dev_headers()
#         return render_template('device_list/device_list.html', devices=devices, dev_headers=dev_headers)


@app.route("/UsrList", methods=['GET','POST'])
def UsrList():
    """Creates the list table Stuff of for current admin to use"""
    if request.method == 'GET':
        cur = get_cursor()
        cur.execute("select Users_name, Phone, Email, Role, Location, Status from users;")
        
        users = cur.fetchall()
        print(users)
        columnnames = [desc[0] for desc in cur.description]
        return render_template('admin/user_list.html', users=users, columnnames=columnnames)

@app.route("/delete", methods=['GET', 'POST'])
def delete():
    """Deletes users from the database when admin enters UsrList and clicks 
    the delete button"""
    flash("User deleted successfully")
    if request.method == 'POST':
        Usersname = request.form.get('Users_name')
        cur = get_cursor()
        
        command = """SELECT Device_name, date_format(End_Date, '%d-%m-%Y') AS End_Date from usersdevices where Users_name='{}';""".format(Usersname)
        print(command)
        cur.execute(command)
        print(20)
        devices = cur.fetchall()

        borroweddevices = devices
        for borrowed in borroweddevices:
            cur.execute("""UPDATE devices SET Available=1 WHERE Device_Name=%s
            """,(borrowed[0],))

            ReturnTime = datetime.now()
            
            cur.execute("""UPDATE usersdevices SET Return_Date=CAST(%s AS DATETIME) WHERE Device_Name=%s""",(ReturnTime,borrowed[0]))
        cur.execute("""delete from users 
        where Users_name=%s;""",(Usersname,))
        

        return redirect(url_for('admin_app.admin_home'))

@app.route("/admin/user/update", methods=['GET', 'POST'])
def admin_update():
    """Allows an admin update/edit user info when they clicking on the
    edit button in Usrlist page"""
    return update_users()

@app.route("/admin/addnewdevice", methods=['GET', 'POST'])
def admin_addnewdevice():
    """Setup the new device creation form page and controls form submission
    and checks that the device name is unique."""
    return add_device()

    
@app.route("/dev_return", methods = ["POST"])
def device_return():
    """returns the devices selected making it availible when return button is clicked"""
    user = session.get('user')
    if request.method == "POST":
        device_name = request.form.get("device_name")
        print(device_name)
        cur = get_cursor()
        cur.execute("""UPDATE devices SET Available=1 WHERE Device_Name=%s
        """,(device_name,))

        ReturnTime = datetime.now()
        cur.execute("""UPDATE usersdevices SET Return_Date=CAST(%s AS DATETIME) WHERE Device_Name=%s""",(ReturnTime,device_name))
        

    
        if user[3] == 1:
            return redirect("/admin/home")
        if user[3] == 0:
            return redirect("/user/home")
        else:
            abort(404)

@app.route("/dev_return_all", methods = ["POST"])
def device_return_all():
    """returns the devices selected making then all availible when return all button is clicked"""
    user = session.get('user')
    BorrowedDevices = get_currently_devices_by_username(user[0])
    Overdue = get_overdue_by_username(user[0])
    if request.method == "POST":

        borroweddevices = request.form.getlist("borrowed")
        print("borroweddevices",borroweddevices)
        overduedevices = request.form.getlist("overdue")
        print("overduedevices",overduedevices)
        cur = get_cursor()
        for borrowed in borroweddevices:
            cur.execute("""UPDATE devices SET Available=1 WHERE Device_Name=%s
            """,(borrowed,))

            ReturnTime = datetime.now()
            cur.execute("""UPDATE usersdevices SET Return_Date=CAST(%s AS DATETIME) WHERE Device_Name=%s""",(ReturnTime,borrowed))

        for overdue in overduedevices:
            cur.execute("""UPDATE devices SET Available=1 WHERE Device_Name=%s
            """,(overdue,))

            ReturnTime = datetime.now()
            cur.execute("""UPDATE usersdevices SET Return_Date=CAST(%s AS DATETIME) WHERE Device_Name=%s""",(ReturnTime,overdue))


    
        if user[3] == 1:
            return redirect("/admin/home")
        if user[3] == 0:
            return redirect("/user/home")
        else:
            abort(404)



    
@app.route("/admin/edit_devices", methods=['GET','POST'])
def edit_devices():
    """function generates the edit devices form page & controls form submission"""
    devicename = request.args.get("device")
    select_options = [['Windows', 'Android', 'IOS', 'VR', 'XV'],
                        ['32','64'],
                        ['High','Medium','Low - Mid','Low','Obsolete']]
    cur = get_cursor()
    print("edit_devices")
    print("request.method",request.method)
    if request.method == "POST": # Updates the device details
        Device_Name = request.form.get("Device_Name")
        Device_Type = request.form.get("Device_Type")
        OS_Type = request.form.get("OS_Type")
        OS_Version = request.form.get("OS_Version")
        Ram = request.form.get("Ram")
        CPU = request.form.get("CPU")
        Bits = request.form.get("Bits")
        Screen_Resolution = request.form.get("Screen_Resolution")
        Grade = request.form.get("Grade")
        UUID = request.form.get("UUID")
        Activity = request.form.get("Activity")
        

        cur.execute("""UPDATE devices SET
                                Device_Type=%s,
                                OS_Type=%s,
                                OS_Version=%s,
                                Ram=%s,
                                CPU=%s,
                                Bits=%s,
                                Screen_Resolution=%s,
                                Grade=%s,
                                UUID=%s,
                                Activity=%s
                                WHERE Device_Name=%s""",
                                (Device_Type,
                                    OS_Type,
                                    OS_Version,
                                    Ram,
                                    CPU,
                                    Bits,
                                    Screen_Resolution,
                                    Grade,
                                    UUID,
                                    Activity,
                                    Device_Name,))

        return redirect("/Search")
    else:

        
        cur.execute("SELECT * FROM devices WHERE Device_Name = %s",(devicename,))
        device_detials = cur.fetchone()
        return render_template("/admin/edit_device.html", device_detials=device_detials,
                                                            select_options=select_options)


@app.route("/admin/overdue", methods=['GET','POST'])
def overdue():
    """returns a list of overdue devices for the admin to view."""
    overdue = get_overdue()
    return render_template("/admin/overdue_device.html",overdue=overdue)
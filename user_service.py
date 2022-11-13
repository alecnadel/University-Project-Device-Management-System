from db.db_helper import get_cursor
from flask import Flask, render_template, session, request, redirect, abort, url_for, flash

def get_users():
    """Fetchs all the user_name and Role for all users"""
    cursor = get_cursor()
    cursor.execute('SELECT Users_name, Role FROM users')
    return cursor.fetchall()


def get_user_by_username(username):
    """get User info by using their username"""
    cursor = get_cursor()
    cursor.execute('SELECT * FROM users WHERE Users_name=%s;', (username,))
    users = cursor.fetchall()
    return users[0] if len(users) else None


def get_devices():
    """Get devices for device list (but is not currently in use due 
    to changes in database structure)"""
    cursor = get_cursor()
    cursor.execute(
        "SELECT devices.Device_Name, devices.Device_Type, devices.OS_Type, devices.OS_Version, devices.Ram, devices.CPU, devices.Bits, devices.Screen_Resolution, devices.Grade, devices.Available, UsersDevices.Users_name, DATE_FORMAT(UsersDevices.End_Date,'%d/%m/%Y') FROM dev_mgmt_sys.devices INNER JOIN dev_mgmt_sys.usersdevices ON devices.Device_name = usersdevices.Device_name;")
    return cursor.fetchall()


def get_dev_headers():
    """Gets column names for device list"""
    cur = get_cursor()
    cur.execute("select * from devices;")
    column_names = [desc[0] for desc in cur.description]  # getting values for colmn headers
    return column_names


def update_user_by_username(username, form):
    """Used to update user contact detials on profile page
    for both users and admins"""
    cursor = get_cursor()
    email = form.get('email')
    phone = form.get('phone')
    location = form.get('Location')
    role = form.get('Role')
    status = form.get('status')
    update_sql = 'UPDATE users SET Email=%s,Phone=%s, Location=%s, Role=%s, Status=%s WHERE Users_name=%s'
    parameters = (email, phone, location, role, status, username)
    cursor.execute(update_sql, parameters)


def create_user(username, form):
    """Used to create a new user on the newUser page"""
    cursor = get_cursor()
    email = form.get('email')
    phone = form.get('phone')
    location = form.get('Location')
    role = form.get('Role')
    status = form.get('Status')
    update_sql = 'INSERT INTO users (Users_name, Phone, Email, Role, Location, Status) VALUES (%s,%s,%s,%s,%s,%s)'
    parameters = (username, phone, email, role, location, status,)
    cursor.execute(update_sql, parameters)


def get_overdue_by_username(username):
    """obtains the list of overdue device a user has not yet returned"""
    cursor = get_cursor()
    command = """SELECT Device_name, date_format(End_Date, '%d-%m-%Y') AS End_Date From usersdevices where Return_Date is null and NOW() > End_Date and Users_name='{}';""".format(
        username)
    cursor.execute(command)
    devices = cursor.fetchall()
    return devices

# not currently in use

# def get_borrower_info(Device_name):
#     
#     cursor = get_cursor()
#     cursor.execute(
#         'SELECT Users_name, End_Date FROM dev_mgmt_sys.usersdevices where End_Date >= NOW() and Device_name=%s',
#         (Device_name,))

#     return cursor.fetchall()


def get_currently_devices_by_username(username):
    """Returns all devices a user currently as checkout(currently borrowing)"""
    cursor = get_cursor()
    command = """SELECT Device_name, date_format(End_Date, '%d-%m-%Y') AS End_Date from usersdevices where Return_Date IS NULL and Users_name='{}';""".format(username)
    cursor.execute(command)
    devices = cursor.fetchall()
    return devices

def get_overdue():
    """returns all devices that are currently borrowed by all users"""
    cursor = get_cursor()
    command = """SELECT UD.Device_name, 
                        date_format(UD.End_Date, '%d-%m-%Y') AS Expected_Return_Date,
                        U.Users_name,
                        U.Phone, 
                        U.Email, 
                        U.Location
                    From usersdevices AS UD
                        INNER JOIN users AS U
                            on U.Users_name = UD.Users_name
                        where Return_Date is null and NOW() > End_Date;"""
    cursor.execute(command)
    devices = cursor.fetchall()
    return devices
from flask import Blueprint, render_template, request,redirect, session
from db.db_helper import get_cursor
from service.user_service import get_currently_devices_by_username,get_overdue_by_username
# import json

# No longer used
# select_options = [['Windows', 'Android', 'IOS', 'VR', 'XV'],
#             ['4 GB','2 GB','500MB','1GB','1 GB','1 GB DDR3','2 GB DDR 4','500 MB','3 GB','1.5 GB'],
#             [64,32],
#             ['High','Low','Obsolete','Medium','Low - Mid']]

def get_devices():
    """Returns all fields of all devices in the database"""
    cursor = get_cursor()
    cursor.execute("""SELECT D.Device_Name, D.Device_Type, D.OS_Type, D.OS_Version, D.Ram, D.CPU, D.Bits, D.Screen_Resolution, D.Grade, D.Available FROM devices D """) 
    return cursor.fetchall()


def current_borrowing_infomation():
    """Gets list of all currently borrowed devices info"""
    cursor = get_cursor()
    cursor.execute("""SELECT Device_name, Users_name, DATE_FORMAT(End_Date, '%d/%m/%Y') from usersdevices where Return_Date IS NULL;""")
    borrowed = cursor.fetchall()
    return borrowed

def get_dev_headers():
    """returns a list of column names from devices table"""
    cur = get_cursor()
    cur.execute("""SELECT Device_Name, 
                            Device_Type, 
                            OS_Type, 
                            OS_Version, 
                            Ram,
                            CPU, 
                            Bits, 
                            Screen_Resolution, 
                            Grade, 
                            Available 
                    FROM devices""")
    column_names = [desc[0] for desc in cur.description]#getting values for colmn headers
    return column_names

from datetime import datetime

def Sevice_Search():
    """loads in the device list & search funcitionilty page
    where devices can be borrowed from"""

    # loading required user information from session or database
    cur = get_cursor() 
    Users_name = session.get("user")[0]
    Role = session.get("user")[3]
    BorrowedDevices = get_currently_devices_by_username(Users_name)
    Overdue = get_overdue_by_username(Users_name)
    CountDevice = len(BorrowedDevices) 

    
    
    if request.method == 'POST':  # Runs on Borrow device form submisssion
        count = request.form.get("count")
        count = int(count)

        
        if CountDevice + count <= 3:
            # go though all device being borrowed and individual adding row
            # to userdevices table and mark the device unavailable in devive table
            for i in range(1,int(count)+1): 
                Device = request.form.get("Device_name_{}".format(i))
                Start = request.form.get("Start_Date_{}".format(i))
                
                Return = request.form.get("ReturnDate_{}".format(i))
                Return = (datetime.strptime(Return, "%Y-%m-%dT%H:%M")).strftime("%Y-%m-%d %H:%M")
            
                command = """INSERT INTO usersdevices (Device_name, Users_name, Start_Date, End_Date)
                                                VALUES ('{}', '{}', CAST('{}' AS DATETIME), CAST('{}' AS DATETIME));""".format(Device,Users_name,Start,Return)
                cur.execute(command)
                cur.execute("UPDATE devices SET Available=0 WHERE Device_Name = %s",(Device,))
        else:
            print("No Devices can be added")
        
        if Role == 1: # sends user back to correct home page
            return redirect("/admin/home")
        else:
            return redirect("/user/home")
        

    else:
        # Gets all device list then currently unavaible devices list
        devices = get_devices()
        All_BorrowedDevices = current_borrowing_infomation()
        # Finds devices borrowed by current user
        BorrowedDevices = get_currently_devices_by_username(Users_name)
        
        CountDevice = len(BorrowedDevices) # user current borrowed divces count
        dev_headers = get_dev_headers() # device table headings
        if Role == 1: # sends user to correct device list page
            return render_template('admin/dev_search_filter.html', 
                                                            devices=devices, 
                                                            dev_headers=dev_headers,
                                                            CountDevice=CountDevice,
                                                            All_BorrowedDevices=All_BorrowedDevices)
        else:
            return render_template('user/dev_search_filter.html', 
                                                          devices=devices, 
                                                          dev_headers=dev_headers,
                                                          CountDevice=CountDevice,
                                                          All_BorrowedDevices=All_BorrowedDevices)
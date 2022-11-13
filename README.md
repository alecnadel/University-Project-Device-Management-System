## Device Tracking System

Issue date: 	March 30, 2022 

Group members: 	Alec Arnold, Bo Liu, Craig Melton

### Purpose of the Project 

Our team have been approached by the product owner who wants a system that can manage the borrowing and returning of devices.

This project is to set up a web app for device tracking and management of a small company of 50 staff 
members split between two offices. This app will allow all staff members to track the current location 
and staff member using a device and the projects they are working on. This is to fix the problems with 
devices getting lost due to stuff members failing to update the physical board and allow all staff 
members in separate offices to track devices currently in use.

### Currently Completed Features

*	As a Staff member or administrator, I want to identify myself with the device management application so that I can be presented with the appropriate feature for my role in the company.

*	As a staff member, I want to be able to edit my contact details e.g., email and phone number so that I can allow fellow staff members to easily access my work contact and keep this information correct.

*	As a staff member, I want to be able to view the list of devices.

*	As a staff member, I want to be able to view the devices with search functionality.

*	As a staff member I want to be alerted if my device/s are overdue.

*	As a staff member, I want to borrow devices so that I can use them. 

*	As a staff member, I want to be able to return devices so that it is free for other staff to borrow. 

*	As an administrator, I want to be able to modify information regarding any device in the database so that I can keep the device information up to date.

*	As an administrator, I want to edit any information regarding staff members, so I can maintain correct staff member information. 

*	As an administrator, I want to be able to add devices to the list so that I can add new devices that can be borrowed. 

*	As an administrator, I want to be able to add staff members from the list of team members so that all team members can borrow devices needed for their work. 

*	As an administrator, I want to be able to remove staff members from the list when the staff member is not available anymore.

*	As an administrator I want to view a list of overdue devices so that I can remind borrowers to return these devices.

*	As an administrator I want to see the most popular devices borrowed in the previous month. 

### Data Model
 
 
 <a href="#"><img src="https://github.com/LUMasterOfAppliedComputing/Project1Group3-S1-2022/blob/68981c3bc1c1a142c6ec5cd053bee4dfa435f7e9/DatabaseFiles/Schema_2.png"></a>
 

### GUI Design

Nav bar, button group, grid, containers, columns, bootstrap 5 icons, mouse Onclicks JavaScript, dynamic forms.

The GUI was created primarily using bootstrap 5 features, like buttons, and formatting using grids with 
containers, rows & columns. All pages having a nav bar at the top of the screen with buttons, using 
bootstrap icons to navigate to the rest of the app, in accordance with the features available to the user
depending on their role within the app (admin/user). From there a section containing any alerts or 
 tables pertaining to relevant information for that page.

 <a href="#"><img src="https://github.com/LUMasterOfAppliedComputing/Project1Group3-S1-2022/blob/68981c3bc1c1a142c6ec5cd053bee4dfa435f7e9/image/Design_diagram_for_presentation_slide.png" width="611" height="495"></a>

JavaScript was also used to generate the dynamic device borrowing form and show alerts when a user tries 
to borrow too many advice’s or tries to the submit a form with no devices selected. It is also used to
display alert messages when a user currently has no devices assigned to them or when the device tables
 search filters that enter returns with no results. 

#### Validation: Javascript alert message, green and red colours bootstrap 5 form validation.

JavaScript was used to stylise forms that provide invalid information to input fields on form submission 
which would then implement bootstrap default CSS styling to show the validation state of the form to the 
user, red lines surrounding input fields containing invalid inputs and green for those containing valid 
inputs.

#### Verification: Standard user log in, admin user log-in, users name identifier, company role. 
 
The application verifies a User’s user by having a default value for their role within the system on 
login. This takes them to the correct pages within the device tracking system ensuring that 
administrators can access many administrative features and users can only use non-administrative features.

### Currently State of the System

Our team developed a tracking system for tracking all devices within a company, with two user interfaces.
These being ‘standard user’ and ‘administrator’. Standard user can see their borrowed devices, view 
devices that are available to borrow and check their profile information to make sure their contact 
details are up to date. Search filtering on devices can be carried out on their own device type, name and 
other specifications to return a list of devices matching the search criteria. 

Admin has all the standard user features and functionality plus some additional features, such as being 
able to add new or remove a user from the system when staff joins or leaves the company. Edit ‘users’ 
information based on the changes such as office location, their role and contact information. Check 
overdue devices to allow them to alert the staff members personally if the device/s are long overdue and 
remind them to return these devices. Or to enquire as to why they have not yet returned the device/s. 
Viewing the most popular devices over a month period so that an administrator can perceive which devices 
are in high demand by staff members working at the company. Additionally, admin could add a new device 
that the company has just procured with a new device specification entered into the database allowing 
staff members to utilise the newly obtained device.

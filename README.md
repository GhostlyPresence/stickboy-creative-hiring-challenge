# stickboy-creative-hiring-challenge
steps to run the app:
1.Clone the repository
2.cd into the directory
3.run pip install -r requrements.txt to install the dependencies
4.Now cd into sbcHiringApp directory
5.run python manage.py runserver to run the app

To log into the admin panel add a superuser using the following command:
python manage.py createsuperuser
select a username and a add a password

#Admin panel
Open the admin panel by visiting localhost:8000/admin
1.Admin can add/remove any user.
2.Admin can change its password using the old password.
3.Admin can change any user's password without requiring the old password.
4.Admin can add/remove tasks.
5.Admin can schedule task to any employee user and also delete it.

#Login and register
1.To use the app one needs to register as a user if they aren't one already.
2.After registering as a user they can login using login screen.
3.There is also an option for resetting forgotten password. But the admin needs to add their email as host email in settings.py.

#Dashboard
1.List task page lists all the task added by the admin and its start date and end date.
2.Your task page has all the tasks assigned to the logged in employee by the admin.

##Permission Portal
This website is aimed at managing student requests of an institute by passing them through a customizable chain of approvers.

There are four types of users:

1. <b>Superuser</b> : Superuser can manage the entire database, create new users and assign them to hierarchial positions.

2. <b>Admins</b> : Admins stand at the top of the hierarchy in the list of approvers. Their approval confirms the request.

3. <b>Secretaries</b> : Secretaries can customize the chain of approvers for a particular template of requests by specifying the user in each layer.

4. <b>Students</b> : Students can request permissions and can discuss with the admins through a chat box below their request.

Use case:
Ravi, a student of an institute, wants to book the projector for a specific time interval. He sends a request from this website with all the necessary details. The secretary corresponding to projector receives the permission and he sends it through a series of secretaries and finally to the admin. Then Admin can ask additional details about the request in the chat box and can confirm or reject the request with appropriate message with which the student is notified.
The secretary can create a template for the chain of secretaries a request for a projector passes through and can just select this template from then.

######Requirements
* [Python == 2.7](https://www.python.org/downloads/).
* [Django == 1.7](https://pypi.python.org/pypi/Django/1.7).

######Installation and Running
* After installing python, download [Django 1.7](https://pypi.python.org/pypi/Django/1.7), extract it and install using `python2 setup.py install` inside the source folder.
* Now, clone the permission\_portal repository and in `permission_portal/IIGPermission/` folder and enter `python2 manage.py migrate` in terminal.
* Then, to run the server, enter `python2 manage.py runserver` and in the browser type `localhost:8000/Permission` and login.

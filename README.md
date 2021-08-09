# dashboard-api

To use API - it returns json objects

1) Create a new user entry - pass a dictionary.

/create_user

Eg: http://127.0.0.1:8000/create_user

2) Get users sorted by educational qualification

http://127.0.0.1:8000/sort_by_qualification


3) Get data for active users:

http://127.0.0.1:8000/get_active_users

4) Get data of a user by providing his/her email.

Eg: http://127.0.0.1:8000/user_info/nishikaithwas2000@gmail.com

5) update data of a user by providing his/her email.

/update_an_entry/<email goes here>

Eg : http://127.0.0.1:8000/update_an_entry/nishikaithwas2000@gmail.com
  
  

Initial Commit - 09/08/2021

Following files have been commited to the repository.

1) From /api : apps.py, models.py, serializers.py, rest_api_urls, views.py of which serializers and rest_api_urls have been made by me. Rest are system generated files which were edited for the functionality of the REST api.

 a) apps.py -  consists of 'api' django app Config class named as  - 'ApiConfig'
 b) models.py - responsible for MongoDB database creation named 'user_inforamtion_record'. It has following fields - first_name, last_name, email_id, contact_number,                               permanent_address, educaiton_qualification, active_status.

 c) serializers.py - responsible for serialization and deserialization to and from JSON format.
 d) rest_api_urls.py - configures urls that will be used to access to send or receive data to and from DB.
 e) views.py - consists functions for sending and receving data to and from DB - user_info, sort_by_qualification, get_active_users, create_user, update_an_entry.
               
               Description for the above listed view functions.
               
                i) user_info - Get all info of a particular user
               ii) sort_by_qualification - Get all users sort by particular educational qualification
              iii) get_active_users - Get all active users
               iv) update_an_entry - Update entry of a particular user.
                v) create_user - Create entry of a particular user.

2) From /student_management_system : urls.py, settings.py

 a) urls.py - edited to match urls entered by the user according to the rest_api_urls description.
 b) settings.py - edited to include MongoDB configuration in 'DATABASES' and added ApiConfig and rest_framework to the 'INSTALLED_APPS' section.

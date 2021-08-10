# dashboard-api

To use API - it returns json objects

1) Create a new user entry - pass a dictionary.

POST- http://localhost:8000/v1/users


2) Get users sorted by educational qualification

GET - http://localhost:8000/v1/users


3) Get data for active users:

GET- http://localhost:8000/v1/users/active


4) Get data of a user by providing his/her email.

GET - http://localhost:8000/v1/users/<email-goes-here>

  Eg: http://localhost:8000/v1/users/nishikaithwas2000@gmail.com


5) update data of a user by providing his/her email.

PUT - http://localhost:8000/v1/users/<email-goes-here>

  Eg: http://localhost:8000/v1/users/nishikaithwas2000@gmail.com
  
  

Initial Commit - 09/08/2021

Following files have been commited to the repository.

1) From /api : apps.py, models.py, serializers.py, rest_api_urls, views.py of which serializers and rest_api_urls have been made by me. Rest are system generated files which were edited for the functionality of the REST api.

 a) apps.py -  consists of 'api' django app Config class named as  - 'ApiConfig'
 b) models.py - responsible for MongoDB database creation named 'user_inforamtion_record'. It has following fields - first_name, last_name, email_id, contact_number,                               permanent_address, educaiton_qualification, active_status.

 c) serializers.py - responsible for serialization and deserialization to and from JSON format.
 d) rest_api_urls.py - configures urls that will be used to access to send or receive data to and from DB.
 e) views.py - consists functions for sending and receving data to and from DB - user_info, sort_by_qualification, get_active_users, create_user, update_an_entry.
               
               Description for the above listed view functions.
               
                i) user_update_and_fetch - Update entry of a particular user by his/her email and fetch data of a particular user by his/her email.
               ii) get_active_users - Get all active users
              iii) user_create_and_retreive - create a new entry and get data of all users sorted by education qualification.
                
  2) From /student_management_system : urls.py, settings.py

 a) urls.py - edited to match urls entered by the user according to the rest_api_urls description.
 b) settings.py - edited to include MongoDB configuration in 'DATABASES' and added ApiConfig and rest_framework to the 'INSTALLED_APPS' section.

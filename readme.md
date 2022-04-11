
<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href=https://github.com/blavian/FireMoney/blob/main/readme.md>
  </a>



  <h1 align="center">Members</h1>
   
<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
    <li>
     <a href="#endpoints">Endpoints</a>
    </li>
    <li>
     <a href="#uploading-csv">Uploading Csv</a>
    </li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Coding challenge to create crud functionality for members

### Built With
 
* Django



<!-- GETTING STARTED -->
## Getting Started

1. Clone this repository 

   ```bash
   git clone https://github.com/blavian/members.git
   ```

2. Install dependencies

      ```bash
       pipenv install -r requirements.txt
      ```



3. Get into your pipenv shell, migrate your database, create your superuser, and run the server

   ```bash
   pipenv shell
   ```

   ```bash
    python manage.py migrate
   ```

   ```bash
   python manage.py createsuperuser

   ```
    - Follow the prompts to create a username and password
   ```bash
   python manage.py runserver
   ```
<!-- Endpoints -->
## Endpoints
The Postman collection is [here](https://www.getpostman.com/collections/0e1e95e60b9cbe973e44)
<br>
In order to access the collection, you need to provide your username and password that you created for teh django admin asin basic auth

## Uploading Csv
You can import a csv file via the django admin interface
The endpoint for it is [here](http://127.0.0.1:8000/admin/project/members/)

## Improvements
1. Allow for token based authentication
2. Have more test cases
3. Integrate Celery with django-import-export to run processes in the background


# Balcongardens - A plant exchange community!

BALCONGARDENS is a social network plattform designed for plant lovers in Berlin. 
The app encourages all users to contact the plants owners and exchange them. As a visitor you can also search for the plants by the plants type in case you are looking for an epecific plant one. 
The users can register for the website and have access to more features such as liking your favourite plants picture that you are most interested in as well as follow certain plant's owner in order to be aware of what they will post in the future. 
This is the backend API part of the project, based on the Django REST framework, and it serves the front end part of the project by retrieving and storing data in the database.

[View the live project here.](https://balcongardens.herokuapp.com/)

### [](https://github.com/vivignutz/balcongardens-drf-api#links-to-the-frontend-project)Links to the Frontend Project

-   [Frontend - Repository](https://github.com/vivignutz/balcongardens-fe)
-   [Frontend - Deployment](https://balcongardens-fe.herokuapp.com/)

## [](https://github.com/vivignutz/balcongardens-drf-api#toc)Table of Content

-   [User Stories](https://github.com/vivignutz/balcongardens-drf-api#user-stories)
-   [Database Schema](https://github.com/vivignutz/balcongardens-drf-api#database-schema)
-   [Features](https://github.com/vivignutz/balcongardens-drf-api#features)
    -   [Future Features](https://github.com/vivignutz/balcongardens-drf-api#future-features)
-   [Technologies Used](https://github.com/vivignutz/balcongardens-drf-api#technologies-used)
    -   [Languages and Frameworks Used](https://github.com/vivignutz/balcongardens-drf-apid#languages-and-frameworks-used)
    -   [Python Modules Used](https://github.com/vivignutz/balcongardens-drf-api#python-modules-used)
    -   [Packages Used](https://github.com/vivignutz/balcongardens-drf-api#packages-used)
    -   [Programs and Tools Used](https://github.com/vivignutz/balcongardens-drf-api#programs-and-tools-used)
-   [Testing](https://github.com/vivignutz/balcongardens-drf-api#testing)
    -   [Bugs](https://github.com/vivignutz/balcongardens-drf-api#bugs)
        -   [Fixed Bugs](https://github.com/vivignutz/balcongardens-drf-api#fixed-bugs)
        -   [Remaining Bugs](https://github.com/vivignutz/balcongardens-drf-api#remaining-bugs)
-   [Deployment](https://github.com/vivignutz/balcongardens-drf-api#deployment)
    -   [Forking the GitHub Repository](https://github.com/vivignutz/balcongardens-drf-api#forking-the-github-repository)
    -   [Making a Local Clone](https://github.com/vivignutz/balcongardens-drf-api#making-a-local-clone)
    -   [Deploying with Heroku](https://github.com/vivignutz/balcongardens-drf-api#deploying-with-heroku)
-   [Credits](https://github.com/vivignutz/balcongardens-drf-api#credits)
    -   [Code](https://github.com/vivignutz/balcongardens-drf-api#code)
    -   [Acknowledgements](https://github.com/vivignutz/balcongardens-drf-api#acknowledgements)


## [](https://github.com/vivignutz/balcongardens-drf-api#database-schema)Database Schema

-   The database models for the project were created based on the schema below.  [![DatabaseSchema](https://github.com/vivignutz/balcongardens-drf-api/blob/main/assets/database_diagram1.jpg)](https://github.com/vivignutz/balcongardens-drf-api/blob/main/assets/database_diagram1.jpg)

## [](https://github.com/vivignutz/balcongardens-drf-api#future-features)Future Features

Some future features were idealized to be implemented:
-   Offer more search options with filters based on different criteria.
-   Implement a star rating system for the plants offered to rate the plant offerers in order to increase trust and credibility of the community.
-   Implement a location algorithm to allow users to search for plants or offeres through a certain distance.
-   To offer the functionality for an image gallery to allow the offeres to upload more pictures of the plants to give.

## [](https://github.com/vivignutz/balcongardens-drf-api#technologies-used)Technologies Used

### [](https://github.com/vivignutz/balcongardens-drf-api#languages-and-frameworks-used)Languages and Frameworks Used

-   [Python](https://www.python.org/)  - The main programming language.
-   [Django](https://pypi.org/project/Django/3.2.14/)  - Python Web framework used to develop the project.
-   [djangorestframework](https://pypi.org/project/djangorestframework/3.14.0/)  - Toolkit for building web API's with Django.

### [](https://github.com/vivignutz/balcongardens-drf-api#python-modules-used)Python Modules Used

-   Built-in Packages/Modules
    -   [pathlib](https://docs.python.org/3/library/pathlib.html)  - Used to work with filepaths.
    -   [os](https://docs.python.org/3/library/os.html)  - This module provides a portable way of using operating system dependent functionality.

### [](https://github.com/vivignutz/balcongardens-drf-api#packages-used)Packages Used

-   External Python Packages
    -   [cloudinary](https://pypi.org/project/cloudinary/1.30.0/)  - Cloudinary intergration.
    -   [django-cloudinary-storage](https://pypi.org/project/django-cloudinary-storage/0.3.0/)  - Cloudinary intergration.
    -   [dj-database-url](https://pypi.org/project/dj-database-url/0.5.0/)  - Allows the use of 'DATABASE_URL' environmental variable in the Django project settings file to connect to a PostgreSQL database.
    -   [django-allauth](https://pypi.org/project/django-allauth/0.51.0/)  - Set of Django application used for account registration, management and authentication.
    -   [dj-rest-auth](https://pypi.org/project/dj-rest-auth/2.2.5/)  - API endpoints for handling authentication in Django Rest Framework.
    -   [django-filter](https://pypi.org/project/django-filter/22.1/)  - Application that allows dynamic QuerySet filtering from URL parameters.
    -   [djangorestframework-simplejwt](https://pypi.org/project/djangorestframework-simplejwt/5.2.1/)  - JSON Web Token authentication backend for the Django REST Framework.
    -   [django-cors-headers](https://pypi.org/project/django-cors-headers/3.13.0/)  - Django App that adds CORS headers to responses.
    -   [gunicorn](https://pypi.org/project/gunicorn/20.1.0/)  - Python WSGI HTTP Server.
    -   [Pillow](https://pypi.org/project/Pillow/9.2.0/)  - Fork of PIL, the Python Imaging Library which provides image processing capabilities.
    -   [psycopg2](https://pypi.org/project/psycopg2/2.9.3/)  - Python PostgreSQL database adapter.

### [](https://github.com/vivignutz/balcongardens-drf-api#programs-and-tools-used)Programs and Tools Used

-   [Lucidchart](https://drawsql.app/)  - Create Database Schema/ERD
-   [Gitpod:](https://gitpod.io/)
    -   Gitpod was used as my code editor for this project.
-   [Git](https://git-scm.com/)
    -   Git was used for version control, using the terminal to commit to Git and Push to GitHub.
-   [GitHub:](https://github.com/)
    -   GitHub is used to store the projects code after being pushed from Git.
 -   [PicResize](https://lucid.app/)  - To resize the database picture and the logo in order to reduce its size.

## [](https://github.com/vivignutz/balcongardens-drf-api#testing)API Testing

Manual testing was done several timas to try to discover some bugs and to know yout the functionality of the API.  These included visiting each URL to ensure accurate results were returned depending on authorization state, the creation, update and deletion of items:

### Testing Endpoints

| URL | Passed |
|---|---|
| root route | :white_check_mark: |
| /profiles/ | :white_check_mark: |
| /profiles/\<id>/ | :white_check_mark: |
| /posts/ | :white_check_mark: |
| /posts/\<id>/ | :white_check_mark: |
| /likes/ | :white_check_mark: |
| /likes/\<id>/ | :white_check_mark: |
| /followers/ | :white_check_mark: |
| /followers/\<id>/ | :white_check_mark: |
| /review/ (* to be implemented) | :white_check_mark: | * to be implemented

### Testing CRUD Functionality

#### Like App

| App | Action | Authenticated | Anonymous | Passed |
|---|---|---|---|---|
| Save | Read (List) | Array of owned objects | 403 Response | :white_check_mark: |
| Save | Read - Valid ID and Owner | Returns Detail | 404 Response | :white_check_mark: |
| Save | Read - Valid ID and not Owner | 404 Response | 404 Response | :white_check_mark: |
| Save | Read - Invalid ID | 404 Response | 404 Response  | :white_check_mark: |
| Save | Create | 201 Response | N/A | :white_check_mark: |
| Save | Update | N/A| N/A | N/A |
| Save | Delete | 204 Response | N/A | :white_check_mark: |

#### Followers App

| App | Action | Authenticated | Anonymous | Passed |
|---|---|---|---|---|
| Followers | Read (List) | Array of owned objects | Empty Results Array | :white_check_mark: |
| Followers | Read - Valid ID and Owner | Returns Detail | 403 Response | :white_check_mark: |
| Followers | Read - Valid ID and not Owner | 404 Response | 404 Response | :white_check_mark: |
| Followers | Read - Invalid ID | 404 Response | 404 Response  | :white_check_mark: |
| Followers | Create | 201 Response | N/A | :white_check_mark: |
| Followers | Update | N/A | N/A | N/A |
| Followers | Delete | 204 Response | N/A | :white_check_mark: |

#### Profiles App

| App | Action | Authenticated | Anonymous | Passed |
|---|---|---|---|---|
| Profiles | Read (List) | Array of profiles | Array of profiles | :white_check_mark: |
| Profiles | Read | Returns Detail | Returns Detail | :white_check_mark: |
| Profiles | Create | N/A | N/A | N/A |
| Profiles | Update | 200 Response | N/A | :white_check_mark: |

#### Posts App

| App | Action | Authenticated | Anonymous | Passed |
|---|---|---|---|---|
| Cars | Read (List) | Array of all cars | Array of all cars | :white_check_mark: |
| Cars | Read | Returns Detail | Returns Detail | :white_check_mark: |
| Cars | Create | 201 Response | N/A | :white_check_mark: |
| Cars | Update | 200 Response | N/A | :white_check_mark: |
| Cars | Delete | 204 Response | N/A | :white_check_mark: |

## Validating Code

The `pycodestyle` package was used throughout the development of the project to validate and fix problems in the code continuously. No validation errors were present in the final deployed version.

### [](https://github.com/vivignutz/balcongardens-drf-api#bugs)Bugs

#### [](https://github.com/vivignutz/balcongardens-drf-api#fixed-bugs)Fixed Bugs

During the tests some bugs appear:

-   Error 500 in which my database was not properli connected with the frontend. - FIXED
-  Error 401 in which three fo these errors belongs to the process, according to the walkthrough "Moments". Several bugs with same errors were solved when the JD-REST-AUTH was solved, and the only ones still remaining bugs are the three, which will be fixed during the improvement of the app.
- 

#### [](https://github.com/vivignutz/balcongardens-drf-api#remaining-bugs)Remaining Bugs

-   The three error 401.

## [](https://github.com/vivignutz/balcongardens-drf-api#deployment)Deployment

### [](https://github.com/vivignutz/balcongardens-drf-api#forking-the-github-repository)Forking the GitHub Repository

1.  Go to  [the project repository](https://github.com/vivignutz/balcongardens-drf-api)
2.  In the right most top menu, click the "Fork" button.
3.  There will now be a copy of the repository in your own GitHub account.

### [](https://github.com/vivignutz/balcongardens-drf-api#making-a-local-clone)Making a local clone

1.  Go to  [the project repository](https://github.com/vivignutz/balcongardens-drf-api)
2.  Click on the "Code" button.
3.  Choose one of the three options (HTTPS, SSH or GitHub CLI) and then click copy.
4.  Open the terminal in you IDE program.
5.  Type  `git clone`  and paste the URL that was copied in step 3.
6.  Press Enter and the local clone will be created.

### [](https://github.com/vivignutz/balcongardens-drf-api#alternatively-by-using-gitpod)Alternatively by using Gitpod:

1.  Go to  [the project repository](https://github.com/vivignutz/balcongardens-drf-api)
2.  Click the green button that says "Gitpod" and the project will now open up in Gitpod.

### [](https://github.com/vivignutz/balcongardens-drf-api#deploying-with-heroku)Deploying with Heroku

I followed the below steps using the Code Institute tutorial:

The following command in the Gitpod CLI will create the relevant files needed for Heroku to install your project dependencies  `pip3 freeze --local > requirements.txt`. Please note this file should be added to a .gitignore file to prevent the file from being committed.

1.  Go to  [Heroku.com](https://dashboard.heroku.com/apps)  and log in; if you do not already have an account then you will need to create one.
2.  Click the  `New`  dropdown and select  `Create New App`.
3.  Enter a name for your new project, all Heroku apps need to have a unique name, you will be prompted if you need to change it.
4.  Select the region you are working in.

#### [](https://github.com/vivignutz/balcongardens-drf-api#heroku-settings)Heroku Settings

You will need to set your Environment Variables - this is a key step to ensuring your application is deployed properly.

1.  In the Settings tab, click on  `Reveal Config Vars`  and set the following variables:
    -   Key as  `ALLOWED_HOSTS`  and the value as the name of you project with '.herokuapp.com' appended to the end e.g.  `example-app.herokuapp.com`. Click the Add button.
    -   Key as  `CLOUDINARY_URL`  and the value as your cloudinary API Environment variable e.g.  `cloudinary://**************:**************@*********`. Click the Add button.
    -   Key as  `SECRET_KEY`  and the value as a complex string which will be used to provide cryptographic signing. The use of a secret key generator is recommended such as  [https://djecrety.ir](https://djecrety.ir/). Click the Add button.
    -   Ensure the key  `DATABASE_URL`  is already populated. This should have been created automatically by Heroku.
    -   The  `DATABASE_URL`  should be copied into your local  `.env`, created during the cloning process.
    -   To make authenticated requests to this API (e.g. from a fontend application) you are required to add the key  `CLIENT_ORIGIN`  with the value set as the URL you will be sending the authentication request from.
    -   Additionally, a  `CLIENT_ORIGIN_DEV`  key can be set with the value of a development server (IP or URL) for use during local development.

#### [](https://github.com/vivignutz/balcongardens-drf-api#heroku-deployment)Heroku Deployment

In the Deploy tab:

1.  Connect your Heroku account to your Github Repository following these steps:
    -   Click on the  `Deploy`  tab and choose  `Github-Connect to Github`.
    -   Enter the GitHub repository name and click on  `Search`.
    -   Choose the correct repository for your application and click on  `Connect`.
2.  You can then choose to deploy the project manually or automatically, automatic deployment will generate a new application every time you push a change to Github, whereas manual deployment requires you to push the  `Deploy Branch`  button whenever you want a change made.
3.  Once you have chosen your deployment method and have clicked  `Deploy Branch`  your application will be built and you should now see the  `View`  button, click this to open your application.

## [](https://github.com/vivignutz/balcongardens-drf-api#credits)Credits

### [](https://github.com/vivignutz/balcongardens-drf-api#online-resources)Online resources

-   [Django Documentation](https://docs.djangoproject.com/en/3.2/)
-   [Django REST Documentation](https://www.django-rest-framework.org/)
-   [Python Documentation](https://docs.python.org/3/)
-   [Youtube tutorials](https://www.youtube.com/)

### [](https://github.com/vivignutz/balcongardens-drf-api#code)Code

-   Code Institute DRF Tutorial Project, used through as a basis for the creation of this API
    -   CREDIT: Code Institute DRF-API Tutuorial Project
    -   URL:  [https://github.com/Code-Institute-Solutions/drf-api](https://github.com/Code-Institute-Solutions/drf-api)

### [](https://github.com/vivignutz/balcongardens-drf-api#acknowledgements)Acknowledgements

-   The tutor support team at Code Institute for their support.
-   My Code Institute Mentor, the best one of the CI school, for feedback, help and suggestions.
-   The Code Institute Slack community, specially to Tony, the colleague for his patience to teach me.

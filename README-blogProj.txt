# Blogsite

The project is a blog site ,where a normal user can read posts and a logged in user can  subscribe to a certain category of posts write comments. The administrator has full control of the blog he can add users ,block them or even delete them or he can promote them to be administrators too. Also ,an administrator  can add categories ,tags posts and put a list of forbidden words to be displayed as stars.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites


In order to run this project you need to have:
1-MySQL database
2-Apache2 server
3-Django  framework
4-python package

refer to the official sites to install them if you don't have them already 

### Installing
1-make a database with a name and password of your choice on MySQL

2-clone the repository from gitHub.com using this url:
https://github.com/Minos32x/PythonProject.git 

3-open the settings.py file in PythonProject/Blogz/Blogz
fill DATABASES with the proper info as demonstrated

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',
//1-put your database name
        'USER': '',
/2-put the user name of your database
        'PASSWORD': '',
//3-put the password of your database
    }
}

4-go to  PythonProject/Blogz using the terminal  and perform the following commands
  pyhton manage.py makemigrations 

  python manage.py migrate

  python manage.py runserver


5-go to your browser ang write in the url bar:
 127.0.0.1:8000/blogersite/home

and voila your in the the home page of your blog you can now perform all the actions you discussed before in the introduction  depending on whether you are a logged in user o r Not a logged in user or an administrator.




## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [apache2](https://httpd.apache.org/) - Used as a server
* [MySQL](https://www.mysql.com/) - Used to build a database


## Versioning

We use [gitHub](http://github.com/) for versioning. For the versions available, see the [tags on this repository](https://github.com/Minos32x/PythonProject.git). 

## Authors
Team H

Mina Samy
Amira 
Kamal Magdy
Rola Mamdouh



## Acknowledgments

* Great thanks to our instructors for their informative lectures 
and to all our colleagues who were always ready to help!


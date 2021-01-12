# **DevelopsToday Task**

For any questions:

email: kolenat2002@gmail.com

telegram : @arc_lena

Deployment link: [https://rocky-spire-00690.herokuapp.com/](https://rocky-spire-00690.herokuapp.com/)

Postman collection link:  [https://documenter.getpostman.com/view/12674086/TVzSiGeW](https://documenter.getpostman.com/view/12674086/TVzSiGeW)

Code formatted with black.

Flake8:
- news\tests.py:1:1: F401 'django.test.TestCase' imported but unused
- news\migrations\0001_initial.py:66:80: E501 line too long (83 > 79 characters)
- developstoday\settings.py:101:80: E501 line too long (91 > 79 characters)
- developstoday\settings.py:104:80: E501 line too long (81 > 79 characters)
- developstoday\settings.py:110:80: E501 line too long (83 > 79 characters)

They are default, created with django project.

### _api/docs/_ : url for swagger

## *Running locally (Windows)*

1. Clone repo '' 
2. Create virtualenv 'virtualenv venv' 
3. Activate by command 'venv\Scripts\activate'
4. Run 'docker-compose build'
5. Run 'docker-compose up'
6. In another terminal repeat 1, 2 and 3 steps and run 'docker-compose run web python manage.py createsuperuser'
7. Name - admin, email - blank, password - developstoday

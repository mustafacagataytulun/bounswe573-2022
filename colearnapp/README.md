# ColearnApp
A web application written in [Python](https://www.python.org/) by using [Django](https://www.djangoproject.com/) framework.

[![CircleCI](https://img.shields.io/circleci/build/github/mustafacagataytulun/bounswe573-2022/main.svg?logo=circleci&logoColor=fff&label=CircleCI)](https://circleci.com/gh/mustafacagataytulun/bounswe573-2022/tree/main)

## Purpose
This web application is created as an assignment for SWE 573 course in Boğaziçi University. It allows people to create colearning spaces and share knowledge.

## Development
Required Python package information is provided in _requirements.txt_ file. So, you can install dependencies like this:

```bash
pip install -r requirements.txt
```

After that, the application can be run on development server like this:

```bash
python manage.py runserver
```

## CI/CD
The application uses CircleCI as a CI/CD tool. It is currently in progress.

[https://app.circleci.com/pipelines/github/mustafacagataytulun/bounswe573-2022](https://app.circleci.com/pipelines/github/mustafacagataytulun/bounswe573-2022)

## Deployment
The application is hosted on [https://colearnapp.mustafatulun.com](https://colearnapp.mustafatulun.com).

## Attributions
This application uses following assets:

- [Bootstrap Starter Template](https://startbootstrap.com/template/bare) under [MIT License](https://github.com/startbootstrap/startbootstrap-bare/blob/master/LICENSE)
- [Profile avatar placeholder large](https://commons.wikimedia.org/wiki/File:Profile_avatar_placeholder_large.png) under [BSD License](http://opensource.org/licenses/bsd-license.php)

This application uses following libraries:

- [django-bootstrap5](https://github.com/zostera/django-bootstrap5) under [BSD 3-Clause License](https://github.com/zostera/django-bootstrap5/blob/main/LICENSE)
- [Django Markdownify](https://github.com/erwinmatijsen/django-markdownify) under [MIT License](https://github.com/erwinmatijsen/django-markdownify/blob/master/LICENSE)
- [django storages](https://github.com/jschneier/django-storages) under [BSD 3-Clause License](https://github.com/jschneier/django-storages/blob/master/LICENSE)
- [Psycopg](https://www.psycopg.org/) under [GNU Lesser General Public License](https://github.com/psycopg/psycopg2/blob/master/LICENSE)

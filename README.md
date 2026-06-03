![Python](https://img.shields.io/badge/Python-3.14-blue)
![Django](https://img.shields.io/badge/Django-6.x-green)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple)
![Docker](https://img.shields.io/badge/docker-ready-blue)

# Django Notes App

A note-taking web application built with Django 6.

## Features

* Create notes
* View notes
* Edit notes
* Delete notes
* Bootstrap 5 UI
* User authentication
* Search
* Pagination
* Profile

## Tech Stack

* Python 3
* Django 6
* Bootstrap 5

## Installation

Clone repository:

```bash
git clone https://github.com/prs2rnn/django-notes-app.git
cd django-notes-app
```

Create virtual environment and install dependencies:

```bash
poetry install
```

Apply migrations:

```bash
make migrate
```

Run server:

```bash
make runserver
```

Open:

http://127.0.0.1:8000/

## Screenshots

![](./screenshots/home.png)
![](./screenshots/notes.png)
![](./screenshots/details.png)

## Future Improvements

* Categories
* Tags
* REST API

## Contributing

Contributions are welcome!

You can help by:

- Reporting bugs
- Suggesting features
- Improving architecture
- Writing tests

## License

This project is licensed under the MIT License.

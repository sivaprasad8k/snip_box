# SnipBox Backend

SnipBox is a simple note-taking app that allows users to save short text snippets and organize them with tags. The snippets can be categorized by title, note, timestamps, and tags. The app uses JWT (JSON Web Token) for authentication.

## Table of Contents

1. [Project Setup](#project-setup)
2. [Running the Project](#running-the-project)
   - [Using Docker](#using-docker)
   - [Using Virtual Environment (Direct Setup)](#using-virtual-environment-direct-setup)

---

## Project Setup

This project is built using Django 5.1.5 and Django Rest Framework (DRF). The backend uses JWT for authentication, and the database stores snippets and tags with relationships between them.

### Requirements

- Python 3.11 or higher (for virtual environment setup)
- Docker (if using Docker)
- Docker Compose (for orchestrating services)
- Django 5.1.5
- Django Rest Framework
- Simple JWT for authentication

---

## Running the Project

Follow these steps to set up the backend on your local machine.

### Clone the Repository

```bash
git clone https://github.com/sivaprasad8k/snip_box.git
cd snipbox-backend
```
### Using Docker
Build the Docker Image
Ensure you have Docker installed. From the project root directory, build the Docker image by running:

```bash
docker build -t snipbox .
```
Run the Docker Compose
After building the image, run the following command to start the services:

```bash
docker-compose up
```
This will start the backend service and any other dependencies defined in the docker-compose.yml file.

### Using Virtual Environment (Direct Setup)
Create and Activate a Virtual Environment
Run the following commands to set up and activate a virtual environment:

```bash
virtualenv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
# Install the required dependencies using pip:
pip install -r requirements.txt
# Set Up the Database
# Run migrations to set up the database:
python manage.py makemigrations
python manage.py migrate
````
### Creating a Superuser
To access the Django Admin interface and manage users, snippets, and tags, you'll need to create a superuser account. Follow these steps:

Run the following command to create a superuser:

```bash
python manage.py createsuperuser
# You will be prompted to enter a username, email, and password for the superuser. Make sure to remember the credentials.
# Example:
# Username: admin
# Email: admin@example.com
# Password: ********
```
After creating the superuser, you can log in to the Django Admin interface at:

http://127.0.0.1:8000/admin/

Use the superuser credentials you just created to log in.

Running the Server
To start the development server, use the following command:

```bash
python manage.py runserver
```
snipbox will be available at:
http://127.0.0.1:8000/
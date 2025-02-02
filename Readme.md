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
# Start the Server
# Finally, start the development server:
python manage.py runserver
```
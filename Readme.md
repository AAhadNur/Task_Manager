# Task Manager

A Django web app for users to create, manage, and organize tasks efficiently. Includes features like due dates, priority levels, and photo attachments.

### Installation / Set up

--> Clone the repository using the command below :

```bash
git clone https://github.com/AAhadNur/Task_Manager.git
```

--> Move into the directory where we have the project files :

```bash
cd StudyBud
```

--> Create a virtual environment :

```bash
pip install virtualenv
virtualenv envname
```

--> Activate the virtual environment :

```bash
source envname\bin\activate
```

--> Install the requirements :

```bash
pip install -r requirements.txt
```

--> Create the .env file and configure it :

```bash
echo "DEBUG = True" >> .env
```

--> Apply Database Migrations :

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

--> Load Data from data.json :

```bash
python3 manage.py loaddata data.json
```

#

### Running the App

--> To run the App, we use :

```bash
python3 manage.py runserver
```

> ⚠ Then, the development server will be started at `http://127.0.0.1:8000/`

### Environment variables set up instruction and their usage

--> Create the `.env` File :

```bash
touch .env
```

--> Add all the environment variables needed for this project :

**Django Settings:**

- SECRET_KEY: This should be replaced with a secret key for your Django application, used for cryptographic operations.
- DEBUG: A boolean setting that controls whether your application runs in debug mode. Set to True for development but should be False in production.

**Database Configuration:**

- DB_ENGINE: Specifies the database engine. In this case, it's set to PostgreSQL.
- DB_NAME, DB_USER, DB_PASSWORD: These should be replaced with your actual database name, username, and password.
- DB_HOST: The hostname or IP address of the database server.
- DB_PORT: The port on which the database server is listening.

**Email Configuration:**

- EMAIL_HOST: The hostname of your email server (SMTP server).
- EMAIL_PORT: The port used for sending emails (e.g., 587 for TLS).
- EMAIL_HOST_USER: Your email address used to authenticate with the email server.
- EMAIL_HOST_PASSWORD: Your email password or an application-specific password.
- EMAIL_USE_TLS: A boolean setting indicating whether to use TLS for secure email communication. Set to True if your email server supports TLS.

> ⚠ We set up our settings.py file to load variables from .env file automatically

### API Documentation

#### List of All Tasks

Endpoint: `http://localhost:8000/api/tasks`

- **HTTP Method**: GET
- **Description**: Retrieve a list of all tasks.
- **Authentication**: Required (User authentication)
- **Authorization**: Required (Authenticated users can access)
- **Response Format**: JSON

#### Retrieve a Single Task

Endpoint: `http://localhost:8000/api/tasks/{id}`

- **HTTP Method**: GET
- **Description**: Retrieve details of a specific task by its ID.
- **Authentication**: Required (User authentication)
- **Authorization**: Required (Authenticated users can access)
- **Response Format**: JSON

#### Create a Task

Endpoint: `http://localhost:8000/api/tasks/create`

- **HTTP Method**: POST
- **Description**: Create a new task.
- **Authentication**: Required (User authentication)
- **Authorization**: Required (Authenticated users can access)
- **Request Format**: JSON
- **Response Format**: JSON

#### Update a Task

Endpoint: `http://localhost:8000/api/tasks/{id}`

- **HTTP Method**: PUT
- **Description**: Update details of a specific task by its ID.
- **Authentication**: Required (User authentication)
- **Authorization**: Required (Authenticated users can access and update their tasks)
- **Request Format**: JSON
- **Response Format**: JSON

#### Delete a Task

Endpoint: `http://localhost:8000/api/tasks/{id}`

- **HTTP Method**: DELETE
- **Description**: Delete a specific task by its ID.
- **Authentication**: Required (User authentication)
- **Authorization**: Required (Authenticated users can access and delete their tasks)
- **Response Format**: JSON

Please note that authentication and authorization are required for most API endpoints to ensure data security and privacy. Users should authenticate and be authorized to access and perform operations on tasks.

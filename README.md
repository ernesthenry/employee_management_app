# Employee Management Portal

## Backend Setup

1. Create a virtual environment and activate it:
    ```sh
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Update `settings.py` with your PostgreSQL database credentials.

4. Run migrations and create a superuser:
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    ```

5. Run the Django server:
    ```sh
    python manage.py runserver
    ```

## Frontend Setup

1. Install the required packages:
    ```sh
    npm install
    ```

2. Run the React development server:
    ```sh
    npm start
    ```

## Features

- User authentication using JWT.
- CRUD operations for employees.
- Export employee data to CSV.
- Responsive UI with React and TypeScript.

## Video Walk-through

Watch the project demo and walk-through here: [Loom Video](#)


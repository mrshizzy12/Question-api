# Welcome to Question-API!

The question-api is a beginner friendly introductory tutorial app on how to build 
web api's using python and FastAPi. It covers the basic CRUD operations of backend development and
it leverages fastapi's native async/await functionality, pydantic models for data serialization. It also covers authentication/authorization using oAuth2 and json web token. The project includes basic written tests using pytest.

## How to run this application

1. create a python virtual environment

     *For Unix and Mac computers:*

    ```
    $ python3 -m venv env
    $ source venv/bin/activate
    (env) $ _
    ```

    *For Windows computers:*

    ```
    $ python -m venv env
    $ venv\bin\activate
    (env) $ _
    ```

2. Istall the project dependencies into the virtual environment using [pip]:

    ```
    (env) $ pip install -r requirements.txt
    ```
    
3. Create database migrations and upgrade:

    **Note: postgresql is a requirement for this project.**

    ```
    (env) $ alembic init migrations
    (env) $ alembic revision --autogenerate -m "initial migration"
    (env) $ alembic upgrade head
    ```

4. Start the development web server:

    ```
    (env) $ python manage.py
    ```

5. To view the api endpoints, open `http://localhost:8000/docs` on your web browser to leverage
    openApi.
   Alternatively, you can use postman or thunder client(visual studio code extension).


6. to run tests:
    ```
    (env) $ pytest
    ```

    **NOTE: you must have pytest installed in your virtual environment.**


Happy Learning!!!
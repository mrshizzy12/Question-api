# Welcome to Question-API!

The question-api is a beginner friendly introductory tutorial app on how to build 
web api's using python and FastAPi. It covers the basic CRUD operations of backend development and
it leverages fastapi's native async/await functionality, pydantic models for data serialization. It also covers authentication/authorization using oAuth2 and json web token. The project includes basic written tests using pytest.

## How to run this application

1. create a python virtual environment

     *For Unix and Mac computers:*

    ```
    $ python3 -m venv venv
    $ source venv/bin/activate
    (venv) $ _
    ```

    *For Windows computers:*

    ```
    $ python -m venv venv
    $ venv\bin\activate
    (venv) $ _
    ```

2. Istall the Python dependencies into the virtual environment using [pip]:

    ```
    (venv) $ pip install -r requirements.txt
    ```

3. Start the development web server:

    ```
    (venv) $ python manage.py


5. To view the api endpoints, open `http://localhost:8000/docs` on your web browser to leverage openApi.
   or you could use postman or thunder client for visual studio.


6. to run tests:
    ```
    (venv) $ pytest

    NOTE: you must have pytest installed in your virtual environment.


Happy Learning!!!
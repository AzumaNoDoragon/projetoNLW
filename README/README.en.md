# Event Management API

This is a Python application that allows the registration and management of events and their participants. The API was built with Flask and uses SQLAlchemy for data manipulation in the database. The application follows good REST API development practices, using the repository, interface, and controller design pattern. Additionally, it includes data validation with Cerberus and automated tests with Pytest.

## Technologies Used

- **Python**: Main programming language
- **Flask**: Framework for creating the REST API
- **SQLAlchemy**: ORM for database manipulation
- **Cerberus**: Library for data validation
- **Pytest**: Framework for automated tests
- **Postman**: Tool for testing and validating API routes

## Features

- Event registration
- Event data updating
- Participant management
- Data validation
- Automated tests

## How to Run the Project

1. Clone o repositório:
   ```bash
   git clone https://github.com/usuario/repositorio.git
2. intall the dependencies:
   ```bash
   pip install -r requirements.txt
3. Run the database (if needed):
   ```bash
   python manage.py db upgrade
4. Start the Flask server:
   ```bash
   python app.py
5. Acess the API in the browser or Postman:
   ```bash
   http://127.0.0.1:5000

## Tests
Automated tests can be run with Pytest:
```bash
pytest
```

### Contributing
If you would like to contribute to the development of this project, feel free to open *`issues`* or *`pull requests`*.

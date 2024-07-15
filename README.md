# FastApi-Postgres-Integration

This project demonstrates how to integrate PostgreSQL with FastAPI by building a simple quiz game. It includes two models: `Question` and `Choice`, with Pydantic used for data validation. This README provides an overview of the project setup, installation instructions, and usage.

## Table of Contents

- [Project Overview](#project-overview)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Running Tests](#running-tests)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The project consists of a FastAPI application integrated with a PostgreSQL database. It allows users to create and manage quiz questions and their respective choices. The main features include:

- Creating, reading, updating, and deleting quiz questions.
- Creating, reading, updating, and deleting choices for each question.
- Data validation using Pydantic models.

## Installation

Follow these steps to set up and run the project locally.

### Prerequisites

- Python 3.8 or higher
- PostgreSQL
- `pip` (Python package installer)

### Steps

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/FastApi-Postgres-Integration.git
   cd FastApi-Postgres-Integration
   ```

2. **Create a virtual environment and activate it:**

   ```sh
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

4. **Set up the PostgreSQL database:**

   - Create a new PostgreSQL database.
   - Update the database configuration in the `.env` file.

5. **Apply the database migrations:**

   ```sh
   alembic upgrade head
   ```

## Configuration

The project uses environment variables for configuration. Create a `.env` file in the root directory of the project with the following content:

```env
DATABASE_URL=postgresql://username:password@localhost/dbname
```

Replace `username`, `password`, and `dbname` with your PostgreSQL credentials and database name.

## Usage

To run the FastAPI application, execute the following command:

```sh
uvicorn main:app --reload
```

The application will be available at `http://127.0.0.1:8000`.

## API Endpoints

The following API endpoints are available:

### Questions

- **GET** `/questions/`: Retrieve all questions.
- **GET** `/questions/{id}/`: Retrieve a specific question by ID.
- **POST** `/questions/`: Create a new question.


### Choices

- **GET** `/choices/`: Retrieve all choices.
- **GET** `/choices/{id}/`: Retrieve a specific choice by ID.
- **POST** `/choices/`: Create a new choice.


## Running Tests

To run the tests, use the following command:

```sh
pytest
```

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes.
4. Push the changes to your fork.
5. Submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to reach out if you have any questions or suggestions! Happy coding!

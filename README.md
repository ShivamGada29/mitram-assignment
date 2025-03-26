# Project Overview

This project integrates with an external API to fetch the initial status of a task when it is created. If the API is unresponsive or returns an error, the task's status defaults to pending.

## Design Choices

* Asynchronous API Calls: httpx.AsyncClient is used to avoid blocking operations.

* Graceful Error Handling: Implements timeouts and error logging to ensure system stability.

* Default Fallback Mechanism: If the external API fails, the system assigns a default status (pending).

* Logging: Errors and API failures are logged for debugging.


## Steps to run the application

1. Make sure you have Python 3.9+
2. Make sure you have mysql on your local system running, otherwise you might run into errors.
3. create python virtual environment.
4. python -m venv venv
5. pip install -r requirements.txt (Command to run)
6. uvicorn main:app --host 127.0.0.1 --port 8080  --reload (Command to run)

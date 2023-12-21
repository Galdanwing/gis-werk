## Installation

To set up and run the project, ensure that you have Docker and Docker Compose installed on your system. Once installed, use the following Makefile commands:

- To start the project:
  - `make start-project`

- To run the unit tests:
  - `make run-tests`

- To create a superuser:
  - `make create-superuser`

- To import data, make sure the `municipalities_nl.geojson` file is located in `geoProject/geoProject`, and run:
  - `make import-data`

## Accessing the Application

After running the commands, open your web browser and navigate to `localhost:8000/api/schema/swagger-ui` to explore the available endpoints and interact with the application.

## Code Quality

To ensure consistent code standards across development, the project uses pre-commit hooks. Run the following commands, as specified in the Makefile, to install and utilize pre-commit:

- `make install-pre-commit`
- `make run-pre-commit`

These commands help maintain code quality by enforcing predefined standards and best practices.

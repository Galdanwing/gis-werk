# Gis-werk

Gis-werk or geoProject is a Django website for ingesting and showing municipality data.

## Installation

You can use a make command to install the project, it requires docker and docker compose and goes like this:

```bash
make start-project
```

## Usage

The project can do a few things:

### Ingest data
```bash
make import-data
```

After this you can see the data, either in the API, visually exposed via swagger at:
`http://127.0.0.1:8000/api/schema/swagger-ui/`.
Where after creating a token for your given user, which you can create via `make create-superuser` you can use the endpoints.
Or by looking at the admin at `http://127.0.0.1:8000/admin`

## Contributing

You can contribute to the repo by pushing changes, make sure you install `pre-commit`
 first via `pipx` or other means to run the linting suite.
Also make sure your tests run via `make run-tests`

## Things that were skipped
Given the interest of time I skipped a few things along the lines, that I would normally include in a project:
- Error handling, most of the code assumes everything is input properly, if a file is not found for the ingest the error message is not great for example.
- Negative tests, currently I only tested happy paths but it's vital that you also test what happens when non normal things occur
- CI, I've come to learn from experience that just having an easily installable set of linting rules still might get skipped by some devs. So CI to make sure these rules are ran is vital.
- Factories for data generation. Very useful for testing, but due to limited amount I did, not needed.

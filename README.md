# UVRS2021_app
A dashboard for [UVRS](https://uppervalleyrunningclub.org/2021-upper-valley-running-series) scoring.

## github, deployment, environment, and tests
* `build.py` script to build `output_data` from `input_data`
* `app.py` contains the frontend logic for the Dash app
* `requirements.txt` contains the dependencies for the virtualenv
* `Procfile` is necessary for Heroku deployment
* `.github/workflows/main.yml` controls github action to deploy to Heroku on a push
* `tests/`: example use is as follows (in the virtualenv)
```
(venv) otto@pop-os:~/Projects/UVRS2021_app$ python -m pytest --log-cli-level=info -s tests
```

## python code
### `utils/` directory with the backend python code
### classes
* `Person`: a person in the membership list
* `Race`: a UVRS race
* `Racer`: a racer in a UVRS race
* `Participant`: a person that has been matched to at least one racer

## data

### `input_data/`
* `rosters_private/` contains local snapshots of the UVRC membership list (not committed for privacy)
* `race_data/` directory contains the tabular data for the UVRS races, directories are named with race dates of the form YYYYMMDD

### `output_data/`
* `tables/df_YYYYMMDDHHMMSS.csv` snapshot scores table to be used by `app.py` including all races
* `filtered_tables/df_YYYYMMDDHHMMSS.csv` snapshot scores table to be used by `app.py` filtering top N races for each individual
* `participation/snapshot_YYYYMMDDHHMMSS.csv` snapshot of all matched UVRS participants for a given membership snapshot (with private data excluded for privacy) with columns `name`, `age_group`, `number_of_races_participated_in`, `total_score`

## References
* [https://stackoverflow.com/questions/58873457/gunicorn-20-failed-to-find-application-object-app-server-in-index](https://stackoverflow.com/questions/58873457/gunicorn-20-failed-to-find-application-object-app-server-in-index)
* [https://dash.plotly.com/basic-callbacks](https://dash.plotly.com/basic-callbacks)
* [https://dash.plotly.com/deployment](https://dash.plotly.com/deployment)
* [https://github.com/marketplace/actions/deploy-to-heroku](https://github.com/marketplace/actions/deploy-to-heroku)
* [https://stackoverflow.com/questions/54106071/how-can-i-set-up-a-virtual-environment-for-python-in-visual-studio-code](https://stackoverflow.com/questions/54106071/how-can-i-set-up-a-virtual-environment-for-python-in-visual-studio-code)
* [https://developers.google.com/drive/api/v3/quickstart/python](https://developers.google.com/drive/api/v3/quickstart/python)
* [https://developers.google.com/sheets/api/quickstart/python](https://developers.google.com/sheets/api/quickstart/python)

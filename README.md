# UVRS2021_app
A Dash app deployed via github actions.

## github, deployment, and environment
* `.gitignore`
* `app.py` contains the frontend logic for the Dash app
* `requirements.txt` contains the dependencies for the virtualenv
* `Procfile` is necessary for Heroku deployment
* `.github/workflows/main.yml` controls github action to deploy to Heroku on a push

## database
* `private_data/` contains a local copy of the UVRC membership list (not committed)
* `race_data/` directory contains the tabular data for the UVRS races

## python code
* `utils/` directory with the python code

## References
* [https://stackoverflow.com/questions/58873457/gunicorn-20-failed-to-find-application-object-app-server-in-index](https://stackoverflow.com/questions/58873457/gunicorn-20-failed-to-find-application-object-app-server-in-index)
* [https://dash.plotly.com/basic-callbacks](https://dash.plotly.com/basic-callbacks)
* [https://dash.plotly.com/deployment](https://dash.plotly.com/deployment)
* [https://github.com/marketplace/actions/deploy-to-heroku](https://github.com/marketplace/actions/deploy-to-heroku)
* [https://stackoverflow.com/questions/54106071/how-can-i-set-up-a-virtual-environment-for-python-in-visual-studio-code](https://stackoverflow.com/questions/54106071/how-can-i-set-up-a-virtual-environment-for-python-in-visual-studio-code)
* [https://developers.google.com/drive/api/v3/quickstart/python](https://developers.google.com/drive/api/v3/quickstart/python)
* [https://developers.google.com/sheets/api/quickstart/python](https://developers.google.com/sheets/api/quickstart/python)

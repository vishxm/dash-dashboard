# Welcome to the repository!
This is a __basic dashboard__ which takes in data from a .csv (that has only 8 records) and then gives user the control to display whatever he wants based on the _filters in the data table._ __Dash by Plotly__ has been used in this project. One also can __export__ the data table in its current state and save it as a _.xls file_. 

## Installation
> `pip install -r requirements.txt`

This requires the framework _Dash_ and its libraries and dependencies. It also requires pandas for reading the .csv file.  _gunicorn_ is used to deploy the app on heroku.

## Deployment 
App has been deployed on [Heroku](https://bq-test-4.herokuapp.com/). Procfile has been uploaded with it. It has been deployed in United State servers (because it doesn't have servers in India) so the callbacks may take _few hundred milliseconds_.
## Layout 
![Layout of the application](https://raw.githubusercontent.com/vishxm/dash-table-app/master/layout.png)
## Callback flow-graph
![Callback](https://raw.githubusercontent.com/vishxm/bq-test-1/master/callback.png)
Here, the _item-selector_ is the id of checklist component. Whatever changes are made to that checklist, they are reflected in _data-table_ (the Dash data table) and _table-graph_ (the lineplot of the data table).
Whatever changes are made to the data table using either filters or the checklist, the changes are also reflected in the lineplot!

## Future additions

* Better UI.
* Adding a bootstrap theme.

## Thank you!


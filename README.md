# suade_analytics

__Suade Labs Analytics Challenge__

This is a Flask API that parses ```.csv``` data for a demo shop, for a given date in the format __YYYY-MM-DD__

## Info
Due to the time constraints of this challenge (24 hrs) I had some challenges with the structure of the application. This app is loading the .csv files into memory and directly querying the files using python and some SQL queries brought in from the __pandasql__ python package.

This __IS NOT__ an optimal solution by any means. If i had more time, I would read these .csv files into a MySQL database (preferably through Amazon RDS using an EC2 instance) then parse the data with actual SQL queries. An actual RDMS would help this data parsing immensely.

## Build
To build, Create a __VM__ using Python __3.9__ import requirements from
```
suade_labs/requirements.txt
```

And point the configuration class to
```
suade_labs/app.py
```

If using terminal, just run
And point the configuration class to
```
python app.py
```
## Running
API will be running on http://127.0.0.1:5000/ with the swagger docs on http://127.0.0.1:5000/apidocs

## Example Output

http://127.0.0.1:5000/get_analytics_report/2019-08-02
```
{
  "commissions": {
    "order_average": 10514893.66,
    "promotions": {
      "1": 22633010.44,
      "2": 19293679.09,
      "3": 22016151.23,
      "4": 15290844.79,
      "5": 13743272.78
    },
    "total": 92976958.32
  },
  "customers": 10,
  "discount_rate_avg": 0.13,
  "items": 123,
  "order_total_avg": 164998295.76,
  "total_discount_amount": 150457385.36
}
```
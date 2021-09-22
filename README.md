# We+ Test

## Task

> Give 25 list nearby hospitals base on user geolocation 
> User geolocation can be changed base on user location
> Give information about distance between user and hospital in kilometer

## How to run

#### Manage the working directory

- create new folder in your computer and name it as u want example PorjectFolder
- inside the folder u create before create virualenv folder example venv
- also clone this repo example we-_test

```
|- PorjectFolder
    |- we-_test
    |- venv
```

#### Run Application

- Activate virtualenv
```bash=
Linux/PorjectFolder$ source venv/bin/activate
Windiws/PorjectFolder> source venv/Scripts/activate
```
- in your repository folder copy and rename .env.example as .env

```bash=
Linux/PorjectFolder$ cd we-_test
Linux/PorjectFolder/we-_test$ cp .env.example .env
```
- install the requirements (make sure ur venv is already active)
```bash=
Linux/PorjectFolder/we-_test$ pip install -r requirements.txt
```
- run the service
```bash=
python app.py
```
![](https://i.imgur.com/Uh33E2L.png)

:rocket: 

#### Result Endpoints

> http://127.0.0.1:5000/hospital/list

Enpoint to get all list of hospital in database

![](https://i.imgur.com/xQIMbht.png)

> http://127.0.0.1:5000/hospital/my-location

Endpoint to get your location (base on ur IP)

![](https://i.imgur.com/bKEdOJF.png)

> http://127.0.0.1:5000/hospital/nearby

![](https://i.imgur.com/r1emvZ0.png)
![](https://i.imgur.com/SIBnkPd.png)
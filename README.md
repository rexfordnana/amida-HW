#How to Run
***
##Step 1:
Clone Repo into local folder

Create a virtual environment and activate it

>For MAC/LINUX:
```bash
$ python3 -m venv myvenv

```

The command above will create a directory called myvenv (or whatever name you chose) that contains your virtual environment (basically a bunch of directory and files).

##Step 2:
Start your virtual environment by running:
```bash
$ source myvenv/bin/activate
```

With your virtualenv started you can install Django
```bash
(myvenv) ~$ pip install django
```
>That's it! You're now (finally) ready to RUN!
##Step 3:
Start the server by running:
```bash
$python manage.py rumserver 4000
```

Then launch 127.0.0.1:4000 from your browser
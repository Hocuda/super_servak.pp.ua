# Super_servak.pp.ua

## Python Django online product mall

This is an online product mall, written in the django framework with pretty design
and self-tuned DNS and hosting

Here is the [link](http://super_servak.pp.ua:8000/)

## Download and boot

### For Linux
```
git clone https://github.com/Hocuda/super_servak.pp.ua
cd super_servak.pp.ua
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
script -c 'python3 manage.py runserver' log.txt
```

### Fot Windows
```
git clone https://github.com/Hocuda/super_servak.pp.ua
cd super_servak.pp.ua
python -m venv venv
venv/Scripts/activate
pip install -r requirements.txt
python manage.py runserver
```
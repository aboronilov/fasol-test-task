# Install packages
pip install -r requirements.txt

# CSS
python manage.py collectstatic --no-input

# Migrate
python manage.py migrate

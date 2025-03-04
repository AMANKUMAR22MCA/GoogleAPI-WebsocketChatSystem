import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "google_apis.settings")
django.setup()

from django.contrib.auth.models import User

# Function to create a user if they don't exist
def create_user(username, password):
    if not User.objects.filter(username=username).exists():
        user = User.objects.create_user(username=username, password=password)
        user.is_staff = True
        user.save()
        print(f"User '{username}' created successfully!")
    else:
        print(f"User '{username}' already exists.")

# Create users
create_user("user_a", "password123")
create_user("user_b", "password123")

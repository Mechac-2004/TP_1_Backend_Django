from booking.models import User
from django.contrib.auth.hashers import make_password

for i in range(1, 3):
    sexe = 'M' if i % 2 == 1 else 'F'
    role = 'client'
    if i == 1:
        role = 'administrateur'
    
    User.objects.create(
        email=f"user{i}@example.com",
        username=f"user_{i}",
        first_name=f"Prénom_{i}",
        last_name=f"Nom_{i}",
        password=make_password('password123'), 
        role=role,
        is_staff=True if i == 1 else False,
        is_superuser=True if i == 1 else False
    )

print("Création de 3 utilisateurs terminée.")


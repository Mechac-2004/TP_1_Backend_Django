from booking.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group

# Assure-toi que les groupes existent
admin_group, _ = Group.objects.get_or_create(name="Admin")
client_group, _ = Group.objects.get_or_create(name="Client")

for i in range(1, 3):
    sexe = 'M' if i % 2 == 1 else 'F'
    role = 'client'
    if i == 1:
        role = 'administrateur'
    
    user = User.objects.create(
        email=f"user{i}@example.com",
        username=f"user{i}",
        first_name=f"Prénom_{i}",
        last_name=f"Nom_{i}",
        password=make_password('password123'), 
        role=role,
        is_staff=True if i == 1 else False,
        is_superuser=True if i == 1 else False
    )

    # Ajouter l'utilisateur au groupe correspondant
    if role == 'administrateur':
        user.groups.add(admin_group)
    else:
        user.groups.add(client_group)

print("Création des utilisateurs Admin et Client terminée.")

# Pour créer les utilisateur il faut faire    python manage.py shell

# Ensuite écrit la requête     exec(open("file.py").read())
# Exercice numéro 1 
## introduction : 
Le but de cet exercice est de creer mon premier projet django.
Il me faut 4 vues : 
- la creation
- la modification
- la suppression
- l'affichage d'une facture
- l'affichage de toutes les factures

Pour ce faire, je dois avoir un model de donnee solide pour ne pas 
perdre de temps par la suite.

## prerequis
Pour commencer, il faut avoir un dossier avec un venv pour le projet python,
dans lequel je viens installer django : `pip install -r requirement.txt`

Ensuite, on peut lancer le container de base de donnee avec `docker compose up --build -d`.

Une fois ça fait, on peut creer le super user et effectuer les migrations des different tables creer dans les models et du superuser : 
- `python manage.py createsuperuser`
- `python manage.py makemigrations`
- `python manage.py migrate`


Pour finir une fois la migration faites et les donnes bien en base, 
on peux taper la commande : `python manage.py runserver` pour lancer le 
serveur python. Si tout fonctionne correctement, le serveur devrais se lancer

## creer son application
A la suite de ca, je vais creer mon application python. pour l'application
facture je ferais cette commande : `python manage.py startapp factures`
ca donneras l'arborescence suivante : 
```
factures/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```


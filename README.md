# Projet Pokemon CRUD API

Ce projet est une API basée sur Django et Django REST Framework qui permet de gérer les actions CRUD pour les entites Pokemon.

## Configuration requise

Avant de commencer, assurez-vous d'avoir les éléments suivants installés sur votre système :

- Docker
- Docker Compose

## Pour lancer l'application :

1. Clonez cette repo sur votre machine locale :
``` 
  git clone <URL_DU_REPO> 
  cd pokedex-api 
 ```

2. Créez un fichier `.env` à la racine du projet et ajoutez-y les variables d'environnement nécessaires, vous pouvez utiliser le contenu de `.env.example`


3. Lancez Docker Compose pour construire et exécuter les contenaires avec :
` docker-compose up --build`
4. Un superuser est crée. Login pour `/admin/`: 
```
username = admin
password = admin
```

5. Une page documentation Swagger est disponible sur `/swagger/`.

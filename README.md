# Développez une application Web en utilisant Django


Projet n°9 de la formation développeur d'Application Python.

:lock: ## Introduction : Voici la liste des contraintes à réspecter pour ce projet  :

Cahier des charges:

Un utilisateur devra pouvoir :

* se connecter et s’inscrire – le site ne doit pas être accessible à un utilisateur non connecté;
* consulter un flux contenant les derniers tickets et les commentaires des utilisateurs qu'il suit, classés par ordre chronologique, les plus récents en premier ;
* créer de nouveaux tickets pour demander une critique sur un livre/article ;
* créer des critiques en réponse à des tickets ;
* créer des critiques qui ne sont pas en réponse à un ticket. Dans le cadre d'un processus en une étape, l'utilisateur créera un ticket puis un commentaire en réponse * à son propre ticket;
* voir, modifier et supprimer ses propres tickets et commentaires ;
* suivre les autres utilisateurs en entrant leur nom d'utilisateur ;
* voir qui il suit et suivre qui il veut ;
* cesser de suivre un utilisateur.


Un développeur devra pouvoir :

* créer un environnement local en utilisant venv, et gérer le site en se basant sur la documentation détaillée présentée dans le fichier README.md.


Le site devra :

* avoir une interface utilisateur correspondant à celle des wireframes ;
* avoir une interface utilisateur propre et minimale ;


:pushpin: ## Utilisation : Voici la liste des outils utilisées pour ce projet :

#### Outils : 

* Python 
* HTML5
* CSS3
* Bootstrap 5

### Librairies Python :

* asgiref==3.5.2
* crispy-bootstrap5==0.7
* Django==4.1.4
* django-crispy-forms==2.0
* Pillow==9.3.0
* sqlparse==0.4.3
* tzdata==2022.7


:pushpin: ## Installation du projet : 



:computer: ### Python
Vous devez avoir Python, version 3.9 minimum, installé sur votre ordinateur (si ce n'est pas le cas vous pouvez le télécharger [ici - Python](https://www.python.org/downloads/))


:mag: Ensuite téléchargez le repo version zip sur github  :


:point_right: Créez un nouveau dossier sur votre bureau avec le nom que vous souhaitez par exemple le nom du projet : LitReview_P9



:point_right: Dé-zippez le contenu du dossier zip dans ce nouveau dossier : LitReview_P9




Une fois cela fait ouvrez le terminal de commande (Invite de commande) :



:point_right: Une fois le terminal ouvert nous allons rejoindre notre bureau dans un premier temps
```
cd desktop
```
:point_right: Ensuite nous allons rejoindre notre nouveau dossier sur le bureau
```
cd LitReview_P9
```
:point_right: Une fois là nous allons créer notre environnement virtuel ( exemple : envVirtuel ) sur python avec cette commande
```
python -m venv envVirtuel
```
:point_right: Une fois l'environnement créé nous allons nous rendre dans le dossier de l'environnement virtuel afin de l'activer:


Pour cela il nous faut récupérer le chemin du dossier:


* Rendez-vous sur votre bureau
* Allez dans le dossier "LitReview_P9"
* Maj + Clic Droit sur le dossier "envVirtuel"
* Faire : "Copier en tant que chemin d'accès"



:point_right: Une fois cela fait, retournez sur le terminal copiez votre chemin d'accès en rajoutant "\Scripts\activate" à la fin :
```
C:\Users\wolf\Desktop\LitReview_P9\envVirtuel\Scripts\activate
```
:point_right: Si tout va bien vous devez voir apparaître un (env) à côté de votre chemin d'accès, comme ceci
```
(env) C:\Users\wolf\Desktop\LitReview_P9>
```
:point_right: Déplacez-vous dans le dossier source du projet qui se nomme LitReview, comme ceci
```
(env) C:\Users\wolf\Desktop\LitReview_P9> cd LitReview
```
:point_right: Maintenant nous allons télécharger les librairies associés au projet nécessaire, pour cela tapez
```
pip install -r requirements.txt
```


:computer: ### Tout est fin prêt, pour lancer votre projet Django sur un navigateur !



:point_right: Pour lancer le serveur tapez la commande suivante :
```
python manage.py runserver
```

Entrer l'adresse suivante dans votre navigateur pour accéder au site : http:/127.0.0.1:8000/

Afin de tester les différentes fonctionalités du site, 3 comptes utilisateurs ont été créés : "Peter" mdp : "peterpassword", "Glaxer" mdp : "password" et "Jean" mdp : "jeanpassword".

Pour accéder à l'interface d'administration::

Aller sur http:/127.0.0.1:8000/admin

Nom du compte: Scar
Mot de passe: password

:mag: Il ne vous reste plus qu'à parcourir le site internet LitReview afin d'essayer toutes ces fonctionnalités.



### Générer un rapport Flake8 HTML sur le programme Python :

:point_right: Dans le terminal dans votre dossier :
```
(env) C:\Users\wolf\Desktop\LitReview_P9>
```

:point_right: Pour voir si il y a des erreur de Flake8 :
```
(env) C:\Users\wolf\Desktop\LitReview_P9> Flake8
```

:point_right: Si il n'y a pas d'erreur il ne vous affichera rien et vous aurez de nouveau :
```
(env) C:\Users\wolf\Desktop\LitReview_P9> 
```

:point_right: Pour générer un rapport Flake8 HTML :
```
flake8 --format=html --htmldir=flake-report
```
:point_right: Celà fait un nouveau dossier nommée "Flake-report" est apparue !

:point_right: Vous pouvez vous rendre dedans et ouvrire dans un navigateur le fichier Index.html 

:point_right:La page s'ouvre , si il vous affiche un bandeau vert avec all Good !  - Tout est bon !!  :

<h3 align="left">Languages and Tools:</h3>
<p align="left"> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> </p>




# Gestionnaire de tournoi d'échecs
### Auteur : Nicolas Sylvestre  
### Contact :<sylvestrenicolas@sfr.fr>

## Présentation
### Cet outil est un gestionnaire de tournois d'échecs.  
- Il permet de gérer une base de données de joueurs.
- Il permet de créer un tournoi d'échecs pour 8 joueurs.
- Aucune limite sur les rounds.
- Le tournoi lancé peut être repris à tout moment.
- Une section dédiée à l'affichage d'un rapport d'un tournoi en cours sur le terminal ou en version texte.
- Une section dédiée à l'affichage d'un rapport des tournois précédents sur le terminal ou en version texte.

### Lors de la première exécution du programme, celui-ci va procéder à la création de plusieurs répertoires.
- **data**
- data/**players_list**
- data/**tournament**
- data/**tournament_old**

### Lors de l'enregistrement des joueurs dans la base de données.
- data/**players_list** : Le répertoire **players_list** contiendra un fichier nommé **List_Registered_Players.json**,  
ce fichier sera la base de données des joueurs enregistrés.


### Lors de la création d'un tournoi.
- data/**tournament**/**Nom_Du_Tournoi** : Le répertoire **tournament** contiendra un répertoire qui  
portera le nom du tournoi.


- data/tournament/**Nom_Du_Tournoi**/**Match** : Le répertoire **Match** contiendra des fichiers nommés  
**List_MatchX.json**, ces fichiers permettent de lister les équipes de chaque Round. 


- data/tournament/**Nom_Du_Tournoi**/**Player_Select** : Le répertoire Player_Select contiendra un fichier nommé  
**List_Players_Select.json**, ce fichier contiendra la liste des joueurs selectionnés au tournoi.


- data/tournament/**Nom_Du_Tournoi**/**Rounds** : Le répertoire Rounds contiendra des fichiers nommés **RoundX.json**,  
ces fichiers contiendront les informations des joueurs ainsi que les résultats de chaque Round.
 

- data/tournament/**Nom_Du_Tournoi**/**ScoreBoard** : Le répertoire **ScoreBoard** contiendra un fichier nommé  
**ScoreBoard.json**, ce fichier permet d'afficher le classement des joueurs par scores pendant le tournoi en cours.
 

- data/tournament/**Nom_Du_Tournoi**/**Tournament_Info.json** : Lors de la création d'un tournoi d'échecs, le  
fichier **Tournament_Info.json** contiendra ces informations.


### Création d'un rapport d'un tournoi en cours au format texte.
- data/**Rapport_tournoi_en_cours.txt** : Le fichier **"Rapport_tournoi_en_cours.txt"** contiendra toutes les  
informations sur le tournoi en cours.

### Création d'un rapport des tournois pércédents au format texte.
- data/**Rapport_tournois_précédents.txt** : Le fichier **"Rapport_tournois_précédents.txt"** contiendra toutes les  
informations sur les anciens tournois.

### Lorsqu'un tournoi d'échecs prend fin.
- data/**tournament_old** : Le programme récupère le répertoire portant le **"Nom_Du_Tournoi"**, il le renomme à la date  
du jour puis le déplace dans le réprtoire **tournament_old**

## Prérequis
Installez la dernière version de Python, pour cela, cliquez sur le lien ci-dessous.

<https://fr.wikihow.com/installer-Python>

## Installation sous Windows.
- Suivre les indications **"Méthode 1"**.

## Installation sous Mac / Linux.
- Suivre les indications **"Méthode 2"**.

## Cration d'un répertoire sur le bureau.
Saisir les lignes de commandes suivantes :  

### Ouvrir PowerShell Sous Windows :
```sh
cd desktop   
   ```
```sh
mkdir ChessTournament   
   ```
```sh
cd ChessTournament   
   ```
### Ouvrir Terminal Sous Mac \ Linux :
```sh
cd ~/Desktop   
   ```
```sh
mkdir ChessTournament   
   ```
```sh
cd ChessTournament   
   ```

**Garder PowerShell ou Terminal ouvert.**

## Téléchargement et décompression du Script.  
Cliquer sur le lien ci-dessous pour télécharger le programme.  
<https://github.com/Nico13118/Projet4-V2/archive/refs/heads/master.zip>

Une fois téléchargé, placer le fichier zip dans le répertoire **ChessTournament**, vous allez devoir ensuite  
le décompresser.

## Pour décompresser un fichier zip sous Windows.  
- Faites un clic droit sur le fichier .zip puis sélectionner **"Extraire tout..."**, puis **"Extraire**.


## Pour décompresser un fichier zip sous Mac \ Linux.  
- Cliquez deux fois sur le fichier .zip, l’élément décompressé apparaît dans le même dossier que le fichier .zip.


## Création d'un environnement virtuel.
Saisir la commande suivante :

### Depuis PowerShell sous Windows :
```sh
python -m venv env   
   ```

### Depuis Terminal Sous Mac \ Linux :
```sh
python3 -m venv env   
   ```

## Activation de l'environnement virtuel.
Saisir la commande suivante :

### Depuis PowerShell Sous Windows :  

```sh
env\Scripts\activate.ps1 ou env\Scripts\activate.bat
   ```

### Depuis Terminal sous Mac \ Linux :
```sh
env/bin/activate
   ```

## Installation des packages Python.
Saisir la commande suivante :

### Depuis PowerShell ou Terminal (Windows, Mac \ Linux) :  
```sh
pip install -r requirements.txt
   ```

### Exécution du Script.
Saisir la commande suivante :

### Depuis PowerShell ou Terminal (Windows, Mac \ Linux) :
```sh
python main.py   
   ```

## Utilisation

Lors de l'exécution du programme, vous allez arriver dans le **"MENU PRINCIPAL"**  
### Choix 1 : Gestionnaire de joueurs  
Dans le menu **"GESTIONNAIRE DE JOUEURS"**, vous aurez la possibilité : 
- Choix 0 : Retourner au menu principal
- Choix 1 : Enregistrer des joueurs (Enregistrement des joueurs dans la base de données)
- Choix 2 : Voir la liste des joueurs enregistrés (Consulter la base de données)
- Choix 3 : Supprimer un joueur enregistré (Supprimer un joueur de la base de données)

### Choix 2 : Gestionnaire de tournoi
Dans le menu **"GESTIONNAIRE DE TOURNOI"**, vous aurez la possibilté :  

- Choix 0 : Retourner au menu principal
- Choix 1 : Créer un tournoi
- Choix 2 : Inscrire des joueurs au tournoi
- Choix 3 : Lister les joueurs inscrits au tournoi
- Choix 4 : Retirer un joueur du tournoi
- Choix 5 : Lancer le tournoi
- Choix 6 : Saisir les scores 
- Choix 7 : Liste les équipes
- Choix 8 : Supprimer un tournoi

### Choix 3 : Rapport de tournoi

Dans le menu **"RAPPORT DE TOURNOI"**, vous aurez la possibilité :
- Choix 0 : Retourner au menu principal
- Choix 1 : Visualiser le rapport du tournoi en cours
- Choix 2 : Visualiser le rapport des tournois précédents
- Choix 3 : Éditer un rapport du tournoi en cours (format txt)
- Choix 4 : Éditer un rapport des tournois précédents (format txt)

### Choix 4 : Quitter l'application

## Création d'un rapport flake8.
Saisir les commandes suivantes :

### Ouvrir PowerShell sous Windows : 
```sh
cd desktop    
   ```
```sh
cd ChessTournament
   ```

```sh
flake8 --format=html --htmldir=flake8_rapport   
   ```

### Ouvrir Terminal sous Mac \ Linux :
```sh
cd ~/Desktop 
   ```
```sh
cd ChessTournament
   ```

```sh
flake8 --format=html --htmldir=flake8_rapport   
   ```

Une fois terminé, vous aurez dans le répertoire **ChessTournament** un répertoire nommé **flake8_rapport**  
qui permettra d'indiquer que le code est conforme aux directives PEP 8.  
Pour consulter le résultat, ouvrir le répertoire flake8_rapport et cliquer sur **index.html**.


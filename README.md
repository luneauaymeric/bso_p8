[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gl/Cthulhus_Queen%2Fbarometre_scienceouverte_universitedelorraine/master?filepath=barometre_universite_lorraine.ipynb)


Travail inspiré du Baromètre français de la Science Ouverte : https://barometredelascienceouverte.esr.gouv.fr/

1) Téléchargez l'ensemble du Baromètre lorrain sur le bureau en utilisant le bouton "Download". Dé-zippez l'archive.

2) Installez la suite Anaconda Navigator (https://www.anaconda.com/products/individual).

3) Lancez Anaconda puis Jupyter Lab. Le dossier du Baromètre lorrain téléchargé sur le bureau apparaît sur la partie gauche de l'écran.

4) Faire les extractions dans les différentes bases de données souhaitées pour faire le corpus de votre établissement. 
La liste des requêtes utilisées est dans le fichier "requetes_bdd".
Les extractions dans les bases de données doivent se faire exactement comme c'est expliqué dans le notebook qui s'appelle "01_nettoyage_donnees".

5) Dans le dossier qui est sur le bureau, enlever les fichiers lorrains dans le dossier Data/raw et les remplacer par les vôtres. 
Attention, il faut reproduire très exactement le nommage des fichiers. Dans le code lorrain par exemple, le fichier 2016 pour PubMed 
s'appelle "pubmed_lorraine_2016". Il faut aussi effacer le contenu du dossier 'outputs' pour enlever les graphiques et résultats lorrains (mais conserver le dossier vide).

6) Ouvrir le notebook "01_nettoyage_donnees". Remplacer toutes les occurrences de "lorraine" par le nom de l'établissement (attention : utiliser le même nom que pour les extractions de bases de données).

7) Exécutez le notebook "01_nettoyage_donnees" en lisant bien les instructions à chaque étape. Pour exécuter les lignes de code les unes après les autres, il suffit de cliquer sur la première ligne tout en haut du code puis cliquer successivement sur le bouton "play" de la barre d'outils. Il faut bien lire les instructions.

8) Après avoir obtenu votre liste de DOI, l'envoyer au MESR en suivant les instructions sur cette page : https://barometredelascienceouverte.esr.gouv.fr/declinaisons/comment-realiser-bso-local


La première version du Baromètre lorrain nécessitait ensuite d'ouvrir le notebook "02_barometre_universite_lorraine". Il fallait ensuite remplacer toutes les occurrences de "lorraine" par le nom de l'établissement (attention : utiliser le même nom que pour les extractions de bases de données) puis d'exécuter le notebook "02_barometre_universite_lorraine" en lisant toutes les instructions. Enfin, il fallait exécuter le notebook "03_clustering" en lisant toutes les instructions.
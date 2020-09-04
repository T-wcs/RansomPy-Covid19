Ransomware Basé sur Python3

Vous pouvez trouver la source du code de base dans le répertoire de:
Cette version est améliorée et j'ai décidé d'ajouter des répertoires spécifiques à chiffrer. En plus d'ajouter un fond d'écran personnalisé

Le code s'améliore constamment, ceci à des fins éducatives pour apprendre comment fonctionne un Ransomware.
Je ne suis en aucun cas responsable de ce que vous ferez avec ce code.

# Fonctionnement du programme
Le code est constructible en plusieurs étapes mais est essentiellement destiné à chiffrer les fichiers dans un système Windows et est compilé avec Cx_Freeze qui permet d'importer toutes les bibliothèques du Ransomware.

L'utilisation de Cx_Freeze est relativement simple, vous pouvez consulter la documentation officielle à cette adresse:
https://cx-freeze.readthedocs.io/en/latest/

Vous pouvez également exécuter le code sans le compiler, il sera nécessaire que la cible ait Python installé sur le système, cependant il est préférable de le compiler pour l'automatisation après avoir créé un package SFX avec Winrar.

# Détails
Le ransomware n'attaque pas les fichiers système, il chiffre uniquement les répertoires personnels et le répertoire contenant tous les programmes installés.

# Exécution automatique avec WinRAR
1. Sélectionnez le dossier contenant le code et les bibliothèques
2. Renommez le dossier en "setup"
3. Clic droit et "Ajouter aux archives"
4. Sélectionnez le format d'archive sur "ZIP"
5. Sélectionnez "Créer une archive SFX"
6. Dans "l'onglet Avancé", cliquez sur "Options SFX"
7. Sélectionnez "Créer dans le dossier actuel"
8. Copiez "Powershell Start-Process setup / Ransomware.exe -Verb RunAs" dans la section "Launch after installation".
9. Dans "Onglet Avancé" sur "Options SFX" cochez la case "Demander les droits administratifs" (Très important, il vous permet d'exécuter le ransomware en tant qu'administrateur)
10. Dans l'onglet "Mod" des "Options SFX" cochez la case "Tout cacher"
11. Dans l'onglet "Mise à jour" de "Options SFX", cochez la case "Remplacer tous les fichiers"
12. Cliquez sur OK
13. Envoyez les "archives SFX" à la victime.

L'avantage de cette méthode de construction d'une archive est que je n'ai pas besoin de demander de privilèges dans le code et cela permet également de contenir toutes les bibliothèques dans un seul fichier exécutable.

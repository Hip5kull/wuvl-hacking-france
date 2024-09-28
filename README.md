## Hacking-France writeup template

Le script `vulnlab.py` permet à chaque personne souhaitant rédiger des writeup et contribuer pour [Hacking-France](https://github.com/frozenka/Hack-france). Le but est d'automatiser le squelette et de respecter le frontmatter du site.

Pour ce faire cloner le dépôt:

```sh 
git clone https://github.com/Hip5kull/wuvl-hacking-france.git
chmod +x vulnlab.py
pip install -r requirements.txt
```

Je vous conseille de copier le fichier du script dans votre $PATH `/usr/local/bin/` ceci vous permettra d'utiliser le script à partir de n'importe quel répertoire.

### Fonctionnement

`python3 vulnlab.py`

Dans le $PATH:

`vulnlab`

EDIT: **Version 1.1** ajout de la catégorie *chains*, choix utilisateur au lancement puis nom de la machine.


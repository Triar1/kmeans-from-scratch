# K-Means from Scratch — TP Python

Implémentation pédagogique de l'algorithme **K-Means sans `sklearn`**, réalisée en Python dans le cadre d'un TP.

## Contenu

- `RenduTPNovembre.py` : implémentation et visualisation en 2D (fichier configuré sur `clustering_1.csv`).
- `RenduTPNovembre 3d.py` : version prenant en charge les données 2D et 3D (fichier configuré sur `clustering_2.csv`).

## Fonctionnement

1. Tirage aléatoire de `N` centroïdes parmi les points.
2. Attribution de chaque point au centroïde le plus proche (distance euclidienne).
3. Recalcul des centroïdes à partir des moyennes des points attribués.
4. Visualisation des itérations et arrêt selon `epsilon` ou la limite de 30 itérations.
5. Conservation du centroïde précédent si un cluster est vide.

## Installation

Python 3, puis :

```bash
pip install -r requirements.txt
```

Placer les fichiers de données `clustering_0.csv`, `clustering_1.csv` et/ou `clustering_2.csv` dans le même dossier que les scripts. **Ces CSV ne sont pas inclus dans ce dépôt** : vérifier les autorisations de partage avant de les publier.

## Exécution

```bash
python 2DKmean.py
python "3Dand2DKmean.py"
```

Modifier au besoin le nom du CSV et `N` en haut du script. Les graphiques sont affichés à chaque itération.

## Note sur l'assistance IA

Le code a été construit progressivement par l'étudiant. ChatGPT a été utilisé ponctuellement pour expliquer et déboguer certaines parties du programme, notamment pour identifier et gérer le cas des clusters vides. La méthode `.iloc[]` a été recherchée dans la documentation en ligne.

## Remarque

Projet pédagogique, non destiné à remplacer une bibliothèque optimisée de clustering.

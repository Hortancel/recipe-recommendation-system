   Système de recommandation de recettes

# Présentation

Dans ce projet, j’ai réalisé un système de recommandation de recettes basé sur les ingrédients et les catégories (tags).
L’idée est simple : à partir d’une recette choisie par l’utilisateur, le système propose d’autres recettes qui lui ressemblent le plus.
L'objectif etait de proposer un systeme simple,fonctionnel et facile à utiliser,tout en comprenant les bases des systemes de recommendation.


#  Objectifs

L’objectif du projet était de :
- comprendre le principe des systèmes de recommandation
- manipuler des données textuelles (ingrédients, tags)
- utiliser des techniques comme TF-IDF
- créer une interface simple avec Streamlit


#  Technologies utilisées

- Python
- Pandas
- Scikit-learn (TF-IDF + similarité cosinus)
- Streamlit
- jupyter Notebook


#  Fonctionnement du système

Le système repose sur une approche de recommendation basee sur le contenu  *content-based filtering*.

#  Étapes de realisation :

1. Chargement des donees : les donnees ont ete chargees dans un DataFrame avec Pandas (df =pd.read_csv...)
    NB: le dataset a ete limite a environ 500 recettes afin d'optimiser les performances et faciliter le deployement du projet.

2. Exploration du dataset :
    -taille (len(df)),
    -collonnes disponibles (df.columns),
    -types de donnees (df.dtypes),
    -verificatio des valeurs manquantes (df.insull().sum()),
    
3. Nettoyage des donnees :
    -suppressions des doublons (df=df.dropna(subset=['name'])),
    -suppressions des colonnes inutiles (df=df.drop(columns=['description'])),
    -selection des colonnes utiles (df=df[['name', 'ingredients', 'minutes', 'tags']]),

4. Ensuite j'ai fait la preparation du texte en nettoyant des listes d'ingredients et tags, suivi du remplissage des vides,
5. Fusion des colonnes texte et mise en minuscule, 
6. J'ai utilise TF-IDF pour transformer le texte en nombre,
7. J'ai calcule la similarite entre les recettes avec la similarite cosinus pour trié les recettes pour proposer les plus proches,
8. indexer les recettes et en fin ecrire une fonction de recommandation


#  Interface utilisateur

J’ai utilisé Streamlit pour créer une interface simple avec :

- un menu déroulant pour choisir une recette
- un slider pour définir le temps maximum
- un champ pour filtrer par ingrédient
- un bouton pour lancer la recommandation

Les résultats sont affichés sous forme de tableau.


# Lancer le projet

Installer les dépendances :

pip install streamlit pandas scikit-learn jupyter notebook

Lancer l’application :
streamlit run app.py


# Exemple d’entree d'utilisateur

Utilisateur : "crab filled crescent snacks"
Temps max : 60 minutes

# Exemple de sortie

1. curried bean salad (20 min)
2. delicious steak with onion marinade(25 min)
3. pork tenderlion with hoisin (15 min)
4. mixed baby greens with oranges grapefruit and avocado(15 min)
5. buttercream frosting(30 min)

# Demonstration

Une video de demonstration du systeme est disponible ici :[voir la video](image/video_demo.mp4)

# Analyse des resultats

Pour la recette "crab filled crescent snacks" avec un temps maximum de 60 minutes, les recommendations obteneus sont generees grace au model TF-IDF combine a la similarite cosinus.
Le systeme analyse principalement deux types d'informations : les tags et les ingredients qui sont fusionne pour representer chaque recette sous forme de texte. Le modele TF-IDF  transforme ensuite ces textes en vecteurs numeriques en donnant plus d'importance aux mots comme "crab","snacks"..; quant a la similariye cosinus elle vient mesurer la proximite entre les recettes ,d'ou celles proposees sont celles dont les vecteurs sont les plus proches de la recette recherchee.

# Exemple de resultats en image

![recommendation](image/recommendation.png)
![interface](image/interface.png)

# Limites du système

Le système fonctionne, mais il a des limites :

- il ne comprend pas réellement les goûts
- il ne prend pas en compte les quantités
- il n’y a pas de profil utilisateur
- certaines recommandations peuvent être approximatives

#  Initiative personnelle

En plus des fonctionnalitees demandees ,j'ai ajouté un filtre(ingredients) afin de rendre les recommendations  plus pertinentes
et proches des besoins d'utilisateurs ,j'ai egalement ajouté une gestion des cas ou aucune recette n'est trouvée.


# Conclusion

Ce projet m’a permis de mettre en pratique les bases de fonctionnement les systèmes de recommandation,
notament l'utilisation de TF-IDF et la similarite cosinus pour comparer du contenu textuel. Il m'a surtout
donné l'envie d'aller plus loin et à continuer à apprendre et approfondir ces concepts.

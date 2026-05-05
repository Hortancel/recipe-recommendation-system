import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv('data/recipes_small.csv', encoding='latin-1', on_bad_lines='skip')

df = df.sample(500, random_state=42).reset_index(drop=True)

# Nettoyage

df['ingredients'] = df['ingredients'].fillna('')
df['tags'] = df['tags'].fillna('')

# Création du texte
df['text'] = df['ingredients'] + " " + df['tags']
df['text'] = df['text'].str.lower()
df['text'] = df['text'].str.replace('[^a-zA-Z]', ' ', regex=True)


# TF-IDF

vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['text'])

# Similarité cosinus
# cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Index
indices = pd.Series(df.index, index=df['name']).drop_duplicates()
indices=indices[~indices.index.duplicated()]


# Fonction recommandation

def recommander(nom_recette, max_minutes=60, top_n=5):

    if nom_recette not in indices:
        return pd.DataFrame()
    
    idx = indices[nom_recette]

    sim_scores = cosine_similarity(tfidf_matrix[idx], tfidf_matrix).flatten()
    
    scores = list(enumerate(sim_scores))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    scores = scores[1:top_n+1]
    
    recette_indices = [i[0] for i in scores]

    resultats=df.iloc[recette_indices].copy()

    resultats['score'] = [i[1] for i in scores]
    
    # resultats = df[['name', 'ingredients', 'minutes', 'tags']].iloc[recette_indices]
    
    # Filtrer par temps

    resultats = resultats[resultats['minutes'] <= max_minutes]
    
    # Ajouter score

    resultats['score'] = [i[1] for i in scores][:len(resultats)]
    resultats=resultats[['name', 'ingredients', 'minutes', 'tags', 'score']]
    
    return resultats


# INTERFACE STREAMLIT


st.title("Recipe Recommendation System ")

st.markdown("## personalisez votre recherche")

recette = st.selectbox("Choisir une recette :", df['name'].unique())

temps = st.slider("Temps maximum (minutes)", 10, 200, 60)
ingredient = st.text_input("Filtrer par ingredient ")

if st.button("Recommander"):
    resultats = recommander(recette, temps)
    if ingredient:
        resultats=resultats[resultats['ingredients'].str.contains(ingredient,case=False)]
    if resultats.empty:
        st.warning("Aucune recette trouvee avec cet ingredient!")
    else:
        st.success(f"{len(resultats)} recettes trouvees : ")
    st.dataframe(resultats)
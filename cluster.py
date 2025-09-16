from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans
import plotly.express as px
import pandas as pd

embedder = SentenceTransformer('all-MiniLM-L6-v2')

def cluster_ideas(ideas, n_clusters=3):
    """Cluster similar ideas and return a Plotly scatter figure"""
    embeddings = embedder.encode(ideas)
    kmeans = KMeans(n_clusters=min(n_clusters, len(ideas)), random_state=42)
    labels = kmeans.fit_predict(embeddings)

    df = pd.DataFrame({
        "idea": ideas,
        "cluster": labels,
        "x": embeddings[:,0],
        "y": embeddings[:,1]
    })
    fig = px.scatter(df, x="x", y="y", color="cluster",
                     hover_data=["idea"], title="Your Subconscious Idea Map")
    return fig

from .storage_service import load_submissions
import numpy as np
from scipy.sparse import hstack
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.cluster import KMeans


def trigger_clustering():
    """
    Load submissions, preprocess features, and run KMeans clustering.
    Returns a list of cluster labels corresponding to each submission.
    """
    submissions = load_submissions()
    if not submissions:
        return []

    # Prepare text corpus from relevant text fields
    text_corpus = []
    for s in submissions:
        fields = [
            s.get('injuries', ''),
            s.get('medications', ''),
            s.get('painPoints', ''),
            s.get('historyMotivation', ''),
            s.get('reflectMotivation', ''),
            s.get('reflectReaction', ''),
            s.get('reflectUse', '')
        ]
        text_corpus.append(' '.join(fields))

    tfidf = TfidfVectorizer()
    text_features = tfidf.fit_transform(text_corpus)

    # Encode multi-select fields
    history_lists = [s.get('historyTypes', []) for s in submissions]
    goals_lists = [s.get('goals', []) for s in submissions]

    mlb_history = MultiLabelBinarizer()
    hist_features = mlb_history.fit_transform(history_lists)

    mlb_goals = MultiLabelBinarizer()
    goals_features = mlb_goals.fit_transform(goals_lists)

    # Numeric VO2 result
    vo2 = []
    for s in submissions:
        try:
            vo2.append(float(s.get('vo2Result', 0)))
        except Exception:
            vo2.append(0.0)
    vo2_array = np.array(vo2).reshape(-1, 1)

    # Combine all feature matrices
    feature_matrix = hstack([
        text_features,
        hist_features,
        goals_features,
        vo2_array
    ])

    # Determine number of clusters based on data size
    n_samples = feature_matrix.shape[0]
    n_clusters = min(3, n_samples) if n_samples > 0 else 1
    # Convert sparse matrix to dense for KMeans
    if hasattr(feature_matrix, "toarray"):
        feature_matrix = feature_matrix.toarray()
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    labels = kmeans.fit_predict(feature_matrix)

    return labels.tolist()

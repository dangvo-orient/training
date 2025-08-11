import seaborn as sns
import pandas as pd
import streamlit as st
from sklearn.datasets import load_iris
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier


@st.cache_resource
def load_data():
    iris = load_iris()

    target_names = iris["target_names"]
    target = list(map(lambda i: target_names[i], iris["target"]))

    data = pd.DataFrame(iris["data"], columns=iris["feature_names"])
    data["species"] = target
    return data

data = load_data()

with st.sidebar:
    selected_species = st.pills(
        "Filter by species:",
        data["species"].unique(),
        selection_mode="multi",
        default=data["species"].unique(),
        width=125,
    )
    standardize_feature = st.radio("Standardize the features:", options=["Yes", "No"], index=1)

    st.header("Model Selection")
    selected_model = st.radio("Model:", options=["Logistic Regression", "Decision Tree", "K-Nearest Neighbor"])
    model_kwargs = {}
    if selected_model == "Logistic Regression":
        model_kwargs = {
            "tol": st.number_input("Tolerance:", min_value=0.0, value=0.0001, step=0.0001, format="%.6f"),
            "C": st.number_input("C:", min_value=1e-6, value=1.0, step=1.0),
        }
    elif selected_model == "Decision Tree":
        model_kwargs = {
            "n_estimators": st.number_input("Number of estimators:", 1, value=100, step=1),
            "criterion": st.radio("Criterion:", options=['gini', 'entropy', 'log_loss'], index=0),
        }
    else:
        model_kwargs = {
            "n_neighbors": st.number_input("n_neighbor", 1, value=5, step=1),
            "weights": st.radio("weights", options=['uniform', 'distance']),
        }

# Filter dataset
data = data[data["species"].isin(selected_species)]

# Show dataset
st.write("### Iris Dataset")
st.write(data)

# Show summary statistics
st.write("### Summary Statistics")
st.write(data.describe())

@st.cache_data
def plot(data):
    g = sns.pairplot(data, hue="species")
    st.pyplot(g)

st.write("### Pairwise Feature Relationships by Species")
plot(data)


scaler = StandardScaler()

if standardize_feature == "Yes":
    standardized_data = scaler.fit_transform(data.drop(columns=["species"]))
    standardized_data = pd.DataFrame(standardized_data)
    data.iloc[:, :4] = standardized_data

    st.write("### Standardized Iris")
    st.write(data.head())

# Train model
X = data.drop(columns=["species"])

labels = data["species"]
encoder = LabelEncoder()
y = encoder.fit_transform(labels)

if selected_model == "Logistic Regression":
    clf = LogisticRegression(**model_kwargs)
    clf.fit(X, y)
elif selected_model == "Decision Tree":
    clf = RandomForestClassifier(**model_kwargs)
    clf.fit(X, y)
else:
    clf = KNeighborsClassifier(**model_kwargs)
    clf.fit(X, y)

# Score
st.write("### Score")
st.metric("Score", f"{clf.score(X, y): .4f}")


# Prediction
st.write("### Prediction")
x_input = [[
    st.number_input("Sepal length (cm):", 0.0, value=5.1),
    st.number_input("Sepal width (cm):", 0.0, value=3.5),
    st.number_input("Petal length (cm):", 0.0, value=1.4),
    st.number_input("Petal width (cm):", 0.0, value=0.2),
]]
if standardize_feature == "Yes":
    x_input = scaler.transform(x_input)

pred = clf.predict(x_input)
st.write(f"Prediction: **{(encoder.inverse_transform(pred)[0]).upper()}**")

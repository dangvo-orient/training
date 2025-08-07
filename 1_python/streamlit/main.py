import pandas as pd
import plotly.express as px
import streamlit as st


@st.cache_data
def load_data():
    train = pd.read_csv("./data/train.csv")
    test = pd.read_csv("./data/test.csv")
    return train, test


train, test = load_data()

# Handle missing values in age
title = train["Name"].str.extract(',\\s*(\\w+)\\.')[0]
train["Age"] = train["Age"].fillna(train.groupby(title)["Age"].transform('median'))

st.title("Titanic Survivors 🚢")

# Visualize data
st.dataframe(train.head(), hide_index=True)

# Filter
st.header("Filtering")
sex_filter = st.sidebar.pills(
    "Sex",
    train.Sex.unique(),
    selection_mode="multi",
    default=train.Sex.unique(),
)
pclass_filter = st.sidebar.pills(
    "Ticket class",
    sorted(train.Pclass.unique()),
    selection_mode="multi",
    default=train.Pclass.unique(),
)
age_filter = st.sidebar.slider(
    "Age",
    min_value=int(train["Age"].min()),
    max_value=int(train["Age"].max()),
    value=(0, 80),
)

filtered = train[
    train.Sex.isin(sex_filter)
    & train.Pclass.isin(pclass_filter)
    & train.Age.between(*age_filter)
]

if len(filtered) == 0:
    st.metric("Number of passengers", len(filtered))

else:
    survival_count = filtered.Survived.value_counts()
    survival_sum = sum(v for v in survival_count)

    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("Number of passengers", survival_sum)
    with c2:
        st.metric("Survived", f"{survival_count[1] / survival_sum:.4f}")
    with c3:
        st.metric("Deceased", f"{survival_count[0] / survival_sum:.4f}")

    st.dataframe(filtered, hide_index=True)

    fig = px.bar(
        filtered.groupby("Sex")["Survived"].mean().reset_index(),
        x="Sex",
        y="Survived",
        title="Survival Rate by Sex",
    )
    st.plotly_chart(fig)

    fig = px.histogram(
        filtered,
        x="Age",
        color="Survived",
        barmode="overlay",
        title="Age Distribution: Survived vs Did Not Survive",
    )
    st.plotly_chart(fig)

    fig = px.box(
        filtered,
        x="Pclass",
        y="Fare",
        color="Survived",
        title="Fare Distribution by Pclass & Survival",
    )
    st.plotly_chart(fig)

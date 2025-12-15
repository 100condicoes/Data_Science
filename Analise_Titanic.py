import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# --------------------------------
# CONFIGURAÇÃO DA PÁGINA
# --------------------------------
st.set_page_config(page_title="Dashboard Titanic", layout="wide")

st.title("     Análise de Dados – Titanic")
st.write("Projeto de Data Science conforme roteiro da disciplina.")

# --------------------------------
# CARREGAMENTO DOS DADOS
# --------------------------------
df = pd.read_csv("data/train.csv")

st.subheader("Visão geral do dataset")
st.dataframe(df.head())

# --------------------------------
# LIMPEZA E PREPARAÇÃO
# --------------------------------
df["Age"].fillna(df["Age"].median(), inplace=True)
df["Embarked"].fillna(df["Embarked"].mode()[0], inplace=True)
df["Fare"].fillna(df["Fare"].median(), inplace=True)

le = LabelEncoder()
df["Sex"] = le.fit_transform(df["Sex"])
df["Embarked"] = le.fit_transform(df["Embarked"])

scaler = StandardScaler()
cols = ["Age", "Fare", "SibSp", "Parch"]
df[cols] = scaler.fit_transform(df[cols])

# --------------------------------
# ANÁLISE EXPLORATÓRIA (EDA)
# --------------------------------
st.subheader("Análise Exploratória")

col1, col2 = st.columns(2)

with col1:
    st.write("Distribuição da Idade")
    fig, ax = plt.subplots()
    sns.histplot(df["Age"], bins=20, kde=True, ax=ax)
    st.pyplot(fig)

with col2:
    st.write("Idade x Sobrevivência")
    fig, ax = plt.subplots()
    sns.boxplot(x="Survived", y="Age", data=df, ax=ax)
    st.pyplot(fig)

# --------------------------------
# GRÁFICO INTERATIVO (ESCOLHA)
# --------------------------------
st.subheader("Análise Interativa")

feature = st.selectbox(
    "Escolha uma variável numérica:",
    ["Age", "Fare", "SibSp", "Parch"]
)

fig, ax = plt.subplots()
sns.histplot(df[feature], bins=20, kde=True, ax=ax)
ax.set_title(f"Distribuição de {feature}")
st.pyplot(fig)

# --------------------------------
# MODELAGEM PREDITIVA
# --------------------------------
st.subheader("Modelagem Preditiva")

features = ["Pclass", "Sex", "Age", "Fare", "SibSp", "Parch"]
X = df[features]
y = df["Survived"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)

st.success(f"Acurácia do modelo: {acc:.2f}")

# --------------------------------
# CONCLUSÃO
# --------------------------------
st.subheader("Conclusão")
st.write("""
A análise demonstra que fatores como idade, sexo e classe social
influenciaram significativamente a sobrevivência dos passageiros.
""")

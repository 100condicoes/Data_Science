# 🚢 Projeto Data Science – Titanic

## Descrição do Problema

Este projeto tem como objetivo analisar os dados do desastre do Titanic e identificar quais fatores influenciaram a sobrevivência dos passageiros. A partir de técnicas de Data Science, busca-se gerar insights relevantes e construir um modelo preditivo simples capaz de estimar a probabilidade de sobrevivência.

O projeto foi desenvolvido conforme o roteiro da atividade da unidade curricular **Data Science – Princípios e Técnicas**.

---

## Fonte dos Dados

Os dados utilizados neste projeto foram obtidos a partir da plataforma **Kaggle**, especificamente do conjunto de dados:

* **Titanic: Machine Learning from Disaster**
* Link: [https://www.kaggle.com/competitions/titanic](https://www.kaggle.com/competitions/titanic)

O dataset contém informações demográficas e socioeconômicas dos passageiros, como idade, sexo, classe social, número de familiares a bordo e tarifa paga.

---

## Limpeza e Preparação dos Dados

Foram aplicadas as seguintes técnicas de preparação dos dados:

* Tratamento de valores ausentes:

  * Idade (Age): substituída pela mediana
  * Porto de embarque (Embarked): substituído pela moda
  * Tarifa (Fare): substituída pela mediana
* Codificação de variáveis categóricas:

  * Variável `Sex` e `Embarked` transformadas utilizando **Label Encoding**
* Padronização dos dados numéricos:

  * Aplicação do **StandardScaler** nas variáveis: Age, Fare, SibSp e Parch

Essas etapas garantem maior consistência dos dados e melhor desempenho do modelo preditivo.

---

## Análise Exploratória de Dados (EDA)

A análise exploratória teve como foco compreender a distribuição dos dados e identificar padrões relevantes. Foram utilizadas estatísticas descritivas e visualizações gráficas, incluindo:

* Histogramas para análise da distribuição das variáveis numéricas
* Boxplots para identificação de dispersão e possíveis outliers
* Gráficos de dispersão para observar relações entre variáveis
* Análise comparativa entre sobreviventes e não sobreviventes

Principais insights obtidos:

* Mulheres apresentaram maior taxa de sobrevivência
* Passageiros mais jovens tiveram maior probabilidade de sobreviver
* Classes sociais mais altas estiveram associadas a maiores taxas de sobrevivência

---

## Modelagem Preditiva

Foi aplicado um modelo de **Random Forest Classifier**, adequado para problemas de classificação binária.

Etapas realizadas:

* Seleção das variáveis preditoras: Pclass, Sex, Age, Fare, SibSp e Parch
* Separação dos dados em conjuntos de treino e teste (80% / 20%)
* Treinamento do modelo
* Avaliação do desempenho utilizando a métrica de **acurácia**

### Resultado do Modelo

* Acurácia obtida: aproximadamente **80%** (valor pode variar conforme a execução)

O modelo apresentou desempenho satisfatório para um problema de classificação simples.

---

## Dashboard Interativo

Foi desenvolvido um **dashboard interativo utilizando Streamlit**, permitindo:

* Visualização dinâmica do dataset
* Análise exploratória interativa
* Seleção de variáveis para análise gráfica
* Exibição dos resultados do modelo preditivo

O dashboard facilita a interpretação dos dados e torna a análise mais intuitiva.

Para executar o dashboard localmente:


```bash ou cmd da Pasta que você colocou os arquivos
python Analise_Titanic.py


pip install streamlit pandas numpy matplotlib seaborn scikit-learn
```
execute o codigo Para as Biblotecas Carregarem depois no bash ou cmd execute esse código 

```bash ou cmd
streamlit run Analise_Titanic.py
```

---

## Vídeo de Apresentação

O vídeo de apresentação do projeto, com duração máxima de 5 minutos, está disponível no link abaixo:

🔗 **Link do vídeo:** https://www.youtube.com/watch?v=oVswXFZLqbE

No vídeo são explicadas as etapas do projeto, as decisões tomadas e os principais resultados obtidos.

---

## Conclusão

A análise dos dados do Titanic evidencia que fatores demográficos e socioeconômicos influenciaram significativamente a sobrevivência dos passageiros. O uso de técnicas de Data Science possibilitou a extração de insights relevantes e a construção de um modelo preditivo eficiente.

Como trabalhos futuros, sugere-se a aplicação de outros algoritmos de classificação e a inclusão de novas variáveis para aprimorar o desempenho do modelo.

---

## 🛠 Tecnologias Utilizadas

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Streamlit
* Visual Studio Code

---

## 👤 Autor

Projeto desenvolvido por **Hericc Rocha de Araujo Melo e Davi Maia**.

OBS: Eu Hericc não sou muito bom com Visual de sites/DashBoard/jogos/... por isso eu mantive a aparencia de agora, espero que isso não comprometa sua experiencia sobre o código do dashboard.

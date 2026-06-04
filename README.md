[README (4).md](https://github.com/user-attachments/files/28568218/README.4.md)
# 📊 Pipeline de Análise do ENEM 2023 com PySpark

Projeto completo de engenharia de dados e machine learning aplicado aos microdados do ENEM 2023, disponibilizados pelo INEP. O pipeline processa quase 4 milhões de registros com Apache Spark e entrega um modelo preditivo com interface interativa.

---

## 🎯 Objetivo

Analisar o desempenho dos candidatos no ENEM 2023 e construir um modelo capaz de prever a nota de redação a partir do perfil socioeconômico e das notas das provas objetivas.

---

## 🔍 Principais Resultados

- **~4 milhões de registros** processados com PySpark em ambiente local
- **2,09 milhões de candidatos** válidos após limpeza (presença em todas as provas, nota de redação > 0)
- Nota média de redação: **647 pontos** — acima da média das provas objetivas (~522)
- Alunos de escolas **privadas** têm média de redação significativamente superior aos de escolas públicas
- Estados do **Sul e Sudeste** concentram as maiores médias de redação

### Sobre o modelo preditivo

Foram testados três algoritmos — Regressão Linear, Random Forest e Gradient Boosting — com os seguintes resultados:

| Modelo | MAE | R² |
|---|---|---|
| Regressão Linear | 116 | 0.34 |
| Random Forest | 113 | 0.36 |
| Gradient Boosting | 114 | 0.36 |

**Conclusão:** o R² de ~0.36 indica que as features disponíveis explicam apenas 36% da variação na nota de redação. Isso **não é uma limitação do algoritmo** — todos os modelos convergiram para resultados semelhantes, o que indica que o teto está nas features.

A nota de redação depende fortemente de habilidades de escrita, domínio da norma culta e repertório cultural — fatores que simplesmente não existem nos microdados do ENEM. Essa é uma conclusão analítica relevante: **dados socioeconômicos e desempenho em provas objetivas são preditores fracos da nota de redação**, o que reforça a natureza subjetiva e multifatorial dessa competência.

A feature mais importante no modelo foi `media_objetivas` (~82% de importância no Random Forest), seguida de `TP_ESCOLA`. A renda familiar (`Q006`) teve impacto mínimo — possivelmente porque o tipo de escola já captura indiretamente essa informação.

---

## 🛠️ Tecnologias

- **Apache Spark (PySpark 4.1)** — leitura, limpeza e transformação dos dados em escala
- **scikit-learn** — treinamento e avaliação dos modelos de ML
- **Matplotlib** — visualizações da análise exploratória
- **Streamlit** — dashboard interativo para predição em tempo real
- **Parquet** — formato de armazenamento dos dados processados

---

## 📁 Estrutura do Projeto

```
enem-pipeline/
├── notebooks/
│   └── enem_pipeline.ipynb   # Pipeline completo: EDA + Feature Engineering + ML
├── dashboard/
│   └── app.py                # App Streamlit para predição interativa
├── data/
│   ├── raw/                  # Microdados originais do INEP (não versionados)
│   └── processed/            # Dados limpos em Parquet (não versionados)
├── src/
│   └── modelo_rf.pkl         # Modelo treinado (não versionado)
└── .gitignore
```

---

## 🚀 Como Executar

**Pré-requisitos:** Python 3.12, Java 11+, WSL/Ubuntu

```bash
# Instalar dependências
pip install pyspark pandas pyarrow matplotlib streamlit scikit-learn

# Baixar os microdados do ENEM 2023
wget --no-check-certificate https://download.inep.gov.br/microdados/microdados_enem_2023.zip
unzip microdados_enem_2023.zip -d data/raw/

# Rodar o notebook completo
jupyter lab notebooks/enem_pipeline.ipynb

# Rodar o dashboard
streamlit run dashboard/app.py
```

---

## 📈 Dashboard

O app permite inserir as notas das quatro provas objetivas e o tipo de escola para obter a previsão da nota de redação em tempo real.

---

## 📚 Fonte dos Dados

Microdados do ENEM 2023 — [INEP / dados.gov.br](https://dados.inep.gov.br/educacao-basica/enem/microdados)

---

## 👤 Autor

**Thiago Mota** — [@th900](https://github.com/th900)  
Estudante de Ciência da Computação — 5º período

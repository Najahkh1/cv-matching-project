# CV Matching Project

## 1. Projectomschrijving

Dit project is een concept voor CV matching met Natural Language Processing (NLP).

Het doel van het project is om cv’s automatisch te vergelijken met vacatures en de meest relevante vacatures terug te geven.

De applicatie ondersteunt twee verschillende matching-methodes:

- TF-IDF + cosine similarity
- Semantic matching met Sentence Transformers (`all-MiniLM-L6-v2`)

Daarnaast bevat het project:

- data preprocessing
- deduplicatie
- modelvergelijking
- evaluatie-output
- visualisaties
- Testen
- Streamlit-app met CV-upload

---

## 2. Onderzoeksvraag

**Hoe kunnen cv’s automatisch worden gekoppeld aan passende vacatures met behulp van NLP-technieken zoals TF-IDF en semantic matching?**

## Hypothese
De verwachting is dat semantic matching met Sentence Transformers betere vacaturematches oplevert dan TF-IDF, omdat semantic matching de betekenis van tekst begrijpt en daardoor ook overeenkomsten kan herkennen wanneer verschillende woorden worden gebruikt voor vergelijkbare vaardigheden, functies of werkervaringen.
---

## 3. Projectstructuur

```text
cv-matching-project/
│
├── data/
│   ├── raw/
│   │   ├── job_descriptions.csv
│   │   └── resume_data.csv
│   │
│   └── processed/
│       ├── jobs_processed.csv
│       └── resumes_processed.csv
│
├── docs/
│   └── experiments.md
│
├── results/
│   ├── model_evaluation.csv
│   ├── average_scores_per_model.png
│   ├── scores_per_resume.png
│   └── top_roles.png
│
├── src/
│   ├── app/
│   │   └── app.py
│   │
│   ├── preprocessing/
│   │   ├── data_loader.py
│   │   ├── text_preprocessor.py
│   │   ├── deduplicator.py
│   │   └── run_preprocessing.py
│   │
│   ├── models/
│   │   ├── tfidf_matcher.py
│   │   └── semantic_matcher.py
│   │
│   ├── evaluation/
│   │   ├── evaluate_models.py
│   │   └── visualize_results.py
│   │
│   └── config/
│       └── settings.py
│
├── tests/
│   ├── test_loader.py
│   ├── test_preprocessor.py
│   ├── test_matcher.py
│   ├── test_semantic_matcher.py
│   └── test_model_comparison.py
│
├── requirements.txt
└── README.md

## 4. Dataset

De gebruikte datasets staan in:

```text
data/raw/
```

Bestanden:

```text data
job_descriptions.csv
resume_data.csv
```

### Vacaturedata

Belangrijke kolommen:

- `Job Title`
- `Role`
- `Job Description`
- `skills`
- `Responsibilities`
- `Qualifications`
- `Company`

### CV-data

Belangrijke kolommen:

- `skills`
- `responsibilities`
- `degree_names`
- `positions`
- `certification_skills`
- `job_position_name`

---

## 5. Environment setup

### Maak virtual environment

```bash
python3 -m venv .venv
```

### Activeer virtual environment

```bash
source .venv/bin/activate
```

### Installeer dependencies

```bash
pip install -r requirements.txt
```

### Download NLTK-data

```bash
python
```

```python
import nltk

nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("omw-1.4")

exit()
```

---

## 6. Preprocessing

De preprocessing wordt uitgevoerd met:

```text
src/preprocessing/run_preprocessing.py
```

### Run preprocessing

```bash
PYTHONPATH=src python src/preprocessing/run_preprocessing.py
```

### Dit script doet:

1. datasets laden
2. kolomnamen schoonmaken
3. lowercase toepassen
4. speciale tekens verwijderen
5. stopwoorden verwijderen
6. lemmatization toepassen
7. relevante kolommen combineren naar:
   - `job_text`
   - `resume_text`
8. duplicaten verwijderen
9. processed data opslaan

### Output

```text
data/processed/jobs_processed.csv
data/processed/resumes_processed.csv
```

### Deduplicatie resultaat

```text
Aantal rijen voor deduplicatie: 1.615.940
Aantal rijen na deduplicatie: 3.760
Aantal verwijderde duplicaten: 1.612.180
```

Dit was een belangrijk stap omdat duplicaten de matchingresultaten kunnen vertekenen.

---

## 7. TF-IDF baseline model

Het eerste model gebruikt:

```text
TF-IDF + cosine similarity
```

Bestand:

```text
src/models/tfidf_matcher.py
```

### Waarom TF-IDF?

TF-IDF is gekozen als baseline omdat het:

- snel is
- goed uitlegbaar is
- geschikt is voor keyword matching
- weinig rekenkracht nodig heeft
- goed werkt met technische skills (Python)

### Beperking

TF-IDF kijkt vooral naar exacte woorden.

Het begrijpt geen betekenis of synoniemen.

Voorbeeld:

```text
software engineer
```

en

```text
programmer
```

kunnen als verschillend worden gezien. Daarom is naar gekeken naar een ander type model

---

## 8. Semantic matching model

Het tweede model gebruikt:

```text
sentence-transformers/all-MiniLM-L6-v2
```

Bestand:

```text
src/models/semantic_matcher.py
```

### Waarom semantic matching?

Semantic matching vergelijkt teksten op basis van betekenis in plaats van alleen woordoverlap.

Dit is nuttig omdat cv’s en vacatures vaak andere woorden gebruiken voor vergelijkbare vaardigheden.

Voorbeeld:

```text
business analytics
```

kan inhoudelijk lijken op:

```text
business intelligence analyst
```

### Sterke punten

- begrijpt context beter
- herkent semantisch verwante functies
- werkt beter bij bredere functiebeschrijvingen

### Beperkingen

- langzamer dan TF-IDF
- minder goed uitlegbaar
- gebruikt meer geheugen/rekenkracht

---

## 9. Modelvergelijking

### Run vergelijkingstest

```bash
PYTHONPATH=src python tests/test_model_comparison.py
```

### Voorbeeldresultaat

#### TF-IDF

```text
Data Scientist / Machine Learning Engineer
score: 0.5826
```

#### Semantic

```text
Business Analyst / Data Business Analyst
score: 0.7154
```


---

## 10. Evaluatie

De evaluatie wordt uitgevoerd met:

```text
src/evaluation/evaluate_models.py
```

### Run evaluatie

```bash
PYTHONPATH=src python src/evaluation/evaluate_models.py
```

### Output

```text
results/model_evaluation.csv
```

### Voorbeeld output

```csv
resume_index,model,job_title,role,company,score
0,TF-IDF,Data Engineer,Big Data Engineer,Lendlease Group,0.4772
0,Semantic,Data Engineer,Big Data Engineer,Fidelity Investments Inc.,0.6437
1,TF-IDF,Data Scientist,Machine Learning Engineer,Victrex,0.5826
1,Semantic,Business Analyst,Data Business Analyst,American Tower,0.7154
```

---

## 11. Waarom geen accuracy of confusion matrix?

Een confusion matrix en accuracy zijn alleen geschikt wanneer er echte labels zijn.

Bijvoorbeeld:

```text
CV 1 → juiste klasse: Data Engineer
CV 2 → juiste klasse: Business Analyst
```

In deze dataset is er geen officiële juiste vacature per CV.

Daarnaast kan één CV bij meerdere functies passen, bijvoorbeeld:

- Data Analyst
- Data Scientist
- Business Intelligence Analyst
- Machine Learning Engineer

Daarom is CV matching in dit project behandeld als een ranking/similarity probleem en niet als klassieke classificatie.

Daarom gebruiken we:

- similarity scores
- top-k resultaten
- modelvergelijking
- kwalitatieve beoordeling
- visualisaties

---

## 12. Visualisaties

Visualisaties worden gemaakt met:

```text
src/evaluation/visualize_results.py
```

### Run visualisaties

```bash
PYTHONPATH=src python src/evaluation/visualize_results.py
```

### Output bestanden

```text
results/average_scores_per_model.png
results/scores_per_resume.png
results/top_roles.png
```

### Deze grafieken laten zien:

- gemiddelde score per model
- scoreverschil per CV
- meest voorkomende top-match rollen

---

## 13. Streamlit applicatie

De applicatie staat in:

```text
src/app/app.py
```

### Run applicatie

```bash
PYTHONPATH=src streamlit run src/app/app.py
```

### Functionaliteiten

De applicatie ondersteunt:

- CV tekst plakken

- CV uploaden als:

  - `.txt`

  - `.pdf`

  - `.docx`

- kiezen tussen twee matching-methodes:

  - `TF-IDF + cosine similarity`

  - `Semantic matching met Sentence Transformers`

- top-k vacatures tonen op basis van similarity score

- similarity scores tonen per vacaturematch

- functie-uitleg tonen via:

  - `Job Description`

- preview van de geüploade CV tekst tonen

- foutafhandeling bij:

  - lege invoer

  - ontbrekende bestanden

  - ongeldige kolommen

  - parsing fouten

- interactieve instellingen via sidebar:

  - modelkeuze

  - aantal matches (`top_n`)

  - aantal vacatures in de sample (`sample_size`)

- ondersteuning voor semantic embeddings via:

- resultaten tonen in een interactieve tabel met:

  - `Job Title`

  - `Role`

  - `Company`

  - `similarity_score`

  - `Job Description`

---

## 14. Belangrijkste resultaten

### TF-IDF

Sterk bij:

- exacte skill overlap
- technische keywords
- snelle matching



### Semantic matching

Sterk bij:

- bredere context
- business analytics
- synoniemen en andere formuleringen


---

## 15. Conclusie

Binnen dit project bleek TF-IDF geschikt als snelle en uitlegbare baseline.

Het model werkte goed wanneer cv’s en vacatures dezelfde technische keywords bevatten.

Semantic matching gaf vaak contextueel bredere resultaten en was beter in het herkennen van inhoudelijke overeenkomsten wanneer woorden niet exact hetzelfde waren.

### Belangrijkste conclusie

```text
TF-IDF is geschikt voor keyword matching.
Semantic matching is geschikter voor betekenisvolle CV-vacature matching.
```

Voor een realistische recruitmenttoepassing lijkt een combinatie van beide modellen interessant.

---

## 16. Beperkingen

- De dataset bevatte veel duplicaten
- Er waren geen officiële labels voor correcte CV-vacature matches
- Accuracy, precision, recall en F1-score konden daardoor niet betrouwbaar worden berekend
- Semantic matching is langzamer dan TF-IDF
- Scores van TF-IDF en semantic matching zijn niet direct vergelijkbaar
- De evaluatie is deels kwalitatief

---

## 18. Commands overzicht

### Preprocessing

```bash
PYTHONPATH=src python src/preprocessing/run_preprocessing.py
```

### TF-IDF test

```bash
PYTHONPATH=src python tests/test_matcher.py
```

### Semantic test

```bash
PYTHONPATH=src python tests/test_semantic_matcher.py
```

### Modelvergelijking

```bash
PYTHONPATH=src python tests/test_model_comparison.py
```

### Evaluatie

```bash
PYTHONPATH=src python src/evaluation/evaluate_models.py
```

### Visualisaties

```bash
PYTHONPATH=src python src/evaluation/visualize_results.py
```

### Streamlit app

```bash
PYTHONPATH=src streamlit run src/app/app.py
```

---

## 19. Gebruikte technieken

- Python
- pandas
- scikit-learn
- TF-IDF
- cosine similarity
- NLTK stopwords
- WordNet lemmatization
- Sentence Transformers
- Streamlit
- matplotlib

---

## 20. Projectstatus

### Status

```text
Werkend prototype
```

### Werkende onderdelen

- data loading
- preprocessing
- deduplicatie
- TF-IDF matching
- semantic matching
- modelvergelijking
- evaluatie-export
- visualisaties
- Streamlit demo
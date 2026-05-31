# CV Matching Project

## 1. Inleiding

Het handmatig koppelen van cv’s aan vacatures is een tijdrovend proces. Recruiters moeten grote hoeveelheden cv’s beoordelen en bepalen welke kandidaten het beste aansluiten bij een functie. Dit proces is niet alleen arbeidsintensief, maar ook gevoelig voor subjectieve interpretatie. Daarnaast gebruiken kandidaten en werkgevers vaak verschillende termen voor vergelijkbare vaardigheden, functies en werkervaringen. Hierdoor kunnen relevante matches over het hoofd worden gezien.

Binnen dit project is onderzocht hoe Natural Language Processing (NLP) kan worden ingezet om cv’s automatisch te koppelen aan passende vacatures. Het project richt zich op het vergelijken van twee verschillende NLP-benaderingen:

- TF-IDF met cosine similarity
- Semantic matching met Sentence Transformers

Door beide methoden te implementeren, testen en vergelijken wordt onderzocht welke techniek het meest geschikt is voor het automatisch matchen van cv’s en vacatures.

Naast de matching-algoritmen is aandacht besteed aan:

- data preprocessing
- deduplicatie van vacatures
- modelvergelijking
- evaluatie van resultaten
- visualisaties
- reproduceerbaarheid
- een interactieve Streamlit-applicatie

Het uiteindelijke resultaat is een werkend prototype waarmee gebruikers een cv kunnen uploaden of invoeren en automatisch de meest relevante vacatures kunnen laten vinden.

---

## 2. Onderzoeksvraag

**Hoe kunnen cv’s automatisch worden gekoppeld aan passende vacatures met behulp van NLP-technieken zoals TF-IDF en semantic matching?**

---

## 3. Onderzoeksdoel

Het doel van dit project is het ontwikkelen en evalueren van een prototype voor automatische cv-vacaturematching.

Daarbij wordt onderzocht welke NLP-techniek de meest relevante resultaten oplevert. Hiervoor worden zowel een traditionele benadering (TF-IDF) als een moderne semantic matching benadering (Sentence Transformers) geïmplementeerd en vergeleken.

De focus ligt op:

- het automatisch verwerken van cv’s
- het vergelijken van cv’s met vacatures
- het evalueren van verschillende matching-methoden
- het analyseren van de invloed van preprocessing
- het onderzoeken van de meerwaarde van semantic matching ten opzichte van traditionele NLP-technieken

---

## 4. Hypothese

De verwachting is dat semantic matching met Sentence Transformers betere vacaturematches oplevert dan TF-IDF.

TF-IDF kijkt voornamelijk naar woordfrequenties en exacte woordoverlap tussen documenten. Hierdoor werkt het goed wanneer dezelfde termen voorkomen in zowel het cv als de vacature.

Semantic matching maakt gebruik van embeddings die teksten representeren op basis van hun betekenis. Hierdoor kan het model overeenkomsten herkennen tussen verschillende formuleringen van dezelfde vaardigheden of functies.

### Voorbeeld

**CV**

- Business Analytics
- Power BI
- Data Visualisatie

**Vacature**

- Business Intelligence Analyst
- Dashboard Development
- Reporting

Hoewel de gebruikte woorden verschillen, beschrijven beide teksten grotendeels dezelfde inhoud. Daarom wordt verwacht dat semantic matching deze relatie beter kan herkennen dan TF-IDF.

---

## 5. Dataset

Voor dit project zijn twee datasets gebruikt.

### Vacaturedataset

Bestand:

```text
job_descriptions.csv
```

Belangrijke kolommen:

- Job Title
- Role
- Job Description
- skills
- Responsibilities
- Qualifications
- Company

Oorspronkelijke omvang:

```text
1.615.940 vacatures
```

Tijdens de analyse bleek dat een groot deel van de vacatures inhoudelijk identiek was. Hierdoor ontstond een sterke vertekening in de matchingresultaten. Om dit probleem op te lossen is deduplicatie toegepast op de gecombineerde vacaturetekst.

| Stap | Aantal |
|--------|--------:|
| Voor deduplicatie | 1.615.940 |
| Na deduplicatie | 3.760 |
| Verwijderd | 1.612.180 |

### CV-dataset

Bestand:

```text
resume_data.csv
```

Belangrijke kolommen:

- skills
- responsibilities
- degree_names
- positions
- certification_skills
- job_position_name

Omvang:

```text
9.544 cv-profielen
```

Deze dataset is gebruikt om de matching-algoritmen te testen en te evalueren.

---

## 6. Methodologie

Het project is uitgevoerd volgens een iteratieve onderzoeksaanpak.

De ontwikkeling verliep in meerdere fasen:

1. Data loading
2. Text preprocessing
3. Deduplicatie
4. TF-IDF baseline
5. Semantic matching
6. Modelvergelijking
7. Evaluatie
8. Visualisaties
9. Streamlit-applicatie

Door beide modellen op dezelfde datasets te testen kon een eerlijke vergelijking worden gemaakt tussen traditionele en moderne NLP-technieken.

Tijdens de evaluatie is gekeken naar:

- similarity scores;
- inhoudelijke relevantie;
- kwaliteit van de gevonden functies;
- verschillen tussen beide modellen;
- invloed van preprocessing.

Omdat geen officiële labels beschikbaar waren voor correcte cv-vacaturematches is gekozen voor een ranking- en similarity-benadering in plaats van een classificatiebenadering.

# 7. Experiment 1 Data Loading

## Doel

Voordat cv's en vacatures met elkaar konden worden vergeleken, moest eerst worden gecontroleerd of beide datasets correct konden worden ingelezen en verwerkt binnen Python.

Het doel van dit experiment was daarom het ontwikkelen van een herbruikbare oplossing voor het laden van de datasets en het controleren van de structuur van de beschikbare data.

## Aanpak

Hiervoor is een `DataLoader`-klasse ontwikkeld. Deze klasse bevat functies voor het laden van zowel de vacaturedataset als de cv-dataset.

Tijdens het laden werden de datasets gecontroleerd op:

- aantal rijen;
- aantal kolommen;
- kolomnamen;
- ontbrekende waarden;
- mogelijke problemen in de brondata.

## Resultaten

Beide datasets konden succesvol worden geladen.

Tijdens de analyse werd een probleem ontdekt in de cv-dataset. Eén van de kolomnamen bevatte een verborgen karakter:

```text
\ufeffjob_position_name
```

Dit karakter ontstond door de manier waarop het CSV-bestand was opgeslagen.

## Conclusie

Het experiment liet zien dat de datasets bruikbaar waren voor verdere verwerking. Daarnaast werd direct een eerste datakwaliteitsprobleem gevonden, wat het belang van preprocessing laten zien.

---

# 8. Experiment 2 Text Preprocessing

## Doel

De ruwe datasets bevatten tekst die niet direct geschikt was voor NLP-verwerking. Het doel van dit experiment was daarom het voorbereiden van de data voor TF-IDF en semantic matching.

## Aanpak

Er is een `TextPreprocessor` ontwikkeld die verschillende preprocessingstappen uitvoert:

- kolomnamen opschonen;
- tekst omzetten naar lowercase;
- verwijderen van speciale tekens;
- verwijderen van stopwoorden;
- lemmatization;
- combineren van meerdere kolommen.

Voor vacatures werd een nieuwe tekstkolom gemaakt:

```text
job_text
```

Voor cv's werd een nieuwe tekstkolom gemaakt:

```text
resume_text
```

Hierin werden relevante velden samengevoegd zodat iedere vacature en ieder cv als een tekstrepresentatie kon worden verwerkt.

## Resultaten

De preprocessing leverde consistente tekstrepresentaties op die gebruikt konden worden door beide matchingmodellen.

Daarnaast werden kolomnamen opgeschoond waardoor eerder gevonden problemen met verborgen tekens werden opgelost.

## Conclusie

De preprocessing verbeterde de kwaliteit van de tekstdata en vormde de basis voor alle volgende experimenten.

---

# 9. Experiment 3 TF-IDF Baseline

## Doel

Het doel van dit experiment was het ontwikkelen van een eenvoudige maar uitlegbare baseline voor cv-vacaturematching.

## Waarom TF-IDF?

TF-IDF is een klassieke NLP-techniek die documenten omzet naar numerieke vectoren op basis van woordfrequenties.

Voordelen:

- snel;
- weinig geheugen;
- goed uitlegbaar;
- veel gebruikt binnen informatieopzoeksystemen.

## Aanpak

Vacatureteksten werden omgezet naar TF-IDF-vectoren.

Vervolgens werd cosine similarity gebruikt om de overeenkomst tussen een cv en alle vacatures te berekenen.

## Resultaten

Het model werkte technisch correct en gaf relevante vacatures terug.

Voor een Data Science-profiel werden bijvoorbeeld functies gevonden zoals:

- Data Engineer;
- Data Scientist;
- Machine Learning Engineer.

De eerste similarity score lag rond:

```text
0.42
```

## Beperkingen

Tijdens de evaluatie bleek dat TF-IDF sterk afhankelijk was van exacte woordoverlap.

Wanneer vergelijkbare functies andere woorden gebruikten, daalde de similarity score aanzienlijk.

## Conclusie

TF-IDF vormde een sterke baseline maar had moeite met context en synoniemen.

---

# 10. Experiment 4 Deduplicatie

## Doel

Tijdens het testen van TF-IDF viel op dat veel vacatures meerdere keren terugkwamen in de resultaten.

Het doel van dit experiment was onderzoeken hoeveel duplicaten aanwezig waren in de vacaturedataset.

## Resultaten

| Stap | Aantal |
|--------|--------:|
| Voor deduplicatie | 1.615.940 |
| Na deduplicatie | 3.760 |
| Verwijderd | 1.612.180 |

## Analyse

Meer dan 99% van de vacatures bleek een duplicaat van een andere vacature te zijn.

Zonder deduplicatie zouden modellen steeds dezelfde vacatures teruggeven. Daarnaast zou de verwerkingstijd onnodig hoog worden.

## Conclusie

Deduplicatie bleek belangrijk voor betrouwbare matchingresultaten.

---

# 11. Experiment 5 Semantic Matching

## Doel

Onderzoeken of semantic embeddings relevantere matches opleveren dan TF-IDF.

## Aanpak

Hiervoor is gebruikgemaakt van:

```text
sentence-transformers/all-MiniLM-L6-v2
```

Dit model zet teksten om naar embeddings die de betekenis van een tekst representeren.

Daarna werd opnieuw cosine similarity gebruikt.

## Resultaten

Voor dezelfde cv werden andere functies gevonden dan bij TF-IDF.

### TF-IDF

- Data Scientist
- Machine Learning Engineer

### Semantic Matching

- Business Analyst
- Data Business Analyst
- Business Intelligence Analyst

## Analyse

De cv bevatte termen zoals:

- PowerBI
- Tableau
- Data Visualisation
- Reporting

Semantic matching herkende dat deze vaardigheden beter passen bij Business Intelligence-gerelateerde functies.

## Conclusie

Semantic matching leek beter in staat om inhoudelijke relaties tussen functies te herkennen.

---

# 12. Experiment 6 Modelvergelijking

## Doel

Het direct vergelijken van TF-IDF en semantic matching.

## Resultaten

| Resume | TF-IDF | Semantic |
|----------|----------:|----------:|
| 0 | 0.477 | 0.644 |
| 1 | 0.583 | 0.715 |
| 4 | 0.446 | 0.713 |
| 7 | 0.455 | 0.706 |

## Analyse

Semantic matching behaalde consequent hogere similarity scores.

Daarnaast waren de gevonden functies inhoudelijk beter afgestemd op de vaardigheden uit de cv's.

## Conclusie

De resultaten ondersteunen de hypothese dat semantic matching beter presteert dan TF-IDF.
## 16. Reproduceerbaarheid

Een belangrijk onderdeel van dit project is reproduceerbaarheid. Het doel hiervan is dat andere gebruikers dezelfde resultaten kunnen verkrijgen wanneer zij dezelfde code, datasets en instellingen gebruiken.

Om de reproduceerbaarheid te verbeteren is het project opgebouwd volgens een vaste mappenstructuur waarbij preprocessing, modellen, evaluatie en testen van elkaar zijn gescheiden.


Daarnaast zijn alle experimenten uitgevoerd op dezelfde datasets en met dezelfde preprocessingstappen. Hierdoor kunnen resultaten opnieuw worden gegenereerd zonder wijzigingen aan de code.

Voor het uitvoeren van het project hoeft een gebruiker enkel:

1. de repository te clonen;
2. de virtual environment aan te maken;
3. de dependencies te installeren;
4. de preprocessing uit te voeren;
5. de evaluatie of Streamlit-app te starten.

Hierdoor is het project transparant en reproduceerbaar voor andere studenten en onderzoekers.

---

## 17. Reflectie

Tijdens dit project zijn verschillende NLP-technieken onderzocht voor het automatisch matchen van cv's en vacatures.

Een belangrijk inzicht was dat datakwaliteit minstens zo belangrijk is als de keuze van het model. In eerste instantie werd vooral gefocust op de implementatie van TF-IDF en semantic matching. Tijdens het analyseren van de vacaturedataset bleek echter dat een groot deel van de vacatures uit duplicaten bestond. Zonder deduplicatie zouden de resultaten sterk vertekend zijn geweest.

Daarnaast liet het project zien dat preprocessing een grote invloed heeft op de uiteindelijke prestaties van de modellen. Het verwijderen van stopwoorden en het toepassen van lemmatization zorgde voor hogere similarity scores en consistenter gedrag van beide modellen.

Een ander belangrijk inzicht was het verschil tussen traditionele NLP en moderne embedding-gebaseerde technieken. TF-IDF bleek een sterke en uitlegbare baseline, maar semantic matching kon beter omgaan met context en verschillende formuleringen van vergelijkbare vaardigheden.

Een beperking van het project is dat er geen officiële labels beschikbaar waren voor correcte cv-vacaturematches. Hierdoor konden evaluatiemethoden zoals accuracy, precision, recall en F1-score niet worden toegepast. De evaluatie moest daarom grotendeels worden gebaseerd op similarity scores en inhoudelijke beoordeling van de resultaten.

---

## 18. Conclusie

Binnen dit project is onderzocht hoe NLP kan worden ingezet voor automatische cv-vacaturematching.

Hiervoor zijn twee verschillende technieken ontwikkeld en vergeleken:

- TF-IDF met cosine similarity;
- Semantic matching met Sentence Transformers.

De resultaten laten zien dat beide technieken bruikbaar zijn voor het vinden van relevante vacatures. TF-IDF presteerde goed wanneer dezelfde vaardigheden en termen voorkwamen in zowel het cv als de vacature. Semantic matching bleek echter beter in staat om inhoudelijke overeenkomsten te herkennen wanneer verschillende woorden werden gebruikt voor vergelijkbare functies of vaardigheden.

De uitgevoerde experimenten laten zien dat semantic matching gemiddeld hogere similarity scores behaalde dan TF-IDF. Daarnaast werden de gevonden functies vaak als inhoudelijk relevanter beoordeeld.

Ook werd duidelijk dat preprocessing en deduplicatie een grote invloed hebben op de kwaliteit van de resultaten. Zonder deze stappen zouden de prestaties van beide modellen aanzienlijk lager zijn geweest.

Op basis van de uitgevoerde experimenten kan worden geconcludeerd dat semantic matching met Sentence Transformers de meest geschikte techniek was voor dit project. TF-IDF blijft echter waardevol als snelle en uitlegbare baseline.

De hypothese wordt daarmee grotendeels bevestigd: semantic matching levert in de meeste gevallen relevantere cv-vacaturematches op dan TF-IDF.

---

## 19. Bronnen

### Wetenschappelijke bronnen

Reimers, N., & Gurevych, I. (2019). *Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks*. Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing (EMNLP-IJCNLP).

https://aclanthology.org/D19-1410/

---

Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., ... Duchesnay, É. (2011). *Scikit-learn: Machine Learning in Python*. Journal of Machine Learning Research, 12, 2825–2830.

https://jmlr.org/papers/v12/pedregosa11a.html

---

### Technische documentatie

#### TF-IDF Vectorizer

https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html

#### Cosine Similarity

https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html

#### Sentence Transformers

https://www.sbert.net/

#### all-MiniLM-L6-v2

https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2

#### NLTK

https://www.nltk.org/

#### Pandas

https://pandas.pydata.org/docs/

#### Streamlit

https://docs.streamlit.io/

---

### Gebruikte software

- Python 3.9
- Pandas
- Scikit-learn
- NLTK
- Sentence Transformers
- Hugging Face Transformers
- Streamlit
- Git
- GitHub
- Visual Studio Code
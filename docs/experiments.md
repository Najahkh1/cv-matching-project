# CV Matching Project

## 1. Projectbeschrijving

Binnen recruitment worden vacatures vaak handmatig gekoppeld aan cv’s. Dit proces kost tijd en is afhankelijk van menselijke interpretatie. Daarnaast gebruiken kandidaten en werkgevers vaak verschillende woorden voor vergelijkbare functies of vaardigheden. Hierdoor kan relevante informatie over het hoofd worden gezien.

In dit project is onderzocht hoe Natural Language Processing (NLP) kan worden ingezet om cv’s automatisch te koppelen aan passende vacatures. Hierbij zijn twee verschillende benaderingen onderzocht:

- TF-IDF met cosine similarity
- Semantic matching met Sentence Transformers

Het doel van het project was niet alleen het bouwen van een werkende applicatie, maar ook het vergelijken van traditionele NLP-technieken met moderne embedding-gebaseerde technieken.

---

## 2. Onderzoeksvraag

Hoe kunnen cv’s automatisch worden gekoppeld aan passende vacatures met behulp van NLP-technieken zoals TF-IDF en semantic matching?

---

## 3. Hypothese

De verwachting is dat semantic matching met Sentence Transformers betere vacaturematches oplevert dan TF-IDF.

TF-IDF kijkt voornamelijk naar exacte woorden en woordfrequenties. Semantic matching kijkt naar de betekenis van tekst en kan daardoor overeenkomsten herkennen tussen verschillende formuleringen van dezelfde vaardigheden of functies.

Hierdoor wordt verwacht dat semantic matching relevantere resultaten oplevert wanneer cv’s en vacatures niet exact dezelfde woorden gebruiken.

---

## 4. Gebruikte data

Voor dit project zijn twee datasets gebruikt:

### Vacaturedataset

Bestand:

job_descriptions.csv

Belangrijke kolommen:

- Job Title
- Role
- Job Description
- Skills
- Responsibilities
- Qualifications
- Company

### CV-dataset

Bestand:

resume_data.csv

Belangrijke kolommen:

- skills
- responsibilities
- degree_names
- positions
- certification_skills
- job_position_name

De vacaturedataset bevatte oorspronkelijk 1.615.940 records.

Tijdens de analyse bleek dat een groot deel van deze vacatures duplicaten bevatte.

Na deduplicatie bleven 3.760 unieke vacatures over.

Dit betekent dat meer dan 1,6 miljoen dubbele records zijn verwijderd.

---

## 5. Methodologie

Het onderzoek is uitgevoerd volgens een iteratieve aanpak.

Eerst werd een traditionele NLP-baseline ontwikkeld met TF-IDF. Vervolgens werd een tweede model gebouwd op basis van semantic embeddings.

Beide modellen werden getest op dezelfde cv’s en dezelfde vacaturedataset.

De resultaten zijn vergeleken op basis van:

- similarity scores
- top-k resultaten
- inhoudelijke relevantie
- kwaliteit van de vacaturematches

Omdat de dataset geen officiële labels bevatte, kon geen gebruik worden gemaakt van accuracy of confusion matrices.

Daarom is gekozen voor kwalitatieve evaluatie en vergelijking van similarity scores.

---

## 6. Experiment 1 Data loading

### Doel

Controleren of beide datasets correct konden worden geladen.

### Aanpak

Een DataLoader class werd ontwikkeld voor het inlezen van cv’s en vacatures.

### Resultaat

Beide datasets konden succesvol worden geladen.

### Bevinding

Tijdens het laden werd een foutieve kolomnaam ontdekt:

\ufeffjob_position_name

Deze kolom is tijdens preprocessing gecorrigeerd.

---

## 7. Experiment 2  Text preprocessing

### Doel

Tekst voorbereiden voor NLP-verwerking.

### Aanpak

De volgende preprocessingstappen zijn uitgevoerd:

- lowercase
- verwijderen van speciale tekens
- stopwords removal
- lemmatization
- combineren van tekstkolommen

Nieuwe velden:

- job_text
- resume_text

### Waarom deze keuzes?

Stopwoorden voegen weinig betekenis toe aan similarity berekeningen.

Lemmatization zorgt ervoor dat woorden zoals:

- engineers
- engineering
- engineer

naar dezelfde woordvorm worden teruggebracht.

Hierdoor worden teksten consistenter.

---

## 8. Experiment 3 TF-IDF Baseline

### Doel

Een eerste werkende baseline ontwikkelen.

### Waarom TF-IDF?

TF-IDF is:

- snel
- uitlegbaar
- weinig rekenintensief
- veel gebruikt binnen traditionele informatieopzoeksystemen

### Resultaat

Top match:

Data Engineer

Similarity score:

0.42

### Bevinding

Het model werkte technisch correct maar bleek gevoelig voor duplicaten.

---

## 9. Experiment 4 Deduplicatie

### Resultaat

Voor deduplicatie:

1.615.940 vacatures

Na deduplicatie:

3.760 unieke vacatures

Verwijderd:

1.612.180 duplicaten

### Conclusie

Deduplicatie was noodzakelijk omdat herhaalde vacatures de resultaten sterk vertekenden.

---

## 10. Experiment 5 Semantic Matching

### Doel

Onderzoeken of semantic embeddings betere matches geven dan TF-IDF.

### Model

sentence-transformers/all-MiniLM-L6-v2

### Waarom gekozen?

Dit model:

- is relatief klein
- draait lokaal
- vereist beperkte hardware
- wordt veel gebruikt voor semantic similarity

### Resultaten

TF-IDF:

Data Scientist – score 0.58

Semantic:

Business Analyst – score 0.71

### Interpretatie

Semantic matching herkende beter dat de cv sterk gericht was op:

- PowerBI
- Tableau
- Business Analytics
- Reporting

waardoor Business Intelligence-gerelateerde functies werden gevonden.

---

## 11. Vergelijking TF-IDF en Semantic Matching

### Voorbeeldresultaten

| Resume | TF-IDF | Score | Semantic | Score |
|----------|----------|----------|----------|----------|
| 0 | Data Engineer | 0.477 | Data Engineer | 0.644 |
| 1 | Data Scientist | 0.583 | Business Analyst | 0.715 |
| 4 | Accountant | 0.446 | Accountant | 0.713 |
| 7 | Electrical Engineer | 0.455 | Electrical Engineer | 0.706 |

### Bevinding

Semantic matching behaalde consequent hogere similarity scores.

Daarnaast waren de gevonden functies vaak inhoudelijk beter passend bij de cv-inhoud.

---

## 12. Validatie

Omdat geen ground-truth labels beschikbaar waren, zijn de resultaten handmatig beoordeeld.

Per cv werd gekeken naar:

- functie-overeenkomst
- skill-overeenkomst
- inhoudelijke relevantie

Deze beoordeling liet zien dat semantic matching vaker logische matches produceerde.

---

## 13. Foutenanalyse

Niet alle resultaten waren correct.

Voorbeelden:

- sommige cv’s kregen functies terug die inhoudelijk te breed waren
- semantic matching was soms te gevoelig voor algemene context
- TF-IDF miste functies wanneer synoniemen werden gebruikt

Dit laat zien dat beide methoden beperkingen hebben.

---

## 14. Belangrijkste conclusie

TF-IDF bleek een sterke baseline voor exacte skill matching.

Semantic matching bleek beter in het herkennen van inhoudelijke overeenkomsten tussen cv’s en vacatures.

Voor realistische recruitmenttoepassingen lijkt een combinatie van beide technieken het meest kansrijk.

---

## 15. Beperkingen

- geen officiële labels beschikbaar
- kwalitatieve evaluatie
- semantic matching vereist meer rekenkracht
- resultaten blijven afhankelijk van datakwaliteit
- geen menselijke recruiter als referentie gebruikt

---


# CV Matching Project – Experiment Log

---

## Experiment 1

### Doel
Controleren of de datasets correct kunnen worden ingelezen.

### Aanpak
- DataLoader class gemaakt
- jobs dataset geladen
- resumes dataset geladen

### Resultaat
- jobs dataset geladen
- resumes dataset geladen

### Bevindingen
- vacaturedataset bevat 1.6 miljoen rijen
- resume dataset bevat 9544 rijen
- vreemde kolomnaam gevonden:
  '\ufeffjob_position_name'


---

## Experiment 2 Text Preprocessing

### Doel
Tekst geschikt maken voor NLP processing.

### Aanpak
TextPreprocessor class gebouwd:
- clean_column_names()
- clean_text()
- combine_columns()

Nieuwe kolommen gemaakt:
- job_text
- resume_text

### Resultaat
- tekst opgeschoond
- lowercase toegepast
- speciale tekens verwijderd
- gecombineerde tekstkolommen aangemaakt

### Bevindingen
TF-IDF input structuur is nu correct voorbereid.


---

## Experiment 3 Eerste TF-IDF Baseline

### Doel
Eerste baseline model testen voor CV matching.

### Aanpak
- TF-IDF vectorization gebruikt
- cosine similarity toegepast
- eerste 10.000 vacatures getest

### Resultaat
Top matches:
- Data Engineer
- similarity score ~0.42

### Bevindingen
- model werkt
- dataset bevat waarschijnlijk veel duplicaten
- meerdere identieke vacatures gevonden

## Experiment 4 duplicaten 
Experiment 3 — Eerste TF-IDF Baseline
1.615.940 vacatures → 3.760 unieke vacatures
1.612.180 duplicaten verwijderd


## Experiment 5 beide modellen testen 

Model     Type

TF-IDF    traditionele NLP

Semantic embeddings   transformer-based NLP

omdat ik kan zien en onderzoeken welke methode geeft betere cv matches?

voor de semantic embeddings gebruiken we sentence-transformers/all-MiniLM-L6-v2

## Experiment 6 Semantic Matching met Sentence Transformers

### Datum
12-05-2026

### Doel
Onderzoeken of semantic embeddings betere en bredere matches geven dan de TF-IDF baseline.

### Aanpak
Naast het TF-IDF model is een semantic matcher gebouwd met het model `sentence-transformers/all-MiniLM-L6-v2`. Dit model zet vacatureteksten en cv-teksten om naar embeddings op basis van betekenis.

### Resultaat
Het TF-IDF model gaf vooral Big Data Engineer vacatures terug. Het semantic model gaf ook Data Analyst, Data Scientist en NoSQL Database Engineer terug.

### Conclusie
Het semantic model lijkt beter in staat om inhoudelijk verwante functies te vinden. TF-IDF is nuttig als baseline voor exacte skill matching, terwijl semantic embeddings beter zijn voor bredere betekenisvolle matching.

Belangrijkste conclusie

TF-IDF matcht vooral op exacte woorden.

Semantic matching kijkt meer naar inhoud en context.

Dit is een sterke modelvergelijking voor je verslag.

## Experiment 7 Vergelijking TF-IDF en Semantic Matching

### Datum
12-05-2026

### Doel
Vergelijken of TF-IDF en semantic embeddings verschillende matches geven bij verschillende cv-profielen.

### Resultaat CV 1
TF-IDF gaf vooral Big Data Engineer functies terug. Semantic matching gaf naast Data Engineer ook Data Analyst, Data Scientist en NoSQL Database Engineer terug.

### Resultaat CV 2
TF-IDF gaf vooral Data Scientist en Software Tester functies terug. Semantic matching gaf meer softwaregerichte functies terug, zoals Software Developer, Mobile App Developer, Front-End Developer en UI Developer.

### Conclusie
TF-IDF is sterk afhankelijk van exacte woordoverlap. Semantic matching geeft bredere en contextueel logischere resultaten. Daarom is semantic matching waarschijnlijk geschikter wanneer cv’s en vacatures niet exact dezelfde woorden gebruiken.


PYTHONPATH=src python tests/test_model_comparison.py

Testing resume index: 1

Resume text preview:
data analysis data analytics business analysis r sas powerbi tableau data visualization business analytics machine learning machine learning leadership cross functional collaboration strategy development ml nlp infrastructure prototype transformation ml system design algorithm research application development dataset selection ml testing statistical analysis r d in ml nlp text representation data pipeline design statistical data analysis model training team collaboration research reporting algor

TF-IDF Resultaten
             Job Title                       Role               Company  similarity_score
306     Data Scientist  Machine Learning Engineer               Victrex          0.528580
153       Data Analyst             Data Scientist                   AES          0.478462
440   Business Analyst      Data Business Analyst        American Tower          0.361359
165   Business Analyst      Data Business Analyst        Balfour Beatty          0.361267
242  Marketing Analyst               Data Analyst  Constellation Brands          0.341195

Semantic resultaten
Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
Loading weights: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████| 103/103 [00:00<00:00, 6682.24it/s]
Batches: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 16/16 [00:01<00:00,  9.60it/s]
            Job Title                           Role                         Company  similarity_score
470      Data Analyst  Business Intelligence Analyst                          DuPont          0.658379
351      Data Analyst  Business Intelligence Analyst                      Tata Steel          0.658338
35       Data Analyst  Business Intelligence Analyst  Wyndham Hotels & Resorts, Inc.          0.656880
440  Business Analyst          Data Business Analyst                  American Tower          0.641338
165  Business Analyst          Data Business Analyst                  Balfour Beatty          0.640824
(.venv) (base) najahkhalifa@MacBook-Pro-van-Najah cv-matching-project % 

Dit is een heel goed vergelijkingsresultaat.

Wat betekent dit?

Deze CV gaat duidelijk over:

data analysis, business analytics, PowerBI, Tableau, ML, NLP, reporting

TF-IDF geeft:

* Data Scientist
* Data Analyst
* Business Analyst

TF-IDF pakt dus veel woorden zoals:

machine learning, data analysis, business analysis

Semantic geeft:

* Business Intelligence Analyst
* Data Business Analyst

Semantic kijkt meer naar de totale betekenis van de CV. Omdat de CV veel gaat over PowerBI, Tableau, reporting en business analytics, vindt semantic Business Intelligence Analyst heel logisch.

Conclusie

TF-IDF matcht sterker op losse keywords zoals machine learning.

Semantic matching begrijpt beter dat deze CV vooral richting:

Business Intelligence / Data Analytics

gaat.

na het lemetaztion toepassen en stopworden verwijderen de resultaten zijn 
t % PYTHONPATH=src python tests/test_model_comparison.py

Testing resume index: 1

Resume text preview:
data analysis data analytics business analysis r sa powerbi tableau data visualization business analytics machine learning machine learning leadership cross functional collaboration strategy development ml nlp infrastructure prototype transformation ml system design algorithm research application development dataset selection ml testing statistical analysis r ml nlp text representation data pipeline design statistical data analysis model training team collaboration research reporting algorithm a

TF-IDF Resultaten
             Job Title                       Role               Company  similarity_score
306     Data Scientist  Machine Learning Engineer               Victrex          0.582633
153       Data Analyst             Data Scientist                   AES          0.544447
440   Business Analyst      Data Business Analyst        American Tower          0.371653
165   Business Analyst      Data Business Analyst        Balfour Beatty          0.371559
242  Marketing Analyst               Data Analyst  Constellation Brands          0.349697

Semantic resultaten
Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
Loading weights: 100%|█████████| 103/103 [00:00<00:00, 6323.29it/s]
Batches: 100%|█████████████████████| 16/16 [00:01<00:00,  8.53it/s]
            Job Title                           Role                         Company  similarity_score
440  Business Analyst          Data Business Analyst                  American Tower          0.715449
165  Business Analyst          Data Business Analyst                  Balfour Beatty          0.715253
470      Data Analyst  Business Intelligence Analyst                          DuPont          0.701560
351      Data Analyst  Business Intelligence Analyst                      Tata Steel          0.700250
35       Data Analyst  Business Intelligence Analyst  Wyndham Hotels & Resorts, Inc.          0.697334
(.venv) (base) najahkhalifa@MacBook-Pro-van-Najah cv-matching-project % 

## Experiment Stopwords + Lemmatization

Na het toevoegen van stopwords removal en lemmatization steeg de TF-IDF top score van ongeveer 0.528 naar 0.582. De resultaten bleven inhoudelijk logisch. Semantic matching gaf vooral Business Analyst en Business Intelligence Analyst rollen terug, wat goed aansluit bij de cv-inhoud met PowerBI, Tableau, data visualization en business analytics.


Ja. Dat is eigenlijk een van de belangrijkste onderdelen van een AI-project.

Niet alleen:

"het model werkt"

maar vooral:

waarom hebben we deze keuzes gemaakt?

Dat laat zien dat je:

* begrijpt wat je bouwt
* methodisch werkt
* kunt evalueren
* bewust keuzes maakt

Hoe jullie project nu eigenlijk opgebouwd is

Stap 1 — Data loading

Waarom?

Omdat:

* datasets gescheiden waren
* herbruikbaarheid belangrijk is
* preprocessing later onafhankelijk moest blijven

Keuze

DataLoader class

Waarom class?

* code herbruikbaar
* overzichtelijk
* makkelijk uitbreiden
* separation of concerns

⸻

Stap 2 — Text preprocessing

Waarom preprocessing nodig?

Raw tekst bevat:

* hoofdletters
* rare tekens
* dubbele spaties
* irrelevante woorden

Dat zorgt voor:

ruis in NLP modellen

⸻

Keuzes preprocessing

lowercase

Waarom?

Python en python moeten hetzelfde woord zijn

⸻

regex cleaning

Waarom?

Speciale tekens:

!, ., ?, /

voegen meestal weinig betekenis toe voor TF-IDF.

⸻

stopwords removal

Waarom?

Woorden zoals:

the, and, with

komen overal voor.

Ze maken similarity minder scherp.

⸻

lemmatization

Waarom?

engineers → engineer
models → model

Dus woorden worden consistenter.

⸻

combine_columns()

Waarom?

Belangrijke informatie zat verspreid over meerdere kolommen.

Bijvoorbeeld:

* skills
* role
* responsibilities
* qualifications

Dus:

1 grote NLP representatie

gemaakt.

⸻

Stap 3 — Deduplicatie

Waarom?

De vacaturedataset had:

1.6 miljoen rijen

maar:

veel duplicaten

Problemen:

* bias
* herhaalde resultaten
* inefficiëntie

⸻

Keuze

drop_duplicates()

op:

job_text

⸻

Stap 4 — TF-IDF baseline

Waarom gekozen?

TF-IDF is:

* snel
* uitlegbaar
* klassieke NLP baseline
* sterk voor keyword matching

En:

CV matching bevat veel skills/keywords

zoals:

* Python
* SQL
* Spark

Dus:

TF-IDF was logische eerste baseline

⸻

Waarom cosine similarity?

Omdat:

* standaard techniek voor tekstsimilarity
* werkt goed met TF-IDF vectoren
* vergelijkt vectorrichting

⸻

Evaluatie TF-IDF

Sterke punten

* snelle matching
* goede skill overlap
* goede keyword herkenning

⸻

Zwakke punten

TF-IDF begrijpt:

geen betekenis/context

Dus:

* synoniemen moeilijk
* semantische relaties beperkt

⸻

Stap 5 — Semantic embeddings

Waarom semantic model?

Omdat TF-IDF beperkt bleef tot:

exacte woord overlap

We wilden testen of:

betekenis/context

betere matches gaf.

⸻

Keuze model

all-MiniLM-L6-v2

Waarom?

* lichtgewicht
* snel
* populair
* goede semantic search performance
* lokaal uitvoerbaar

⸻

Semantic evaluatie

Sterke punten

Semantic model gaf:

* bredere matches
* contextuele functies
* betere business analytics herkenning

Bijvoorbeeld:

Business Intelligence Analyst

in plaats van alleen:

Data Scientist

⸻

Zwakke punten

* langzamer
* zwaarder model
* minder uitlegbaar dan TF-IDF

⸻

Belangrijkste conclusie

TF-IDF

Sterk voor:

exacte skill matching

⸻

Semantic

Sterk voor:

contextuele/inhoudelijke matching

⸻

Waarom dit een sterke pipeline is

Omdat jullie:

* baseline ontwikkeld hebben
* iteratief verbeterd hebben
* preprocessing geëvalueerd hebben
* modellen vergeleken hebben
* semantic vs traditional NLP onderzocht hebben

Dat is een complete NLP workflow voor studentniveau.

Onderzoek: TF-IDF vs Semantic Matching voor CV Matching

Waarom hebben we twee modellen gebruikt?

Binnen dit project wilden we onderzoeken:

Welke NLP techniek geeft de meest relevante matches tussen cv’s en vacatures?

Daarom zijn twee verschillende benaderingen getest:

Model	Type
TF-IDF	traditionele NLP / keyword matching
Sentence Transformers	semantic NLP / meaning-based matching

⸻

1. TF-IDF Model

Wat is TF-IDF?

TF-IDF staat voor:

Term Frequency – Inverse Document Frequency

Het model kijkt naar:

* welke woorden voorkomen
* hoe vaak woorden voorkomen
* hoe uniek woorden zijn binnen de dataset

Daarna worden teksten omgezet naar vectoren en vergeleken met:

cosine similarity

⸻

Waarom gekozen?

TF-IDF is gekozen als:

baseline model

omdat het:

* snel is
* lichtgewicht is
* makkelijk uitlegbaar is
* veel gebruikt wordt in traditionele recruitment systemen
* goed werkt bij skill/keyword matching  ￼

⸻

Sterke punten TF-IDF

Goed in:

* exacte skill matching
* technische keywords
* snelle similarity berekeningen
* grote datasets

Bijvoorbeeld:

* Python
* SQL
* Spark
* Hadoop

werden sterk herkend.

⸻

Zwakke punten TF-IDF

TF-IDF begrijpt:

geen betekenis/context

Dus:

* synoniemen werken minder goed
* andere formuleringen worden lastig
* semantic relaties ontbreken

Bijvoorbeeld:

CV	Vacature
AI engineer	Machine Learning Specialist

kunnen lage similarity krijgen als woorden verschillen.

Onderzoek toont ook aan dat TF-IDF vaak moeite heeft met semantic similarity en vooral afhankelijk blijft van exacte woord overlap  ￼

⸻

Resultaten binnen ons project

TF-IDF gaf vaak:

* Data Engineer
* Data Scientist
* Business Analyst

wanneer dezelfde technische woorden sterk aanwezig waren.

Na preprocessing verbeteringen:

* stopwords removal
* lemmatization

werden scores beter en consistenter.

Bijvoorbeeld:

* TF-IDF score steeg van ongeveer 0.52 → 0.58.

⸻

2. Semantic Matching (Sentence Transformers)

Wat is semantic matching?

Semantic matching probeert niet alleen woorden te vergelijken, maar:

de betekenis van teksten

Daarvoor gebruikten we:

sentence-transformers/all-MiniLM-L6-v2

Dit model zet teksten om naar embeddings:

* dense vector representaties
* gebaseerd op context en betekenis

Daarna wordt opnieuw cosine similarity gebruikt.

⸻

Waarom gekozen?

Het semantic model is gekozen omdat:

* TF-IDF beperkt bleef tot keyword overlap
* cv’s en vacatures vaak andere formuleringen gebruiken
* semantic similarity belangrijk is bij recruitment matching  ￼

⸻

Waarom specifiek all-MiniLM-L6-v2?

Dit model is gekozen omdat het:

* lichtgewicht is
* snel draait op gewone laptops
* populair is voor semantic search
* goede performance levert voor sentence similarity taken  ￼

⸻

Sterke punten semantic matching

Semantic matching was beter in:

* context begrijpen
* business analytics herkennen
* bredere functierelaties vinden
* synoniemen herkennen

Bijvoorbeeld:

* Business Intelligence Analyst
* Data Business Analyst

werden gevonden terwijl TF-IDF vooral focuste op:

* Machine Learning Engineer
* Data Scientist

⸻

Zwakke punten semantic matching

Nadelen:

* langzamer
* meer rekenkracht nodig
* moeilijker uitlegbaar
* embeddings zijn complexer dan TF-IDF vectoren

⸻

Belangrijkste verschil

TF-IDF	Semantic Matching
kijkt naar woorden	kijkt naar betekenis
keyword overlap	contextuele similarity
snel	zwaarder
eenvoudig uitlegbaar	complexer
goed voor skills	goed voor semantic matching

⸻

Welke werkte beter voor ons project?

Conclusie

Voor ons CV matching project bleek:

TF-IDF

goed te werken voor:

* technische skill overlap
* exacte keyword matching

Semantic matching

beter te werken voor:

* context
* business analytics rollen
* bredere inhoudelijke overeenkomsten

Daardoor lijkt semantic matching geschikter voor realistische recruitment matching, vooral wanneer cv’s en vacatures verschillende formuleringen gebruiken. TF-IDF bleef echter een sterke baseline vanwege snelheid en uitlegbaarheid.

⸻

Waarom beide modellen belangrijk waren

Door beide modellen te gebruiken konden we:

* traditionele NLP vergelijken met moderne NLP
* modelverschillen analyseren
* preprocessing evalueren
* verschillende matchingstrategieën onderzoeken

Dit maakte het project methodischer en beter uitlegbaar.

t % PYTHONPATH=src python src/evaluation/evaluate_models.py
Loading processed datasets...
Initializing models...
Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
Loading weights: 100%|█████████| 103/103 [00:00<00:00, 6205.57it/s]
Training TF-IDF model...
Creating semantic embeddings...
Batches: 100%|█████████████████████| 16/16 [00:01<00:00, 10.43it/s]
Starting evaluation...

Evaluation Results:

    resume_index     model              job_title                        role                     company     score
0              0    TF-IDF          Data Engineer           Big Data Engineer             Lendlease Group  0.477241
1              0  Semantic          Data Engineer           Big Data Engineer  Fidelity Investments, Inc.  0.643776
2              1    TF-IDF         Data Scientist   Machine Learning Engineer                     Victrex  0.582633
3              1  Semantic       Business Analyst       Data Business Analyst              American Tower  0.715449
4              2    TF-IDF         Data Scientist   Machine Learning Engineer                     Victrex  0.383038
5              2  Semantic         Data Scientist   Machine Learning Engineer                     Victrex  0.506131
6              3    TF-IDF        Account Manager       Sales Account Manager                 BYD Company  0.359569
7              3  Semantic      Account Executive     Sales Account Executive      China Eastern Airlines  0.684466
8              4    TF-IDF             Accountant        Financial Accountant                    Huntsman  0.446002
9              4  Semantic             Accountant        Financial Accountant                    Huntsman  0.713220
10             5    TF-IDF  IT Support Specialist  Desktop Support Technician                     Corteva  0.306286
11             5  Semantic  Network Administrator            Network Engineer         HeidelbergCement AG  0.654965
12             6    TF-IDF         Data Scientist   Machine Learning Engineer                     Victrex  0.180031
13             6  Semantic         Data Scientist   Machine Learning Engineer                     Victrex  0.501023
14             7    TF-IDF    Electrical Designer         Electrical Engineer           Regions Financial  0.454807
15             7  Semantic    Electrical Designer         Electrical Engineer                Revlon, Inc.  0.706167
16             8    TF-IDF           Data Analyst              Data Scientist                         AES  0.442077
17             8  Semantic         Data Scientist   Machine Learning Engineer                     Victrex  0.598129
18             9    TF-IDF    Procurement Manager  Strategic Sourcing Manager              Commerzbank AG  0.249142
19             9  Semantic      Software Engineer           Backend Developer                      Cintas  0.589303

Results saved to:
results/model_evaluation.csv
(.venv) (base) najahkhalifa@MacBook-Pro-van-Najah cv-matching-project % 

resume_index,model,job_title,role,company,score
0,TF-IDF,Data Engineer,Big Data Engineer,Lendlease Group,0.4772413009017212
0,Semantic,Data Engineer,Big Data Engineer,"Fidelity Investments, Inc.",0.6437762975692749
1,TF-IDF,Data Scientist,Machine Learning Engineer,Victrex,0.5826328502740151
1,Semantic,Business Analyst,Data Business Analyst,American Tower,0.715449333190918
2,TF-IDF,Data Scientist,Machine Learning Engineer,Victrex,0.3830383728481323
2,Semantic,Data Scientist,Machine Learning Engineer,Victrex,0.5061307549476624
3,TF-IDF,Account Manager,Sales Account Manager,BYD Company,0.3595692749549099
3,Semantic,Account Executive,Sales Account Executive,China Eastern Airlines,0.6844656467437744
4,TF-IDF,Accountant,Financial Accountant,Huntsman,0.44600154174888845
4,Semantic,Accountant,Financial Accountant,Huntsman,0.7132200002670288
5,TF-IDF,IT Support Specialist,Desktop Support Technician,Corteva,0.30628647090048533
5,Semantic,Network Administrator,Network Engineer,HeidelbergCement AG,0.6549652814865112
6,TF-IDF,Data Scientist,Machine Learning Engineer,Victrex,0.18003076075300015
6,Semantic,Data Scientist,Machine Learning Engineer,Victrex,0.5010230541229248
7,TF-IDF,Electrical Designer,Electrical Engineer,Regions Financial,0.4548065140106469
7,Semantic,Electrical Designer,Electrical Engineer,"Revlon, Inc.",0.7061669826507568
8,TF-IDF,Data Analyst,Data Scientist,AES,0.44207741790976596
8,Semantic,Data Scientist,Machine Learning Engineer,Victrex,0.5981294512748718
9,TF-IDF,Procurement Manager,Strategic Sourcing Manager,Commerzbank AG,0.24914202014991266
9,Semantic,Software Engineer,Backend Developer,Cintas,0.5893030166625977


Waarom geen confusion matrix / accuracy?

Een confusion matrix en accuracy werken alleen bij supervised classification. Dan heb je per voorbeeld een echte juiste klasse nodig.

Bijvoorbeeld:
V 1 → echte label: Data Engineer

CV 2 → echte label: Business Analyst

In ons project hebben we dat niet. We hebben wel CV’s en vacatures, maar geen officiële “juiste vacature” per CV. Daarom kunnen we niet eerlijk zeggen of een match goed of fout is.

Ook kan één CV bij meerdere vacatures passen. Bijvoorbeeld een profiel met Python, ML en data-analyse kan passen bij:


Data Analyst

Data Scientist

Machine Learning Engineer

Business Intelligence Analyst
Daarom gebruiken we geen accuracy of confusion matrix. In plaats daarvan evalueren we met:

similarity scores

modelvergelijking

kwalitatieve beoordeling

top-k analyse

Dit past beter bij CV matching, omdat het een ranking/similarity probleem is en geen gewone classificatie.

Code voor visualisaties

Maak dit bestand:
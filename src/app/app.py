import sys
from pathlib import Path

import pandas as pd
import streamlit as st
from docx import Document
from pypdf import PdfReader

sys.path.append("src")

from models.tfidf_matcher import TFIDFMatcher
from models.semantic_matcher import SemanticMatcher


JOBS_PATH = "data/processed/jobs_processed.csv"
SUPPORTED_FILE_TYPES = ["txt", "pdf", "docx"]


st.set_page_config(
    page_title="CV Matching App",
    layout="wide"
)


def extract_text_from_txt(uploaded_file):
    return uploaded_file.read().decode("utf-8", errors="ignore")


def extract_text_from_pdf(uploaded_file):
    reader = PdfReader(uploaded_file)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    return text


def extract_text_from_docx(uploaded_file):
    document = Document(uploaded_file)
    text = ""

    for paragraph in document.paragraphs:
        text += paragraph.text + "\n"

    return text


def extract_cv_text(uploaded_file):
    if uploaded_file is None:
        return ""

    file_name = uploaded_file.name.lower()

    if file_name.endswith(".txt"):
        return extract_text_from_txt(uploaded_file)

    if file_name.endswith(".pdf"):
        return extract_text_from_pdf(uploaded_file)

    if file_name.endswith(".docx"):
        return extract_text_from_docx(uploaded_file)

    return ""


@st.cache_data
def load_jobs_data():
    if not Path(JOBS_PATH).exists():
        st.error(
            "Processed vacaturebestand niet gevonden. "
            "Run eerst: PYTHONPATH=src python src/preprocessing/run_preprocessing.py"
        )
        st.stop()

    jobs_df = pd.read_csv(JOBS_PATH)

    required_columns = [
        "Job Title",
        "Role",
        "Company",
        "Job Description",
        "job_text",
    ]

    missing_columns = [
        col for col in required_columns
        if col not in jobs_df.columns
    ]

    if missing_columns:
        st.error(f"Deze kolommen ontbreken in jobs_processed.csv: {missing_columns}")
        st.stop()

    return jobs_df


def run_matching(model_choice, cv_text, jobs_sample, top_n):
    if model_choice == "TF-IDF":
        matcher = TFIDFMatcher()
        matcher.fit_transform_jobs(jobs_sample["job_text"])
        return matcher.match_resume_to_jobs(cv_text, jobs_sample, top_n=top_n)

    matcher = SemanticMatcher()
    matcher.fit_jobs(jobs_sample["job_text"].tolist())
    return matcher.match_resume_to_jobs(cv_text, jobs_sample, top_n=top_n)


def prepare_display_results(results):
    display_results = results.copy()

    if "Job Description" not in display_results.columns:
        display_results["Job Description"] = "Geen functie-uitleg beschikbaar"

    display_results["Job uitleg"] = (
        display_results["Job Description"]
        .fillna("Geen functie-uitleg beschikbaar")
        .astype(str)
        .str[:500]
    )

    display_results["similarity_score"] = (
        display_results["similarity_score"]
        .astype(float)
        .round(4)
    )

    return display_results[
        [
            "Job Title",
            "Role",
            "Company",
            "similarity_score",
            "Job uitleg",
        ]
    ]


st.title("CV Matching App")

st.write(
    "Upload of plak een CV. De app vergelijkt het CV met vacatures "
    "en toont de best passende functies met een korte functie-uitleg."
)

jobs_df = load_jobs_data()

with st.sidebar:
    st.header("Instellingen")

    model_choice = st.selectbox(
        "Kies matching model",
        ["TF-IDF", "Semantic"],
        help="TF-IDF kijkt vooral naar woordoverlap. Semantic kijkt meer naar betekenis."
    )

    top_n = st.slider(
        "Aantal matches",
        min_value=3,
        max_value=10,
        value=5
    )

    sample_size = st.slider(
        "Aantal vacatures gebruiken",
        min_value=100,
        max_value=min(3000, len(jobs_df)),
        value=500,
        step=100,
        help="Een kleinere sample is sneller. Een grotere sample zoekt in meer vacatures."
    )

st.subheader("CV invoer")

uploaded_file = st.file_uploader(
    "Upload een CV bestand",
    type=SUPPORTED_FILE_TYPES
)

manual_text = st.text_area(
    "Of plak hier de CV tekst",
    height=250,
    placeholder="Voorbeeld: I have experience with Python, SQL, PowerBI, Tableau and data analysis..."
)

uploaded_text = extract_cv_text(uploaded_file)

if uploaded_text.strip():
    cv_text = uploaded_text
else:
    cv_text = manual_text

if cv_text.strip():
    st.subheader("CV preview")
    st.text(cv_text[:1000])

jobs_sample = jobs_df.head(sample_size)

if st.button("Zoek matches", type="primary"):
    if not cv_text.strip():
        st.warning("Upload een CV of plak eerst CV tekst.")
    else:
        try:
            with st.spinner("Matches zoeken..."):
                results = run_matching(
                    model_choice=model_choice,
                    cv_text=cv_text,
                    jobs_sample=jobs_sample,
                    top_n=top_n
                )

            display_results = prepare_display_results(results)

            st.subheader("Top matches")
            st.dataframe(display_results, use_container_width=True)

            st.info(
                "Let op: de similarity score is een hulpmiddel. "
                "Een hogere score betekent dat het CV tekstueel of semantisch sterker lijkt op de vacature."
            )

        except Exception as error:
            st.error("Er is iets misgegaan tijdens het matchen.")
            st.code(str(error))
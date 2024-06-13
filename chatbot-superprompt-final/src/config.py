import os

# API KEY
OPENAI_API_KEY = ""
COHERE_API_KEY = "NtPSNPeesZ1ruJGpi6zoxfhxNZlA88D491TYXykm"
HUGGINGFACEHUB_API_TOKEN = "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"
TOGETHER_AI_API_KEY = "c30748cca2a1b1e7a76b3f80e5bbd29f0475a5ba8fb87a54559509927390b446" # Api Llama

# LLM
MODEL_LLM_LOCAL_XS = "google/flan-t5-base"
MODEL_LLM_LOCAL_XL = "google/flan-t5-xl"
SPACY_LLM = "en_core_web_md"
SPACY_LLM_FR = "fr_core_news_md"

# Vectorstores Data Base
DATA_PATH = "data"
DATABASE_PATH = "vectorstores"
PDF_FILE_PATH = os.path.join(DATA_PATH, "files")
FILE_EXTENTION = ".md"

# Scrapping
NB_SCRAP_RESEARCH = 2
import streamlit as st
from tools.view import get_readme

st.set_page_config(
    page_title="V-Nutrition",
    page_icon="🥦",
    layout="wide",
    menu_items={
        "Get Help": "https://gitlab.com/vnutrition/vnutrition-github",
        "Report a bug": "https://gitlab.com/vnutrition/vnutrition-github",
        "About": """
            Fait par [Tonow](https://gitlab.com/Tonow). Sous licence libre **GNU 3** \n
            N'hésitez pas à aider ou faire des commentaires.
        """,
    },
)

get_readme(["pages"])

from os import path
import streamlit as st


@st.cache_data
def get_readme(readme_path: list):
    """From a path read README.md file and use st.markdown.

    Args:
        path (list): Path of the readme file.
    """
    with open(
        path.join(*readme_path, "README.md"), "r", encoding="utf-8"
    ) as readme_file:
        readme_content = readme_file.read()

    st.markdown(readme_content)

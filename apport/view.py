import streamlit as st

def show_columns_value(df):
    columns_name = st.multiselect("apport", df.columns)
    for column_name in columns_name:
        if df[column_name].any():
            try:
                value = float(df[column_name])
                st.metric(label=column_name, value=value, delta=None)
            except ValueError as ve:
                st.error(f"Pour {column_name} : {ve}")
        else:
            st.error(f"Aucune Valeur pour {column_name}")

def get_readme(path: str):
    # Read content from README.md
    with open(f"{path}/README.md", "r", encoding="utf-8") as readme_file:
        readme_content = readme_file.read()

    # Display the content using st.markdown()
    st.markdown(readme_content)

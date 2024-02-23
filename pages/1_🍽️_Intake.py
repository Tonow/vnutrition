from pages.intake.sidebar import show_sidebar
from pages.intake.main_content import show_main_content

df, show_columns = show_sidebar()
show_main_content(df, show_columns)

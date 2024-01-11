import streamlit as st

st.set_page_config(page_title="DSBS FOUI Rapport", page_icon="favicon.ico")
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        #GithubIcon {visibility: hidden;}
        footer {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

st.image("logo.png", width=180)
st.title ("FOUI Rapport - Drottning Silvias Barn och Ungdomssjukhus")
st.header ("Om rapporten")
st.write("Rapporten är en sammanställning av forskning, handledning och undervisning på DSBS. Den innehåller information från alla år, med möjlighet att filtrera på år och forskare. Rapportens källkod finns att tillgå.")
st.write("---")
st.write("Verksamhetschef: X (X.X@vgregion.se)")
st.write("Information om applikationen: Maria Henningsson (maria.k.henningsson@vgregion.se)")
st.subheader("DSBS FOU-Råd")
st.write("""
         X, Y, Z
         """)

# Link to website of ALF Västra Götaland (https://www.alfvastragotaland.se/)
st.subheader("Länkar")
if st.button("ALF Västra Götaland"):
    st.write("https://www.alfvastragotaland.se/")
if st.button("Drottning Silvias Barn och Ungdomssjukhus"):
    st.write("https://www.sahlgrenska.se/om-sjukhuset/nya-barnsjukhuset/")
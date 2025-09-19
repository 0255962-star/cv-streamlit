import streamlit as st
from pathlib import Path
import base64

st.set_page_config(page_title="CV de Alejandro", page_icon="📄", layout="centered")
st.title("📄 Currículum de Alejandro Gascón de Alba")

st.write("Aquí puedes ver y descargar mi CV en PDF.")

cv_file = Path("cv.pdf")

def show_pdf(file):
    with open(file, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        iframe = f'<iframe src="data:application/pdf;base64,{b64}" width="100%" height="850"></iframe>'
        st.markdown(iframe, unsafe_allow_html=True)
        st.download_button("⬇️ Descargar CV", data=data, file_name="Alejandro_Gascon_CV.pdf", mime="application/pdf")

if cv_file.exists():
    show_pdf(cv_file)
else:
    st.error("No encontré el archivo cv.pdf en la carpeta del proyecto.")

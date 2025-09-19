import streamlit as st
from pathlib import Path

st.set_page_config(page_title="CV – Alejandro Gascón de Alba", page_icon="📄", layout="wide")

# ----- Archivos esperados en la carpeta -----
CV_PATH = Path("cv.pdf")
# Pon tu foto con este nombre (recomiendo 600–900 px de ancho, JPG o PNG)
PHOTO_CANDIDATES = ["foto_perfil.jpg", "foto_perfil.png", "foto.jpg", "foto.png", "profile.jpg", "profile.png"]
PHOTO_PATH = next((Path(p) for p in PHOTO_CANDIDATES if Path(p).exists()), None)

# ----- Estilos suaves -----
st.markdown("""
<style>
#MainMenu, footer, header {visibility: hidden;}
.block-container {padding-top: 1rem; padding-bottom: 2rem; max-width: 1100px;}
.badge {display:inline-block; padding:4px 8px; border-radius:10px; background:#f1f3f5; margin:2px 6px 2px 0;}
.small { color:#666; font-size:0.95rem; }
</style>
""", unsafe_allow_html=True)

# ----- Encabezado -----
st.markdown("# Alejandro Gascón de Alba")
st.markdown("📧 [gascondealbaalejandro@gmail.com.mx](mailto:gascondealbaalejandro@gmail.com.mx)  •  📞 33 3954 3566  •  📍 Zapopan, Jalisco")
st.divider()

col1, col2 = st.columns([2.2, 1], gap="large")

# --------- Columna izquierda: contenido del CV (texto) ----------
with col1:
    st.subheader("Perfil")
    st.write(
        "Actualmente, soy estudiante de Administración y Finanzas en la Universidad Panamericana de Guadalajara. "
        "Busco un aprendizaje continuo y la oportunidad de crecer en un entorno que fomente el desarrollo de "
        "habilidades valiosas para mi carrera a largo plazo. Me apasiona entender los procesos de contaduría y "
        "finanzas para involucrarme al máximo y aportar en la operación diaria."
    )

    st.subheader("Formación")
    st.markdown("**Universidad Panamericana** — Licenciatura en Administración y Finanzas  \n*ago 2022 – presente*")
    st.markdown("**Instituto de Ciencias** — Preparatoria  \n*ago 2019 – jun 2022*")
    st.markdown("**St. Catherines Academy** — Internado con tradición militar  \n*ago 2016 – jun 2017*")

    st.subheader("Experiencia")
    st.markdown("**Auxiliar Administrativo Financiero — Harmony Shake**  \n*jun 2022 – ene 2024*")
    st.markdown(
        "- Responsable de finanzas y contabilidad de la startup, gestión de registros y control administrativo.  \n"
        "- Elaboración de reportes y apoyo en toma de decisiones."
    )
    st.markdown("**Gerente de ventas — Macetas 4 Hermanos**  \n*sep 2021 – ago 2022*")
    st.markdown(
        "- Venta y distribución de macetas para viveros de la ciudad.  \n"
        "- Atención a clientes y seguimiento a inventarios."
    )

    # Recuadro de descarga del PDF
    with st.container(border=True):
        st.subheader("Descargar mi CV en PDF")
        if CV_PATH.exists():
            with open(CV_PATH, "rb") as f:
                st.download_button("⬇️ Descargar CV (PDF)",
                                   data=f.read(),
                                   file_name="Alejandro_Gascon_CV.pdf",
                                   mime="application/pdf")
        else:
            st.error("No encontré `cv.pdf`. Súbelo a la carpeta del proyecto.")

# --------- Columna derecha: foto con recuadro + habilidades ----------
with col2:
    st.subheader("Mi foto")
    with st.container(border=True):
        if PHOTO_PATH and PHOTO_PATH.exists():
            st.image(str(PHOTO_PATH), caption="Alejandro Gascón de Alba", use_container_width=True)
        else:
            st.info("Agrega una imagen llamada **foto_perfil.jpg** (o .png) a la carpeta para mostrarla aquí.")

    st.subheader("Datos personales")
    st.write("**Fecha de nacimiento:** 11 de agosto de 2003")

    st.subheader("Competencias")
    st.write("- Contabilidad básica")
    st.write("- Ventas")
    st.write("- E-commerce")
    st.write("- Manejo de Commerce/Point")

    st.subheader("Herramientas")
    st.caption("Nivel de Excel");  st.progress(0.85)
    st.caption("PowerPoint");      st.progress(0.75)

    st.subheader("Habilidades blandas")
    st.markdown(
        "<span class='badge'>Liderazgo</span>"
        "<span class='badge'>Comunicación asertiva</span>"
        "<span class='badge'>Inglés avanzado</span>"
        "<span class='badge'>Iniciativa</span>"
        "<span class='badge'>Pensamiento crítico</span>"
        "<span class='badge'>Trabajo en equipo</span>"
        "<span class='badge'>Aprendizaje continuo</span>"
        "<span class='badge'>Flexibilidad</span>",
        unsafe_allow_html=True
    )

st.divider()
st.markdown("<span class='small'>Actualiza este archivo y haz <code>git push</code> para refrescar tu CV en línea.</span>", unsafe_allow_html=True)


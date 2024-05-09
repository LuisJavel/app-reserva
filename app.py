import streamlit as st
from streamlit_option_menu import option_menu

page_title = "cita de clinina dental Salasaca"
page_icon= '✅'
layout = 'centered'

horas = ["9:00", "10:00", "11:00"]
Pista= ["Pista 1", "Pista 2"]

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)


#st.image("assets/doct.png")
st.title("Dental Salasaka")
st.text("Av. el Rosario comunidad centro Salasaca")

selected = option_menu(menu_title=None, options=["Reserva", "Pista", "Detalles"],
                       icons=["calendar-date", "building", "clipboard-minus"],
                       orientation="horizontal")


if(selected  == "Detalles"):

  st.image("assets/map.png")
  st.markdown("Pulsa [aqui](https://maps.app.goo.gl/7GXS3Db6mvDn1fbi6) para ver la dirreccion")


  st.subheader("Horarios")
  dia, hora = st.columns(2)

  dia.text("Lunes")
  hora.text("9:00 - 18:00")
  dia.text("Martes")
  hora.text("9:00 - 18:00")
  dia.text("Miercoles")
  hora.text("9:00 - 18:00")
  dia.text("Jueves")
  hora.text("9:00 - 18:00")
  dia.text("Viernes")
  hora.text("9:00 - 18:00")
  dia.text("Sabado")
  hora.text("9:00 - 14:00")

  st.subheader("Contacto")
  st.text("📞65492333")
  st.subheader("Facebook")
  st.text("")


  if (selected == "Pista"):
    st.subheader("Nuestro servicios")
  
if selected == "Reserva":
  st.subheader("Reserva")

  c1,c2 = st.columns(2)

  nombre = c1.text_input("Tu Nombre")
  email = c2.text_input("Tu email")
  fecha = c1.date_input("Fecha")
  hora = c2.selectbox("Hora",horas)
    #c1.selectbox("Pista",pista)
  c2.text_area("Notas")

  enviar = st.button("Reservar")

  if enviar:

    if nombre == "":
      st.warning("El nombre en Obligatorio")
    elif email == "":
      st.warning("El email en Obligatorio")

    else:
      #google calendario
      #crea googleshio
      st.success("su pista ha sido reservado con exito")

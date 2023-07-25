# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 11:56:22 2022

@author: Arnaud
"""
# Libraries
from streamlit_folium import st_folium
from PIL import Image
import streamlit as st
import folium as fo
import pandas as pd

# links
# https://www.webfx.com/tools/emoji-cheat-sheet/
# https://formsubmit.co/
# https://randyzwitch-streamlit-folium-examplesstreamlit-app-qc22uj.streamlitapp.com/
# https://www.python-graph-gallery.com/all-charts/
# C:\Users\Arnaud\Desktop\Webpage\
# https://getbootstrap.com/docs/3.3/components/

# Variables
logo_age=Image.open('logo_age.png')
image1 = Image.open('narva_1.jpeg')
image_cloud = Image.open('p_image_cloud.jpg')
image_maplegend = Image.open('p_maplegend_2.png')
p_profile = Image.open('p_profile.png')



# Set page layouts
st.set_page_config(page_title="AGE", page_icon=":fr:", layout="wide")

# Local css for style
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style.css")


# intro
with st.container():
    #st.title("ARNAUD GUIRAUD INGENIERIE")
    st.image(logo_age)
    st.write('---')

with st.container():
    column_left, column_right = st.columns([1,1])
    with column_left:
        st.write(""" """)
        st.image(image1)
    with column_right:
        #st.title("Bonjour et Bienvenue :rocket:")
        st.subheader('''QUI SOMMES NOUS?''')
        st.write(
        """
        Société de services aux industriels, principalement énergéticiens. 
        
        Notre coeur de métier est l'accompagnement de nos clients dans la conduite de leurs projets clé en main, dit EPCC:
        
        _Engineering, Procurement, Construction, Commissioning_. 
        
        Nous intervenons à chaque étapes du projet, selon vos besoins: 
            Renfort de vos équipes, 
            Expertise technique, 
            Prestation sur mesure.
        
        Afin de nous adapter à vos modes de fonctionnement, nos prestations se déclinent sous différents formats: A distance, dans vos bureaux, sur chantier. 
        Notre structure réduite nous permet de cultiver nos forces: Agilité, dynamisme, savoir-faire. En France comme à l'étranger. 
             
        """)       
        

#Savoir-faire
with st.container():
    st.write('---')
    st.subheader(''':gear: DOMAINES D'EXPERTISE''')
              
    st.subheader('''Pour vos réalisations d'ouvrages énergétiques...''')
    
    column_one, column_two, column_three = st.columns(3)
    with column_one:
          st.subheader("""_ENGINEERING & PROCUREMENT_""")
          st.write(
              """
              - Définition des besoins et solutions techniques appropriés
              - Expertise technique et process
              - Etudes fonctionnelles et de faisabilité
              - Rédaction des procédures d'Essais et de Mise en Service
              - Rédaction des procédures de mise en sécurité type TOP/LOTO
              - Rédaction de spécifications techniques d'achâts
              - Consultation de fournisseurs et sous-traitant
              - Planification et coordination des intenventions sur site
              """
              )
          
    with column_two:     
          st.subheader("""_CONSTRUCTION & COMMISSIONING_""")
          st.write("""
              - Mise en place des politiques Qualités et EHS
              - Pilotage des activités (Avancement, Budget, Equipes)
              - Supervision montage Electriques et Mécaniques
              - Réalisation et/ou supervision de la Mise en Service 
              - Réalisation et/ou supervision des campagnes d'essais et essais de performances
              - Gestion des relations clients et partenaires
              """
              )
          
    with column_three:     
          st.subheader("""_OPERATION & EXPLOITATION_""")
          st.write(""" """)
          st.write(""" """)
          st.write("""
              - Rédaction des documents de formation aux nouveaux systèmes
              - Formation des opérateurs et du personnel exploitant
              - Pilotage des installations - Exploitation - Chargé de quart
              """
              )
          
          
    st.subheader(''' ... Et après leur mise en service.''')
    
    column_one, column_two=st.columns(2)
    with column_one: 
        st.subheader("""_ANALYSES ET OPTIMISATION DE VOS ACTIFS_""")
        st.write("""
                 - Création d'outils d'aide au pilotage opérationnel (KFI/KPI)
                 - Automatisation des tâches informatiques récurrentes
                 - Analyses de la performance (Industries, Retail, Finance)
                 - Etudes quantitatives et statistiques
                 - Projets Big Data et data science appliqués à vos business (ex: Prédictif pour production d'énergies renouvelables)
                 """
                 )  
    with column_two:
        st.subheader("""_MAINTENANCE ET ARRETS PROGRAMMES_""")
        st.write("""
                 - Préparation et Pilotage des interventions
                 - Expertise, conseil, études techniques pour revamping ou modification des installations
                 """
                 )  

# Le président
with st.container():
    st.write('---')
    st.subheader(''':sparkles: LE MOT DU FONDATEUR ET DIRIGEANT''')
    columns_left, columns_right=st.columns([1,2])
    with columns_left:
        st.image(p_profile)
    with columns_right:
        st.write(
            """
            Je suis un ingénieur passionné. Cette voie a toujours été une évidence. Prendre chaque problème à bras le corps, travailler dur lorsque les difficultés s’accumulent pour enfin trouver la clé qui déverrouille l’ensemble est mon moteur. 
Lorsque je m’engage dans un projet, je ne garantie pas un voyage sans encombre.  Chacun de nous, professionnels et acteurs de nos écosystèmes industriels, avons bien conscience que difficultés et imprévus sont lots communs. Cependant je certifie que toute mon energie ainsi que celle de mes collaborateurs sera concentré vers l’objectif commun, vers la réussite commune. Mes années en tant que manager mon appris au combien il est important que les collaborateurs soient part d’une solution et non du problème. Que la prise d’initiative pour trouver des solutions est bien plus appréciable qu’un simple retour d’information.  
J’ai créé AGE en ce sens, avec cette volonté féroce d’apporter une réelle assistance, un service de qualité. Réellement utile à ceux qui nous font confiance. A vous, managers, dirigeants, chefs de projets, qui ferraillent jours après jours pour mener à bien leur mission. 

            """
            )

#Valeurs
with st.container(): 
    st.write('---')
    st.subheader('''🧬DES VALEURS COMME ADN''')
    st.image(image_cloud)

#Parcours
with st.container(): 
    st.write('---')
    st.subheader(""":sparkles: REALISATIONS""")
    
    column_left, column_right= st.columns([3, 1])
    with column_left:
    
        # Add map and markers
        file = pd.read_excel('e_map_list.xlsx')
        world= fo.Map(location=[30, 10], zoom_start=2)
            
        pro=file.loc[file['Type']==1]
        #pers=file.loc[file['Type']==2]

        for lat, lon, loc, fon, trav, im, url in zip(pro['latitude'],pro['longitude'], pro['location'], pro['fonction'], pro['travaux'], pro['image'], pro['url']):
            id_html = fo.Html(f"""
            <p style="text-align: center;"><img src={im} alt="Oups, there should be an image" width="90" height="90">
            <p style="text-align: left;"><a href={url} target="_blank" title="Click for more..."><span style="font-family: Arial, serif; font-size: 18px; color:navy;"><U><B>{loc}</B></U></span></a></p>
            <p style="text-align: left;"><b><span style="font-family: Arial, serif; font-size: 16px; color:dimgray;"> FONCTION : <br>{fon}</br></b></span></p>
            <p style="text-align: left;"><b><span style="font-family: Arial, serif; font-size: 16px; color:dimgray;"> TRAVAUX : <br>{trav}</br></b></span></p>
            """, script=True)
            
            popup=fo.Popup(id_html, max_width=400) 
                
            fo.Marker(location=[lat,lon], 
                      tooltip=loc, 
                      popup=popup,
                      icon =fo.Icon(color='darkred', icon='send')).add_to(world)
    
        #for lat1, lon1, loc1, fon1, im1, url1 in zip(pers['latitude'],pers['longitude'], pers['location'], pers['fonction'],  pers['image'],  pers['url']):
        #    id_html1 = fo.Html(f"""
        #    <p style="text-align: center;"><img src={im1} alt="Oups, there should be an image" width="90" height="90">
        #    <p style="text-align: left;"><a href={url1} target="_blank" title="Click for more..."><span style="font-family: Arial, serif; font-size: 18px; color:navy;"><U><B>{loc1}</B></U></span></a></p>
        #    <p style="text-align: left;"><b><span style="font-family: Arial, serif; font-size: 16px; color:dimgray;"> ACTIVITE : <br>{fon1}</br></b></span></p>
        #    """, script=True)
            
        #    popup1=fo.Popup(id_html1, max_width=400) 
        
        #    fo.Marker(location=[lat1,lon1], 
        #              tooltip=loc1, 
        #              popup=popup1,
        #              icon=fo.Icon(color='blue', icon='pencil')).add_to(world)
            
        mymap = st_folium(world, height= 480, width=800)
        
        
    with column_right:
        st.write(
                """
                De nombreuses interventions à travers le monde sur des projets d'envergures.
                """)
        st.image(image_maplegend)
        st.write(
                """
                Click on icons for more details ...
                """)
    
    
# Contact me
with st.container():
    st.write('---')
    st.subheader('''GET CONNECTED''')
    contact_form = """
    <form action="https://formsubmit.co/arnaud.guiraud@hotmail.fr" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html = True)

        
# Foot page
with st.container():
    st.write('---')
    st.markdown("<h6 style='text-align: center; color: grey;'>Created by Arnaud Guiraud - All rights reserved</h6>", unsafe_allow_html=True)

# Bonus
with st.container():
    st.write('---')
    
         
         
         
         
         
         
         
         
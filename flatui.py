# Packages

import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")
from datetime import datetime
import streamlit as st
from streamlit_option_menu import option_menu
import pickle
from PIL import Image

def town_mapping(town_map):
    if town_map == 'ANG MO KIO':
        town_1 = int(0)
    elif town_map == 'BEDOK':
        town_1 = int(1)
    elif town_map == 'BISHAN':
        town_1= int(2)
    elif town_map == 'BUKIT BATOK':
        town_1= int(3)
    elif town_map == 'BUKIT MERAH':
        town_1= int(4)
    elif town_map == 'BUKIT PANJANG':
        town_1= int(5)
    elif town_map == 'BUKIT TIMAH':
        town_1= int(6)
    elif town_map == 'CENTRAL AREA':
        town_1= int(7)
    elif town_map == 'CHOA CHU KANG':
        town_1= int(8)
    elif town_map == 'CLEMENTI':
        town_1= int(9)
    elif town_map == 'GEYLANG':
        town_1= int(10)
    elif town_map == 'HOUGANG':
        town_1 = int(11)
    elif town_map == 'JURONG EAST':
        town_1= int(12)
    elif town_map == 'JURONG WEST':
        town_1= int(13)
    elif town_map == 'KALLANG/WHAMPOA':
        town_1= int(14)
    elif town_map == 'LIM CHU KANG':
        town_1= int(15)
    elif town_map == 'MARINE PARADE':
        town_1= int(16)
    elif town == 'PASIR RIS':
        town_1= int(17)
    elif town == 'PUNGGOL':
        town_1= int(18)
    elif town == 'QUEENSTOWN':
        town_1= int(19)
    elif town == 'SEMBAWANG':
        town_1= int(20)
    elif town == 'SENGKANG':
        town_1= int(21)
    elif town == 'SERANGOON':
        town_1= int(22)
    elif town == 'TAMPINES':
        town_1= int(23)
    elif town == 'TOA PAYOH':
        town_1= int(24)
    elif town == 'WOODLANDS':
        town_1= int(25)        
    elif town == 'YISHUN':
        town_1= int(26)      

    return town_1

def flat_type_mapping(flt_type):
    if flt_type == '3 ROOM':
        flat_type_1= int(2)
    elif flt_type == '4 ROOM':
        flat_type_1= int(3)
    elif flt_type == '5 ROOM':
        flat_type_1= int(4)
    elif flt_type == '2 ROOM':
        flat_type_1= int(1)
    elif flt_type == 'EXECUTIVE':
        flat_type_1= int(5)
    elif flt_type == '1 ROOM':
        flat_type_1= int(0)
    elif flt_type == 'MULTI-GENERATION':
        flat_type_1= int(6)

    return flat_type_1

def flat_model_mapping(fl_m):

    if fl_m == 'Improved':
        flat_model_1= int(5)
    elif fl_m == 'New Generation':
        flat_model_1= int(12)
        
    elif fl_m == 'Model A':
        flat_model_1= int(8)
    elif fl_m == 'Standard':
        flat_model_1= int(17)
    elif fl_m == 'Simplified':
        flat_model_1= int(16)
    elif fl_m == 'Model A-Maisonette':
        flat_model_1= int(9)
    elif fl_m == 'Apartment':
        flat_model_1= int(3)

    elif fl_m == 'Maisonette':
        flat_model_1= int(7)
    elif fl_m == 'Terrace':
        flat_model_1= int(18)
    elif fl_m == '2-room':
        flat_model_1= int(0)
    elif fl_m == 'Improved-Maisonette':
        flat_model_1= int(6)
    elif fl_m == 'Multi Generation':
        flat_model_1= int(11)

    elif fl_m == 'Premium Apartment':
        flat_model_1= int(13)
    elif fl_m == 'Adjoined flat':
        flat_model_1= int(2)
    elif fl_m == 'Premium Maisonette':
        flat_model_1= int(15)
    elif fl_m == 'Model A2':
        flat_model_1= int(10)
    elif fl_m == 'DBSS':
        flat_model_1= int(4)
    elif fl_m == 'Type S1':
        flat_model_1= int(19)

    elif fl_m == 'Type S2':
        flat_model_1= int(20)
    elif fl_m == 'Premium Apartment Loft':
        flat_model_1= int(14)
    
    elif fl_m == '3Gen':
        flat_model_1= int(1)

    return flat_model_1


def predict_price(year,town,flat_type,flr_area_sqm,flat_model,stry_start,stry_end,re_les_year,
              re_les_month,les_coms_dt):
    
    year_1= int(year)
    town_2= town_mapping(town)
    flt_ty_2= flat_type_mapping(flat_type)
    flr_ar_sqm_1= int(flr_area_sqm)
    flt_model_2= flat_model_mapping(flat_model)
    str_str= np.log(int(stry_start))
    str_end= np.log(int(stry_end))
    rem_les_year= int(re_les_year)
    rem_les_month= int(re_les_month)
    lese_coms_dt= int(les_coms_dt)


    with open(r"Resale_Flat_XGB_Regressor.pkl","rb") as f:
        regg_model= pickle.load(f)

    user_data = np.array([[year_1,town_2,flt_ty_2,flr_ar_sqm_1,
                           flt_model_2,str_str,str_end,rem_les_year,rem_les_month,
                           lese_coms_dt]])
    y_pred_1 = regg_model.predict(user_data)
    price= np.exp(y_pred_1[0])

    return round(price)

#STREAMLIT PART

#PAGE LAYOUT

st.set_page_config(page_title="Flatprice",page_icon="🌍",layout="wide",initial_sidebar_state="expanded")
col1,col2,col3= st.columns([1,1.2,1])
with col2:
        st.image(Image.open(r"C:\Users\Aishwarya MMPL\Documents\GUVI_PYTHON\Projects\singapore\image\into.jpg"), 
                    caption=None, width=600, use_column_width=False, clamp=True, channels="RGB", output_format="auto")

#TITLE
st.write("""<p style="font-family:Times New Roman;font-size: 45px; text-align: center; color:#FFFFF ">
         SINGAPORE RESALE FLAT PRICES PREDICTING</p>""", unsafe_allow_html=True)

st.write("")
#MENU BAR
col1,col2,col3= st.columns([1,4,1])
with col2:    
    select = option_menu(menu_title=None,options = ["Home","Price Prediction","About"],icons =["house","upload","exclamation-diamond"],
        default_index=0,orientation="horizontal",styles={"container": {"background-size":"auto", "width": "100%"},
        "icon": {"color": "black", "font-size": "20px"},"nav-link": {"font-size": "15px","font-family":"Cursive, Lucida Handwriting", 
        "text-align": "center", "margin": "0px", "--hover-color": "#FF7F50"},
        "nav-link-selected": {"background-color": "#85C1E9"}})

if select == "Home":
    st.write("""<p style="font-family:PhonePeSans,sans-serif,Helvetica,Arial;font-size: 35px; text-align: center">
            Introduction</p>""", unsafe_allow_html=True)
    with st.container(border=False,height=80):
        st.write("""<p style="font-family:PhonePeSans,sans-serif,Helvetica,Arial;font-size: 18px; text-align: left"> The resale flat market in Singapore 
                 is highly competitive, and it can be challenging to accurately estimate the resale value of a flat. 
                 There are many factors that can affect resale prices, such as location, flat type, floor area, and lease duration. 
                 A predictive model can help to overcome these challenges by providing users with an estimated resale price based on these factors.</p>""", unsafe_allow_html=True)

    with st.container(border=False,height=1500):
        col1,col2 = st.columns([1.5,3])
        with col1:
            st.image(Image.open(r"C:\Users\Aishwarya MMPL\Documents\GUVI_PYTHON\Projects\singapore\image\hdb1.webp"), 
            caption=None, width=400, use_column_width=False, clamp=False, channels="RGB",output_format="auto" )    
        with col2:
            st.text(" ") 
            st.text(" ")
            with st.container(border=False,height=250):
                st.subheader("Housing & Development Board Flats in singapore :")
                st.write("""<p style="font-family:PhonePeSans,sans-serif,Helvetica,Arial;font-size: 18px; text-align: left">
                        The Housing & Development Board (HDB) is Singapore's public housing authority. We plan and develop Singapore's 
                        housing estates; building homes and transforming towns to create a quality living environment for all.</p>""", unsafe_allow_html=True)
                st.write("""<p style="font-family:PhonePeSans,sans-serif,Helvetica,Arial;font-size: 18px; text-align: left">
                        The majority of Singaporeans live in public housing provided by the HDB.
    HDB flats can be purchased either directly from the HDB as a new unit or through the resale market from existing owners.</p>""", unsafe_allow_html=True)
                        
        col1,col2,col3 = st.columns([4,0.5,2])
        with col1:
            st.text(" ") 
            st.text(" ")
            with st.container(border=False,height=250):
                st.subheader("Resale Process:")
                st.write("""<p style="font-family:PhonePeSans,sans-serif,Helvetica,Arial;font-size: 18px; text-align: left">
                        In the resale market, buyers purchase flats from existing flat owners, and the transactions are facilitated through the HDB resale process.
    The process involves a series of steps, including valuation, negotiations, and the submission of necessary documents.</p>""", unsafe_allow_html=True)
                st.write("""<p style="font-family:PhonePeSans,sans-serif,Helvetica,Arial;font-size: 18px; text-align: left">
                        Apply for an HDB Flat Eligibility (HFE) letter, Plan your finances, Search for a resale HDB flat
                         , Obtain an Option to Purchase (OTP) from a seller., Submit a Request for Value (if needed)
, Submit resale application.</p>""", unsafe_allow_html=True)
                
        with col3:
            st.image(Image.open(r"C:\Users\Aishwarya MMPL\Documents\GUVI_PYTHON\Projects\singapore\image\resale.jpg"), 
            caption=None, width=280, use_column_width=False, clamp=False, channels="RGB",output_format="auto" ) 

        col1,col2 = st.columns([1.5,3])
        with col1:
            st.image(Image.open(r"C:\Users\Aishwarya MMPL\Documents\GUVI_PYTHON\Projects\singapore\image\val.jpg"), 
            caption=None, width=400, use_column_width=False, clamp=False, channels="RGB",output_format="auto" )    
        with col2:
            st.text(" ") 
            st.text(" ")
            with st.container(border=False,height=250):
                st.subheader("Valuation & Eligibility Criteria:")
                st.write("""<p style="font-family:PhonePeSans,sans-serif,Helvetica,Arial;font-size: 18px; text-align: left">
                        The HDB conducts a valuation of the flat to determine its market value. This is important for both buyers and sellers in negotiating a fair price.</p>""", unsafe_allow_html=True)
                st.write("""<p style="font-family:PhonePeSans,sans-serif,Helvetica,Arial;font-size: 18px; text-align: left">
                        Buyers and sellers in the resale market must meet certain eligibility criteria, including citizenship requirements and income ceilings.</p>""", unsafe_allow_html=True)

        col1,col2,col3 = st.columns([4,0.5,2])
        with col1:
            st.text(" ") 
            st.text(" ")
            with st.container(border=False,height=250):
                st.subheader("Grant Schemes & Bank Loans:")
                st.write("""<p style="font-family:PhonePeSans,sans-serif,Helvetica,Arial;font-size: 18px; text-align: left">
                        There are various housing grant schemes available to eligible buyers, such as the CPF Housing Grant, which provides financial assistance for the purchase of resale flats.</p>""", unsafe_allow_html=True)
                st.write("""<p style="font-family:PhonePeSans,sans-serif,Helvetica,Arial;font-size: 18px; text-align: left">
                        Buyers can choose to finance their flat purchase through an HDB loan or a bank loan. HDB loans are provided by the HDB, while bank loans are obtained from commercial banks.</p>""", unsafe_allow_html=True)
                
        with col3:
            st.image(Image.open(r"C:\Users\Aishwarya MMPL\Documents\GUVI_PYTHON\Projects\singapore\image\loan.jpg"), 
            caption=None, width=400, use_column_width=False, clamp=False, channels="RGB",output_format="auto" )

        col1,col2 = st.columns([1.5,3])
        with col1:
            st.image(Image.open(r"C:\Users\Aishwarya MMPL\Documents\GUVI_PYTHON\Projects\singapore\image\mar.jpg"), 
            caption=None, width=400, use_column_width=False, clamp=False, channels="RGB",output_format="auto" )    
        with col2:
            st.text(" ") 
            st.text(" ")
            with st.container(border=False,height=250):
                st.subheader("Market Trends & Online Platforms")
                st.write("""<p style="font-family:PhonePeSans,sans-serif,Helvetica,Arial;font-size: 18px; text-align: left">
                        The resale market is influenced by various factors such as economic conditions, interest rates, and government policies. Property prices in Singapore can fluctuate based on these factors.</p>""", unsafe_allow_html=True)
                st.write("""<p style="font-family:PhonePeSans,sans-serif,Helvetica,Arial;font-size: 18px; text-align: left">
                        There are online platforms and portals where sellers can list their resale flats, and buyers can browse available options.</p>""", unsafe_allow_html=True)



elif select == "Price Prediction":

    col1,col2= st.columns(2)
    with col1:

        year= st.selectbox("Select the Year",['1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000',
       '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011',
       '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022',
       '2023', '2024'])
        
        town= st.selectbox("Select the Town", ['ANG MO KIO', 'BEDOK', 'BISHAN', 'BUKIT BATOK', 'BUKIT MERAH',
                                            'BUKIT PANJANG', 'BUKIT TIMAH', 'CENTRAL AREA', 'CHOA CHU KANG',
                                            'CLEMENTI', 'GEYLANG', 'HOUGANG', 'JURONG EAST', 'JURONG WEST',
                                            'KALLANG/WHAMPOA', 'MARINE PARADE', 'PASIR RIS', 'PUNGGOL',
                                            'QUEENSTOWN', 'SEMBAWANG', 'SENGKANG', 'SERANGOON', 'TAMPINES',
                                            'TOA PAYOH', 'WOODLANDS', 'YISHUN'])
        
        flat_type= st.selectbox("Select the Flat Type", ['1 ROOM', '2 ROOM','3 ROOM', '4 ROOM', '5 ROOM', 'EXECUTIVE',
                                                        'MULTI GENERATION'])
        
        flr_area_sqm= st.number_input("Enter the Value of Floor Area sqm (Min: 28 / Max: 307")

        flat_model= st.selectbox("Select the Flat Model", ['Improved', 'New Generation', 'Model A', 'Standard', 'Simplified',
                                                        'Premium Apartment', 'Maisonette', 'Apartment', 'Model A2',
                                                        'Type S1', 'Type S2', 'Adjoined flat', 'Terrace', 'DBSS',
                                                        'Model A-Maisonette', 'Premium Maisonette', 'Multi Generation',
                                                        'Premium Apartment Loft', 'Improved-Maisonette', '2-room', '3Gen'])
        
    with col2:

        stry_start= st.number_input("Enter the value of Storey start")

        stry_end= st.number_input("Enter the Value of Storey End")

        re_les_year= st.number_input("Enter the Value of Remaining Lease Year (Min: 0 / Max: 97)")

        re_les_month= st.number_input("Enter the Value of Remaining Lease Month (Min: 0 / Max: 11)")
        
        les_coms_dt= st.selectbox("Select the Lease_Commence_Date", [str(i) for i in range(1966,2018)])

    button= st.button("Predict the Price", use_container_width= True)

    if button:

            
        pre_price= predict_price(year, town, flat_type, flr_area_sqm, flat_model,
                        stry_start, stry_end, re_les_year, re_les_month, les_coms_dt)

        st.write("## :green[**The Predicted Price is :**]",pre_price)


elif select == "About":
    st.write("""<p style="font-family:PhonePeSans,sans-serif,Helvetica,Arial;font-size: 25px; text-align: center">
            Data Collection and Preprocessing</p>""", unsafe_allow_html=True)
    st.write("Collect a dataset of resale flat transactions from the Singapore Housing and Development Board (HDB) for the years 1990 to Till Date. Preprocess the data to clean and structure it for machine learning.")

    st.write("""<p style="font-family:PhonePeSans,sans-serif,Helvetica,Arial;font-size: 25px; text-align: center">
            Feature Engineering</p>""", unsafe_allow_html=True)
    st.write("Extract relevant features from the dataset, including town, flat type, storey range, floor area, flat model, and lease commence date. Create any additional features that may enhance prediction accuracy.")
    
    st.write("""<p style="font-family:PhonePeSans,sans-serif,Helvetica,Arial;font-size: 25px; text-align: center">
            Model Selection and Training</p>""", unsafe_allow_html=True)
    st.write("Choose an appropriate machine learning model for regression (e.g., linear regression, decision trees, or random forests). Train the model on the historical data, using a portion of the dataset for training.")

    st.write("""<p style="font-family:PhonePeSans,sans-serif,Helvetica,Arial;font-size: 25px; text-align: center">
            Model Evaluation</p>""", unsafe_allow_html=True)
    st.write("Evaluate the model's predictive performance using regression metrics such as Mean Absolute Error (MAE), Mean Squared Error (MSE), or Root Mean Squared Error (RMSE) and R2 Score.")

    st.write("""<p style="font-family:PhonePeSans,sans-serif,Helvetica,Arial;font-size: 25px; text-align: center">
            Streamlit Web Application</p>""", unsafe_allow_html=True)
    st.write("Develop a user-friendly web application using Streamlit that allows users to input details of a flat (town, flat type, storey range, etc.). Utilize the trained machine learning model to predict the resale price based on user inputs.")

    st.write("""<p style="font-family:PhonePeSans,sans-serif,Helvetica,Arial;font-size: 25px; text-align: center">
            Deployment on Render</p>""", unsafe_allow_html=True)
    st.write("Deploy the Streamlit application on the Render platform to make it accessible to users over the internet.")
    
    st.write("""<p style="font-family:PhonePeSans,sans-serif,Helvetica,Arial;font-size: 25px; text-align: center">
            Testing and Validation</p>""", unsafe_allow_html=True)
    st.write("Thoroughly test the deployed application to ensure it functions correctly and provides accurate predictions.")


import streamlit as st

import joblib
model=joblib.load("model.pkl")
l1=joblib.load("le.pkl")
s=joblib.load("scaler.pkl")

st.title("Crop Recommendation")
st.write("Enter Data Description")

N =st.number_input('Enter the nitrogen content')
P =st.number_input("Enter the phosphorous contet")
K =st.number_input('Enter the pottssium content')
temperature =st.number_input("Enter the temperature")
humidity =st.number_input("Enter the relative humidity")
ph =st.number_input("Enter the ph value of the soil")
rainfall =st.number_input("Enter the rainfall")

if st.button("predict"):
    result=model.predict(s.transform([[N,P,K,temperature,humidity,ph,rainfall]]))[0]
    if result == 0:
        st.success('The predicted crop is APPLE')
        st.success('''Apple trees need a balanced supply of nutrients, along with a favourable climate with adequate temperature,humidity and rainfall,
              and slightly acidic soil for optimal growth.''')
    
    elif result ==  1:
        st.success('The predicted crop is BANANA')
        st.success(''' Bananas grow best in well-drained, fertile soils with a balanced supply of nutrients, warm temperature, high humidity, and adequate 
              rainfall.''')
        
    elif result == 2:
        st.success('The predicted soil type is BLACKGRAM ')
        st.success("""Blackgram needs balanced soil nutrients, a warm climate, moderate humidity, and rainfall for healthy growth.""")

    elif result ==  3:
        st.success('The predicted crop is CHICKPEA')
        st.success(''' Chickpeas perform best in moderately warm, dry climates with well-drained soils and optimal levels of nutrients, slightly acidic to 
                  neutral pH and sufficient but mot excessive rainfall.''')
        
    elif result == 4:
        st.success('The predicted soil type is COCONUT ')
        st.success("""Requires high potassium, moderate phosphorous, and nitrogen, a warm, humid climate, and abundant rainfall for optimal growth.""")

    elif result ==  5:
        st.success('The predicted crop is COFFEE')
        st.success('''Coffee needs a cool, humid climate with high nitrogen, and moderate phosphorous and potassium for healthy growth. ''')
        
    elif result == 6:
        st.success('The predicted soil type is COTTON ')
        st.success("""Cotton thrives in warm climate with moderate humidity and requires well-drained soil with a moderate level of nutrients.""")

    elif result ==  7:
        st.success('The predicted crop is GRAPES')
        st.success(''' Grapes prefer a warm climate, dry conditions with balanced nutrients, and moderate rainfall.''')
        
    elif result == 8:
        st.success('The predicted soil type is JUTE ')
        st.success("""Jute requires a warm, humid climate with abundant rainfall and high nitrogen for optimal fiber production.""")

    elif result ==  9:
        st.success('The predicted crop is KIDNEYBEANS')
        st.success('''Kidneybeans grows well in warm climates with moderate rainfall and balanced soil nutrients.''')
        
    elif result ==  10:
        st.success('The predicted crop is Lentil')
        st.success('''Lentils prefer cooler climates with moderate rainfall and balance nutrients for optimal growth.''')
        
    elif result == 11:
        st.success('The predicted soil type is MAIZE ')
        st.success("""Maize requires a warm climate, high nitrogen and potassium, and moderate rainfall for healthy growth.""")

    elif result ==  12:
        st.success('The predicted crop is MANGO')
        st.success('''Mangoes need warm conditions, balanced nutrients, and moderate rainfall for healthy fruiting.''')

    elif result ==  13:
        st.success('The predicted crop is MOTHBEANS')
        st.success('''Mothbeans grows well in warm, dry conditions with low humidity and minimal rainfall. Prefers slightly acidic to neutral soil and
              needs nitrogen for leafy growth.''')
        
    elif result == 14:
        st.success('The predicted soil type is MUNGBEAN ')
        st.success("""Mungbeans thrive in warm, dry conditions with moderate rainfall and balanced nutrients.""")

    elif result ==  15:
        st.success('The predicted crop is MUSKMELON')
        st.success('''Muskmelon requires warm, dry conditions with well-drained soil and moderate nutrients for good yield. ''')
        
    elif result == 16:
        st.success('The predicted soil type is ORANGE ')
        st.success("""Oranges need a warm, moderate climate with balanced soil nutrients and consistent rainfall for optimal growth.""")

    elif result ==  17:
        st.success('The predicted crop is PAPAYA')
        st.success('''Papaya prefer warm, humid conditions with balanced nutrients and ample rainfall for fruiting.''')
        
    elif result == 18:
        st.success('The predicted soil type is PIGEONPEAS ')
        st.success("""Pigeonpeas thrive in warm, dry climates with moderate rainfall and balanced nutrients.""")

    elif result ==  19:
        st.success('The predicted crop is POMEGRANTE')
        st.success('''Pomegrante grows well in warm, dry conditions with well-drained soils and  balanced nutrients.''')
        
    elif result == 20:
        st.success('The predicted soil type is RICE ')
        st.success("""Rice needs warm, humid conditions with abdundant rainfall and high nitrogen for healthy growth.""")

    elif result ==  21:
        st.success('The predicted crop is WATERMELON')
        st.success('''Watermelon requires warm, dry conditions with moderate rainfall and high potassium for fruit growth.''')

import streamlit as st
import mysql.connector as sql
import pandas as pd
import numpy as np

st.set_page_config(page_title="PULSE-PDS",
                   layout="wide",
                   initial_sidebar_state="expanded",
                   )

# QUESTION LIST
question_list = [
    "1. I want to buy Sugar.",
    "2. I want to buy Wheat.",
    "3. I want to buy Oil.",
    "4. I want to buy Blackgram.",
    "5. I want to buy Rice.",
    "6. I want to buy Sugar and Wheat.",
    "7. I want to buy Sugar and Oil.",
    "8. I want to buy Sugar and Blackgram.",
    "9. I want to buy Sugar and Rice.",
    "10. I want to buy Wheat and Oil.",
    "11. I want to buy Wheat and Blackgram.",
    "12. I want to buy Wheat and Rice.",
    "13. I want to buy Oil and Blackgram.",
    "14. I want to buy Oil and Rice.",
    "15. I want to buy Blackgram and Rice.",
    "16. I want to buy Sugar, Wheat, and Oil.",
    "17. I want to buy Sugar, Wheat, and Blackgram.",
    "18. I want to buy Sugar, Wheat, and Rice.",
    "19. I want to buy Sugar, Oil, and Blackgram.",
    "20. I want to buy Sugar, Oil, and Rice.",
    "21. I want to buy Sugar, Blackgram, and Rice.",
    "22. I want to buy Wheat, Oil, and Blackgram.",
    "23. I want to buy Wheat, Oil, and Rice.",
    "24. I want to buy Wheat, Blackgram, and Rice.",
    "25. I want to buy Oil, Blackgram, and Rice.",
    "26. I want to buy Sugar, Wheat, Oil, and Blackgram.",
    "27. I want to buy Sugar, Wheat, Oil, and Rice.",
    "28. I want to buy Sugar, Wheat, Blackgram, and Rice.",
    "29. I want to buy Sugar, Oil, Blackgram, and Rice.",
    "30. I want to buy Wheat, Oil, Blackgram, and Rice.",
    "31. I want to buy all the commodities."
]



def speech(random_number):
    speech_mapping = {
        0: "speech1.mp3",
        1: "speech2.mp3",
        2: "speech3.mp3",
        3: "speech4.mp3",
        4: "speech5.mp3",
        5: "speech6.mp3",
        6: "speech7.mp3",
        7: "speech8.mp3",
        8: "speech9.mp3",
        9: "speech10.mp3",
        10: "speech11.mp3",
        11: "speech12.mp3",
        12: "speech13.mp3",
        13: "speech14.mp3",
        14: "speech15.mp3",
        15: "speech16.mp3",
        16: "speech17.mp3",
        17: "speech18.mp3",
        18: "speech19.mp3",
        19: "speech20.mp3",
        20: "speech21.mp3",
        21: "speech22.mp3",
        22: "speech23.mp3",
        23: "speech24.mp3",
        24: "speech25.mp3",
        25: "speech26.mp3",
        26: "speech27.mp3",
        27: "speech28.mp3",
        28: "speech29.mp3",
        29: "speech30.mp3",
        30: "speech31.mp3"
    }

    if random_number in speech_mapping:
        speech = speech_mapping[random_number]
    else:
        speech = "Error Occurred"  # Default if the random_number is not in the mapping

    return speech





# SETTING PAGE CONFIGURATIONS
st.header('PULSE-PDS', divider='rainbow')
st.subheader('Public Utility Logistics System Enhancement with Generative AI for Public Distribution System')
st.markdown("Empowering the fight against hunger with Generative AI: Our non-profit project takes aim at eradicating hunger by optimizing the public distribution system using generative artificial intelligence. We prioritize the welfare of those in need, working towards a world without hunger.", unsafe_allow_html=True)



#connecting to MySQL

mydb = sql.connect(host="localhost",
                   user="root",
                   password="root@123",
                   database= "beneficiary"
                  )
mycursor = mydb.cursor(buffered=True)



# TABLE CREATION
mycursor.execute(" CREATE TABLE IF NOT EXISTS biometric_data ( ID INT AUTO_INCREMENT PRIMARY KEY, black_gram INT, rice INT, oil INT, sugar INT, wheat INT)")


    



# SELECTING MENU
selected_menu = st.sidebar.radio("Select an option", ("Transaction","Report"))

################Creating Transaction##################
if selected_menu == "Transaction":
    st.markdown("# Creating Transaction")
    
    mycursor.execute("SELECT * FROM card_data")
    data = mycursor.fetchall()
    columns = ["ID", "card_holder_name", "card_type", "black_gram", "rice", "oil", "sugar", "wheat"]
    data_frame = pd.DataFrame(data, columns=columns)
    st.write(data_frame)

############ Time Analysis

    st.subheader("TimeDelay")
    st.caption("Can you please provide information about today's ration shop entry delay?")
    Dtime=st.number_input("Enter the Delayed time in Minutes" , min_value=0)
    st.write(Dtime)
    #if st.button("Save Delayed Time"):
        #insert_query = "INSERT INTO time_delay (delayed_time_in_minutes) VALUES (%s)"
        #data=(Dtime)
     #   mycursor.execute(insert_query, data)
        # Commit the changes to the database.
      #  mydb.commit()
        # Display a success message.
       # st.success("Time saved successfully!")
        #st.markdown("### Time Transaction")
        


############Biometric Analysis
    
    st.subheader('Biometric Transaction')

    col1, col2 = st.columns(2)
    with col1:
        id = st.number_input("Enter the ID of the Beneficiary ", min_value=1 , max_value=25)
        black_gram = st.number_input("Enter the black_gram quantity in Kg")
        rice = st.number_input("Enter the Rice quantity in Kg")
        
    with col2:
        oil = st.number_input("Enter the oil quantity in Kg")
        sugar = st.number_input("Enter the sugar quantity in Kg")
        wheat = st.number_input("Enter the wheat quantity in Kg")


    if st.button("Save Transaction"):
        #update_query = "INSERT Report_data SET ID=%s , card_holder_name=%s ,card_type=%s , black_gram=%s, rice=%s, oil=%s, sugar=%s, wheat=%s WHERE ID=%s"
        # Define the values to be updated.
     #   update_values = (id ,black_gram, Rice, oil, sugar, wheat, id)
        # Execute the update query with the values.
        insert_query = "INSERT INTO biometric_data (id, black_gram, rice, oil, sugar ,wheat) VALUES (%s, %s, %s, %s, %s , %s)"
        data = (id, black_gram, rice, oil, sugar,wheat)
        mycursor.execute(insert_query, data)
        # Commit the changes to the database.
        mydb.commit()
        # Display a success message.
        st.success("Transaction saved successfully!")
        st.markdown("### Saved Transaction")



####### Speech to text Generation
    
    st.subheader('Speech to Text & report Transaction')
    
    questions = st.selectbox('Questions', question_list)
    
    question_index = question_list.index(questions)
    st.write(questions)
    if st.button("Play Audio"):
        st.write("Audio playing")
        q=speech(question_index)
        speech=q
        audio_file = open(speech, 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/ogg')
        sample_rate = 44100  # 44100 samples per second
        seconds = 2  # Note duration of 2 seconds
        frequency_la = 440  # Our played note will be 440 Hz
    random_selection_expander = st.expander("Will I select a question randomly?")
    with random_selection_expander:
        if st.button("Random Selection"):
            random_number = np.random.randint(0, len(question_list))
            st.write(random_number + 1)
            question_index = random_number
            selected_question = question_list[question_index]
            st.write(selected_question)

    



    

##################### Generating Report##############
if selected_menu == "Report":
    st.markdown("### Generating Report")



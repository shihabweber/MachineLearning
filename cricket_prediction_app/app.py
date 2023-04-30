import pandas as pd
import streamlit as st
import pickle
import pandas
st.title('IPL Win Predictor')
teams= ['Sunrisers Hyderabad',
    'Mumbai Indians',
    'Royal Challengers Bangalore',
    'Kolkata Knight Riders',
    'Kings XI Punjab',
    'Chennai Super Kings',
    'Rajasthan Royals',
    'Delhi Capitals']
cities=['Hyderabad', 'Pune', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata',
       'Delhi', 'Rajkot', 'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town',
       'Port Elizabeth', 'Durban', 'Centurion', 'East London',
       'Johannesburg', 'Kimberley', 'Bloemfontein', 'Ahmedabad',
       'Cuttack', 'Nagpur', 'Dharamsala', 'Kochi', 'Visakhapatnam',
       'Raipur', 'Ranchi', 'Abu Dhabi', 'Sharjah', 'Kanpur',
       'Mohali', 'Bengaluru']
pipe=pickle.load(open('pipes.pkl','rb'))



col1,col2=st.columns(2)
with col1:
    batting_team=st.selectbox('Select the batting team',sorted(teams))
with col2:
    bowling_team=st.selectbox('Select the bowling team',sorted(teams))
select_city=st.selectbox('City',sorted(cities))
target=int(st.number_input('Target'))
col3,col4,col5=st.columns(3)
with col3:
    score=st.number_input('Current Score')
with col4:
    overs=st.number_input('Current Overs')
with col5:
    wickets=st.number_input('Wickets')
if st.button('Predict Win Probability'):
    runs_left=int((target-score))
    balls_left=int(120-(overs*6))
    wickets_left=int(10-wickets)
    current_run_rate= '%.2f' % (score/overs)
    required_run_rate=(runs_left)/(balls_left/6)
    required_run_rate=('%.2f' % required_run_rate)

    input_df=pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],'city':[select_city],'runs_left':[runs_left]
                  ,'balls_left':[balls_left],'wickets_left':[wickets_left],'target':[target],'current_run_rate':[current_run_rate]
                  ,'required_run_rate':[required_run_rate]})

    st.table(input_df)

    result=pipe.predict_proba(input_df)
    loss=result[0][0]
    win=result[0][1]

    st.text(batting_team +'-'+str(round(loss*100))+"%")
    st.text(bowling_team+'-'+str(round(win*100))+"%")


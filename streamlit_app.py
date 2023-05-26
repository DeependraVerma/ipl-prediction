import streamlit as st
import pickle
import pandas as pd

st.title("IPL Win Predictor")

teams = ['Rajasthan Royals',
 'Royal Challengers Bangalore',
 'Sunrisers Hyderabad',
 'Chennai Super Kings',
 'Gujarat Titans',
 'Lucknow Super Giants',
 'Kolkata Knight Riders',
 'Mumbai Indians',
 'Kings XI Punjab',
 'Delhi Capitals']
city = ['Bangalore',
 'Chennai',
 'Mumbai',
 'Delhi',
 'Sharjah',
 'Chandigarh',
 'Durban',
 'Kolkata',
 'Hyderabad',
 'Ahmedabad',
 'Pune',
 'Johannesburg',
 'Jaipur',
 'Dharamsala',
 'Centurion',
 'Abu Dhabi',
 'Bengaluru',
 'Cuttack',
 'Cape Town',
 'Port Elizabeth',
 'Ranchi',
 'Indore',
 'Dubai',
 'Navi Mumbai',
 'Visakhapatnam',
 'Bloemfontein',
 'Kimberley',
 'Nagpur',
 'Raipur',
 'East London']

pipe = pickle.load(open("model.pkl","rb"))
col1,col2 = st.columns(2)

with col1:
    batting_team = st.selectbox("Select the batting team",sorted(teams))
with col2:
    bowling_team = st.selectbox("Select the bowling team",sorted(teams))

selected_city = st.selectbox("Select host city", sorted(city))
target = st.number_input("Target Run")
col3,col4,col5 = st.columns(3)

with col3:
    score = st.number_input("Score")
with col4:
    overs = st.number_input("Overs completed")
with col5:
    wickets = st.number_input("Wicket Out")


runs_left = (target - score)
ball_left =120-(overs*6)
wicket_left =10 - wickets
try:
    crr = score/overs
except ZeroDivisionError:
    crr = 0
rrr=(runs_left*6)/ball_left




input_df = pd.DataFrame ({'BattingTeam': [batting_team], 'Bowling Team': [bowling_team],
'City':[selected_city],'runs_left': [runs_left], 'ball_left':[ball_left], 'wicket_left': [wicket_left],
'run_win':[target], 'crr':[crr], 'rrr':[rrr]})

result = pipe.predict_proba(input_df)
win = result[0][0]
loss = result[0][1]
st.header(batting_team + "-"+ str(round(win*100))+"%") 
st.header(bowling_team +"-"+str(round(loss*100)) + "%")

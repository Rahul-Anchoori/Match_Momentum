import streamlit as st
import pandas as pd
import pickle
teams=['Kings XI Punjab',
       'Mumbai Indians',
       'Kolkata Knight Riders',
       'Rajasthan Royals',
       'Chennai Super Kings',
       'Sunrisers Hyderabad',
       'Delhi Capitals',
       'Lucknow Super Giants',
       'Gujarat Titans',
       'Royal Challengers Bengaluru']
city=['Bangalore', 'Chandigarh', 'Delhi', 'Mumbai', 'Kolkata', 'Jaipur',
       'Hyderabad', 'Chennai', 'Cape Town', 'Port Elizabeth', 'Durban',
       'Centurion', 'East London', 'Johannesburg', 'Kimberley',
       'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
       'Kochi', 'Indore', 'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi',
       'Abu Dhabi','Rajkot', 'Kanpur', 'Bengaluru', 'Dubai',
       'Sharjah', 'Navi Mumbai', 'Lucknow', 'Guwahati', 'Mohali']
with open('pipes2.pkl','rb') as f:
    pipe= pickle.load(f)
st.title('Cricket Win Predictor')
col1, col2 = st.columns(2)
with col1:
       batting_team = st.selectbox('Batting Team',teams)
ateams = [team for team in teams if team!=batting_team]
with col2:
       bowling_team = st.selectbox('Bowling Team',ateams)
city = st.selectbox('City',city)
target = st.number_input('Enter Total score')
col3, col4, col5 = st.columns(3)
with col3:
       present_score = st.number_input('Present Score')
with col4:
       overs=st.number_input('Overs Completed')
with col5:
       wickets=st.number_input('Wickets Out')
if st.button('Predict Win Probability'):
    runs_left = target - present_score
    balls_left = 120 - (overs*6)
    wickets = 10 - wickets
    crr = present_score/overs
    rrr = (runs_left*6)/balls_left
    input_data = {
        'batting_team': [batting_team],
        'bowling_team': [bowling_team],
        'city': [city],
        'runs_left': [runs_left],
        'balls_left': [balls_left],
        'wicket_left': [wickets],
        'total_runs_x': [target],
        'crr': [crr],
        'rrr': [rrr]
    }
    input_df = pd.DataFrame(input_data)
    win_probability = pipe.predict_proba(input_df)[:, 1]
    import plotly.graph_objects as go
    batting_win = round(win_probability[0] * 100, 2)
    bowling_win = round(100 - batting_win, 2)
    labels = [f"{batting_team} {batting_win}%", f"{bowling_team} {bowling_win}%"]
    values = [batting_win, bowling_win]
    colors = ['#91c44c', '#2b4c7e']
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=[values[0]],
        y=["Win Probability"],
        orientation='h',
        name=batting_team,
        marker_color=colors[0],
        text=labels[0],
        textposition="outside",
    ))
    fig.add_trace(go.Bar(
        x=[values[1]],
        y=["Win Probability"],
        orientation='h',
        name=bowling_team,
        marker_color=colors[1],
        text=labels[1],
        textposition="inside"
    ))
    fig.update_layout(
        barmode='stack',
        height=50,
        margin=dict(l=20, r=20, t=5, b=5),
        xaxis=dict(
            showticklabels=False,
            showgrid=False,
            zeroline=False,
            range=[0, 100]
        ),
        yaxis=dict(showticklabels=True),
        plot_bgcolor='white',
        paper_bgcolor='white'
    )
    st.plotly_chart(fig)
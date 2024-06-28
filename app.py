import math
import joblib
import pandas as pd
import streamlit as st

# Import model and column transformer
model = joblib.load("model.joblib")
transformer = joblib.load("transformer.joblib")

# Load the data
df = pd.read_csv("preprocessed_data.csv")

def main():
    st.title("IPL Powerplay Score Predictor")

    batting_teams = df.batting_team.unique().tolist()
    bowling_teams = df.bowling_team.unique().tolist()
    venues = df.venue.unique().tolist()
    
    # Input fields
    batting_team = st.selectbox('Select Batting Team', batting_teams)

    bowling_teams = [team for team in bowling_teams if team != batting_team]

    bowling_team = st.selectbox('Select Bowling Team', bowling_teams)
    venue = st.selectbox('Select Venue', venues)
    # inning = st.selectbox('Select Inning', ['1st Inning', '2nd Inning'])
    is_toss_winner = st.selectbox('Is Toss Winner?', ['Yes', 'No'])

    if is_toss_winner == "Yes" :
        toss_decision = st.selectbox('Toss Decision', ['Bat', 'Bowl', "NA"])
    else:
        toss_decision = st.selectbox('Toss Decision', ["NA"])

    wickets = st.selectbox('Wickets in powerplay', list(range(12)))
    

    if st.button('Predict Total Runs Scored in Powerplay'):
        
        # Value selection for is_toss_winner
        if is_toss_winner == "Yes":
            is_toss_winner = 1
        else:
            is_toss_winner = 0
            toss_decision = "NA"

        # Value selection for toss_decision
        if toss_decision == "Bat":
            toss_decision = "bat"
        elif toss_decision == "Bowl":
            toss_decision = 'field'
        elif toss_decision == "NA":
            toss_decision = "Not Applicable"
        
        test_case = {
            "batting_team": batting_team,
            "bowling_team": bowling_team,
            "venue": venue,
            "toss_winner": is_toss_winner,
            "toss_decision": toss_decision,
            "wickets": int(wickets)
        }
        test_case_df = pd.DataFrame(data=test_case, index=[0])
        total_runs = model.predict(transformer.transform(test_case_df))[0]
        st.write(f'Total runs scored in powerplay: {math.ceil(total_runs)}')
        
if __name__ == "__main__":
    main()

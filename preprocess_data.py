import pandas as pd

df = pd.read_csv('extracted_data.csv')

df = df[df['over'] < 6.0]

df = df[["match_id","inning", "batting_team", "bowling_team", "venue", "toss_winner", "toss_decision",  "runs_total", "wickets"]]

df = df.groupby(["match_id", "inning", "batting_team", "bowling_team", "venue", "toss_winner", "toss_decision"]).agg({"runs_total": "sum", "wickets": "sum"})

df = df.reset_index()

df['batting_team'] = df.batting_team.replace(to_replace={"Deccan Chargers": "Sunrisers Hyderabad", 
                                    "Delhi Daredevils": "Delhi Capitals", 
                                    "Gujarat Lions": "Gujarat Titans",
                                    "Kings XI Punjab": "Punjab Kings",
                                    "Rising Pune Supergiant": "Pune Warriors",
                                    "Rising Pune Supergiants": "Pune Warriors",
                                    "Royal Challengers Bangalore": "Royal Challengers Bengaluru"
                                    })


df['bowling_team'] = df.bowling_team.replace(to_replace={"Deccan Chargers": "Sunrisers Hyderabad", 
                                    "Delhi Daredevils": "Delhi Capitals", 
                                    "Gujarat Lions": "Gujarat Titans",
                                    "Kings XI Punjab": "Punjab Kings",
                                    "Rising Pune Supergiant": "Pune Warriors",
                                    "Rising Pune Supergiants": "Pune Warriors",
                                    "Royal Challengers Bangalore": "Royal Challengers Bengaluru"
                                    })


replace_dict = {
    "MA Chidambaram Stadium": "MA Chidambaram Stadium, Chepauk, Chennai", #1
    "MA Chidambaram Stadium, Chepauk":"MA Chidambaram Stadium, Chepauk, Chennai", #1
    "Dr DY Patil Sports Academy":"Dr DY Patil Sports Academy, Mumbai", #2
    "Arun Jaitley Stadium":"Arun Jaitley Stadium, Delhi", #3
    "Feroz Shah Kotla":"Arun Jaitley Stadium, Delhi", #3
    "Sardar Patel Stadium, Motera": "Narendra Modi Stadium, Ahmedabad", #4
    "Himachal Pradesh Cricket Association Stadium": "Himachal Pradesh Cricket Association Stadium, Dharamsala", #5
    "Maharashtra Cricket Association Stadium": "Maharashtra Cricket Association Stadium, Pune", #6
    "Punjab Cricket Association IS Bindra Stadium":"Punjab Cricket Association IS Bindra Stadium, Mohali", #7
    "Punjab Cricket Association Stadium, Mohali": "Punjab Cricket Association IS Bindra Stadium, Mohali", #7
    "Punjab Cricket Association IS Bindra Stadium, Mohali, Chandigarh":"Punjab Cricket Association IS Bindra Stadium, Mohali", #7
    "Wankhede Stadium": "Wankhede Stadium, Mumbai", #8
    "Eden Gardens": "Eden Gardens, Kolkata", #9
    "Brabourne Stadium": "Brabourne Stadium, Mumbai",#10
    "Sawai Mansingh Stadium": "Sawai Mansingh Stadium, Jaipur",#11
    "M Chinnaswamy Stadium": "M Chinnaswamy Stadium, Bengaluru", #12
    "M.Chinnaswamy Stadium": "M Chinnaswamy Stadium, Bengaluru", #12
    "Rajiv Gandhi International Stadium": "Rajiv Gandhi International Stadium, Uppal, Hyderabad", #13
    "Rajiv Gandhi International Stadium, Uppal": "Rajiv Gandhi International Stadium, Uppal, Hyderabad", #13
    "Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium": "Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium, Visakhapatnam", #14
}

df['venue'] = df.venue.replace(to_replace=replace_dict)

df = df[["batting_team", "bowling_team", "venue", "toss_winner", "toss_decision", "inning", "wickets", "runs_total"]]

df.to_csv("preprocessed_data.csv")
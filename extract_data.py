import os
import json
import shutil
import pandas as pd

if os.path.isfile("ipl_data.zip"):
   shutil.unpack_archive("ipl_data.zip", "ipl_data")
else:
    raise Exception("ipl_data.zip file is required to extract data")

data_list = []


data_dir = "ipl_data"
for filename in os.listdir(data_dir):
    filepath = os.path.join(data_dir, filename)
    if filename == "README.txt":
        continue
    with open(filepath, "r") as f:
        data = json.load(f)

        for inning_id, inning in enumerate(data["innings"]):
            for over in inning["overs"]:
                for delivery_no, delivery in enumerate(over["deliveries"]):
                    match_teams = data["info"]["teams"].copy()
                    match_teams.remove(inning["team"])
                    non_inning_team = match_teams[0]
                    toss_winner = (
                        1 if (data["info"]["toss"]["winner"] == inning["team"]) else 0
                    )
                    toss_decision = (
                        data["info"]["toss"]["decision"] if toss_winner else "Not Applicable"
                    )
                    wickets = 0
                    wicket_type = "NA"
                    if "wickets" in delivery:
                        wickets = int(len(delivery['wickets']))
                        wicket_type = delivery['wickets'][0]['kind']
                    data_dict = {
                        "match_id": filename.split(".")[0],
                        "match_date": data["info"]["dates"][0],
                        "batting_team": inning["team"],
                        "bowling_team": non_inning_team,
                        "venue": data["info"]["venue"],
                        "toss_winner": toss_winner,
                        "toss_decision": toss_decision,
                        "inning": inning_id + 1,
                        "batter": delivery["batter"],
                        "non_striker": delivery["non_striker"],
                        "bowler": delivery["bowler"],
                        "over": (over["over"]) + (0.1 * (delivery_no + 1)),
                        "runs_batter": delivery["runs"]["batter"],
                        "runs_extras": delivery["runs"]["extras"],
                        "runs_total": delivery["runs"]["total"],
                        "wickets": wickets,
                        "wicket_type": wicket_type
                    }
                    data_list.append(data_dict)

df = pd.DataFrame(data_list)

df.to_csv("extracted_data.csv")
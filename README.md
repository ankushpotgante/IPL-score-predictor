# IPL Score Predictor

This is a Streamlit web application that predicts the total runs at the end of the 6th over in a cricket match. The prediction is based on inputs such as the batting team, bowling team, venue, inning, toss winner, toss decision, and wickets at the end of the 6th over. The app uses a machine learning model built with scikit-learn.

## Requirements
* Python 3.7 or higher ( 3.10 Recommended )
* Streamlit
* scikit-learn
* pandas

## Features
### User Inputs:
* Batting team
* Bowling team
* Venue
* Toss winner status
* Toss decision
* Wickets at the end of the 6th over
### Output: 
* Predicted total runs at the end of the 6th over


## Setup
### Create Virtual Environment
Create a virtual environment

``` sh
python -m venv env
```

Activate the environment

For windows
```sh
env\Scripts\activate
```

For linux
``` sh
source env/bin/activate
```

### Install dependencies

```sh
pip install -r requirements.txt
```

### Extract Data
Extract data by running the `extract_data.py` script:
``` bash
python extract_data.py
```

### Preprocess Data
Preprocess data by running the `preprocess_data.py` script:
``` bash
python preprocess_data.py
```

### Train Machine Learning Model
Train the machine learning model by running `train.py` script:
``` bash
python train.py
```
## Usage
### Run the app
Run the streamlit app and access the url [http://localhost:8501](http://localhost:8501):
``` bash
streamlit run app.py
```


## Project Structure

``` bash
IPL Score Predictor/
├── app.py               # Streamlit app script
├── train.py             # Model training script
├── transformer.joblib   # Trained column transformer pipeline
├── model.joblib         # Trained machine learning model
├── ipl_data/            # Historical match data for training
├── requirements.txt     # Python packages required
└── README.md            # Project documentation

```
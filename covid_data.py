import requests
import pandas as pd

def fetch_data():
    url ="https://disease.sh/v3/covid-19/countries"
    response = requests.get(url)
    data=response.json()
    return pd.DataFrame(data)

if __name__ == "__main__":
    df=fetch_data()
    print(df.head())
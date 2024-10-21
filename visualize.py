import matplotlib.pyplot as plt

def plot_cases(data,country):
    country_data = data[data['country'] == country]
    country_data = data[data['country'] == country]
    plt.figure(figsize=(10, 5))
    plt.bar(country_data['country'], country_data['cases'])
    plt.title(f"COVID-19 Cases in {country}")
    plt.show()

if __name__ == "__main__":
    from covid_data import fetch_data
    data = fetch_data()
    plot_cases(data,"Pakistan")


from covid_data import fetch_data
from visualize import plot_cases

if __name__ == "__main__":
    data = fetch_data()
    country=input("Enter your country ")
    plot_cases(data,country)
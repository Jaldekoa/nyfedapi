import pandas as pd

# JSON que mencionaste
data = {
  "pd": {
    "marketShare": {
      "quarterly": {
        "releaseDate": "2024-09-19",
        "title": "QUARTER I 2022",
        "numDealers": {
          "firstQuint": 5,
          "secondQuint": 5,
          "thirdQuint": 5,
          "fourthQuint": 5,
          "fifthQuint": 4
        },
        "interDealerBrokers": [
          {
            "securityType": "U.S. TREASURY SECURITIES (EXCLUDING TIPS)",
            "security": "TREASURY BILLS",
            "percentFirstQuintRange": ">=7.78",
            "percentFirstQuintMktShare": "46.11",
            "percentSecondQuintRange": "4.47 - 7.77",
            "percentSecondQuintMktShare": "31.11",
            "percentThirdQuintRange": "2.16 - 3.42",
            "percentThirdQuintMktShare": "12.72",
            "percentFourthQuintRange": "1.35 - 2.16",
            "percentFourthQuintMktShare": "8.85",
            "percentFifthQuintRange": "<=0.65",
            "percentFifthQuintMktShare": "1.22",
            "dailyAvgVolInMillions": 33331.4
          }
        ],
        "others": [
          {
            "securityType": "U.S. TREASURY SECURITIES (EXCLUDING TIPS)",
            "security": "TREASURY BILLS",
            "percentFirstQuintRange": ">=7.78",
            "percentFirstQuintMktShare": "46.11",
            "percentSecondQuintRange": "4.47 - 7.77",
            "percentSecondQuintMktShare": "31.11",
            "percentThirdQuintRange": "2.16 - 3.42",
            "percentThirdQuintMktShare": "12.72",
            "percentFourthQuintRange": "1.35 - 2.16",
            "percentFourthQuintMktShare": "8.85",
            "percentFifthQuintRange": "<=0.65",
            "percentFifthQuintMktShare": "1.22",
            "dailyAvgVolInMillions": 33331.4
          }
        ],
        "totals": [
          {
            "securityType": "U.S. TREASURY SECURITIES (EXCLUDING TIPS)",
            "security": "TREASURY BILLS",
            "percentFirstQuintRange": ">=7.78",
            "percentFirstQuintMktShare": "46.11",
            "percentSecondQuintRange": "4.47 - 7.77",
            "percentSecondQuintMktShare": "31.11",
            "percentThirdQuintRange": "2.16 - 3.42",
            "percentThirdQuintMktShare": "12.72",
            "percentFourthQuintRange": "1.35 - 2.16",
            "percentFourthQuintMktShare": "8.85",
            "percentFifthQuintRange": "<=0.65",
            "percentFifthQuintMktShare": "1.22",
            "dailyAvgVolInMillions": 33331.4
          }
        ]
      }
    }
  }
}

# Extraer la lista de interDealerBrokers, others y totals
inter_dealer_brokers = data['pd']['marketShare']['quarterly']['interDealerBrokers']
others = data['pd']['marketShare']['quarterly']['others']
totals = data['pd']['marketShare']['quarterly']['totals']

# Unir todas las listas en una sola
combined_data = inter_dealer_brokers + others + totals

# Convertir en DataFrame de pandas
df = pd.DataFrame(combined_data)
df.to_csv("marketshare.csv", sep=";")
# Mostrar el DataFrame
print(df)

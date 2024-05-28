import pandas as pd
import matplotlib.pyplot as plt

options = [
    {
        "opt": "Teambaserat arbete - goda möten (struktur och genomförande), problemlösning",
        "nr": 0
    },
    {
        "opt": "Kollegialt lärande - auskultationer, fokus på pedagogers behov och elevernas lärande",
        "nr": 0
    },
    {
        "opt": "Att skapa en god lärmiljö i klassrummet - placering, information, utsmyckning, ljus och ljud",
        "nr": 0
    },
    {
        "opt": "Att skapa relation till elever - betydelsen att belysa behov, engagemang på klassnivå, individnivå",
        "nr": 0
    },
    {
        "opt": "Att starta lektionen - hälsningsrutin, skapa intresse, ge instruktioner, variation och kreativitet",
        "nr": 0
    },
    {
        "opt": "Strukturerad undervisning - att skapa en optimal lärmiljö, ledarskapet, visa, öva på egen hand, utvärdering och bedömning",
        "nr": 0
    },
    {
        "opt": "Att avsluta lektionen - sammanfatta, kontroll vad eleverna lärt sig, avskedsrutin",
        "nr": 0
    },
    {
        "opt": "Regler och förväntningar - våra skolregler, förväntningar på elever",
        "nr": 0
    },
    {
        "opt": "Att förebygga störande och oroliga beteenden - förstärka elevers positiva beteenden",
        "nr": 0
    },
    {
        "opt": "Att hantera störande och oroliga beteenden - hur du kan agera på olika sätt beroende på situation",
        "nr": 0
    }
]

units = [
    "Myrsjöskolan",
    "Orminge skola",
    "Sågtorpsskolan",
    "Myrsjö resursskola"]

def reset_options():
    for option in options:
        option["nr"] = 0


df = pd.read_csv('./data.csv', delimiter=';')

for unit in units:
    for idx, row in df.iterrows():
        if unit in row.iloc[2]:
            for option in options:
                if option["opt"] in row.iloc[3]:
                    option["nr"] = option["nr"] + 1
    print(options)
    print(f"\nCreating bar chart for {unit}...\n")
    
    fig, ax = plt.subplots(figsize=(20, 12))
    plt.bar([option["opt"].split(' - ')[0] for option in options], [option["nr"] for option in options])
    plt.xticks(rotation=45, fontsize=8)
    plt.yticks(fontsize=8)
    plt.yticks(range(0, max([option["nr"] for option in options]) + 1))  # Set y-axis ticks to increment of 1
    plt.grid(axis='y', linestyle='-', alpha=0.7)
    plt.title(f'Survey Results for {unit}', fontsize=16) # Title can be changed
    plt.xlabel('Survey Option', fontsize=14) # X-axis label can be changed
    plt.ylabel('Number of Employees', fontsize=14) # Y-axis label can be changed
    plt.tight_layout()
    plt.savefig(f'{unit}_survey_results.png')
    plt.close(fig)
    reset_options()

print("Bar charts saved for each location.")
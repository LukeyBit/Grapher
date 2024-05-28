# Grapher

Ett enkelt program för att skapa grafer från en CSV-fil.

## Användning

Vid användning av programmet kan en Virtual Environment användas för att installera de nödvändiga biblioteken. För att skapa en Virtual Environment kan följande kommando användas:

```bash
python3 -m venv venv
```

För att aktivera Virtual Environment kan följande kommando användas:

```bash
source venv/bin/activate
```

Användningen av en Virtual Environment är dock inte nödvändig. Oavsett om en Virtual Environment används eller inte används följande kommando för att installera nödvändiga bibliotek och köra programmet:

```bash
pip install -r requirements.txt
python3 grapher.py
```

## Filer och namn på grafernas axlar

För att programmet ska fungera korrekt måste en CSV-fil finnas i samma mapp som programmet. Filen måste heta `data.csv`.

För att ändra namn på grafernas axlar kan ändringar utföras på de kommenterade raderna.
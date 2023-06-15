# Diccionarios
# { "Key": "value": "key": "value"  }

team={
    "name": "City",
    "country":"England",
    "champions":1,
    "players": ['Haaland', 'Grealish']
}
print(type(team))
print(team)
print(team["name"])
print(team["players"])
team["players"].append("Foden")
team["name"]="Manchester City"
team["league"]="Premier League"
print(team)

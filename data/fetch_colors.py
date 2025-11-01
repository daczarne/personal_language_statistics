import requests
import yaml

DEFAULT_COLOR = "#cccccc"


#* Requests raw file and parses it as a Python dict
linguist_languages_url: str = "https://raw.githubusercontent.com/github/linguist/master/lib/linguist/languages.yml"
linguist_repo = requests.get(url = linguist_languages_url)
raw_data = yaml.safe_load(linguist_repo.content)


#* Parse data into a dict. Language names are the keys, colors the values
languages = list(raw_data.keys())
languages_data = list(raw_data.values())
colors = []

for i in range(0, len(languages)):
    try:
        colors.append((languages_data[i]["color"].lower()))
    except:
        colors.append(DEFAULT_COLOR)

language_colors = dict(zip(languages, colors))


#* Save language_colors to a yaml file
with open(file = "data/language_colors.yaml", mode = "w") as outfile:
    yaml.dump(data = language_colors, stream = outfile, default_flow_style = False)

from typing import TypedDict

import requests
import yaml

DEFAULT_COLOR = "#cccccc"


class LanguageInformation(TypedDict, total = False):
    type: str
    ace_mode: str
    extensions: list[str]
    filenames: list[str]
    language_id: int
    tm_scope: str
    aliases: list[str]
    codemirror_mode: str
    codemirror_mime_type: str
    color: str
    fs_name: str
    group: str
    interpreters: list[str]
    wrap: bool


type LanguageColor = dict[str, str]


def update_colors() -> None:
    #* Request raw file and parses it as a Python dict
    linguist_languages_url: str = "https://raw.githubusercontent.com/github/linguist/master/lib/linguist/languages.yml"
    linguist_repo: requests.Response = requests.get(url = linguist_languages_url)
    raw_data: dict[str, LanguageInformation] = yaml.safe_load(stream = linguist_repo.content)
    
    language_colors: LanguageColor = {
        name: information.get("color", DEFAULT_COLOR).lower() for name, information in raw_data.items()
    }
    
    #* Save language_colors to a yaml file
    with open(file = "modules/language_colors.yaml", mode = "w") as outfile:
        yaml.dump(data = language_colors, stream = outfile, default_flow_style = False)


if __name__ == "__main__":
    update_colors()

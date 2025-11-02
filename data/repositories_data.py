import json
from typing import Any

import pandas as pd
import requests
from github import Github

type Credentials = dict[str, str]


#* Fetches credentials
with open(file = "data/credentials.json", mode = "r") as file:
    auth: Credentials = json.load(file)


def update_repositories_data() -> None:
    #* Creates GitHub client
    gh = Github(login_or_token = auth["pat"])
    
    
    #* Fetches repos languages data
    repo_name: list[str] = []
    is_private: list[bool] = []
    created_date: list = []
    is_archived: list[bool] = []
    languages: list[dict[str, Any]] = []
    
    for repo in gh.get_user().get_repos():
        
        im_owner: bool = repo.owner.login == auth["user_name"]
        
        if im_owner and not repo.fork:
            
            print(f"Fetching data for repo {repo.name}")
            repo_name.append(repo.name)
            is_private.append(repo.private)
            created_date.append(repo.created_at)
            is_archived.append(repo.archived)
            languages_data: dict = requests.get(
                url = repo.languages_url,
                auth = (auth["user_name"], auth["pat"])
            ).json()
            languages.append(
                {
                    "repo_name": repo.name,
                    "L": list(languages_data.keys()),
                    "S": list(languages_data.values())
                }
            )
    
    df_data = {
        "repo_name": repo_name,
        "is_private": is_private,
        "created_date": created_date,
        "is_archived": is_archived,
    }
    
    df: pd.DataFrame = pd.DataFrame(data = df_data)
    lang_df: pd.DataFrame = pd.json_normalize(data = languages) \
        .explode(column = list("LS")) \
        .rename(columns = {"L": "language", "S": "size"})
    
    df: pd.DataFrame = df.merge(
        right = lang_df,
        how = "left",
        on = "repo_name",
    )
    
    #* Saves CSV with data
    df.to_csv(path_or_buf = "data/languages.csv", index = False)


if __name__ == "__main__":
    update_repositories_data()

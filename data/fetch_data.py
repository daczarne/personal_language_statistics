import json

import pandas as pd
import requests
from github import Github

#* Fetches credentials
with open("data/credentials.json", "r") as file:
    auth = json.load(file)

#* Creates GitHub client
gh = Github(auth["pat"])


#* Fetches repos languages data
repo_name = []
is_private = []
created_date = []
is_archived = []
languages = []

for repo in gh.get_user().get_repos():
    
    im_owner = repo.owner.login == auth["user_name"]
    
    if im_owner and not repo.fork:
        
        print(f"Fetching data for repo {repo.name}")
        repo_name.append(repo.name)
        is_private.append(repo.private)
        created_date.append(repo.created_at)
        is_archived.append(repo.archived)
        languages_data = requests.get(
            repo.languages_url,
            auth = (auth["user_name"], auth["pat"])
        ).json()
        languages.append({
            "repo_name": repo.name,
            "L": list(languages_data.keys()),
            "S": list(languages_data.values())
        })

df_data = {
    "repo_name": repo_name,
    "is_private": is_private,
    "created_date": created_date,
    "is_archived": is_archived,
}

df = pd.DataFrame(data = df_data)
lang_df = pd.json_normalize(data = languages) \
    .explode(column = list("LS")) \
    .rename(columns = {"L": "language", "S": "size"})

df = df.merge(
    right = lang_df,
    how = "left",
    on = "repo_name"
)

#* Saves CSV with data
df.to_csv(path_or_buf = "data/languages.csv", index = False)

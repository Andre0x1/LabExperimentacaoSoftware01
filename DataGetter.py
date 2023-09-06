import requests
import json
import time
import csv
from datetime import datetime


def get_repositories():
    url = "https://api.github.com/graphql"

    headers = {
        'Authorization': "token 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",
    }

    query = """
        query ($cursor: String) {
            search(query: "stars:>100", type: REPOSITORY, first: 10, after: $cursor) {
                pageInfo {
                    hasNextPage
                    endCursor
                }
                nodes {
                    ... on Repository {
                        nameWithOwner
                        stargazers {
                            totalCount
                        }
                        createdAt
                        updatedAt
                        releases {
                            totalCount
                        }
                        primaryLanguage {
                            name
                        }
                        issues {
                            totalCount
                        }
                        issuesClosed: issues(states: CLOSED) {
                            totalCount
                        }
                        defaultBranchRef {
                            target {
                                ... on Commit {
                                    history {
                                        totalCount
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    """

    repositories = []

    cursor = None
    count =  0
    while count<100:
        response = requests.post(url, json={"query": query, "variables": {"cursor": cursor}}, headers=headers)

        if response.status_code == 200:
            try:
                data = response.json()
                search_result = data.get("data", {}).get("search", {})
                repositories.extend(search_result.get("nodes", []))
                page_info = search_result.get("pageInfo", {})
                count += 1
                print((count*100)/100,"%")
                if page_info.get("hasNextPage"):
                    cursor = page_info.get("endCursor")
                else:
                    break  
            except json.JSONDecodeError as e:
                print(f"JSON error: {e}")
        else:
            print(f"Erro: status code {response.status_code}...")
            time.sleep(60) 
        
    with open("data_1000.json", "w") as json_file:
        json.dump(repositories, json_file, indent=4)

def get_info():
    with open('data.json', 'r') as json_file:
        data = json.load(json_file)


    with open('repos.csv', 'w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['nome_repo', 'n_estrelas', 'dias_desde_criacao', 'd_criacao', 'dias_desde_atualizacao', 'd_atualizacao', 'n_releases', 'linguagem', 'n_issues', 'n_issues_fechadas', 'n_pull_requests']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        

        writer.writeheader()


        for repo in data:

            data_criacao =  datetime.strptime(repo['createdAt'], "%Y-%m-%dT%H:%M:%SZ")
            data_atualizacao =  datetime.strptime(repo['updatedAt'], "%Y-%m-%dT%H:%M:%SZ")


            diferenca_criacao = datetime.utcnow() - data_criacao
            diferenca_atualizacao = datetime.utcnow() - data_atualizacao
           


            writer.writerow({
                'nome_repo': repo['nameWithOwner'],
                'n_estrelas': repo['stargazers']['totalCount'],
                'dias_desde_criacao' : diferenca_criacao.days,
                'd_criacao': repo['createdAt'],
                'dias_desde_atualizacao' : diferenca_atualizacao.days,
                'd_atualizacao': repo['updatedAt'],
                'n_releases': repo['releases']['totalCount'],
                'linguagem': repo['primaryLanguage']['name'] if repo['primaryLanguage'] else '',
                'n_issues': repo['issues']['totalCount'],
                'n_issues_fechadas': repo['issuesClosed']['totalCount'],
                'n_pull_requests': repo['defaultBranchRef']['target']['history']['totalCount']
            })

    print("Dados salvos no arquivo CSV.")

if __name__ == "__main__":
    get_repositories()
    get_info()


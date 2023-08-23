import requests
import json
import time

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
                print((count*100)/10,"%")
                if page_info.get("hasNextPage"):
                    cursor = page_info.get("endCursor")
                else:
                    break  
            except json.JSONDecodeError as e:
                print(f"JSON decoding error: {e}")
        else:
            print(f"Request failed with status code {response.status_code}. Retrying in 10 minutes...")
            time.sleep(60)  

    return repositories


if __name__ == "__main__":
    data = get_repositories()

    with open("data.json", "w") as json_file:
        json.dump(data, json_file, indent=4)

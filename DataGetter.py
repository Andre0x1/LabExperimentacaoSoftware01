import requests
import json
import time

def get_top_repositories():
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
    while count<10:
        response = requests.post(url, json={"query": query, "variables": {"cursor": cursor}}, headers=headers)

        if response.status_code == 200:
            try:
                data = response.json()
                search_result = data.get("data", {}).get("search", {})
                repositories.extend(search_result.get("nodes", []))
                page_info = search_result.get("pageInfo", {})
                count += 1
                if page_info.get("hasNextPage"):
                    cursor = page_info.get("endCursor")
                else:
                    break  # No more pages
            except json.JSONDecodeError as e:
                print(f"JSON decoding error: {e}")
        else:
            print(f"Request failed with status code {response.status_code}. Retrying in 10 minutes...")
            time.sleep(60)  # Pause for 10 minutes before retrying

    return repositories


if __name__ == "__main__":
    top_repositories = get_top_repositories()

    with open("top_repositories.json", "w") as json_file:
        json.dump(top_repositories, json_file, indent=4)

import requests


def get_top_repositories():
    url = "https://api.github.com/graphql"

    headers = {
        "Authorization": "Bearer YOUR_GITHUB_ACCESS_TOKEN",
    }

    query = """
            {
        search(query: "stars:>100", type: REPOSITORY, first: 10) {
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
                releases {
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

    response = requests.post(url, json={"query": query}, headers=headers)
    data = response.json()

    repositories = data["data"]["search"]["edges"]

    return repositories


if __name__ == "__main__":
    top_repositories = get_top_repositories()

    for idx, repo in enumerate(top_repositories, start=1):
        node = repo["node"]
        print(
            f"{idx}. {node['owner']['login']}/{node['name']} - Stars: {node['stargazers']['totalCount']} - Forks: {node['forks']['totalCount']} - URL: {node['url']}"
        )

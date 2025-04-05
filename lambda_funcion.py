import requests

LEETCODE_API_URL = "https://leetcode.com/graphql"

PROBLEM_OF_THE_DAY_QUERY = {
    "query": """
    query questionOfToday {
        activeDailyCodingChallengeQuestion {
            date
            question {
                titleSlug
            }
        }
    }
    """
}

def lambda_handler(event, context):
    response = requests.post(LEETCODE_API_URL, json=PROBLEM_OF_THE_DAY_QUERY)
    data = response.json()

    result = data["data"]["activeDailyCodingChallengeQuestion"]

    slug = result["question"]["titleSlug"]
    date = result["date"]

    leetcode_url = f"https://leetcode.com/problems/{slug}/description/?envType=daily-question&envId={date}"

    return {
        "statusCode": 302,
        "headers": {
            "Location": leetcode_url
        }
    }


import requests
import time

# 🔐 Replace with your personal GitHub token
GITHUB_TOKEN = [YOUR_GITHUB_TOKEN]

headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}

query = "location:Chennai followers:>110"
search_url = "https://api.github.com/search/users"
all_users = []

print("🔍 Starting GitHub user search...")

# Step 1: Paginate through up to 10 pages (1000 users max)
for page in range(1, 11):
    print(f"📄 Fetching page {page}...")
    params = {
        "q": query,
        "per_page": 100,
        "page": page
    }
    response = requests.get(search_url, headers=headers, params=params)

    if response.status_code != 200:
        print(f"❌ GitHub Search API failed on page {page}: {response.status_code}")
        print(response.json())
        break

    users = response.json().get("items", [])
    if not users:
        print("✅ No more users returned by GitHub.")
        break

    all_users.extend(users)
    time.sleep(1)  # optional: avoid rate-limit issues

print(f"✅ Total users fetched: {len(all_users)}")

# Step 2: Fetch each user's full profile to get 'created_at'
user_profiles = []

for i, user in enumerate(all_users):
    username = user["login"]
    profile_url = f"https://api.github.com/users/{username}"

    profile_res = requests.get(profile_url, headers=headers)
    if profile_res.status_code == 200:
        profile_data = profile_res.json()
        user_profiles.append({
            "login": username,
            "created_at": profile_data["created_at"]
        })
    else:
        print(f"⚠️ Could not fetch profile for {username} (status: {profile_res.status_code})")
    
    time.sleep(0.5)  # optional: avoid hitting secondary rate limits

# Step 3: Find the newest user
if user_profiles:
    newest_user = max(user_profiles, key=lambda x: x["created_at"])
    print("\n🚀 Newest GitHub user in Chennai with >110 followers:")
    print(f"👤 Username: {newest_user['login']}")
    print(f"📅 Created at: {newest_user['created_at']}")
else:
    print("⚠️ No valid user profiles retrieved.")

#Output : 2024-11-10T15:07:27Z

import requests;
import json;

client_id = "h4gHCnU84iAlINw7VJKZwnv3ObFvxzZ2rg0gCMHm";
client_secret = "ISGMfycU8PsCLWvydoJLpGeAEt8OVOfQ1UDapz4jirgN175L5HoF1txRI7LS6RhttvjKkRxduvIHN7dKKGcO0IXozpmfOX1LTQjJxXKxgQy9JaA3Fxkm9cM1x906MVca";
env = "production";

if (client_id.startswith("test")):
    url = "https://test.instamojo.com/oauth2/token/";
    env = "test";

payload = "grant_type=client_credentials&client_id=" + client_id + "&client_secret=" + client_secret;
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers);
token = env + json.loads(response.text)["access_token"];
print(token);
import requests
import os

def check_facebook_token(user_token, app_access_token):
    url = "https://graph.facebook.com/debug_token"
    params = {
        "input_token": user_token,
        "access_token": app_access_token
    }
    
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            if "data" in data and data["data"]["is_valid"]:
                print("\n[+] Token is LIVE!")
                print(f"  App ID: {data['data']['app_id']}")
                print(f"  User ID: {data['data']['user_id']}")
                expiry = data['data'].get("expires_at", "No expiry (long-lived token)")
                print(f"  Expiry: {expiry}")
            else:
                print("\n[-] Token is INVALID or EXPIRED.")
        else:
            print("\n[!] Error: Unable to validate token.")
            print(response.json())
    except Exception as e:
        print(f"\n[!] Exception: {e}")

def main():
    print("\n--- Facebook Access Token Checker ---\n")
    user_token = input("[?] Enter User Access Token: ").strip()
    app_access_token = input("[?] Enter App Access Token (APP_ID|APP_SECRET): ").strip()
    check_facebook_token(user_token, app_access_token)

if __name__ == "__main__":
    try:
        os.system("clear")
        main()
    except KeyboardInterrupt:
        print("\n[!] Exiting... Goodbye!")


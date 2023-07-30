import requests
 
def save_scam_website(url, description):
    with open('scam_websites.txt', 'a') as file:
        file.write(f"{url}\t{description}\n")

def update_github_file():
    github_username = 'YOUR_GITHUB_USERNAME'
    repo_name = 'YOUR_GITHUB_REPO_NAME'
    access_token = 'YOUR_GITHUB_ACCESS_TOKEN'
    file_path = 'scam_websites.txt'

    with open(file_path, 'rb') as file:
        headers = {
            'Authorization': f"token {access_token}"
        }
        url = f"https://api.github.com/repos/{github_username}/{repo_name}/contents/{file_path}"
        response = requests.get(url, headers=headers)
        existing_content = response.json()['content']
        new_content = file.read().decode('utf-8')
        
        if existing_content != new_content:
            data = {
                'message': 'Update scam_websites.txt',
                'content': new_content,
                'sha': response.json()['sha']
            }
            update_response = requests.put(url, headers=headers, json=data)
            if update_response.status_code == 200:
                print("scam_websites.txt updated successfully!")
            else:
                print("Failed to update scam_websites.txt. Please check the GitHub access token.")
        else:
            print("No changes to the scam_websites.txt file.")

def main():
    print("Welcome! You can use this script to save and update potential scam websites.")
    while True:
        print("\nOptions:")
        print("1. Save a scam website")
        print("2. Update scam_websites.txt on GitHub")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            url = input("Enter the URL of the potential scam website: ")
            description = input("Enter a short description of the potential scam: ")
            save_scam_website(url, description)
            print("Website and description saved successfully!")

        elif choice == '2':
            update_github_file()

        elif choice == '3':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

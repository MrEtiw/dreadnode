import os
import requests


def download_artifact(artifact_files, crucible_url, challenge, crucible_api_key):
    # Ensure data directory exists
    os.makedirs("data", exist_ok=True)
    
    for artifact in artifact_files:
        url = f"{crucible_url}/api/artifacts/{challenge}/{artifact}"
        print(url)
        headers = {"X-API-Key": crucible_api_key}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            # Save file in the data folder
            file_path = os.path.join("data", artifact)
            with open(file_path, "wb") as file:
                file.write(response.content)
            print(f"{artifact} was successfully downloaded to data folder")
        else:
            print(f"Failed to download {artifact}")



def submit_flag(challenge_url, crucible_api_key, flag):
    # Ensure flag is wrapped in curly brackets
    if not (flag.startswith('{') and flag.endswith('}')):
        flag = f"{{{flag}}}"  # Add curly brackets if they're missing
    
    response = requests.post(
        f"{challenge_url}/score",
        headers={"X-API-Key": crucible_api_key},
        json={"data": flag},
    )
    return response.json()
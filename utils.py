import requests
import os


def download_artifact(artifact_files, crucible_url, challenge, crucible_api_key):
    for artifact in artifact_files:
        url = f"{crucible_url}/api/artifacts/{challenge}/{artifact}"
        print(url)
        headers = {"X-API-Key": crucible_api_key}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            with open(artifact, "wb") as file:
                file.write(response.content)
            print(f"{artifact} was successfully downloaded")
        else:
            print(f"Failed to download {artifact}")

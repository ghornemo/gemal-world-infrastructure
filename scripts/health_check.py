from urllib.request import urlopen
from urllib.error import HTTPError, URLError

print("Health check script started")

apps = {
    "Base portfolio": "https://gemal.dev",
    "Gemal World": "https://world.gemal.dev/store",
}

for name, url in apps.items():
    try:
        with urlopen(url, timeout=5) as response:
            if response.status == 200:
                print(f"{name} is live")
            else:
                print(f"{name} returned HTTP {response.status}")

    except HTTPError as error:
        print(f"{name} returned HTTP {error.code}")
    except (URLError, TimeoutError) as error:
        print(f"{name} could not be reached: {error}")
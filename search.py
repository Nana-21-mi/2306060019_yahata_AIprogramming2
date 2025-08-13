import requests

def get_breed_image(breed_name):
    """
    犬種名を受け取り、Dog APIから画像URLを取得して返す。
    見つからなければ None を返す。
    """
    url = f"https://dog.ceo/api/breed/{breed_name.lower()}/images/random"
    response = requests.get(url)

    if response.status_code != 200:
        return None

    data = response.json()
    if data['status'] == 'success':
        return data['message']  # 画像URL
    else:
        return None
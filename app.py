import streamlit as st
import requests
from search import get_breed_image

st.title("犬種画像検索アプリ")

# 犬種リスト（英語：日本語）
breed_dict = {
    "hound": "ハウンド",
    "pug": "パグ",
    "bulldog": "ブルドッグ",
    "beagle": "ビーグル",
    "dachshund": "ダックスフンド",
    "akita": "秋田犬",
    "chihuahua": "チワワ",
    "dalmatian": "ダルメシアン",
    "labrador": "ラブラドール",
    "poodle": "プードル"
}

# サイドバーに表示
st.sidebar.header("犬種例")
for eng, jp in breed_dict.items():
    st.sidebar.write(f"{eng} = {jp}")

# メイン部分
breed = st.text_input("犬種名を英語で入力してください（例：hound, pug, bulldog）")

if breed:
    image_url = get_breed_image(breed)

    if image_url:
        # 画像を表示
        st.image(image_url, caption=f"{breed} の画像", use_container_width=True)

        # 画像をダウンロードできるようにする
        response = requests.get(image_url)
        if response.status_code == 200:
            image_bytes = response.content
            st.download_button(
                label="ダウンロード",
                data=image_bytes,
                file_name=f"{breed}.jpg",
                mime="image/jpeg"
            )
    else:
        st.error("犬種が見つかりませんでした。綴りを確認してください。")

import streamlit as st

# --- アイテム一覧 ---
all_items = [
    "フォーム入力",
    "ボタン操作",
    "リスト表示",
    "DB保存",
    "DB取得",
    "API取得",
    "グラフ表示",
    "検索機能",
    "ローカル保存",
    "画像アップロード",
    "セレクトボックス",
    "日付入力",
    "通知機能"
]

# --- 拡張クラフトレシピ辞書 ---
recipes = {
    frozenset(["フォーム入力", "ボタン操作", "ローカル保存"]): {
        "name": "シンプルメモアプリ",
        "description": "メモを入力してローカル保存する最小構成のアプリ。"
    },
    frozenset(["フォーム入力", "DB保存", "リスト表示"]): {
        "name": "ToDoアプリ",
        "description": "タスクを追加・保存し、一覧表示する定番アプリ。"
    },
    frozenset(["DB取得", "リスト表示", "検索機能"]): {
        "name": "在庫検索システム",
        "description": "データベース上の在庫を一覧・検索できる業務向けアプリ。"
    },
    frozenset(["API取得", "グラフ表示"]): {
        "name": "天気ダッシュボード",
        "description": "天気APIのデータを取得し、可視化するアプリ。"
    },
    frozenset(["フォーム入力", "DB保存", "検索機能"]): {
        "name": "お気に入り登録アプリ",
        "description": "お気に入りを登録・検索できるユーザー支援系アプリ。"
    },
    frozenset(["画像アップロード", "DB保存", "リスト表示"]): {
        "name": "写真投稿ギャラリー",
        "description": "画像を投稿して他人と共有できるビジュアルアプリ。"
    },
    frozenset(["フォーム入力", "日付入力", "通知機能"]): {
        "name": "スケジュールリマインダー",
        "description": "予定に応じた通知が出せる生活支援アプリ。"
    },
    frozenset(["フォーム入力", "セレクトボックス", "DB保存"]): {
        "name": "アンケート集計アプリ",
        "description": "選択式のアンケートを収集・分析できるシンプルな調査ツール。"
    },
    frozenset(["API取得", "検索機能", "リスト表示"]): {
        "name": "書籍検索アプリ",
        "description": "書籍APIを使って本を検索し、表示できるアプリ。"
    },
    frozenset(["フォーム入力", "画像アップロード", "DB保存"]): {
        "name": "プロフィール作成アプリ",
        "description": "ユーザー情報と画像を保存して自己紹介ページを作成できるアプリ。"
    }
}

# --- UI ---
st.title("🧪 クラフト型アプリアイデアメーカー")
st.markdown("学んだ機能（アイテム）を組み合わせて、どんなアプリが作れるかを発見しましょう。")

selected_items = st.multiselect("使用するアイテムを選んでください（最大3つ）", all_items, max_selections=3)

if st.button("クラフト！"):
    key = frozenset(selected_items)
    if key in recipes:
        st.success(f"✨ {recipes[key]['name']}")
        st.markdown(recipes[key]["description"])
    else:
        st.warning("🧪 その組み合わせでは、まだレシピが見つかっていません。新しいアプリを発想してみましょう！")


# --- 逆引きセクション ---
st.divider()
st.subheader("🔍 アプリ名から逆引き")

app_options = sorted([v["name"] for v in recipes.values()])
selected_app = st.selectbox("見たいアプリを選んでください", app_options)

for item_set, info in recipes.items():
    if info["name"] == selected_app:
        st.markdown(f"**{info['name']}** に必要な機能：")
        st.markdown("・" + "\n・".join(sorted(item_set)))
        st.markdown(info["description"])
        break
# 顧客名簿
customers = [
    "Tanaka Hiroshi",
    "Yamada Hanako",
    "Suzuki Taro",
    "Kobayashi Keiko",
    "saito yuki"
]

def search_customer(keyword):
    keyword = keyword.lower()  # ① 全て小文字に変換 
    results = []

    for name in customers:
        # ② 名前も小文字にしてから、キーワードの位置を探す 
        if name.lower().find(keyword) != -1:  
            # ③ 見つかった名前を大文字に変換してリストに追加 [cite: 56, 55]
            results.append(name.upper())  

    return results

# --- コマンドラインでのやり取り ---
if __name__ == "__main__":
    print("=== 顧客検索システム ===")
    while True:
        keyword = input("検索したい名前を入力してください（終了は 'exit'）: ")
        if keyword.lower() == 'exit':
            print("システムを終了します。")
            break

        matched = search_customer(keyword)
        if matched:
            print("\n【検索結果】")
            for name in matched:
                print(" -", name)
        else:
            # ④ 仕様通りのエラーメッセージを表示
            print("一致する顧客が見つかりませんでした")
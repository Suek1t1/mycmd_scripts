import sys
import os
from PIL import Image

# --- メインの画像処理関数 ---
def process_image(source_path, output_path, target_width, target_height):
    try:
        img = Image.open(source_path)
        original_width, original_height = img.size

        # ステップ3: 縦または横が指定サイズ以下か判定
        if original_width < target_width or original_height < target_height:
            # アスペクト比を保ったまま拡大するための計算
            width_ratio = target_width / original_width
            height_ratio = target_height / original_height
            scale_ratio = max(width_ratio, height_ratio) # 大きい方の比率に合わせる

            new_width = int(original_width * scale_ratio)
            new_height = int(original_height * scale_ratio)

            print(f"拡大します: ({original_width}x{original_height}) -> ({new_width}x{new_height})")
            img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

        # 拡大後の画像サイズを再取得
        current_width, current_height = img.size

        # 中央を基準に切り取るための座標を計算
        left = (current_width - target_width) / 2
        top = (current_height - target_height) / 2
        right = (current_width + target_width) / 2
        bottom = (current_height + target_height) / 2

        # 画像を切り取る
        cropped_img = img.crop((left, top, right, bottom))
        # 結果を保存
        cropped_img.save(output_path)
        print(f"保存しました: {output_path}")

    except Exception as e:
        print(f"エラー: {source_path} の処理に失敗しました。 - {e}")

# --- ここからスクリプトの実行部分 ---
# ステップ1: 記述ミス（引数）確認
if len(sys.argv) != 5:
    print("エラー: 引数の数が正しくありません。")
    print("使い方: mycmd crop-center <入力フォルダ> <出力フォルダ> <幅> <高さ>")
    sys.exit(1)

input_folder = sys.argv[1]
output_folder = sys.argv[2]
target_width = int(sys.argv[3])
target_height = int(sys.argv[4])

# 出力フォルダがなければ作成
os.makedirs(output_folder, exist_ok=True)

print(f"処理を開始します... -> {output_folder}")

# ステップ2: フォルダ内の画像を一つずつ参照 (ループ)
for filename in os.listdir(input_folder):
    # 対応する画像形式かチェック
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
        source_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)
        
        print(f"\n処理中: {filename}")
        process_image(source_path, output_path, target_width, target_height)

print("\n🎉 全ての処理が完了しました。")
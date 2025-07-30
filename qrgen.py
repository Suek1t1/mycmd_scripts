import qrcode
import sys

# コマンドラインから渡された引数をチェック
if len(sys.argv) < 2:
    print("エラー: QRコードに変換したいテキストやURLを指定してください。")
    print("使い方: mycmd qrgen 'https://example.com'")
    sys.exit(1)

# 変換したいデータ（URLやテキスト）
data = sys.argv[1]

try:
    # QRコードオブジェクトを生成
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=1, # ターミナル表示なので最小サイズにする
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    print("\n以下にQRコードを表示します：\n")
    # 画像を保存する代わりに、ターミナルに直接描画する
    qr.print_tty()
    print() # QRコードの後に改行を入れる

except Exception as e:
    print(f"エラー: QRコードの生成に失敗しました。")
    print(e)
import http.server
import socketserver
import sys

# デフォルトのポート番号
PORT = 8000

# コマンドライン引数からポート番号を取得する。（指定があれば）
if len(sys.argv) > 1:
    try:
        PORT = int(sys.argv[1])
    except ValueError:
        print(f"エラー: ポート番号は数字で指定してください。例: 8080")
        sys.exit(1)

# サーバーを起動
Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Webサーバーを起動しました。")
    print(f"URL: http://localhost:{PORT}")
    httpd.serve_forever()
# mycmd(My Command)
Zshで日々の定型作業を効率化するための自作コマンド集です。誰でも使って結構です。

## コマンド
### 実装済みコマンド
| コマンド | 使用例                             | 意味                | 機能                                                                |
| :--------- | :----------------------------- | :----------------- | :----------------------------------------------------------------- |
| `mkdir_for`| mycmd mkdir_for rep_ 0715 0720 | make directory for | 指定した範囲で連番のフォルダを連続で作成。                                 |
| `cntf`     | mycmd cntf ~/                  | count file         | 指定したディレクトリ内のファイルとフォルダの数をそれぞれ表示。                |

### 未実装のコマンド
| コマンド | 使用例                             | 意味                | 機能                                                                |
| :--------- | :----------------------------- | :----------------- | :------------------------------------------------------------------ |
| `dict`     | mycmd dict international       | dictionary         | 入力した単語の意味を検索できる                                           |
| `pomodoro` | mycmd pomodoro 3               | Pomodoro Technique | 指定したセット数ポモドーロタイマーが作動する。(25分+5分ワンセット)(通知機能あり)|
| `qrgen`    | mycmd qrgen ~/test.jpg         | QR generator       | 指定したファイルのQRコードを生成する                                      |
| `resize`   | まだ考えていない                  | resize             | フォルダ内にある写真を指定したサイズに変更する。                            |
| `pyhttp`   | mycmd pyhttp                   | python http        | カレントディレクトリを簡単なWebサーバーとして起動する                       |
| `dirsize`  | mycmd dirsize ~/               | directory size     | 指定したディレクトリ内にあるファイル、フォルダのサイズを降順で表示する         |
| `forcus`   | mycmd forcus on                | forcus             | 指定されているサイトへのアクセスを禁止する。サイトの指定はコードに記述。       |

## 実装方法
1.  **リポジトリをクローン**
    任意の場所にリポジトリをクローンします。
    ```sh
    git clone https://github.com/suek1t1/mycmd_scripts.git
    cd ~/mycmd_scripts.git
    ```

2.  **実行権限を付与**
    すべてのスクリプトに実行権限を与えます。
    ```sh
    chmod +x mycmd_scripts/*
    ```

3.  **PATHを通す**
    `mycmd`をどこからでも呼び出せるように、`~/bin`ディレクトリへシンボリックリンクを作成し、`PATH`を通します。
    ```sh
    # ~/bin ディレクトリがなければ作成
    mkdir -p ~/bin

    # シンボリックリンクを作成 (パスは適宜修正してください)
    ln -s "$(pwd)/mycmd_scripts/mycmd" ~/bin/mycmd
    ```

4.  **シェルの設定**
    `.zshrc`に`~/bin`へのパスを追加します。
    ```sh
    echo 'export PATH="$HOME/bin:$PATH"' >> ~/.zshrc
    ```
    ターミナルを再起動するか、`source ~/.zshrc` を実行して設定を反映させてください。

## コマンドの追加方法
1. mycmd_scripts/ ディレクトリに、新しい機能を持つシェルスクリプトを作成します。この時、**拡張子.shは記述しないでください**
2. 作成したスクリプトに  **chmod +x <パス>**  で実行権限を与えます。
3. mycmd_scripts/mycmd ファイル内の サブコマンド に、新しいコマンド用の分岐を追加します。
```sh
# サブコマンド
case $sub_command in
  "mkdir_for")                                          # ファイルを連番で作成するコマンド
    exec "$CMD_DIR/mkdir_for" "$@"
    ;;

  "cntf")                                               # フォルダ内のファイルの個数を数えるコマンド
    exec "$CMD_DIR/cntf" "$@"
    ;;
▽▽▽▽▽▽▽▽▽▽▽▽ 追加 ▽▽▽▽▽▽▽▽▽▽▽▽
"追加したいコマンド名")
    exec "$CMD_DIR/追加したいコマンド名" "$@"
    ;;
△△△△△△△△△△△△ 追加 △△△△△△△△△△△△

  *)
    echo "エラー: '$sub_command' は不明なサブコマンドです。"  # エラー時の表示
    exit 1
    ;;
esac
```

## その他
特になし
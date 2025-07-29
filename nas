#!/bin/zsh
# 使用しているPCをNAS化するコマンド

# サブコマンド(on,off,state)
case "$1" in
  on)                                                           # ファイル共有サービスを停止
    echo "NASを開始します。管理者パスワードが必要です。"
    # macOSのファイル共有サービス(SMB)を起動
    sudo launchctl load -w /System/Library/LaunchDaemons/com.apple.smbd.plist
    echo "開始しました。"

    # 接続用IPアドレスを表示
    IP_ADDRESS=$(ipconfig getifaddr en0)
    echo "\n以下のどちらかのアドレスで他のPCから接続してください："
    echo "  - Macから: smb://$IP_ADDRESS"
    echo "  - Windowsから: \\\\$IP_ADDRESS"
    ;;

  off)                                                          # ファイル共有サービスを停止
    sudo launchctl unload -w /System/Library/LaunchDaemons/com.apple.smbd.plist
    echo "nasを停止しました。"
    ;;

  state)                                                        # サービスが動作中か確認
    if pgrep -q smbd; then
        echo "NASモードは現在”実行中”です。"
    else
        echo "NASモードは現在”停止中”です。"
    fi
    ;;

  *)
    echo "使い方: mycmd nas-share [on|of|state]"
    ;;
esac
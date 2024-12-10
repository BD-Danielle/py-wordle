# Wordle 助手

歡迎使用 Wordle 助手！這個程式可以幫助你在玩 Wordle 遊戲時提供單詞建議。

## 功能

- 根據使用者輸入的反饋，篩選出可能的單詞
- 優先推薦常用的五字母單詞
- 提供互動式的遊戲體驗

## 安裝指南

### 1. 克隆倉庫

```bash
git clone git@github.com:BD-Danielle/py-wordle.git
cd py-wordle
```

### 2. 創建虛擬環境

確保你已經安裝了 Python 3 和 `venv` 模組。

```bash
python3 -m venv venv
```

### 3. 啟動虛擬環境

- **在 Windows 上**:

  ```bash
  venv\Scripts\activate
  ```

- **在 macOS 和 Linux 上**:

  ```bash
  source venv/bin/activate
  ```

### 4. 安裝依賴

```bash
pip install -r requirements.txt
```

## 使用方法

1. 運行程式：

   ```bash
   python3 ai.main.py
   ```

2. 按照提示輸入你的猜測和反饋：

   - 使用大寫字母表示綠色（正確的字母在正確的位置）
   - 使用小寫字母表示黃色（正確的字母在錯誤的位置）
   - 使用減號(-)表示灰色（錯誤的字母）

3. 程式會根據你的輸入提供建議的單詞。

## 示例

```
歡迎來到 Wordle 助手!
使用說明:
1. 在 Wordle 中輸入你的猜測
2. 將結果反饋給助手:
   - 使用大寫字母表示綠色（正確的字母在正確的位置）
   - 使用小寫字母表示黃色（正確的字母在錯誤的位置）
   - 使用減號(-)表示灰色（錯誤的字母）
例如: 如果猜測 'weary'，得到 A 為黃色，其他為灰色，則輸入: '--a--'
開始遊戲！

還剩 6 次機會!
請輸入你猜測的單詞: flung
請輸入反饋結果 (大寫=綠色, 小寫=黃色, '-'=灰色): -----
可能的單詞數量: 5674
建議嘗試以下單詞: ['aahed', 'abaca', 'abaci', 'aback', 'abada']
```

## 退出虛擬環境

在完成使用後，你可以通過以下命令退出虛擬環境：

```bash
deactivate
```

## 貢獻

歡迎提交問題和請求功能！請通過 GitHub 提交。

## 許可證

此項目使用 MIT 許可證。

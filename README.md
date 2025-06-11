```markdown
# Discord Token Checker

A fast and efficient asynchronous Discord token validator that checks tokens from a file and saves the working ones.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![aiohttp](https://img.shields.io/badge/aiohttp-3.8.1+-green)

## Features

- 🚀 **Asynchronous** - Checks multiple tokens simultaneously for maximum speed
- ✅ **Validation** - Verifies tokens against Discord's API (canary endpoint)
- 📊 **User Info** - Displays user ID and username for valid tokens
- 📁 **File I/O** - Reads from `tokens.txt` and saves to `valid.txt`
- 🛡️ **Rate Limit Aware** - Limits concurrent connections to avoid bans

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/discord-token-checker.git
   cd discord-token-checker
   ```

2. Install dependencies:
   ```bash
   pip install aiohttp
   ```

## Usage

1. Add your tokens to `tokens.txt` (one token per line)
2. Run the checker:
   ```bash
   python checker.py
   ```
3. Valid tokens will be saved in `valid.txt`

## Example Output

```
Valid Token: 123456789012345678 | DiscordUser#1234
Valid Token: 987654321098765432 | AnotherUser#5678

Saved 2 valid tokens to valid.txt
```

## Warning

⚠️ This tool is for educational purposes only.  
⚠️ Discord's Terms of Service prohibit automated token checking.  
⚠️ Use at your own risk - you may get rate-limited or banned.  




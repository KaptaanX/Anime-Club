# 📁 FileSaveAdvance — Telegram File Store Bot

A powerful Telegram bot that allows the admin to upload and store up to 25 files and generate a single shareable link. When users click the link, all files are sent to them — simple, clean, and secure.

> ✅ Includes Force Join, Broadcast, Multiple Admins, JSON-based storage, and One-Click Railway Hosting!

---

## ✨ Features

- ✅ **File Linking System** — Admin uploads files, receives a unique `/start` link.
- 👥 **Multiple Admin Support** — Easily manage uploads with multiple trusted admins.
- 🔐 **Force Join** — Ensures users join your updates channel before accessing files.
- 📢 **Broadcast Feature** — Admins can send global messages to all users.
- 🧠 **Persistent Storage** — Files and users are stored safely using JSON files.
- 🖱️ **One-Click Deploy to Railway** — Super easy to host and manage your bot.

---

## 🚀 Deploy on Railway

Click below to deploy the bot in one click:

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/YOUR_TEMPLATE_LINK)

---

## 🛠️ Setup Instructions

### 🔧 Requirements
- Python 3.10+
- Telegram Bot Token
- Telegram Channel (for force join)
- Bot must be **admin** in a public storage channel (for copying messages)

### 🔍 Environment Variables

| Key            | Description                            |
|----------------|----------------------------------------|
| `API_KEY`      | Your Telegram Bot Token                |
| `ADMIN_IDS`    | Admin Telegram user IDs (comma-separated) |
| `CHANNEL`      | Force join channel username (e.g. @yourchannel) |

---

## 🧪 Commands

- `/admin` – Start uploading files
- `/done` – Finalize upload and get the link
- `/start` – Start bot or access a shared file group
- `/broadcast` – Admin-only: Send a message to all users

---

## 📸 Preview

![Bot Preview](https://telegra.ph/file/preview.jpg)

---

## 👤 Developer

Made with ❤️ by [SudipX](https://t.me/sudipx)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

# MetaWiper – Image Metadata Viewer & Shredder

[![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-red?logo=streamlit)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Live App](https://img.shields.io/badge/Live%20Demo-metawiper.streamlit.app-orange?logo=fire)](https://metawiper.streamlit.app)
[![Stars](https://img.shields.io/github/stars/rootsecops/metawiper?style=social)](https://github.com/rootsecops/metawiper/stargazers)
[![Forks](https://img.shields.io/github/forks/rootsecops/metawiper?style=social)](https://github.com/rootsecops/metawiper/network/members)
[![Issues](https://img.shields.io/github/issues/rootsecops/metawiper)](https://github.com/rootsecops/metawiper/issues)
[![Pull Requests](https://img.shields.io/github/issues-pr/rootsecops/metawiper)](https://github.com/rootsecops/metawiper/pulls)
[![Contributors](https://img.shields.io/github/contributors/rootsecops/metawiper)](https://github.com/rootsecops/metawiper/graphs/contributors)

> ⚠️ **Disclaimer:** This app works entirely in your browser. No image or data is sent to any server.

---

## 🔗 Live Demo

🌐 [metawiper.streamlit.app](https://metawiper.streamlit.app)

---

## 📑 Table of Contents

- [Features](#-features)
- [Installation](#-installation)
- [How to Use](#-how-to-use)
- [Project Structure](#-project-structure)
- [Screenshot](#-screenshot)
- [Tech Stack](#-tech-stack)
- [Contributing](#-contributing)
- [License](#-license)
- [Author](#-author)

---

## ✨ Features

- 🖼️ **View Metadata** – Check detailed EXIF metadata (camera, location, device info)
- 🧹 **Remove Metadata** – One-click metadata stripper for privacy
- 🔐 **Secure & Local** – No uploads; all operations done locally
- 📥 **Download Clean Image** – Get a clean, stripped version of your image
- ⚡ **Fast UI** – Lightweight, responsive, and minimal design
- 🧠 **EXIF & Hash** – View SHA256 hash of the image
- 🧾 **EXIF Viewer** – Reads camera model, GPS data, timestamps, etc.
- 🛠️ **Multi-format Support** – Supports `.jpg`, `.jpeg`, `.png`, `.webp`, etc.

---

## 🧰 Installation

### ⚙️ Local Setup

```bash
git clone https://github.com/rootsecops/metawiper.git
cd metawiper
pip install -r requirements.txt
streamlit run app.py
````

> Make sure you’re using Python 3.9+.

---

## ▶️ How to Use

1. **Upload Image** (from your device)
2. **View Metadata** (EXIF, hash)
3. **Strip Metadata** (button click)
4. **Download Clean Image** (safe to share)

---

## 📁 Project Structure

```
metawiper/
├── app.py                      # Main Streamlit app
├── utils/
│   └── metadata_tools.py       # EXIF view, hash & strip logic
├── assets/
│   └── metawiper.streamlit.app.jpeg  # Screenshot
├── requirements.txt            # Required Python packages
└── README.md                   # You're here
```

---

## 📸 Screenshot

![MetaWiper Screenshot](https://raw.githubusercontent.com/rootsecops/metawiper/refs/heads/main/assests/metawiper.streamlit.app.jpeg)

---

## ⚒️ Tech Stack

* 🐍 **[Python](https://www.python.org/)** – Backend scripting language.  
* 🖼️ **[Pillow](https://python-pillow.org/)** – Library for image manipulation and format support.  
* 📸 **[piexif](https://pypi.org/project/piexif/)** – Extracts or strips EXIF metadata from images.  
* 🌐 **[Streamlit](https://streamlit.io/)** – Frontend UI framework for building interactive web apps.

---

## 🤝 Contributing

Contributions are welcome! Here’s how you can help:

* 🚀 Fork the repo
* 🛠️ Create a new branch (`git checkout -b feature-name`)
* 🧪 Test your changes
* 🔁 Submit a pull request

---

## 📜 License

This project is licensed under the **MIT License**.
You are free to use, modify, and distribute this software.

[Read License »](https://github.com/rootsecops/metawiper/blob/main/LICENSE)

---

## 👤 Author

Developed & Maintained by: 

[![GitHub](https://img.shields.io/badge/GitHub-black?style=for-the-badge&logo=github)](https://github.com/rootsecops0x1)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/sonajit0x1/)


---

> ❗ **Disclaimer**: No data is uploaded to any server. This tool is purely client-side and ensures your privacy during use.


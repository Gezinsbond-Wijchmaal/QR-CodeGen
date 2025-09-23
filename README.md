# 📦 QR-CodeGen

Een verzameling Python-scripts voor **QR-code generatie** en **aftelklokken** met geluid en GUI.

---

## 🚀 Snel starten

### 1. Repo clonen
```bash
git clone https://github.com/Gezinsbond-Wijchmaal/QR-CodeGen.git
cd QR-CodeGen
```

### 2. Virtuele omgeving maken
```bash
python -m venv venv
```

Activeer de omgeving:
- **Windows**:
  ```bash
  venv\Scripts\activate
  ```
- **Linux/macOS**:
  ```bash
  source venv/bin/activate
  ```

### 3. Dependencies installeren
```bash
pip install -r gbw/requirements.txt
```

---

## ▶️ Scripts starten

### Hoofdmenu
```bash
python gbw/start.py
```

### Aftelklokken
- **Standaard aftelklok**:  
  ```bash
  python gbw/aftelklok.py
  ```
- **GUI-versie (zonder console)**:  
  ```bash
  python gbw/aftelklok.pyw
  ```
- **Alternatieve versies**:  
  ```bash
  python gbw/aftelklok1.pyw
  python gbw/aftelklok2.py
  python gbw/aftelklok2.pyw
  ```

### QR Code generator
```bash
python gbw/qrgbw.py
```

---

## 🛠 Extra tools

### Automatisch committen naar GitHub
Gebruik het script **`git_auto_commit.py`**:
```bash
python git_auto_commit.py
```
👉 Je voert een commit message in, en het script doet automatisch:
`git add .` → `git commit -m` → `git push`

---

## 📂 Projectstructuur
```
QR-CodeGen/
│── gbw/               # hoofdmap met Python scripts
│   ├── aftelklok*.py  # aftelklok varianten
│   ├── qrgb*.py       # QR-code generator
│   ├── sounds/        # geluiden
│   ├── fonts/         # lettertypes
│   └── pics/          # afbeeldingen
│
├── run.bat            # Windows script om snel te starten
├── git_auto_commit.py # hulpscript voor commits
└── README.md
```

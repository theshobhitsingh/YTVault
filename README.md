# 🎥 YouTube Manager CLI App

A simple and interactive **Command-Line Interface (CLI)** application built with Python to manage your favorite YouTube videos. This project allows users to **add, list, update, and delete** video entries with persistent storage using a JSON-formatted `.txt` file.

---

## 📁 Project Structure

```
youtube_manager/
│
├── youtube.txt         # JSON data file (stores video information)
├── youtube_manager.py  # Main CLI script
└── README.md           # Project documentation
```

---

## 🚀 Features

- 🔍 **List Videos**: View all your favorite YouTube videos with their durations.
- ➕ **Add Videos**: Save a new video entry with a name and duration.
- ✏️ **Update Videos**: Modify existing video information.
- 🗑️ **Delete Videos**: Remove a video entry from the list.
- 💾 **Persistent Storage**: Data is stored and loaded from `youtube.txt` using the `json` module.
- 💡 **User-Friendly Prompts**: Clear instructions and emojis for better usability.

---

## 🛠️ Technologies Used

- **Python 3.10+**
- `json` module for file handling and data persistence
- CLI-based interaction using built-in `input()` function
- `match-case` syntax for clean control flow (Python 3.10+)

---

## 🧠 How It Works

1. On start, it tries to load video data from `youtube.txt`.
2. Displays a menu where users can choose actions:
   - List
   - Add
   - Update
   - Delete
   - Exit
3. All actions are reflected immediately in the file for data persistence.

---

## 🖥️ How to Run

1. **Clone the repository** or download the script:
   ```bash
   git clone https://github.com/yourusername/youtube-manager-cli.git
   cd youtube-manager-cli
   ```

2. **Make sure you have Python 3.10+ installed**:
   ```bash
   python --version
   ```

3. **Run the program**:
   ```bash
   python youtube_manager.py
   ```

---

## 📦 Sample Data Format

Here is how your `youtube.txt` (data file) might look:

```json
[
    {
        "name": "Python Tutorial for Beginners",
        "time": "15:23"
    },
    {
        "name": "Understanding JSON in Python",
        "time": "10:45"
    }
]
```

---

## ✅ Future Improvements

- Add **search/filter** functionality by video name or duration.
- Implement **video tags or categories**.
- Add support for **YouTube URLs** and validation.
- Convert to a **GUI** app using `tkinter` or `PyQt`.
- Export data to CSV or PDF.

---

## 👤 Author

**Shobhit Singh**  

---

## 🙏 Acknowledgements

- Python Docs – for reference
- YouTube – for all the great content we bookmark daily ❤️

---

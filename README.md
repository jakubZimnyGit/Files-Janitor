# Files-Janitor 🧹

A professional, real-time file organization tool built with Python. It monitors a specified directory (like your Downloads folder) and automatically categorizes incoming files into organized subfolders based on their extensions.

## 🌟 Key Features
* **Event-Driven Monitoring:** Uses the `watchdog` library for high-performance, real-time file detection.
* **Smart Categorization:** Automatically sorts files into logical groups (Images, Docs, Archives, etc.).
* **Robust Error Handling:** Features safe file moving with `pathlib`, automatic directory creation, and permission check-ups.
* **Modular Architecture:** Built using **Object-Oriented Programming (OOP)** principles for easy scalability and maintenance.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Core Libraries:** `watchdog`, `pathlib`, `time`
* **Design Pattern:** Observer Pattern

## 📁 Project Structure
- `main.py`: Entry point for the application. Contains configuration and starts the observer.
- `watcher.py`: Defines the `FolderWatcher` class responsible for monitoring the filesystem.
- `handler.py`: Defines the `FileMoveHandler` class containing the logic for processing and moving files.

## 🚀 Getting Started

1. **Clone the repository:**
git clone https://github.com/jakubZimnyGit/Files-Janitor.git

2. **Install dependencies:**
pip install watchdog

3. **Usage:**
- Open main.py and set your WATCH_PATH (e.g., C:\Users\YourName\Downloads).
- Run the script:
python main.py

## 🔮 Future Roadmap
- [ ] Add a JSON configuration file for custom extension mapping.
- [ ] Implement logging to a file for background execution tracking.
- [ ] Add a simple GUI (Tkinter/PyQt) for easier setup.

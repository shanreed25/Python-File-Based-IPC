# File-Based IPC Demonstration

*A simple demonstration of **file-based Inter-Process Communication (IPC)** using a shared JSON file.*

#### Uses
- Python 3.6 or higher
- only Python standard library

## 🎯 Key Concepts Demonstrated
- **Shared State** both processes access the same `ipc_state.json` file as their communication channel
- **Polling** the reader checks the file every 0.5 seconds for updates (see `sleep(0.5)` in reader.py).
- **JSON Serialization** data is stored in human-readable JSON format, making it easy to debug
- **Atomic Updates** the writer reads the current state before updating to avoid overwriting data

### How it works
- **Shared State File:** `ipc_state.json`
- processes communicate by reading and writing to this shared file
- **Reader** `reader.py`:
    - continuously reads the JSON file in a loop
    - updates the display based on the file contents
- **Writer** `writer.py`:
    - writes updates to the JSON file when user issues commands
    - the reader picks up the changes on the next read of the JSON file
- [More About How The Code Works](../Notebooks/FileBasedIPCDemoCode.ipynb)

## 📝 Usage Instructions
### Step 1: Start the Reader
- Open a terminal and run: `python reader.py`
### Step 2: Start the Writer
- Open a **second terminal** (keep the reader running) and run: `python writer.py`
### Step 3: Send Messages
- In the writer terminal
### Step 4: Watch the Reader Update

![ipc demo image](ipc_demo_image.png)
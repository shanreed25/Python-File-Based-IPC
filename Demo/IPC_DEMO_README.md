# File-Based IPC Demonstration

*A simple demonstration of **file-based Inter-Process Communication (IPC)** using a shared JSON file.*

#### Uses
- Python 3.6 or higher
- only Python standard library

## Files
### 1. Shared Json File **`ipc_state.json`**
- processes communicate by reading and writing to this shared file

### 2. Reader File: **`reader.py`** 
- will continuously monitors `ipc_state.json`
- will display the state of `ipc_state.json`

### 3. Writer File **`writer.py`**
- will send messages and commands to update the shared state(`ipc_state.json`)
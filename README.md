# 📄 File Based Interprocess Communication (IPC) 

## 📖 What is File-Based IPC?
**File-based IPC is a method where two or more processes communicate by reading and writing to a shared file. One process writes data to the file, and another process reads it to receive updates.**

### Pros
- Simple to implement
- No socket/network setup needed
- Human-readable state (can manually edit JSON)

### Cons
- Not real-time (polling delay)
- File I/O overhead
- Potential race conditions if both processes write simultaneously
- Not suitable for high-frequency updates
 
- [File Based IPC Demo](./Demo/IPC_DEMO_README.md)
- [More about IPC](./Notebooks/InterprocessCommunication.ipynb)

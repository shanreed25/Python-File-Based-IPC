# Interprocess Communication (IPC) 
**A lightweight IPC method suitable for simple CLI applications where sub-second latency is acceptable It uses file-based IPC (Inter-Process Communication) via a shared JSON file (interface_state.json)**


### How it works
- **Shared State File:** Both processes read/write to `interface_state.json`
- **Interface Server** `interface_server.py`:
    - continuously reads the JSON file in a loop (every 0.25 seconds)
    - updates the display based on the file contents
- **Command Client** `command_client.py`:
    - writes updates to the JSON file when user issues commands
    - the server picks up changes on the next read


### Pros
- Simple to implement
- No socket/network setup needed
- Human-readable state (can manually edit JSON)

### Cons
- Not real-time (polling delay)
- File I/O overhead
- Potential race conditions if both processes write simultaneously
- Not suitable for high-frequency updates
 

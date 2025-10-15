# Asyncio and Thread Exercise

This repository contains an exercise to process a large file concurrently. The task is to **read a large file, modify each line, and save the result into a new file** using different concurrency techniques in Python.  

There are **five implementations**, each demonstrating a different approach to concurrency:

### 1. `without_thread_or_asyncio.py`  
- **Description:** No threading or asyncio used.  
- **Approach:** Sequential processing of file lines.  

### 2. `asyncio_.py`  
- **Description:** Uses only **asyncio**.  
- **Approach:** Processes lines asynchronously with coroutines.  

### 3. `asyncio_queue.py`  
- **Description:** Uses **asyncio** along with **`asyncio.Queue()`**.  
- **Approach:** Implements producer-consumer pattern for asynchronous line processing.  

### 4. `thread_queue_event.py`  
- **Description:** Uses **`concurrent.futures.ThreadPoolExecutor`**, **`queue.Queue()`**, and **`threading.Event()`**.  
- **Approach:** Implements a multi-threaded producer-consumer pattern with proper synchronization.  

### 5. `asyncio_thread.py`  
- **Description:** Combines **asyncio**, **`ThreadPoolExecutor`**, **`queue.Queue()`**, and **`threading.Event()`**.  
- **Approach:** Hybrid approach using both asyncio and threads for concurrent processing.  





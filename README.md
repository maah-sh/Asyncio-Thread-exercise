# Asyncio and Thread Exercise

This repository contains an exercise to process a large file concurrently. The task is to **read a large file, modify each line, and save the result into a new file** using different concurrency techniques in Python.  

There are five implementations, each demonstrating a different approach to concurrency:

### 1. `without_thread_or_asyncio.py`  
- No threading or asyncio used.  
- Sequential processing of file lines.  

### 2. `asyncio_.py`  
- Uses only **asyncio**.  
- Processes lines asynchronously with coroutines.  

### 3. `asyncio_queue.py`  
- Uses **asyncio** along with **`asyncio.Queue()`**.  
- Implements producer-consumer pattern for asynchronous line processing.  

### 4. `thread_queue_event.py`  
- Uses **`concurrent.futures.ThreadPoolExecutor`**, **`queue.Queue()`**, and **`threading.Event()`**.  
- Implements a multi-threaded producer-consumer pattern with proper synchronization.  

### 5. `asyncio_thread.py`  
- Combines **asyncio**, **`ThreadPoolExecutor`**, **`queue.Queue()`**, and **`threading.Event()`**.  
- Hybrid approach using both asyncio and threads for concurrent processing.  





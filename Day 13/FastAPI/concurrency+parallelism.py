# Concurrency and Parallelism in FastAPI are important concepts to understand when building high-performance web applications.
# Concurrency refers to the ability of a system to handle multiple tasks at the same time, while parallelism refers to the ability to execute multiple tasks simultaneously.
# FastAPI is designed to be asynchronous and can handle multiple requests concurrently using async functions and the async/await syntax in Python. This allows FastAPI to efficiently manage I/O-bound tasks, such as database queries or external API calls, without blocking the main thread of execution
# However, for CPU-bound tasks that require intensive computation, FastAPI can leverage parallelism by using multiprocessing or threading to execute tasks in parallel across multiple CPU cores.
# It's important to choose the right approach based on the nature of the tasks being performed, as concurrency is more suitable for I/O-bound tasks, while parallelism is more effective for CPU-bound tasks. FastAPI provides tools and features to help developers implement both concurrency and parallelism in their applications, allowing for efficient handling of a wide range of workloads.

import asyncio
import time

async def fake_io_task(task_id: int, delay: float):
    await asyncio.sleep(delay)  # Simulate an I/O-bound task with a delay
    print(f"Task {task_id} completed after {delay} seconds")

async def main():
    tasks = [
        fake_io_task(1, 2),
        fake_io_task(2, 1),
        fake_io_task(3, 3)
    ]
    await asyncio.gather(*tasks)  # Run tasks concurrently

asyncio.run(main()) # All of these tasks finish in the order of their delay and start at the same time, demonstrating concurrency.

def cpu_bound_task(task_id: int, n: int):
    count = 0
    for i in range(n):
        count += i * 1000  # Simulate a CPU-bound task
    print(f"CPU-bound Task {task_id} completed with count {count}")

from concurrent.futures import ProcessPoolExecutor

def main_parallel():
    with ProcessPoolExecutor() as executor:
        tasks = [
            executor.submit(cpu_bound_task, 1, 10**6),
            executor.submit(cpu_bound_task, 2, 10**6),
            executor.submit(cpu_bound_task, 3, 10**6)
        ]
        for task in tasks:
            task.result()  # Wait for all tasks to complete

if __name__ == "__main__":
    main_parallel() # All of these tasks run in parallel across multiple CPU cores, demonstrating parallelism. Notice that the output comes all at once after all tasks are completed, rather than in the order they were started.
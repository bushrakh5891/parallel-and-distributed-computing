import asyncio
import sys

async def first_coroutine(future, num):
    count = 0
    for i in range(1, num + 1):
        count += i
    await asyncio.sleep(1)
    future.set_result('First coroutine (sum of N integers) result = %s' % count)

async def second_coroutine(future, num):
    count = 1
    for i in range(2, num + 1):
        count *= i
    await asyncio.sleep(2)
    future.set_result('Second coroutine (factorial) result = %s' % count)
    
def got_result(future):
    print(future.result())

if __name__ == "__main__":
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    
    # Use asyncio.run() to start the event loop
    async def main():
        future1 = asyncio.Future()
        future2 = asyncio.Future()

        # Convert coroutines to tasks
        task1 = asyncio.create_task(first_coroutine(future1, num1))
        task2 = asyncio.create_task(second_coroutine(future2, num2))
        
        future1.add_done_callback(got_result)
        future2.add_done_callback(got_result)
        
        await asyncio.gather(task1, task2)

    # Run the main async function
    asyncio.run(main())
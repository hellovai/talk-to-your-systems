import time
import functools
from typing import TypeVar, Callable, Any, Tuple, Optional
from contextlib import contextmanager

T = TypeVar('T')

def time_execution(func: Callable[..., T]) -> Callable[..., Tuple[T, float]]:
    """
    A decorator that measures the execution time of a function in milliseconds.
    
    Args:
        func: The function to be timed
        
    Returns:
        A tuple containing:
        - The result of the function execution
        - The execution time in milliseconds
        
    Example:
        @time_execution
        def my_function(x):
            return x * 2
            
        result, execution_time = my_function(5)
        print(f"Result: {result}, Time: {execution_time}ms")
    """
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Tuple[T, float]:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
        return result, execution_time
    return wrapper

@contextmanager
def timer(description: Optional[str] = None):
    """
    A context manager for timing code blocks in milliseconds.
    
    Args:
        description: Optional description of the code being timed
        
    Example:
        with timer("Data processing"):
            # Your code here
            data = process_large_dataset()
        
        # Or without description
        with timer():
            # Your code here
            result = complex_calculation()
    """
    start_time = time.perf_counter()
    yield
    end_time = time.perf_counter()
    execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
    
    if description:
        print(f"{description} took {execution_time:.2f}ms")
    else:
        print(f"Execution took {execution_time:.2f}ms")

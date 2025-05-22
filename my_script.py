import redis
import sys
import time

def test_redis_connection():
    max_retries = 3
    retry_delay = 1
    
    for i in range(max_retries):
        try:
            print(f"Attempt #{i+1}: Connecting to Redis...", file=sys.stderr)
            cache = redis.Redis(
                host='localhost',
                port=6379,
                db=0,
                socket_connect_timeout=5,
                socket_timeout=5
            )
            
            # Test connection
            if not cache.ping():
                raise redis.ConnectionError("Redis ping failed")
                
            print("Successfully connected to Redis!", file=sys.stderr)
            return cache
            
        except redis.ConnectionError as e:
            print(f"Connection failed: {str(e)}", file=sys.stderr)
            if i < max_retries - 1:
                print(f"Retrying in {retry_delay} seconds...", file=sys.stderr)
                time.sleep(retry_delay)
            else:
                print("Max retries reached. Could not connect to Redis.", file=sys.stderr)
                raise

try:
    cache = test_redis_connection()
    
    def cache_result(task_id, result):
        print(f"Caching result for task {task_id}", file=sys.stderr)
        try:
            return cache.set(task_id, result)
        except redis.RedisError as e:
            print(f"Cache set error: {str(e)}", file=sys.stderr)
            raise
            
    def get_cached_result(task_id):
        try:
            result = cache.get(task_id)
            print(f"Retrieved from cache for task {task_id}: {result}", file=sys.stderr)
            return result
        except redis.RedisError as e:
            print(f"Cache get error: {str(e)}", file=sys.stderr)
            raise

    # Example Usage
    print("\nRunning example usage...", file=sys.stderr)
    cache_result("task_1", "Processed at Edge")
    result = get_cached_result("task_1")
    print(f"\nFinal output: {result}", file=sys.stderr)
    
except Exception as e:
    print(f"Fatal error: {str(e)}", file=sys.stderr)
    print("\nTroubleshooting tips:", file=sys.stderr)
    print("1. Make sure Redis server is running", file=sys.stderr)
    print("2. Check Windows Firewall allows connections on port 6379", file=sys.stderr)
    print("3. Verify Redis configuration in redis.windows.conf", file=sys.stderr)
    sys.exit(1)

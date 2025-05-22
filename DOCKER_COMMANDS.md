# Edge Scheduler Docker Commands

## 1. Build the Docker Image
```bash
docker build -t edge-scheduler -f Dockerfile_v2 .
```
- Uses Python 3.9.18 slim image
- Creates non-root user for security
- Installs dependencies from requirements.txt
 docker run -it --rm edge-scheduler
 -runs 

## 2. Run in Development Mode
```bash
docker run -it --rm \
  -v "$(pwd)":/app \
  -p 8000:8000 \
  edge-scheduler
```
- `-v`: Mounts current directory for live code changes
- `-p`: Exposes port 8000 for health checks

## 3. Run in Production Mode
```bash
docker run -d \
  --name edge-scheduler \
  --restart unless-stopped \
  -p 8000:8000 \
  -e PYTHONUNBUFFERED=1 \
  edge-scheduler
```
- `-d`: Runs in detached mode
- `--restart`: Auto-recovery policy
- `-e`: Ensures real-time logging

## 4. Monitoring Commands
```bash
# View logs
docker logs -f edge-scheduler

# Check health status
docker inspect --format='{{json .State.Health}}' edge-scheduler

# View resource usage
docker stats edge-scheduler
```

## 5. Maintenance Commands
```bash
# Stop container
docker stop edge-scheduler

# Remove container
docker rm edge-scheduler

# Remove image
docker rmi edge-scheduler

# Full cleanup
docker system prune -a
```

## Sample Output
```
Starting AI scheduler...
Health check endpoint: http://0.0.0.0:8000/health
Decision latency: 89ms
Current mode: DQN (ε=0.15)

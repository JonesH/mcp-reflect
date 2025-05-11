FROM python:3.11-slim

WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8000 \
    HOST=0.0.0.0

# Install Poetry
RUN pip install --no-cache-dir poetry==1.7.1

# Copy only the files needed for installation
COPY pyproject.toml poetry.lock* README.md ./

# Configure poetry to not use a virtual environment
RUN poetry config virtualenvs.create false

# Install only runtime dependencies
RUN poetry install --no-dev --no-interaction --no-ansi

# Copy the package files
COPY mcp_reflect/ ./mcp_reflect/

# Expose the port
EXPOSE 8000

# Run the UVX server
CMD ["python", "-m", "mcp_reflect.server", "uvx"]
- `docker buildx create --use`
- `docker buildx inspect --bootstrap`
- `docker buildx build --platform linux/arm64 -t test-uv-numpy-arm .`

- `docker run --rm test-uv-numpy-arm`

# build image
docker build -t titanic-api:latest # --build-args PIP_EXTRA_INDEX_URL=https://.....com

# run container
docker run -p 8001:8001 -e PORT=8001 titanic-api
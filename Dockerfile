FROM python:3-alpine

# Unbuffered output, otherwise output appears with great delay
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY . .

ARG MIN_LON=10.011636032586688
ARG MAX_LON=12.223993889052613
ARG MIN_LAT=48.70792025947608
ARG MAX_LAT=50.25793688217101
ARG BBOX=${MIN_LON},${MIN_LAT},${MAX_LON},${MAX_LAT}
RUN python ./download_dem_zip.py "${BBOX}" \
    && python ./extract_tif_and_credits.py \
    && mkdir -p /data \
    && mv ./dem/*/*.tif /data \
    && mv ./dem/credits.json /data \
    && rm -r ./zip ./dem

# /data contains multiple *.tif files and credits.json \

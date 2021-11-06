FROM rustembedded/cross:s390x-unknown-linux-gnu-0.2.1

RUN dpkg --add-architecture s390x && \
    apt-get update && \
    apt-get install --assume-yes libasound2-dev:s390x

ENV PKG_CONFIG_PATH=/usr/lib/s390x-linux-gnu/pkgconfig/
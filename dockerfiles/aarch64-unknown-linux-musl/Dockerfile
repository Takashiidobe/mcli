FROM rustembedded/cross:aarch64-unknown-linux-musl-0.2.1

RUN dpkg --add-architecture arm64 && \
    apt-get update && \
    apt-get install --assume-yes musl-dev libasound2-dev:arm64

ENV PKG_CONFIG_PATH=/usr/lib/arm64-linux-gnu/pkgconfig/

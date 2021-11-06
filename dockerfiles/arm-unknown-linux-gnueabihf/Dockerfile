FROM rustembedded/cross:arm-unknown-linux-gnueabihf-0.2.1

RUN dpkg --add-architecture armhf && \
    apt-get update && \
    apt-get install --assume-yes libasound2-dev:armhf

ENV PKG_CONFIG_PATH=/usr/lib/arm-linux-gnueabihf/pkgconfig/

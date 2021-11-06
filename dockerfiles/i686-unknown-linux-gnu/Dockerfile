FROM rustembedded/cross:i686-unknown-linux-gnu-0.2.1

RUN dpkg --add-architecture i386 && \
    apt-get update && \
    apt-get install --assume-yes libasound2-dev:i386

ENV PKG_CONFIG_PATH=/usr/lib/i386-linux-gnu/pkgconfig/

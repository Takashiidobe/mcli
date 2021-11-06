FROM rustembedded/cross:powerpc64le-unknown-linux-gnu-0.2.1

RUN dpkg --add-architecture ppc64el && \
  apt-get update && \
  apt-get install --assume-yes libasound2-dev:ppc64el

ENV PKG_CONFIG_PATH=/usr/lib/ppc64el-linux-gnu/pkgconfig/

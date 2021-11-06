#!/usr/bin/env python3

from subprocess import run
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--ubuntu_arch', help='Ubuntu Arch')
parser.add_argument('--rust_triplet', help='Rust Triplet')

args = parser.parse_args()

ubuntu_arch = args.ubuntu_arch
rust_triplet = args.rust_triplet

REPO_NAME = "mcli"
CROSS_VERSION = "0.2.1"
SYSTEM_DEPS = [
    "libasound2-dev"
]

# Ubuntu Archs
dpkg_arches = [
    "amd64",
    "arm64",
    "armhf",
    "i386",
    "ppc64el",
    "s390x",
]

if ubuntu_arch not in dpkg_arches:
    print(f"Provided Ubuntu architecture not in {' '.join(dpkg_arches)}. Try again.")
    exit(1)


rust_triplets = [
    "aarch64-unknown-linux-gnu", "i686-pc-windows-gnu", "i686-unknown-linux-gnu", "i686-pc-windows-msvc", "x86_64-apple-darwin", "x86_64-pc-windows-gnu", "x86_64-pc-windows-msvc", "x86_64-unknown-linux-gnu","aarch64-apple-darwin", "aarch64-pc-windows-msvc", "aarch64-unknown-linux-musl", "arm-unknown-linux-gnueabi", "arm-unknown-linux-gnueabihf", "armv7-unknown-linux-gnueabihf", "mips-unknown-linux-gnu", "mips64-unknown-linux-gnuabi64", "mips64el-unknown-linux-gnuabi64", "mipsel-unknown-linux-gnuabi", "powerpc-unknown-linux-gnu", "powerpc64-unknown-linux-gnu", "powerpc64le-unknown-linux-gnu", "riscv64gc-unknown-linux-gnu", "s390x-unknown-linux-gnu", "x86_64-unknown-freebsd", "x86_64-unknown-illumos", "arm-unknown-linux-musleabihf", "i686-unknown-linux-musl", "x86_64-unknown-linux-musl", "x86_64-unknown-netbsd", "aarch64-apple-ios", "aarch64-apple-ios-sim", "aarch64-fuchsia", "aarch64-linux-android", "aarch64-unknown-none-softfloat", "aarch64-unknown-none", "arm-linux-androideabi", "arm-unknown-linux-musleabi", "arm-unknown-linux-musleabihf", "armebv7r-none-eabi", "armebv7r-none-eabihf", "armv5te-unknown-linux-gnueabi", "armv5te-unknown-linux-musleabi", "armv7-linux-androideabi", "armv7-unknown-linux-gnueabi", "armv7-unknown-linux-musleabi", "armv7-unknown-linux-musleabihf", "armv7a-none-eabi", "armv7r-none-eabi", "armv7r-none-eabihf", "armv5te-unknown-linux-gnueabi", "armv5te-unknown-linux-musleabi", "armv7-linux-androideabi", "armv7-unknown-linux-gnueabi", "armv7-unknown-linux-musleabi", "armv7-unknown-linux-musleabihf", "armv7a-none-eabi", "armv7a-none-eabihf", "asmjs-unknown-emscripten", "i586-pc-windows-msvc", "i586-unknown-linux-gnu", "i586-unknown-lini586-unknown-lini586-u86-linux-androi586-unknown-lini586-u86-unknown-frei586-unknown-lini586-u86-unknown-lini586-unknown-lini586-unknonknown-lini586-unknown-lini586-ups64-unknown-li586-unknown-lini586-ups64el-unknowni586-unknown-lini586-uptx64-nvidia-ci586-unknown-lini586-uscv32i-unknowni586-unknown-lini58", "riscv32imac-unknriscv32imac-unknriscv32cv32imc-unknoriscv32imac-unknriscv3scv64gc-unknown-none-elf", "riscv64imac-unknown-none-elf", "sparc64-unknown-linux-gnu", "sparcv9-sun-solaris", "thumbv6m-none-eabi", "thumbv7em-none-eabi", "thumbv7em-none-eabihf", "thumbv7m-none-eathumbv7m-none-eathumbv7m-none-eathnuthumbv7m-none-eathumbv7m-none-eathknthumbv7m-none-eaihf", "thumbv8m.base-none-eabi", "thumbv8m.main-nothumbv8m.main-nothumbv8m.main-nothnothumbv8m.main-nothumwasm32-unknown-ethumbv8m.main-nothumbv8m.main-noth-unknown", "wasm32-wasi", "wasm32-wasi", "wasm386_64-apple-ioswasm32-wasi", "wasm386_64-fortanix-unknown-sgx", "x86_64-fuchsia", "x86_64-linux-android", "x86_64-pc-solaris", "x86_64-unknown-linux-gnux32", "x86_64-unknown-redox", "aarch64-apple-ios-macabi", "aarch64-apple-tvos", "aarch64-unknown-freebsd", "aarch64-unknown-hermit", "aarch64-unknown-uefi", "aarch64-unknown-linux-gnu_ilp32", "aarch64-unknown-netbsd", "aarch64-unknown-openbsd", "aarch64-unknown-redox", "aarch64-uwp-windows-msvc", "aarch64-wrs-vxworks", "aarch64_be-unknown-linux-gnu_ilp32", "aarch64_be-unknown-linux-gnu", "armv4t-unknown-linux-gnueabi", "armv5te-unknown-linux-uclibceabi", "armv6-unknown-freebsd", "armv6-unknown-netbsd-eabihf", "armv7-apple-ios", "armv7-unknown-freebsd", "armv7-unknown-netbsd-eabihf", "armv7-wrs-vxworks-eabihf", "armv7a-none-eabihf", "armv7s-apple-ios", "avr-unknown-gnu-atmega328", "bpfeb-unknown-none", "bpfel-unknown-none", "hexagon-unknown-linux-musl", "i386-apple-ios", "i686-apple-darwin", "i686-pc-windows-msvc", "i686-unknown-haiku", "i686-unknown-netbsd", "i686-unknown-openbsd", "i686-unknown-uefi", "i686-uwp-windows-gnu", "i686-uwp-windows-gnu", "ndows-msvc", "i686-uwp-windows-gnu", "orks", "i686-uwp-windows-gnu", "wn-linux-uclibci686-uwp-windows-gnu", "y-psp", "i686-uwp-windows-gnu", "nown-linux-uclii686-uwp-windows-gnunknown-none", "i686-uwp-windows-gnu", "6-unknown-linux-gnu", "mipsisa32r6el-unknown-linux-gnu", "mipsisa64r6-unknown-linux-gnuabi64", "mipsisa64r6el-unknown-linux-gnuabi64", "msp430-none-elf", "powerpc-unknown-linux-gnuspe", "powerpc-unknown-linux-musl", "powerpc-unknown-netbsd", "powerpc-unknown-openbsd", "powerpc-unknown-openwrs-vxworks-spe", "powerpc-wrs-vxworks", "powerpc64-unknown-freebsd", "powerpc64le-unknown-freebpowerpc64le-unknown-freebpowerpc6sd", "powerpc64le-unknown-freebpown-linux-mpowerpc64le-unknown-freeb-vxworks", "powerpc64le-unknown-fle-unknown-linuxpowerpc64le-unknown-frenknown-linux-gpowerpc64le-unknown-freebpowerpc64l-mpowerpc64le-unknown-freebpowerpc6", "powerpc64le-unknown-freebpowerpc64l-mpowerpc64le-unknown-frown-linux-musl", "sparc-unknown-linux-gnu", "sparc64-unknown-netbsd", "sparc64-unknown-openbsd", "thumbv4t-none-eabi", "thumbv7a-pc-windows-msvc", "thumbv7a-uwp-windows-msvc", "thumbv7neon-unknown-linuxthumbv7neon-unknown-linown-unknown", "thumbv7neon-unknown-linuxthu-macabi", "thumbv7neon-unknown-line-tvos", "thumbv7neon-unknown-liwindows-msvc", "thumbv7neon-unknown-ln-solaris", "thumbv7neon-unknown-linown-dragonfly", "thumbv7neon-unknow-unknown-haiku", "thumbv7neon-unknown-linuxthumbv7neon-unknown-linown-unknownnown-l4re-uclibthumbv7neon-unknownunknown-none-hermithumbv7neon-unknown-linuxthumbv7neouxkernel", "x86_64-unknown-openbsd", "x86_64-unknown-uefi", "x86_64-uwp-windows-gnu", "x86_64-uwp-windows-msvc", "x86_64-wrs-vxworks"
]

if rust_triplet not in rust_triplets:
    print(f"Provided rust triplet not a valid rust triplet. Try again.")
    exit(1)


linux_dockerfile = f"""FROM rustembedded/cross:{rust_triplet}-{CROSS_VERSION}

RUN dpkg --add-architecture {ubuntu_arch} && \\
    apt-get update && \\
    apt-get install --assume-yes {SYSTEM_DEPS[0]}:{ubuntu_arch}

ENV PKG_CONFIG_PATH=/usr/lib/{ubuntu_arch}-linux-gnu/pkgconfig/"""

cross_file = f"""
[target.{rust_triplet}]
image = "takashiidobe/{REPO_NAME}-{rust_triplet}-{CROSS_VERSION}"
"""

run(['mkdir', '-p', f'dockerfiles/{rust_triplet}'])

with open("Cross.toml", "a+") as f:
    f.write(cross_file)

with open(f"dockerfiles/{rust_triplet}/Dockerfile", "w+") as f:
    f.write(linux_dockerfile)

run(["docker", "build", "-t", f"takashiidobe/mcli-{rust_triplet}-{CROSS_VERSION}", f"dockerfiles/{rust_triplet}/"])

run(["docker", "push", f"takashiidobe/mcli-{rust_triplet}-{CROSS_VERSION}"])

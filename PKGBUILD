pkgname=newm-next-git-qs
pkgver=0.4.4
pkgrel=1
license=('MIT')
pkgdesc="newm-next Wayland compositor"
arch=('x86_64')
depends=(
    python
    wayland
    libinput
    libxcb
    libxkbcommon
    opengl-driver
    pixman
    xcb-util-errors
    xcb-util-renderutil
    xcb-util-wm
    seatd
    xorg-xwayland
    brightnessctl
    python-evdev
    python-numpy
    python-imageio
    python-cairo
    python-psutil
    python-pam
    python-pyfiglet
    python-thefuzz
    python-dasbus
)
makedepends=(
    git
    meson
    ninja
    wayland-protocols
    xorgproto
)
source=('git+https://github.com/SEKAMISehi/newm-next.git#branch=new_maker')
sha512sums=('SKIP')
provides=('newm')
conflicts=('newm' 'newm-git' 'newm-next-git' 'newm-atha-git')

build() {
    cd "$srcdir/newm-next"
    make
}

package() {
    cd "$srcdir/newm-next"
    cp -r make/usr "$pkgdir/"
}

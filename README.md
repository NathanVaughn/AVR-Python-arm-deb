# AVR-Python-arm-deb

Because Nvidia continues to ship operating system images based on Ubuntu 18.04,
we need to install a newer version of Python. However, the
[deadsnakes ppa](https://launchpad.net/~deadsnakes/+archive/ubuntu/ppa)
has [stopped hosting packages](https://github.com/deadsnakes/issues/issues/251)
for EOL-ed versions of Ubuntu (which includes 18.04).

Unfortunately I didn't manage to save the `.deb` files required before the packages
were yanked, so this is a script with a terrible workaround of rebundling and exporting
the `.deb` files from a container image we shipped while the packages were still
available.

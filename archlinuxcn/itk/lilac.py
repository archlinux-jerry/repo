#!/usr/bin/env python3

from lilaclib import *


def pre_build():
    update_pkgrel()


def post_build():
    git_pkgbuild_commit()
# vim:set ts=2 sw=2 et:


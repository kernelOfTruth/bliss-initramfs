# Copyright 2012-2014 Jonathan Vasquez <jvasquez1011@gmail.com>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pkg.hooks.hook import Hook

class ZFS(Hook):
    def __init__(self):
        Hook.__init__(self)

        # Required Files
        self.files = [
            "/sbin/mount.zfs",
            "/sbin/zdb",
            "/sbin/zfs",
            "/sbin/zpool",
        ]

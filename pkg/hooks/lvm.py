"""
Copyright 2012-2014 Jonathan Vasquez <jvasquez1011@gmail.com>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at:

	http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import os

class LVM(object):
	# Enable/Disable Hook
	use = "0"

	# Required Files
	files = [

	]

	# Add the static lvm to the files list if it exists,
	# otherwise add the dynamically-linked lvm if it exists
	if os.path.exists("/sbin/lvm.static"):
		files.append("/sbin/lvm.static")
	elif os.path.exists("/sbin/lvm"):
		files.append("/sbin/lvm")

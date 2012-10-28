# Copyright 2012 django-compresshtml authors. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

dependencies: django

clean:
	@find . -name "*.pyc" -delete

django:
	@python -c 'import django' 2>/dev/null || pip install django
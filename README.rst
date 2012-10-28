++++++++++++++
django-compresshtml
++++++++++++++


HTML compressor for django

Why minify HTML code?
=====================

One of important points on client side optimization is compress HTML, with compressed HTML code, you reduce the size of data transferred from your server to your client, and your pages load faster.

Installing
==========

For install django-compresshtml, run on terminal: ::

    $ [sudo] pip install django-compresshtml

Using the midleware
===================

All you need to do is add ``compresshtml.middleware.CompressHtmlMiddleware`` to your ``MIDDLEWARE_CLASSES`` and enable the ``COMPRESS_HTML`` setting: ::

    MIDDLEWARE_CLASSES = (
        # other middleware classes
        'compresshtml.middleware.HCompressHtmlMiddleware',
    )

    COMPRESS_HTML = True

This middleware should be placed before any other middleware that need to read or write the response body so that compression happens afterward.

The default value for the ``COMPRESS_HTML`` setting is ``not DEBUG``. You only need to set it to ``True`` if you want to minify your HTML code when ``DEBUG`` is enabled.

Keeping comments
----------------

The default behaviour of the middleware is remove all comments but conditional comments from HTML. If you want to keep your comments, set the setting ``KEEP_COMMENTS_ON_COMPRESSING`` to ``True``: ::

    KEEP_COMMENTS_ON_COMPRESSING = True

Using the decorator
===================

django-compresshtml also provides a decorator, that you can use only on views you want to minify the response: ::

    from compresshtml.decorators import compressed_response

    @compressed_response
    def home(request):
        return render_to_response('home.html')

development
===========

* Source hosted at `GitHub <https://github.com/kamagatos/django-compresshtml>`_
* Report issues on `GitHub Issues <https://github.com/kamagatos/django-compresshtml/issues>`_

Pull requests are very welcomed!

running the tests
-----------------

community
=========

Changelog
=========

0.1
-----

* Initial commit

LICENSE
=======

Unless otherwise noted, the django-compresshtml source files are distributed under the BSD-style license found in the LICENSE file.

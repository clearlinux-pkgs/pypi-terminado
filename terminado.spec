#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : terminado
Version  : 0.8.3
Release  : 27
URL      : https://files.pythonhosted.org/packages/13/5b/57e995382718d176aba6168632bd15cf5371a7b1205c83a7e4aae0bc6c2e/terminado-0.8.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/13/5b/57e995382718d176aba6168632bd15cf5371a7b1205c83a7e4aae0bc6c2e/terminado-0.8.3.tar.gz
Summary  : Terminals served to xterm.js using Tornado websockets
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause
Requires: terminado-license = %{version}-%{release}
Requires: terminado-python = %{version}-%{release}
Requires: terminado-python3 = %{version}-%{release}
Requires: XStatic
Requires: XStatic-term.js
Requires: terminado
Requires: tornado
BuildRequires : XStatic
BuildRequires : XStatic-term.js
BuildRequires : buildreq-distutils3
BuildRequires : terminado
BuildRequires : tornado

%description
This is a `Tornado <http://tornadoweb.org/>`_ websocket backend for the
`Xterm.js <https://xtermjs.org/>`_ Javascript terminal emulator
library.

It evolved out of `pyxterm <https://github.com/mitotic/pyxterm>`_, which was
part of `GraphTerm <https://github.com/mitotic/graphterm>`_ (as lineterm.py),
v0.57.0 (2014-07-18), and ultimately derived from the public-domain `Ajaxterm
<http://antony.lesuisse.org/software/ajaxterm/>`_ code, v0.11 (2008-11-13) (also
on Github as part of `QWeb <https://github.com/antonylesuisse/qweb>`_).

Modules:

* ``terminado.management``: controls launching virtual terminals,
  connecting them to Tornado's event loop, and closing them down.
* ``terminado.websocket``: Provides a websocket handler for communicating with
  a terminal.
* ``terminado.uimodule``: Provides a ``Terminal`` Tornado `UI Module
  <http://www.tornadoweb.org/en/stable/guide/templates.html#ui-modules>`_.

JS:

* ``terminado/_static/terminado.js``: A lightweight wrapper to set up a
  term.js terminal with a websocket.

Usage example:

.. code:: python

    import os.path
    import tornado.web
    import tornado.ioloop
    # This demo requires tornado_xstatic and XStatic-term.js
    import tornado_xstatic

    import terminado
    STATIC_DIR = os.path.join(os.path.dirname(terminado.__file__), "_static")

    class TerminalPageHandler(tornado.web.RequestHandler):
        def get(self):
            return self.render("termpage.html", static=self.static_url,
                               xstatic=self.application.settings['xstatic_url'],
                               ws_url_path="/websocket")

    if __name__ == '__main__':
        term_manager = terminado.SingleTermManager(shell_command=['bash'])
        handlers = [
                    (r"/websocket", terminado.TermSocket,
                         {'term_manager': term_manager}),
                    (r"/", TerminalPageHandler),
                    (r"/xstatic/(.*)", tornado_xstatic.XStaticFileHandler,
                         {'allowed_modules': ['termjs']})
                   ]
        app = tornado.web.Application(handlers, static_path=STATIC_DIR,
                          xstatic_url = tornado_xstatic.url_maker('/xstatic/'))
        # Serve at http://localhost:8765/ N.B. Leaving out 'localhost' here will
        # work, but it will listen on the public network interface as well.
        # Given what terminado does, that would be rather a security hole.
        app.listen(8765, 'localhost')
        try:
            tornado.ioloop.IOLoop.instance().start()
        finally:
            term_manager.shutdown()

See the `demos directory <https://github.com/takluyver/terminado/tree/master/demos>`_
for more examples. This is a simplified version of the ``single.py`` demo.

Run the unit tests with:

    $ nosetests

%package license
Summary: license components for the terminado package.
Group: Default

%description license
license components for the terminado package.


%package python
Summary: python components for the terminado package.
Group: Default
Requires: terminado-python3 = %{version}-%{release}

%description python
python components for the terminado package.


%package python3
Summary: python3 components for the terminado package.
Group: Default
Requires: python3-core
Provides: pypi(terminado)

%description python3
python3 components for the terminado package.


%prep
%setup -q -n terminado-0.8.3
cd %{_builddir}/terminado-0.8.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582912370
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/terminado
cp %{_builddir}/terminado-0.8.3/LICENSE %{buildroot}/usr/share/package-licenses/terminado/c469161e7fddd1ac349b03fa2732d18e96c579d2
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/terminado/c469161e7fddd1ac349b03fa2732d18e96c579d2

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

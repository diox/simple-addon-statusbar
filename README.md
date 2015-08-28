'M' in Status Bar
=================

This is a simple add-on for FxOS, in the Web Extensions format, that adds a 'M'
to your statusbar. Nothing else.

Installing
==========

* Run `zip -r * /tmp/simple-addon-statusbar-0.1.zip` from this directory.
* Copy `update.webapp` and `/tmp/simple-addon-statusbar-0.1.zip` to your
  webserver
* Debug the system app in WebIDE and run `navigator.mozApps.installPackage('http://<path>/simple-addon-statusbar.webapp')`,
  replacing <path> by your server name and path to where you copied the files.
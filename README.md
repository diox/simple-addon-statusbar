'{letter}' in Status Bar
========================

This is a generator that creates 26 variants of a simple add-on for FxOS,
in the [WebExtensions](https://wiki.mozilla.org/Browser_Extensions) format,
that adds a colored letter to your statusbar. Nothing else.

Each add-on has its own letter, its own color, and its own corresponding icon.

Installing
==========

Note: you can skip this part and just take the prebuilt add-ons in the `dist`
directory instead.

* Install Python Imaging Library
* Build all 26 variants by launching `python build.py` from this directory.

Submitting
==========

* Submit any of the zip files it created in the `dist` directory to the
  [Firefox Marketplace](https://marketplace.firefox.com/content/addon/submit/).
* Done!

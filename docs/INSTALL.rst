wcc.registration Installation
-----------------------------

To install wcc.registration using zc.buildout and the plone.recipe.zope2instance
recipe to manage your project, you can do this:

* Add ``wcc.registration`` to the list of eggs to install, e.g.:

    [buildout]
    ...
    eggs =
        ...
        wcc.registration

* Re-run buildout, e.g. with:

    $ ./bin/buildout


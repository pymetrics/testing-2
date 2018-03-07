:skip-help: true

.. title: Introduction to Testing

:data-transition-duration: 500

----

:data-x: 0
:data-y: 0


This is the first slide
=======================

Here comes some text.

----

:data-x: r600
:data-y: r900

This is the second slide
========================

#. Here we have

#. A numbered list

#. It will get correct

#. Numbers automatically

----



This slide has some code
========================

.. code-block:: python

    from django.test import TestCase
    from myapp.models import Animal

    class AnimalTestCase(TestCase):
        def setUp(self):
            Animal.objects.create(name="lion", sound="roar")
            Animal.objects.create(name="cat", sound="meow")

        def test_animals_can_speak(self):
            """Animals that can speak are correctly identified"""
            lion = Animal.objects.get(name="lion")
            cat = Animal.objects.get(name="cat")
            self.assertEqual(cat.speak(), 'The cat says "meow"')

        def test_something_else(self):
            self.assertTrue("e=mc**2")

        def test_exception(self):
            with self.raises(IOError):
                open('nofile.example')

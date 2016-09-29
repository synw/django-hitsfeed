Django Hitsfeed
===============

Real time hits monitoring for Django. Define a custom url tree and monitor the hits from these urls.

Install
-------

Install [Django Instant](http://django-instant.readthedocs.io/en/latest/src/install.html) then:

  ```python
pip install django-mptt
pip install git+https://github.com/synw/django-hitsfeed.git
  ```

Installed apps:

  ```python
"mptt",
"hitsfeed",
  ```

Add ``'hitsfeed.middleware.HitsFeedMiddleware'`` to MIDDLEWARE_CLASSES in settings.

Required settings:

  ```python
SITE_SLUG = "mysite"
INSTANT_STAFF_CHANNELS = ['$mysite_staff']
  ```

Urls: ``url('^hits/', include('hitsfeed.urls')),``

Run the migrations.

Create a template ``templates/instant/extra_clients.js`` with this content:

  ```django
{% if request.path == "/hits/" %}
	{% include "instant/channels/staff/client.js" %}
{% endif %}
  ```
Create another template ``templates/instant/extra_handlers.js`` with this content:

  ```django
{% include "hitsfeed/js/handlers.js" %}
  ```

Usage
-----

Define an url tree in the admin and then go as staff to ``/hits/`` to monitor these urls. Only the staff can see this
page.

Screenshot
----------

![Dashboard screenshot](https://raw.githubusercontent.com/synw/django-hitsfeed/master/doc/img/screenshot.png)

Red is a current hit and green is a previous hit.

Todo
----

- Filtering options: users only, filter ajax, etc..
- Exclude paths
- Fix delayed js callbacks
- Maybe add some persistency layers
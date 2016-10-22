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

Urls:

  ```python
from instant.views import instant_auth

urlpatterns = [
	# ...
    url(r'^centrifuge/auth/$', instant_auth, name='instant-auth'),
    url('^instant/', include('instant.urls')),
    url('^hits/', include('hitsfeed.urls')),
    ]
  ```

Run the migrations.

Create a template ``templates/instant/extra_clients.js`` with this content:

  ```django
{% if request.path == "/hits/" %}
	{% if user.is_staff %}
		{% include "instant/channels/staff/client.js" %}
	{% endif %}
{% endif %}
  ```
Create another template ``templates/instant/extra_handlers.js`` with this content:

  ```django
{% if request.path == "/hits/" %}
	{% if user.is_staff %}
		{% include "hitsfeed/js/handlers.js" %}
	{% endif %}
{% endif %}
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
- Fix delayed js callbacks
- View permission options: superuser, staff, groups
- Multiple trees
- Separate lines for anonymous and registered users in the linechart
- Maybe add some optional persistency layers

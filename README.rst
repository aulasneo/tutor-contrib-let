LET plugin for `Tutor <https://docs.tutor.edly.io>`__
#####################################################

Tutor plugin to simplify the configuration of Open edX settings.

Tutor does an outstanding job simplifying the installation and setup of Open edX.
However, doing a deep customization of your platform goes beyond its scope.
This task can become overwhelming when you have to find out which setting serves for
the purpose you are looking for.

Depending on what do you want to change in Open edX you might have to modify different
files and take different actions. For example, to change the link to the support page
you have to set ``SUPPORT_SITE_LINK`` in the ``production.py`` file, then restart the LMS.
But to enable the marketing site you have to set the ``ENABLE_MKTG_SITE`` feature flag, which
is a key in the ``FEATURES`` setting. Or to change the URL of your privacy policy you have to
patch the MFE Dockerfile with a Tutor plugin and rebuild the MFE image. Additionally,
all changes done in the ``env`` directory are lost after the next ``tutor config save``, so you
have to write a tutor plugin to patch specific files just to make a simple change.

LET simplifies all these tasks by letting you modify the most common settings
in a single plugin, plus giving a better set of defaults for these values.

To set a variable just use the ``tutor let`` command, as we did in the old times
(those who grew up programming BASIC in home computers will know what I mean.)

For example, to disable email validation, do:

.. code-block::

    tutor let SKIP_EMAIL_VALIDATION=True

This will be translated to:

.. code-block::

    LET_SKIP_EMAIL_VALIDATION: True

in the ``config.yml`` file, and is equivalent to do:

.. code-block::

    tutor config save --set LET_SKIP_EMAIL_VALIDATION=True

or to manually add ``LET_SKIP_EMAIL_VALIDATION: True`` to the ``config.yml`` file.

To list all the available settings together with their value type, default value
and current value, type ``tutor list``.


Installation
************

To install LET, run:

.. code-block::

    pip install tutor-contrib-let
    tutor plugins enable let

Usage
*****

To configure a setting, run:

.. code-block::

    tutor let <setting name>=<setting value>

Some variables are of type ``dict``. To set them properly, enclose the
``KEY=VALUE`` pair in double quotes. Use curly braces to enclose the value
and leave a space after the colon.
Optionally, enclose the key and/or value in single quotes if needed. E.g.,

.. code-block::

    tutor let "MKTG_URL_OVERRIDES={ABOUT: https://example.com}"

To list the actual non-default settings, just type

.. code-block::

    tutor list

To list all available settings, their type, default and current value, run:

.. code-block::

    tutor list --all --output=table

The yaml output format allows you to copy the output and paste it directly
in a ``config.yml`` file. If used with the `--all` option it will list the configured
values or the default ones.

.. code-block::

    tutor list -o yaml

Available settings
******************

Use ``tutor list -o table`` to see all the available settings together with their value type and default.
Note that these default values are the LET plugin defaults,
not neccesarily the Open edX or the Tutor defaults.
Also note that the values shown come from the current configuration file and may not
represent the actual values in the live site.

ALLOW_AUTOMATED_SIGNUPS
---------------------------------------------------

Enable to show a section in the membership tab of the instructor
dashboard to allow an upload of a CSV file that contains a list of new accounts to create
and register for course.

ALLOW_COURSE_STAFF_GRADE_DOWNLOADS
---------------------------------------------------

Enable to give course staff unrestricted access to grade downloads;
if set to False, only edX superusers can perform the downloads.

ALLOW_HIDING_DISCUSSION_TAB
---------------------------------------------------

If True, it adds an option to show/hide the discussions tab.

ALLOW_PUBLIC_ACCOUNT_CREATION
---------------------------------------------------

Allow public account creation. If this is disabled, users will no longer have access to
the signup page.

AUTHENTICATION_BACKENDS
---------------------------------------------------

See `ENABLE_THIRD_PARTY_AUTH`_.


AUTH_PASSWORD_VALIDATORS
---------------------------------------------------

Set the validators for the passwords. By default:

.. code-block::

    AUTH_PASSWORD_VALIDATORS = [
        {
            "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
        },
        {
            "NAME": "common.djangoapps.util.password_policy_validators.MinimumLengthValidator",
            "OPTIONS": {
                "min_length": 8
            }
        },
        {
            "NAME": "common.djangoapps.util.password_policy_validators.MaximumLengthValidator",
            "OPTIONS": {
                "max_length": 75
            }
        },
    ]

CADDYFILE_PATCH
---------------------------------------------------

Add more elements to the ``Caddyfile``.

CERTIFICATE_FACEBOOK
---------------------------------------------------

Set to False to disable the Facebook link in the certificates page.

CERTIFICATE_FACEBOOK_TEXT
---------------------------------------------------

Text to show in Facebook.

CERTIFICATE_LINKEDIN_HONOR_CERT_NAME
---------------------------------------------------

Text to show in LinkedIn for honor certificates.

CERTIFICATE_LINKEDIN_NO_ID_CERT_NAME
---------------------------------------------------

Text to show in LinkedIn for no-id-verified certificates.

CERTIFICATE_LINKEDIN_PROFESSIONAL_CERT_NAME
---------------------------------------------------

Text to show in LinkedIn for professional certificates.

CERTIFICATE_LINKEDIN_VERIFIED_CERT_NAME
---------------------------------------------------

Text to show in LinkedIn for verified certificates.

CERTIFICATE_TWITTER
---------------------------------------------------

Set to False to disable the Twitter link in the certificates page.

CERTIFICATE_TWITTER_TEXT
---------------------------------------------------

Text to show in Facebook.

COURSES_INVITE_ONLY
---------------------------------------------------

Setting this sets the default value of INVITE_ONLY across all courses in a given deployment

COURSE_BLOCKS_API_EXTRA_FIELDS
---------------------------------------------------

Specifies extra XBlock fields that should available when requested via the Course Blocks API
Should be a list of tuples of (block_type, field_name), where block_type can also be "*" for all block types.
e.g. ``"COURSE_BLOCKS_API_EXTRA_FIELDS=[('course','other_course_settings'),("problem","weight")]"``

COURSE_DISCOVERY_FILTERS
---------------------------------------------------

Setting for overriding default filtering facets for Course discovery.
E.g., ``"COURSE_DISCOVERY_FILTERS=['org','language','modes']"``

COURSE_MODE_DEFAULTS
---------------------------------------------------

Default mode for new courses. The default mode for Open edX is Audit mode:

.. code-block::

    {
        'android_sku': None,
        'bulk_sku': None,
        'currency': 'usd',
        'description': None,
        'expiration_datetime': None,
        'ios_sku': None,
        'min_price': 0,
        'name': _('Audit'),
        'sku': None,
        'slug': 'audit',
        'suggested_prices': '',
    }

As the Audit mode does not allow emitting certificates, we offer a better default
that is the Honor mode.

.. code-block::

    {
        "name": "Honor",
        "slug": "honor",
        "bulk_sku": None,
        "currency": "usd",
        "description": None,
        "expiration_datetime": None,
        "min_price": 0,
        "sku": None,
        "suggested_prices": "",
        'android_sku': None,
        'ios_sku': None,
    }

CUSTOM_CERTIFICATE_TEMPLATES_ENABLED
---------------------------------------------------

Set to True to enable custom certificate templates which are configured via Django admin.

CUSTOM_COURSES_EDX
---------------------------------------------------

Set to True to enable Custom Courses for edX, a feature that is more commonly known as
CCX. Documentation for configuring and using this feature is available at the
`documentation <https://docs.openedx.org/en/latest/site_ops/install_configure_run_guide/configuration/enable_ccx.html>`_.

CUSTOM_COURSE_URLS
---------------------------------------------------

Controls the link pointing to the course about page.
If set to True it will be the ``Social Media Sharing URL`` set in the course's
advanced settings page if any.

DASHBOARD_FACEBOOK
---------------------------------------------------

Set to True to show the Facebook link in the dashboard next to each course.
See also `FACEBOOK_BRAND`_.

DASHBOARD_TWITTER
---------------------------------------------------

Set to True to show the Twitter link in the dashboard next to each course.
See also `TWITTER_BRAND`_.

DASHBOARD_TWITTER_TEXT
---------------------------------------------------

Text to add to the Twitter post after sharing a course from the dashboard.

DEFAULT_MOBILE_AVAILABLE
---------------------------------------------------

This specifies if the courses are available for mobile by default. To make any individual
course available for mobile one can set the value of Mobile Course Available to true in Advanced Settings from the
studio when this is False.

DEFAULT_THROTTLE_RATES
---------------------------------------------------

Override specific values of the Django REST framework's throttle rates.
For more details, pleasee see the `Django REST framework documentation <https://www.django-rest-framework.org/api-guide/throttling/>`_.

Open edX defaults `are <https://github.com/openedx/edx-platform/blob/fb62eaf94ce5b391137956550b184c9dc89e5a42/lms/envs/common.py#L3435-L3440>`_:

.. code-block::

    {
        'user': '60/minute',
        'service_user': '800/minute',
        'registration_validation': '30/minute',
        'high_service_user': '2000/minute',
    }

ELASTIC_SEARCH_INDEX_PREFIX
---------------------------------------------------

Set a prefix for all ElasticSearch indexes. It's useful for sharing a single
ES engine between multiple installations.

ENABLE_ANNOUNCEMENTS
---------------------------------------------------

This feature can be enabled to show system wide announcements
on the sidebar of the learner dashboard. Announcements can be created by Global Staff
users on maintenance dashboard of studio. Maintenance dashboard can accessed at
``https://{studio.domain}/maintenance``

ENABLE_ANONYMOUS_COURSEWARE_ACCESS
---------------------------------------------------

Enable access to courses to non-logged in users.
This setting changes the ``seo.enable_anonymous_courseware_access`` waffle flag.
Run ``tutor <variant> do init --limit let`` to activate the change if you're not running
a ``tutor launch``.

ENABLE_AUTOMATED_SIGNUPS_EXTRA_FIELDS
---------------------------------------------------

When True, the CSV file that contains a list of
new accounts to create and register for a course in the membership
tab of the instructor dashboard will accept the cohort name to
assign the new user and the enrollment course mode.

ENABLE_BULK_ENROLLMENT_VIEW
---------------------------------------------------

When set to True the bulk enrollment view is enabled and one can use it to enroll multiple
users in a course using bulk enrollment API endpoint (/api/bulk_enroll/v1/bulk_enroll).

ENABLE_BULK_USER_RETIREMENT
---------------------------------------------------

Set to True to enable bulk user retirement through REST API. This is disabled by
default.

ENABLE_CERTIFICATES_AUTOGENERATION
---------------------------------------------------

This toggle will enable certificates to be automatically generated.

This setting changes the ``certificates.auto_certificate_generation`` waffle flag.
Run ``tutor <variant> do init --limit let`` to activate the change if you're not running
a ``tutor launch``.

ENABLE_CHANGE_USER_PASSWORD_ADMIN
---------------------------------------------------

Set to True to enable changing a user password through django admin. This is disabled by
default because enabling allows a method to bypass password policy.

ENABLE_COMPREHENSIVE_THEMING
---------------------------------------------------

When enabled, this toggle activates the use of the custom theme
defined by DEFAULT_SITE_THEME.

ENABLE_COOKIE_CONSENT
---------------------------------------------------

Enable header banner for cookie consent using this service:
`<https://cookieconsent.insites.com/>`_

ENABLE_COURSE_DISCOVERY
---------------------------------------------------

Add a course search widget to the LMS for searching courses. When this is enabled, the
latest courses are no longer displayed on the LMS landing page. Also, an "Explore Courses" item is added to the
navbar.

ENABLE_COURSE_EXIT_PAGE
---------------------------------------------------

Supports staged rollout of the new micro-frontend-based implementation of the course exit page.

This setting changes the ``courseware.microfrontend_course_exit_page`` waffle flag.
Run ``tutor <variant> do init --limit let`` to activate the change if you're not running
a ``tutor launch``.


ENABLE_DYNAMIC_REGISTRATION_FIELDS
---------------------------------------------------

When enabled, this toggle adds fields configured in
`REGISTRATION_EXTRA_FIELDS`_ to the registration page.

ENABLE_ENTERPRISE_INTEGRATION
---------------------------------------------------

Set to enable Enterprise integration.

ENABLE_MAX_FAILED_LOGIN_ATTEMPTS
---------------------------------------------------

This feature will keep track of the number of failed login attempts on a given user's
email. If the number of consecutive failed login attempts - without a successful login at some point - reaches
a configurable threshold (default 6), then the account will be locked for a configurable amount of seconds
(30 minutes) which will prevent additional login attempts until this time period has passed. If a user
successfully logs in, all the counter which tracks the number of failed attempts will be reset back to 0. If
set to False then account locking will be disabled for failed login attempts.

You can set the threshold with `MAX_FAILED_LOGIN_ATTEMPTS_ALLOWED`_ and
`MAX_FAILED_LOGIN_ATTEMPTS_LOCKOUT_PERIOD_SECS`_.

ENABLE_MKTG_SITE
---------------------------------------------------

Toggle to enable alternate urls for marketing links. When this is enabled, the MKTG_URLS setting should be defined. The use case of this feature
toggle is uncertain.

ENABLE_NAVIGATION_SIDEBAR
---------------------------------------------------

Enable navigation sidebar on Learning MFE.

This setting changes the ``courseware.enable_navigation_sidebar`` waffle flag.
Run ``tutor <variant> do init --limit let`` to activate the change if you're not running
a ``tutor launch``.

ENABLE_ORA_TEAM_SUBMISSIONS
---------------------------------------------------

Set to True to enable team-based ORA submissions.

ENABLE_ORA_USERNAMES_ON_DATA_EXPORT
---------------------------------------------------

Set to True to add deanonymized usernames to ORA data report.

ENABLE_ORA_USER_STATE_UPLOAD_DATA
---------------------------------------------------

A "work-around" feature toggle meant to help in cases where some file uploads are not
discoverable.  If enabled, will pull file metadata from StudentModule.state for display in staff assessments.

ENABLE_OTHER_COURSE_SETTINGS
---------------------------------------------------

Show a new field in "Advanced settings" that can store custom data about a
course and that can be read from themes.

Check `COURSE_BLOCKS_API_EXTRA_FIELDS`_ if you want to query this value from the REST API.

ENABLE_PASSWORD_RESET_FAILURE_EMAIL
---------------------------------------------------

Whether to send an email for failed password reset attempts or not. This happens when a
user asks for a password reset but they don't have an account associated to their email. This is useful for
notifying users that they don't have an account associated with email addresses they believe they've registered
with. This setting can be overridden by a site-specific configuration.

ENABLE_REQUIRE_THIRD_PARTY_AUTH
---------------------------------------------------

Set to True to prevent using username/password login and registration and only allow
authentication with third party auth.

ENABLE_SAML
---------------------------------------------------

Add the SAML backend to the list of `authentication backends <AUTHENTICATION_BACKENDS>`_.

ENABLE_SPECIAL_EXAMS
---------------------------------------------------

Enable to use special exams, aka timed and proctored exams.

ENABLE_THIRD_PARTY_AUTH
---------------------------------------------------

Turn on third-party auth. Disabled for now because full implementations are not yet
available. Remember to run migrations if you enable this; we don't create tables by default. This feature can
be enabled on a per-site basis. When enabling this feature, remember to define the allowed authentication
backends with the `AUTHENTICATION_BACKENDS`_ setting.

ENABLE_UNICODE_USERNAME
---------------------------------------------------

Set this to True to allow unicode characters in username. Enabling this will also
automatically enable SOCIAL_AUTH_CLEAN_USERNAMES. When this is enabled, usernames will have to match the
regular expression defined by USERNAME_REGEX_PARTIAL.

ENABLE_VIDEO_UPLOAD_PIPELINE
---------------------------------------------------

Enable the video upload pipeline.

Check also `VIDEO_UPLOAD_PIPELINE_ROOT_PATH`_
and `VIDEO_UPLOAD_PIPELINE_VEM_S3_BUCKET`_.


ENTERPRISE_MARKETING_FOOTER_QUERY_PARAMS
---------------------------------------------------

Additional query parameters to add to the business links in the footer.

ENTRANCE_EXAMS
---------------------------------------------------

Enable entrance exams feature. When enabled, students see an exam xblock as the first unit
of the course.

FACEBOOK_BRAND
---------------------------------------------------

Brand to include with the Facebook share link. See `DASHBOARD_FACEBOOK`_.

GOOGLE_ANALYTICS_4_ID
---------------------------------------------------

ID of Google Analytics 4 to include in the site.

LICENSING
---------------------------------------------------

Toggle platform-wide course licensing. The course.license attribute is then used to append
license information to the courseware.
When enabled you can set the license type (all rights reserved or creative commons)
in the course schedule & details page.

LOGIN_AND_REGISTER_FORM_RATELIMIT
---------------------------------------------------

Login and registration form rate limit per IP.
This rate limit is `applied <https://github.com/openedx/edx-platform/blob/fb62eaf94ce5b391137956550b184c9dc89e5a42/openedx/core/djangoapps/user_authn/views/login_form.py#L132>`__
to the GET event that renders the login and registration form.

LOGISTRATION_API_RATELIMIT
---------------------------------------------------

Login and registration REST API request rate limit per IP.
This rate limit is `applied <https://github.com/openedx/edx-platform/blob/fb62eaf94ce5b391137956550b184c9dc89e5a42/openedx/core/djangoapps/user_authn/api/views.py#L26>`__
to the view that sends the context to the Authn MFE.

LOGISTRATION_PER_EMAIL_RATELIMIT_RATE
---------------------------------------------------

Login and registration form rate limit per email address.
This rate limit is `applied <https://github.com/openedx/edx-platform/blob/fb62eaf94ce5b391137956550b184c9dc89e5a42/openedx/core/djangoapps/user_authn/views/login.py#L514>`__
to the login view that catches the POST request from the login form.

LOGISTRATION_RATELIMIT_RATE
---------------------------------------------------

Overall login and registration rate limit.
This rate limit is `applied <https://github.com/openedx/edx-platform/blob/fb62eaf94ce5b391137956550b184c9dc89e5a42/openedx/core/djangoapps/user_authn/views/login.py#L520>`__
to the login view that catches the POST request from the login form.


MAX_FAILED_LOGIN_ATTEMPTS_ALLOWED
---------------------------------------------------

Specifies the maximum failed login attempts allowed to users. Once the user reaches this
failure threshold then the account will be locked for a configurable amount of seconds (30 minutes) which will
prevent additional login attempts until this time period has passed. This setting is related with
`MAX_FAILED_LOGIN_ATTEMPTS_LOCKOUT_PERIOD_SECS`_ and only used when `ENABLE_MAX_FAILED_LOGIN_ATTEMPTS`_ is enabled.

MAX_FAILED_LOGIN_ATTEMPTS_LOCKOUT_PERIOD_SECS
---------------------------------------------------

Specifies the lockout period in seconds for consecutive failed login attempts. Once the user
reaches the threshold of the login failure, then the account will be locked for the given amount of seconds
(30 minutes) which will prevent additional login attempts until this time period has passed. This setting is
related with `MAX_FAILED_LOGIN_ATTEMPTS_ALLOWED`_ and only used when `ENABLE_MAX_FAILED_LOGIN_ATTEMPTS`_ is enabled.

MFE_COURSEWARE_SEARCH
---------------------------------------------------

Enables Courseware Search on Learning MFE.

This setting changes the ``courseware.mfe_courseware_search`` waffle flag.
Run ``tutor <variant> do init --limit let`` to activate the change if you're not running
a ``tutor launch``.

MFE_PROGRESS_MILESTONES
---------------------------------------------------

Display learner progress milestones in a course.

This setting changes the ``courseware.mfe_progress_milestones_streak_celebration`` waffle flag.
Run ``tutor <variant> do init --limit let`` to activate the change if you're not running
a ``tutor launch``.


MFE_PROGRESS_MILESTONES_STREAK_CELEBRATION
---------------------------------------------------

Display a celebration modal when learner completes a configurable streak.

This setting changes the ``courseware.mfe_progress_milestones_streak_celebration`` waffle flag.
Run ``tutor <variant> do init --limit let`` to activate the change if you're not running
a ``tutor launch``.

MKTG_URLS
---------------------------------------------------

Set `ENABLE_MKTG_SITE`_ to enable marketing URLs before.

``MKTG_URLS`` are used when marketing site is enabled.
It must include an entry with key ``ROOT`` and value as the URL of the marketing site.
Calls to the home of the LMS will be redirected to the marketing site URL defined as ``ROOT``.

MKTG_URL_LINK_MAP
---------------------------------------------------

``MKTG_URL_LINK_MAP`` are used when marketing site is disabled.

MKTG_URL_OVERRIDES
---------------------------------------------------

``MKTG_URL_OVERRIDES`` are used whether the marketing site is enabled or not.

OPTIONAL_FIELD_API_RATELIMIT
---------------------------------------------------

Rate limit for the optional field API (used?).

ORGANIZATIONS_AUTOCREATE
---------------------------------------------------

When enabled, creating a course run or content library with
an "org slug" that does not map to an Organization in the database will trigger the
creation of a new Organization, with its name and short_name set to said org slug.
When disabled, creation of such content with an unknown org slug will instead
result in a validation error.
If you want the Organization table to be an authoritative information source in
Studio, then disable this; however, if you want the table to just be a reflection of
the orgs referenced in Studio content, then leave it enabled.

PATCH_EDX_PLATFORM
---------------------------------------------------

Set to True to apply the current version latest patches to edx-platform.

PRIVACY_POLICY
---------------------------------------------------

Set the content of the privacy policy page, in HTML format.

RATELIMIT_ENABLE
---------------------------------------------------

When enabled, `RATELIMIT_RATE`_ is applied.
When disabled, `RATELIMIT_RATE`_ is not applied.

RATELIMIT_RATE
---------------------------------------------------

Due to some reports about attack on /oauth2/access_token/ which took LMS down,
this setting was introduced to rate-limit all endpoints of AccessTokenView up to
120 requests per IP Address in a minute by default.

Set `RATELIMIT_ENABLE`_ to activate it.

RATELIMIT_USE_CACHE
---------------------------------------------------

Cache configuration for rate limit. See the `Django documentation <https://django-ratelimit.readthedocs.io/en/stable/settings.html?highlight=ratelimit_use_cache#ratelimit-use-cache>`_ for more details.
Set to `general` to use Open edX global cache.

REGISTRATION_EXTRA_FIELDS
---------------------------------------------------

The signup form may contain extra fields that are presented to every user. For every field, we
can specifiy whether it should be "required": to display the field, and make it mandatory; "optional": to display
the optional field as part of a toggled input field list; "optional-exposed": to display the optional fields among
the required fields, and make it non-mandatory; "hidden": to not display the field.
When the terms of service are not visible and agreement to the honor code is required (the default), the signup page
includes a paragraph that links to the honor code page (defined my MKTG_URLS["HONOR"]). This page might not be
available for all Open edX platforms. In such cases, the "honor_code" registration field should be "hidden".

You can override individual values. The default values in Open edX are:

.. code-block::

    {
        'confirm_email': 'hidden',
        'level_of_education': 'optional',
        'gender': 'optional',
        'year_of_birth': 'optional',
        'mailing_address': 'optional',
        'goals': 'optional',
        'honor_code': 'required',
        'terms_of_service': 'hidden',
        'city': 'hidden',
        'country': 'hidden',
    }

REGISTRATION_RATELIMIT
---

New users are registered on edx via RegistrationView.
It's POST end-point is rate-limited up to 60 requests per IP Address in a week by default.
Purpose of this setting is to restrict an attacker from registering numerous fake accounts.

This rate limit is `applied <https://github.com/openedx/edx-platform/blob/fb62eaf94ce5b391137956550b184c9dc89e5a42/openedx/core/djangoapps/user_authn/views/register.py#L560>`__
to the view that catches the POST requests from the registration form.

REGISTRATION_VALIDATION_RATELIMIT
---------------------------------------------------

Whenever a user tries to register on edx, the data entered during registration
is validated via RegistrationValidationView.
It's POST endpoint is rate-limited up to 30 requests per IP Address in a week by default.
It was introduced because an attacker can guess or brute force a series of names to enumerate valid users.

This rate limit is `applied <https://github.com/openedx/edx-platform/blob/fb62eaf94ce5b391137956550b184c9dc89e5a42/openedx/core/djangoapps/user_authn/views/register.py#L875>`__
to the view that catches the POST requests from the registration form.


RESET_PASSWORD_API_RATELIMIT
---------------------------------------------------

This rate limit throttles requests to the password reset view.

RESET_PASSWORD_TOKEN_VALIDATE_API_RATELIMIT
---------------------------------------------------

This rate limit throttles requests to the password reset token validation view.

SEARCH_SKIP_SHOW_IN_CATALOG_FILTERING
---------------------------------------------------

If enabled, courses with a catalog_visibility set to "none" will still
appear in search results.

SECURITY_PAGE_URL
---------------------------------------------------

A link to the site's security disclosure/reporting policy,
to display in the site footer. This will only appear for sites using themes that
use the links produced by ``lms.djangoapps.branding.api.get_footer``.

SHOW_PROGRESS_BAR
---------------------------------------------------

Set to True to show progress bar. Looks like it works together with COMPLETION_AGGREGATOR_URL (?).

SITE_ID
---------------------------------------------------

Tutor by default `configures <https://github.com/overhangio/tutor/blob/6a87af76b9244ce9a954f424aa17cbaa13c91e3a/tutor/templates/apps/openedx/settings/partials/common_all.py#L91>`_
SITE_ID=2. However in some situations you might need to change the default site id.

SKIP_EMAIL_VALIDATION
---------------------------------------------------

Turn this on to skip sending emails for user validation.
Beware, as this leaves the door open to potential spam abuse.

SOCIAL_AUTH_OAUTH_SECRETS
---------------------------------------------------

Useful to configure OAuth2 third party authentication.
Check the `tutorial <https://docs.openedx.org/en/latest/site_ops/install_configure_run_guide/configuration/tpa/tpa_integrate_open/tpa_oauth.html>`__.

SOCIAL_AUTH_SAML_SP_PRIVATE_KEY and SOCIAL_AUTH_SAML_SP_PUBLIC_CERT
-------------------------------------------------------------------

Useful to configure SAML third party authentication.
Check the `tutorial <https://docs.openedx.org/en/latest/site_ops/install_configure_run_guide/configuration/tpa/tpa_integrate_open/tpa_SAML_IdP.html>`__.


SUPPORT_SITE_LINK
---------------------------------------------------

Your URL for the Help button.

TOS_AND_HONOR_CODE
---------------------------------------------------

Set the content of the TOS and Honor page, in HTML format.

TWITTER_BRAND
---------------------------------------------------

Brand to include with the Twitter share link. See `DASHBOARD_TWITTER`_.

USERNAME_REGEX_PARTIAL
---------------------------------------------------

Regular expressions for the username. The Open edX default is ``r'[\w .@_+-]+'``.
Set `ENABLE_UNICODE_USERNAME`_ to take effect.

VIDEO_IMAGE_UPLOAD_ENABLED
---------------------------------------------------

Enabling or disable video image upload feature. Not sure if it works outside of 2U/edX.

This setting changes the ``videos.video_image_upload_enabled`` waffle flag.
Run ``tutor <variant> do init --limit let`` to activate the change if you're not running
a ``tutor launch``.

VIDEO_UPLOAD_PIPELINE_ROOT_PATH
---------------------------------------------------

Video pipeline configuration. Check also `ENABLE_VIDEO_UPLOAD_PIPELINE`_

VIDEO_UPLOAD_PIPELINE_VEM_S3_BUCKET
---------------------------------------------------

Video pipeline configuration. Check also `ENABLE_VIDEO_UPLOAD_PIPELINE`_

WIKI_ENABLED
---------------------------------------------------

This setting allows us to have a collaborative tool to contribute or
modify content of course related materials.

Contributing
************

Contributions are welcome!

If you thing there are settings worth adding to this plugin, feel free to open an issue
in this repository.

License
*******

This software is licensed under the terms of the AGPLv3.

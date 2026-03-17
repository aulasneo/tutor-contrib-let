# Change log

## Unreleased
- chore: Upgrade requirements and package versioning for Tutor 20 / Open edX Teak.
- fix: Correct LET CLI handling for falsey values, emit YAML safely, restore ``LOGISTRATION_PER_EMAIL_RATELIMIT_RATE``, and align the default password minimum length to ``8``.
- feat: Add and document Authn-related LET settings with defaults and ownership notes:
  ``ACTIVATION_EMAIL_SUPPORT_LINK=<unset>``, ``AUTHN_PROGRESSIVE_PROFILING_SUPPORT_LINK=<unset>``,
  ``BANNER_IMAGE_EXTRA_SMALL=<unset>``, ``BANNER_IMAGE_LARGE=<unset>``, ``BANNER_IMAGE_MEDIUM=<unset>``,
  ``BANNER_IMAGE_SMALL=<unset>``, ``DISABLE_ENTERPRISE_LOGIN=<unset>``,
  ``ENABLE_AUTO_GENERATED_USERNAME=False``, ``ENABLE_IMAGE_LAYOUT=<unset>``,
  ``ENABLE_POST_REGISTRATION_RECOMMENDATIONS=<unset>``,
  ``ENABLE_PROGRESSIVE_PROFILING_ON_AUTHN=<unset>``, ``GENERAL_RECOMMENDATIONS=<unset>``,
  ``INFO_EMAIL=<unset>``, ``LOGIN_ISSUE_SUPPORT_LINK=<unset>``, ``MARKETING_EMAILS_OPT_IN=<unset>``,
  ``PASSWORD_RESET_SUPPORT_LINK=<unset>``, ``POST_REGISTRATION_REDIRECT_URL=<unset>``,
  ``PRIVACY_POLICY=<unset>``, ``SEARCH_CATALOG_URL=<unset>``,
  ``SHOW_CONFIGURABLE_EDX_FIELDS=<unset>``, ``SHOW_REGISTRATION_LINKS=True``,
  ``TOS_AND_HONOR_CODE=<unset>``, and ``TOS_LINK=<unset>``.
- feat: Clarify ownership of Authn configuration:
  ``ENABLE_AUTO_GENERATED_USERNAME`` is an LMS feature toggle,
  ``ENABLE_DYNAMIC_REGISTRATION_FIELDS`` and ``SHOW_REGISTRATION_LINKS`` are LMS settings,
  and the remaining Authn-only values are passed through Tutor MFE config/build settings only when explicitly configured.

## Version 19.0.0 (2025-04-28)
- chore: Upgrade requirements for Sumac
- revert: Remove openedx patches not needed in Sumac

## Version 18.0.0 (2025-04-04)
- chore: First Redwood release

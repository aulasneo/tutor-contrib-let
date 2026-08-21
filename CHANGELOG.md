# Change log

## Unreleased
- fix: disabling ALLOW_PUBLIC_ACCOUNT_CREATION now does not render the registration page

## Version 21.1.1 (2026-08-05)
- fix: Rename importation of getAuthenticatedUser
- fix: Do not include ENABLE_AUTO_GENERATED_USERNAME in MFE_CONFIG if false.

## Version 21.1.0 (2026-05-05)
- feat: Show the user full name instead of the username in the user menu

## Version 21.0.1 (2026-05-05)
- feat: add support for auto-generated usernames in MFE configuration

## Version 21.0.0 (2026-04-21)
- chore: upgrade package compatibility and local development pins for Tutor 21 / Open edX Ulmo.
- test: validate the plugin against Tutor 21 hook and CLI APIs used by LET.
- fix: align Ulmo-migrated configuration with current Open edX setting locations instead of relying only on legacy ``FEATURES`` keys.
- feat: add Ulmo-native settings for LMS/CMS behavior, explicitly listing ``LOGIN_REDIRECT_WHITELIST``, ``LEARNING_MICROFRONTEND_URL``, ``PARENTAL_CONSENT_AGE_LIMIT``, ``REGISTRATION_EMAIL_PATTERNS_ALLOWED``, ``SESSION_ACTIVITY_SAVE_DELAY_SECONDS``, ``ENABLE_COURSEWARE_SEARCH_FOR_COURSE_STAFF``, ``ENABLE_COURSEWARE_SEARCH_VERIFIED_REQUIRED``, and ``IN_CONTEXT_DISCUSSION_ENABLED_DEFAULT``.
- ref: remove deprecated ``ENABLE_ANNOUNCEMENTS`` from the plugin surface for Ulmo.

## Version 20.0.1 (2026-04-01)
- feat: add local development automation with a `Makefile` and pinned dev requirements
- feat: add GitHub Actions test and release workflows aligned with the current plugin maintenance flow
- ref: adopt `pyproject.toml`-based builds while keeping package metadata aligned
- breaking: require Python 3.11 or newer
- chore: ignore generated Tutor `config.yml` and `env/` artifacts from local test runs
- fix: pass `ENABLE_DYNAMIC_REGISTRATION_FIELDS="true"` to the authn MFE when the LMS setting is enabled

## Version 20.0.0 (2026-03-17)
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

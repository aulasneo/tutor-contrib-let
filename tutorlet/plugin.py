from __future__ import annotations

import os
from glob import glob

import click
import importlib_resources
import yaml

from tabulate import tabulate
from tutor import hooks, fmt
from tutor import config as tutor_config


########################################
# CONFIGURATION
########################################

config = {
    'defaults': {
        #
        # caddyfile patch
        #
        "CADDYFILE_PATCH": '',

        #
        # common-env-features
        #
        "ALLOW_HIDING_DISCUSSION_TAB": True,
        "CUSTOM_COURSES_EDX": True,
        "ALLOW_COURSE_STAFF_GRADE_DOWNLOADS": True,
        "CUSTOM_CERTIFICATE_TEMPLATES_ENABLED": True,
        "ENABLE_ANNOUNCEMENTS": True,
        "ENABLE_AUTOMATED_SIGNUPS_EXTRA_FIELDS": True,
        "ENABLE_BULK_ENROLLMENT_VIEW": True,
        "ENABLE_BULK_USER_RETIREMENT": True,
        "ENABLE_CHANGE_USER_PASSWORD_ADMIN": True,
        "ENABLE_MKTG_SITE": False,
        "ENABLE_ORA_TEAM_SUBMISSIONS": True,
        "ENABLE_ORA_USERNAMES_ON_DATA_EXPORT": True,
        "ENABLE_ORA_USER_STATE_UPLOAD_DATA": True,
        "ENABLE_PASSWORD_RESET_FAILURE_EMAIL": True,
        "ENABLE_SPECIAL_EXAMS": True,
        "ENABLE_UNICODE_USERNAME": True,
        "ENTRANCE_EXAMS": False,
        "SHOW_PROGRESS_BAR": True,
        "ENABLE_OTHER_COURSE_SETTINGS": True,
        "LICENSING": True,
        "SKIP_EMAIL_VALIDATION": False,
        "ENABLE_ENTERPRISE_INTEGRATION": False,
        "ALLOW_AUTOMATED_SIGNUPS": True,
        "ALLOW_PUBLIC_ACCOUNT_CREATION": True,
        "ENABLE_MAX_FAILED_LOGIN_ATTEMPTS": True,
        "COURSES_INVITE_ONLY": False,
        "ENABLE_COOKIE_CONSENT": False,

        #
        # discovery-common-settings
        #
        "ELASTIC_SEARCH_INDEX_PREFIX": "",

        #
        # mfe-dockerfile-pre-npm-build-authn
        #
        "TOS_AND_HONOR_CODE": "https://{{ LMS_HOST }}/tos",
        "PRIVACY_POLICY": "https://{{ LMS_HOST }}/privacy",

        #
        # openedx-auth
        #
        "SOCIAL_AUTH_SAML_SP_PRIVATE_KEY": "",
        "SOCIAL_AUTH_SAML_SP_PUBLIC_CERT": "",

        #
        # openedx-cms-common-settings
        #
        "ENABLE_VIDEO_UPLOAD_PIPELINE": False,
        "VIDEO_UPLOAD_PIPELINE_ROOT_PATH": "videos",
        "VIDEO_UPLOAD_PIPELINE_VEM_S3_BUCKET": "",
        "VIDEO_IMAGE_UPLOAD_ENABLED": True,
        "ORGANIZATIONS_AUTOCREATE": True,

        #
        # openedx-common-settings
        #
        "MKTG_URLS": {},
        "DEFAULT_MOBILE_AVAILABLE": True,
        "ENABLE_COMPREHENSIVE_THEMING": True,
        # Set to True to prevent using username/password login and registration and only allow
        #   authentication with third party auth
        "ENABLE_REQUIRE_THIRD_PARTY_AUTH": False,
        #  If enabled, courses with a catalog_visibility set to "none"
        #  will still appear in search results.
        "SEARCH_SKIP_SHOW_IN_CATALOG_FILTERING": False,  # True by default
        "WIKI_ENABLED": False,
        "COURSE_MODE_DEFAULTS": {
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
        },  # Default is audit mode
        "MKTG_URL_LINK_MAP": {},
        "MKTG_URL_OVERRIDES": {},
        "GOOGLE_ANALYTICS_4_ID": None,
        "SUPPORT_SITE_LINK": '',
        "SECURITY_PAGE_URL": '#',
        "ENTERPRISE_MARKETING_FOOTER_QUERY_PARAMS": {},
        # "SOCIAL_SHARING_SETTINGS"
        'CUSTOM_COURSE_URLS': True,
        'DASHBOARD_FACEBOOK': True,
        "FACEBOOK_BRAND": "",
        "TWITTER_BRAND": "",
        'DASHBOARD_TWITTER': False,
        'DASHBOARD_TWITTER_TEXT': "",
        'CERTIFICATE_FACEBOOK': True,
        'CERTIFICATE_FACEBOOK_TEXT': "",
        'CERTIFICATE_TWITTER': True,
        'CERTIFICATE_TWITTER_TEXT': "",
        'CERTIFICATE_LINKEDIN_HONOR_CERT_NAME': '{platform_name} Honor Code Credential for {course_name}',
        'CERTIFICATE_LINKEDIN_VERIFIED_CERT_NAME': '{platform_name} Verified Credential for {course_name}',
        'CERTIFICATE_LINKEDIN_PROFESSIONAL_CERT_NAME': '{platform_name} Professional Credential for {course_name}',
        'CERTIFICATE_LINKEDIN_NO_ID_CERT_NAME': '{platform_name} Professional Credential for {course_name}',
        "USERNAME_REGEX_PARTIAL": r'[\w .@_+-]+',

        "REGISTRATION_EXTRA_FIELDS": {},
        "ENABLE_DYNAMIC_REGISTRATION_FIELDS": False,
        "MAX_FAILED_LOGIN_ATTEMPTS_ALLOWED": 6,
        "MAX_FAILED_LOGIN_ATTEMPTS_LOCKOUT_PERIOD_SECS": 1800,
        "RATELIMIT_USE_CACHE": "general",
        "RATELIMIT_ENABLE": True,
        "RATELIMIT_RATE": '120/m',

        # Check defaults at https://github.com/openedx/edx-platform/blob/1c14c3a5184b27b344b782dd6ac88f3e64cf2535/lms/envs/common.py#L4905C1-L4912C1
        "LOGISTRATION_RATELIMIT_RATE": '100/5m',
        "LOGISTRATION_PER_EMAIL_RATELIMIT_RATE": '30/5m',
        "LOGISTRATION_API_RATELIMIT": '20/m',
        "LOGIN_AND_REGISTER_FORM_RATELIMIT": '100/5m',
        "RESET_PASSWORD_TOKEN_VALIDATE_API_RATELIMIT": '30/7d',
        "RESET_PASSWORD_API_RATELIMIT": '30/7d',
        "OPTIONAL_FIELD_API_RATELIMIT": '10/h',

        # Check defaults at https://github.com/openedx/edx-platform/blob/1c14c3a5184b27b344b782dd6ac88f3e64cf2535/lms/envs/common.py#L3444-L3459
        "REGISTRATION_VALIDATION_RATELIMIT": '30/7d',
        "REGISTRATION_RATELIMIT": '60/7d',

        # Check default at https://github.com/openedx/edx-platform/blob/1c14c3a5184b27b344b782dd6ac88f3e64cf2535/lms/envs/common.py#L3436-L3441
        'DEFAULT_THROTTLE_RATES': {},

        # Default at https://github.com/overhangio/tutor/blob/6a87af76b9244ce9a954f424aa17cbaa13c91e3a/tutor/templates/apps/openedx/settings/partials/common_all.py#L91
        "SITE_ID": 2,

        # Empty by default, here we let other_course_settings show in the API.
        "COURSE_BLOCKS_API_EXTRA_FIELDS": [
            ('course', 'other_course_settings')
        ],

        #
        # openedx-dockerfile-post-git-checkout
        #
        "PATCH_EDX_PLATFORM": True,


        #
        # openedx-lms-common-settings
        #
        "ENABLE_COURSE_DISCOVERY": True,
        "AUTHENTICATION_BACKENDS": [],
        "SOCIAL_AUTH_OAUTH_SECRETS": {},
        "COURSE_DISCOVERY_FILTERS": ["org", "language", "modes"],
        "ENABLE_SAML": True,

        # openedx-lms-production-settings
        "AUTH_PASSWORD_VALIDATORS": [
            {
                'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'
            },
            {
                'NAME': 'common.djangoapps.util.password_policy_validators.MinimumLengthValidator',
                'OPTIONS': {'min_length': 2}
            },
            {
                'NAME': 'common.djangoapps.util.password_policy_validators.MaximumLengthValidator',
                'OPTIONS': {'max_length': 75}
            }
        ],

        # others waffle flags, switches and settings created at init time
        "ENABLE_CERTIFICATES_AUTOGENERATION": True,
        "ENABLE_ANONYMOUS_COURSEWARE_ACCESS": True,
        "ENABLE_COURSE_EXIT_PAGE": True,
        "MFE_PROGRESS_MILESTONES": True,
        "MFE_PROGRESS_MILESTONES_STREAK_CELEBRATION": True,
        "MFE_COURSEWARE_SEARCH": True,
        "ENABLE_NAVIGATION_SIDEBAR": True,

    }
}

hooks.Filters.CONFIG_DEFAULTS.add_items(
    [
        (f"LET_{key}", value) for key, value in config['defaults'].items()
    ]
)

########################################
# INITIALIZATION TASKS
########################################

MY_INIT_TASKS: list[tuple[str, tuple[str, ...]]] = [
    ('lms', ("let", "tasks", "lms", "init"))
]

for service, template_path in MY_INIT_TASKS:
    full_path: str = str(
        importlib_resources.files("tutorlet")
        / os.path.join("templates", *template_path)
    )
    with open(full_path, encoding="utf-8") as init_task_file:
        init_task: str = init_task_file.read()
    hooks.Filters.CLI_DO_INIT_TASKS.add_item((service, init_task))


########################################
# TEMPLATE RENDERING
# (It is safe & recommended to leave
#  this section as-is :)
########################################

hooks.Filters.ENV_TEMPLATE_ROOTS.add_items(
    # Root paths for template files, relative to the project root.
    [
        str(importlib_resources.files("tutorlet") / "templates"),
    ]
)

hooks.Filters.ENV_TEMPLATE_TARGETS.add_items(
    [
        ("let/build", "plugins"),
        ("let/apps", "plugins"),
    ],
)


########################################
# PATCH LOADING
# (It is safe & recommended to leave
#  this section as-is :)
########################################

# For each file in tutorlet/patches,
# apply a patch based on the file's name and contents.
for path in glob(str(importlib_resources.files("tutorlet") / "patches" / "*")):
    with open(path, encoding="utf-8") as patch_file:
        hooks.Filters.ENV_PATCHES.add_item((os.path.basename(path), patch_file.read()))


#######################################
# CUSTOM CLI COMMANDS
#######################################

from tutor.commands.config import save, ConfigKeyValParamType
import typing as t

@click.command()
@click.argument(
    'setting',
    type=ConfigKeyValParamType(),
    metavar="KEY=VAL",
)
@click.pass_context
def let(context: click.Context, setting: list[tuple[str, t.Any]],) -> None:
    """
    Add a setting to the configuration file.
    """
    if setting[0] not in config['defaults']:
        fmt.echo_error(f"{setting[0]} is not a valid setting.")
        return

    context.invoke(save, set_vars=[(f"LET_{setting[0]}", setting[1])])

hooks.Filters.CLI_COMMANDS.add_item(let)

@click.option('-o', '--output', default='list', help='Output format (list or table)')
@click.option('-a', '--all', is_flag=True, default=False,
              help='Show all values. Otherwise it will show only the non-default values.')
@click.option('-w', '--width', default=50, help='Maximum column width for table output.')
@click.command(name='list', help='Show all values.')
def _list(output: str, all: bool, width: int) -> None:
    """
    List all available settings, their type, default and current value.
    """
    current_context = click.get_current_context()
    root = current_context.parent.params.get('root')
    if root:
        configuration = tutor_config.load_minimal(root)
        defaults = tutor_config.load_defaults()

        data = []
        for key in sorted(config['defaults'].keys()):
            let_key = "LET_" + key
            default = defaults[let_key]
            type_name = str(type(default))[8:-2]
            value = configuration.get(let_key)

            if all or value:
                # truncate long strings for table view
                if output == 'table':
                    key = key[:width]
                    value = str(value)[:width] if value else ''
                    default = str(default)[:width]
                data.append((key, type_name, default, value))

        if output == 'table':
            headers = ["Key", "Type", "Default", "Value"]
            print(tabulate(data, headers=headers, tablefmt="fancy_grid"))

        elif output == 'list':
            for row in data:
                value = row[3] if row[3] else row[2]
                if isinstance(value, str):
                    value = f'"{value}"'
                print(f"LET {row[0]} = {value}")

        elif output == 'yaml':
            print(yaml.dump({
                "LET_"+row[0]: row[3] if row[3] else row[2] for row in data
            }, default_flow_style=False, line_break=None))

        else:
            fmt.echo_error(f"Unsupported output format '{output}'.")

    else:
        fmt.echo_error("Tutor root not specified.")

hooks.Filters.CLI_COMMANDS.add_item(_list)

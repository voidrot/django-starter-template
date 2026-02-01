# django-allauth config
SITE_ID = 1
ACCOUNT_LOGIN_METHODS = {"email", "username"}
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_SIGNUP_FIELDS = [
    "email*",
    "username*",
    "password1*",
]
# Note: * denotes required field
LOGIN_REDIRECT_URL = "/"

AXES_PROTECTED_LOGINS = (
    '/accounts/login/',
    '/login/'
    '/account/password/reset/',
    '/user/password/reset/',
)

MIDDLEWARE_CLASSES = (
    'axes.middleware.FailedLoginMiddleware',
    'user_sessions.middleware.SessionMiddleware'
)

INSTALLED_APPS = (
    'pythias_user_management', # For template overrides
    'axes', # Django-axes for user tracking
    'user_sessions', # For active sessions
)

SESSION_ENGINE = 'user_sessions.backends.db'

DASHBOARD_ADDONS = ['pythias_user']
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,

    "formatters": {
        "simple": {
            "format": "{levelname} {asctime} {name}: {message}",
            "style": "{",
        },
    },

    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "simple",
        },

        "debug_file": {
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "filename": "/app/debug.log",
            "formatter": "simple",
        },

        "error_file": {
            "class": "logging.FileHandler",
            "level": "INFO",
            "filename": "/app/error.log",
            "formatter": "simple",
        },
    },

    "root": {
        "level": "DEBUG",
        "handlers": ["console", "debug_file", "error_file"],
    },
    "loggers":{
        "django.request": {
            "handlers": ["debug_file", 'error_file'],
            "level": "INFO",
            "propagate": False,
        },
    }
}
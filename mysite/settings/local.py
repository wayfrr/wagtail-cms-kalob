
# Recaptcha Settings 
RECAPTCHA_PUBLIC_KEY = "6LfEAIYcAAAAANvl3IxkRraoON5RU-gIkn0TGaOu"
RECAPTCHA_PRIVATE_KEY = "6LfEAIYcAAAAAOB-95YERHS2u0D9kVAXc7xuEguw"
NOCAPTCHA = True


INTERNAL_IPS = ("127.0.0.1", "172.17.0.1")

# Uncomment this line to enable template caching
# Dont forget to change the LOCATION path
CACHES = {
     "default": {
         "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
         "LOCATION": "D:/WT/WTCMS/cache"
     }
 }


try:
    from .local import *
except ImportError:
    pass
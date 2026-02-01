# Content Security Policy
CSP_REPORT_ONLY = True

CSP_DEFAULT_SRC = ("'self'",)
CSP_SCRIPT_SRC = (
    "'self'",
    "'unsafe-inline'", # For HTMX inline scripts if needed, though best to avoid
    "https://unpkg.com", # For HTMX CDN (as used in base.html)
)
CSP_STYLE_SRC = (
    "'self'",
    "'unsafe-inline'", # Tailwind/DaisyUI often inserts inline styles
)
CSP_IMG_SRC = ("'self'", "data:")

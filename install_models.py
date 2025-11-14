import argostranslate.package, argostranslate.translate

# download and install English ↔ Hindi
argostranslate.package.update_package_index()
packages = argostranslate.package.get_available_packages()

# Install only necessary languages
pairs = [
    ("en", "hi"),
    ("en", "es"),
    ("en", "fr"),
    ("en", "de"),
    ("en", "zh"),
    ("hi", "en"),
    ("hi", "es"),
    ("hi", "fr"),
    ("hi", "de"),
    ("hi", "zh"),
    ("es", "en"),
    ("es", "hi"),
    ("es", "fr"),
    ("es", "de"),
    ("es", "zh"),
    ("fr", "en"),
    ("fr", "es"),
    ("fr", "de"),
    ("fr", "zh"),
    ("fr", "hi"),
    ("de", "en"),
    ("de", "es"),
    ("de", "fr"),
    ("de", "zh"),
    ("de", "hi"),
    ("zh", "hi"),
    ("zh", "es"),
    ("zh", "fr"),
    ("zh", "de"),
    ("zh", "en")
]

for from_code, to_code in pairs:
    for pkg in packages:
        if pkg.from_code == from_code and pkg.to_code == to_code:
            print(f"Installing {from_code} → {to_code}")
            download_path = pkg.download()
            argostranslate.package.install_from_path(download_path)

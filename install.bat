@echo off
where python >nul 2>&1 && (
  echo [INSTALL] Found Python

  pip3 >nul 2>&1 && (
    echo [INSTALL] Found pip3
    python -m pip install --upgrade pip
  ) || (
    echo [ERROR] pip3 is not available in PATH
    pause
    exit /b
  )

  echo [INSTALL] Using venv
  rmdir /q /s venv
  python -m venv ./venv
  .\venv\Scripts\activate


  echo [INSTALL] Installing Requirements
  pip install -r requirements.txt

  echo Username Must be in email address format e.g. username@domain.com It does not need to be valid.
  python manage.py createsuperuser

  python manage.py collectstatic

  echo [INSTALL] Migrating Database
  python manage.py makemigrations
  python manage.py makemigrations rule_manager
  python manage.py migrate

  echo [INSTALL] Installation Complete
) || (
  echo [ERROR] python3 is not installed
)
This is the Jules BDD Automation Framework project written in Python.

Site tested: https://jules.app/

Design pattern used: page object model

Methodology: behavior driven development

Libraries to install:

pip install -U selenium
pip install behave
pip install behave-html-formatter
pip install webdriver-manager

Run tests:

behave -f html -o behave-report.html --tags=jules

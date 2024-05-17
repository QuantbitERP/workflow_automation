from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in workflow_automation/__init__.py
from workflow_automation import __version__ as version

setup(
	name="workflow_automation",
	version=version,
	description="Workflow automation",
	author="erpdata",
	author_email="contact@erpdata.in",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)

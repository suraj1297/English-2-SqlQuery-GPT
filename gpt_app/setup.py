from setuptools import setup, find_packages

setup(
    name='gpt-sql',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'openai',
        'mysql-connector-python'
    ],
    entry_points={
        'console_scripts': [
            'jaarus = app:generate_query_and_fetch_data',
        ],
    },
)
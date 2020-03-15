import setuptools

setuptools.setup(name='healthstat',
                 packages=setuptools.find_packages(),
                 version='0.0.1',
                 author='kamil boberek',
                 author_email='kamil.boberek@jezuici.pl',
                 description='Data Science for your health and performance',
                 ulr='https://github.com/kamilsj/healthstat',
                 long_description='''
                 ###Data science for your health and performance
                 **check**
                 ''',
                 long_description_content_type='text/markdown',
                 include_package_data=True,
                 install_requires=[
                     'tensorflow',
                     'stravalib',
                     'bokeh',
                     'scipy',
                     'numpy',
                     'jupyter',
                     'python_tcxparser',
                     'django_countries',
                     'cryptography',
                     'fitparse',
                     'setuptools',
                     'choochoo',
                     'django_heroku'
                     'Django',
                     'djangorestframework',
                     'django_storages'

                 ],
                 entry_points={
                     'console_scripts': [
                         'hs = healthstat:main',
                     ],
                 },
                 classifiers=(
                     "Programming Language :: Python :: 3.7",
                     "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
                     "Operating System :: OS Independent",
                     "Development Status :: 4 - Beta",
                 )
                 )
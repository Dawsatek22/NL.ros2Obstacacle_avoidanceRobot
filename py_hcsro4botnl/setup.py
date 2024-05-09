from setuptools import find_packages, setup

package_name = 'py_hcsro4botnl'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='test1',
    maintainer_email='test1@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            
            'dctest = py_hcsro4botnl.Dctest:main',
             'hctest = py_hcsro4botnl.Hctest:main',
             'rsub = py_hcsro4botnl.Ridesub:main',
             'rpub = py_hcsro4botnl.Ridepub:main',
        ],
    },
)

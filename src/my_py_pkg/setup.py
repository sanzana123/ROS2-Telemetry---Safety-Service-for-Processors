from setuptools import find_packages, setup

package_name = 'my_py_pkg'

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
    maintainer='root',
    maintainer_email='root@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            # 'executable_name = package_name.file_name:function_name'
            'py_node = my_py_pkg.my_first_node:main',
            'publisher_node_name = my_py_pkg.my_publisher:main',
            'subscriber_node_name = my_py_pkg.my_subscriber:main',
            'thermal_sensor_node = my_py_pkg.thermal_sensor:main',
            'thermal_monitor_node = my_py_pkg.thermal_monitor:main',
            'health_service_node = my_py_pkg.health_service:main',
        ],
    },
)

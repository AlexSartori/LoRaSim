import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="LoRaSim",
    version="0.0.1",
    author="Alessandro Sartori, Massimiliano Fronza",
    author_email="alex.sartori1997@gmail.com",
    description="Graphical simulator for LoRa with Markov Chains as models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alexsartori/LoRaSim",
    install_requires=["pyqt5"],
    packages=setuptools.find_packages(),
    package_data={},
    entry_points={
        'gui_scripts': [
            'LoRaSim=LoRaSim:launch_gui',
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Environment :: X11 Applications :: Qt",
        "Topic :: Software Development",
        "Natural Language :: English"
    ],
    keywords='lora markov chain simulator',
    python_requires='>=3.6',
)

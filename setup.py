from setuptools import setup, find_packages

setup(
    name="molecule-x",
    version="1.0.0",
    description="AI-Native Multi-Agent Drug Repurposing System",
    author="Molecule-X Team",
    packages=find_packages(),
    install_requires=[
        "streamlit>=1.28.0",
        "requests>=2.31.0",
        "pandas>=1.5.0",
        "numpy>=1.24.0",
        "scikit-learn>=1.3.0",
        "openai>=1.3.0",
        "langchain>=0.0.300",
        "faiss-cpu>=1.7.0",
        "xmltodict>=0.13.0",
        "rdkit-pypi>=2022.9.5"
    ],
    entry_points={
        'console_scripts': [
            'molecule-x=main:main',
        ],
    },
    python_requires=">=3.8",
)
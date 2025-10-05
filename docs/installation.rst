Installation
============

This project supports multiple installation methods to accommodate different development environments and use cases.

Prerequisites
-------------

* Python 3.11 or higher
* Git
* Docker (optional, for containerized development)

Installation Methods
--------------------

Method 1: Using uv (Recommended)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Install `uv` if you haven't already:

   .. code-block:: bash

      curl -LsSf https://astral.sh/uv/install.sh | sh

2. Clone the repository:

   .. code-block:: bash

      git clone <repository-url>
      cd ensemble-learning-project

3. Install dependencies:

   .. code-block:: bash

      uv sync

4. Start Jupyter Lab:

   .. code-block:: bash

      uv run jupyter lab

Method 2: Using pip
~~~~~~~~~~~~~~~~~~~

1. Clone the repository:

   .. code-block:: bash

      git clone <repository-url>
      cd ensemble-learning-project

2. Create a virtual environment:

   .. code-block:: bash

      python -m venv venv
      source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies:

   .. code-block:: bash

      pip install -r requirements.txt

4. Start Jupyter Lab:

   .. code-block:: bash

      jupyter lab

Method 3: Using Docker
~~~~~~~~~~~~~~~~~~~~~~

1. Clone the repository:

   .. code-block:: bash

      git clone <repository-url>
      cd ensemble-learning-project

2. Build and run with Docker Compose:

   .. code-block:: bash

      docker-compose up --build

3. Open your browser and navigate to `http://localhost:8888`

Development Setup
-----------------

For development work, install additional development dependencies:

.. code-block:: bash

   uv sync --dev
   uv run pre-commit install

This will install:

* Testing frameworks (pytest, pytest-cov)
* Code quality tools (black, isort, flake8, mypy)
* Pre-commit hooks
* Documentation tools (Sphinx)

Verification
------------

To verify your installation, run the test suite:

.. code-block:: bash

   make test

Or run specific tests:

.. code-block:: bash

   uv run pytest tests/ -v

Troubleshooting
---------------

Common Issues
~~~~~~~~~~~~~

**ImportError: No module named 'sklearn'**
   Make sure you've installed all dependencies with `uv sync` or `pip install -r requirements.txt`.

**Jupyter Lab not starting**
   Check that the port 8888 is not already in use. You can specify a different port:

   .. code-block:: bash

      jupyter lab --port 8889

**Docker build fails**
   Ensure Docker is running and you have sufficient disk space. Try cleaning up Docker:

   .. code-block:: bash

      docker system prune -f

**Permission errors on macOS/Linux**
   Make sure the setup script is executable:

   .. code-block:: bash

      chmod +x scripts/setup.sh

Getting Help
~~~~~~~~~~~~

If you encounter issues:

1. Check the `CONTRIBUTING.md` file for development guidelines
2. Review the GitHub Issues for known problems
3. Create a new issue with detailed error information

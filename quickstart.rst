Quick Start Guide
=================

This guide will help you get up and running with the Ensemble Learning project quickly.

Prerequisites
-------------

* Python 3.11+
* Git
* Basic understanding of machine learning concepts

Setup (5 minutes)
-----------------

1. **Clone and setup**:

   .. code-block:: bash

      git clone <repository-url>
      cd ensemble-learning-project
      ./scripts/setup.sh

2. **Start Jupyter Lab**:

   .. code-block:: bash

      make jupyter

3. **Open the notebook**:

   Navigate to `http://localhost:8888` and open `ensembles.ipynb`

Your First Ensemble Model
-------------------------

Let's create a simple ensemble model to get started:

.. code-block:: python

   import pandas as pd
   import numpy as np
   from sklearn.ensemble import RandomForestClassifier
   from sklearn.model_selection import train_test_split
   from sklearn.metrics import accuracy_score

   # Load sample data
   data = pd.read_csv('data/simple.csv')
   X = data.drop('target', axis=1)
   y = data['target']

   # Split the data
   X_train, X_test, y_train, y_test = train_test_split(
       X, y, test_size=0.2, random_state=42
   )

   # Create and train ensemble model
   rf = RandomForestClassifier(n_estimators=100, random_state=42)
   rf.fit(X_train, y_train)

   # Make predictions
   y_pred = rf.predict(X_test)
   accuracy = accuracy_score(y_test, y_pred)
   print(f"Accuracy: {accuracy:.3f}")

Key Concepts
------------

Ensemble Learning
~~~~~~~~~~~~~~~~~

Ensemble learning combines multiple models to improve predictive performance:

* **Bagging**: Trains models independently and averages predictions
* **Boosting**: Trains models sequentially, each correcting previous errors
* **Stacking**: Uses a meta-model to combine predictions

Available Methods
~~~~~~~~~~~~~~~~~

The project includes implementations of:

* Random Forest (Bagging)
* AdaBoost (Boosting)
* Gradient Boosting (Boosting)
* XGBoost (Gradient Boosting variant)
* Stacking (Meta-learning)

Next Steps
----------

1. **Explore the notebook**: Work through `ensembles.ipynb` for detailed examples
2. **Run tests**: Verify everything works with `make test`
3. **Try different data**: Experiment with your own datasets
4. **Read the documentation**: Check out the full documentation in the `docs/` folder

Common Commands
---------------

.. code-block:: bash

   # Development
   make help              # Show all available commands
   make test              # Run tests
   make lint              # Check code quality
   make format            # Format code

   # Docker
   make docker-build      # Build Docker image
   make docker-run        # Run with Docker
   make docker-stop       # Stop Docker containers

   # Jupyter
   make jupyter           # Start Jupyter Lab
   make jupyter-notebook  # Start Jupyter Notebook

Troubleshooting
---------------

**Port already in use**: Change the port with `--port 8889`

**Import errors**: Make sure you've run `uv sync` or installed dependencies

**Docker issues**: Ensure Docker is running and try `docker system prune -f`

Need Help?
----------

* Check the `README.md` for detailed instructions
* Review the `docs/` folder for comprehensive documentation
* Look at the test files in `tests/` for usage examples

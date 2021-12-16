# python-dash-template

Experimental template for Python Dash web apps on the Analytical Platform.

## Instructions

### Create a new repository on GitHub

Click the green "Use this template" button above to create your repository, for reference see [GitHub's help page](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-from-a-template). 

Clone your new repository to the platform in the JupyterLab terminal.

```
git clone git@github.com:moj-analytical-services/YOUR-REPOSITORY-NAME.git
```

See [the platform guidance about GitHub](https://user-guidance.services.alpha.mojanalytics.xyz/github.html#content) for more details.

### Recreate the environment
#### Using the platform

`cd` to your project directory in the terminal and run

```
conda env create -f environment.yml -n YOUR_ENVIRONMENT_NAME
conda activate YOUR_ENVIRONMENT_NAME
```

To install packages preferably use
```
conda install pandas
```
or if you need to use pip
```
python -m pip install pydbtools
```
(There's no need to add `--user` as installation is in the conda environment.)

To save the environment before deployment
```
conda env export > environment.yml
```

After you have finished deactivate the environment with
```
conda deactivate YOUR_ENVIRONMENT_NAME
```

##### JupyterLab notebooks

If you would like to use your environment as a kernel in a JupyterLab notebook, activate it and run
```
conda install ipykernel
python -m ipykernel install --name YOUR_ENVIRONMENT_NAME --display-name "Your environment name"
```
Restart JupyterLab (at least this is the only way I've been able to get it to work) and the environment can then be selected from the top right of the notebook.

See [this guidance](https://github.com/RobinL/cheatsheets_etc/blob/master/jupyter_conda.md) for further details.

#### Using a MacBook

Developing outside the platform means the conda environment file is unlikely to work, in which case use pip and `requirements.txt` to set up the environment.

```
python3 -m venv YOUR_ENVIRONMENT_NAME
source YOUR_ENVIRONMENT_NAME/bin/activate
python3 -m pip install -r requirements.txt
mv Dockerfile Dockerfile.backup
mv Dockerfile_pip Dockerfile
```

After installing packages with pip run

```
python3 -m pip freeze > requirements.txt
``` 


### Edit the app

Edit the section in app.py under `# App starts here`. To test the app in JupyterLab, run
```
python app.py
```
and view the app at `https://YOUR_GITHUB_USERNAME-jupyter-lab.tools.alpha.mojanalytics.xyz/_tunnel_/8050/`. See [the user guidance](https://user-guidance.services.alpha.mojanalytics.xyz/appendix/dash/#content) for details.

To test the app locally, e.g. on a MacBook, run with the deploy flag
```
python app.py -d
```
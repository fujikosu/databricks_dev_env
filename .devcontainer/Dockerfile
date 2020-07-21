FROM python:3.7.8-stretch

# Configure apt
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update \
    && apt-get -y install --no-install-recommends apt-utils 2>&1

# Install git, process tools, lsb-release (common in install instructions for CLIs)
RUN apt-get -y install git procps lsb-release vim

# Install  International Components for Unicode
RUN apt-get install -y libicu[0-9][0-9]

# Install java
RUN apt-get install -y openjdk-8-jdk
ENV JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-amd64

# Install nodejs and npm for jupyterlab extensions
RUN curl -sL https://deb.nodesource.com/setup_14.x | bash -
RUN apt-get install -y nodejs

RUN mkdir /workspace
WORKDIR /workspace

# Install jupyterlab into default python
RUN python -m pip install jupyterlab jupyterlab_code_formatter

# Install jupyterlab extensions
COPY labextensions.txt /workspace/
RUN while read line; do jupyter labextension install --no-build $line; done < labextensions.txt 
RUN jupyter lab build
RUN rm labextensions.txt

# Copy Python requirements files for the later installation
COPY requirements*.txt /workspace/

# Install for local pyspark env
RUN python -m venv /.envs/local_spark_env
RUN /.envs/local_spark_env/bin/pip install -r requirements_dev.txt \
    && /.envs/local_spark_env/bin/pip install -r requirements_local.txt 

# Install for databricks-connect pyspark env
RUN python -m venv /.envs/db_connect_env
RUN /.envs/db_connect_env/bin/pip install -r requirements_dev.txt \
    && /.envs/db_connect_env/bin/pip install -r requirements_db_connect.txt

# Register both venvs as jupyter kernel
RUN /.envs/local_spark_env/bin/python -m ipykernel install --user --name local_spark_env --display-name "local_spark_env"
RUN /.envs/db_connect_env/bin/python -m ipykernel install --user --name db_connect_env --display-name "db_connect_env"

# Need this to use environment variables for databricks-connect setting
# https://forums.databricks.com/questions/21536/databricks-connect-configuration-not-possible-with.html
RUN echo '{}' > ~/.databricks-connect

# Clean up
RUN apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*
RUN rm requirements_*.txt 

# Switch back to the default frontend
ENV DEBIAN_FRONTEND=dialog

# Set the default shell to bash rather than sh
ENV SHELL /bin/bash
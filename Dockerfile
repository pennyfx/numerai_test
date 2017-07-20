# Dockerfile to create env: build using `datmo env build`
# [1] Base environment to start from:
# Find more at https://hub.docker.com/u/datmo/
FROM datmo/scikit-opencv:py-2.7

RUN apt-get update -y
# Numpy / Scipy reqs
RUN apt-get install -y  python-pandas \
                        python-sympy
RUN pip install --upgrade pandas==0.20.2
RUN pip install xgboost
RUN apt-get -y build-dep python-matplotlib
RUN pip install seaborn
RUN pip install bokeh

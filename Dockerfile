FROM continuumio/miniconda3

SHELL ["/bin/bash", "-c"]

COPY . .

RUN conda env create -f environment.yml -n dashapp
RUN echo "source activate dashapp" > ~/.bashrc
ENV PATH /opt/conda/envs/dashapp/bin:$PATH

EXPOSE 80

ENTRYPOINT ["python", "app.py", "--deploy"]

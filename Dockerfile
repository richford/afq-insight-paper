from continuumio/miniconda3

SHELL ["/bin/bash", "-c"]

# Use the environment.yml to create the conda environment.
ADD environment.yml /tmp/environment.yml
WORKDIR /tmp
RUN [ "conda", "env", "create" ]

ADD . /afq-insight-paper
WORKDIR /afq-insight-paper

# Set the ENTRYPOINT to use bash
ENTRYPOINT [ "/bin/bash", "-c" ]
CMD [ "source activate afq-insight-paper && jupyter lab --ip 0.0.0.0 --port 8899 --no-browser --allow-root notebooks" ]


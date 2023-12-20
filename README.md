# Chicken-Disease-Classification--Project


## Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml

### Running the Tensorboard
<b>Command: `tensorboard --logdir artifacts/prepare_callbacks/tensorboard_log_dir/` </b>

### Running the Data Version Control (DVC)

<b>Command: `dvc init` </b> (optional, as the DVC has already been initialized in the project)

<b>Command: `dvc repro` </b>


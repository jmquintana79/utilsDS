# main.py
# Load config (from script by create output logging)

import hydra 

@hydra.main(version_base=None, config_path=".", config_name="config")
def main(config):
    print(f'Process {config.data}')
    print(f'Drop features: {config.variables.drop_features}')
    print(f'Folder input: {config.folders.input}')
    print(f'Folder output: {config.folders.output}')

if __name__ == '__main__':
    main()
import os
import json
import argparse


def get_module_name(module_path: str) -> str:
    base_path = os.path.basename(module_path)
    if os.path.isfile(module_path):
        base_path = os.path.splitext(base_path)[0]
    return base_path

def disable(directory: str):
    """
    Adds '.disabled' to the end of the directory name
    """
    if not os.path.isdir(directory):
        print(f"{directory} is not a valid directory")
        return
    
    # Check if the directory already has the .disabled suffix
    if not directory.endswith('.disabled'):
        new_name = directory + '.disabled'
        try:
            os.rename(directory, new_name)
            print(f"Directory {directory} has been disabled, renamed to {new_name}")
        except Exception as e:
            print(f"Failed to disable directory {directory}, {e}")
        return directory  # Return the disabled directory name
    else:
        print(f"Directory {directory} is already disabled, no changes made.")
        return directory[:-9]

def enable(directory: str):
    """
    Removes the '.disabled' suffix from the directory name
    """
    if not os.path.isdir(directory):
        print(f"{directory} is not a valid directory")
        return
    
    # Check if the directory has the .disabled suffix
    if directory.endswith('.disabled'):
        new_name = directory[:-9]  # Remove the .disabled suffix
        try:
            os.rename(directory, new_name)
            print(f"Directory {directory} has been enabled, renamed to {new_name}")
        except Exception as e:
            print(f"Failed to enable directory {directory}, {e}")
        return directory  # Return the disabled directory name        
    else:
        print(f"Directory {directory} does not have the '.disabled' suffix, no need to enable.")

def load_config(config_file: str):
    """
    Loads the enable_nodes.json configuration file
    """
    try:
        with open(config_file, 'r', encoding='utf-8') as f:
            config = json.load(f)
        return config
    except Exception as e:
        print(f"Error loading configuration file: {e}")
        return None

def save_disabled_list(disabled_dirs: list, config_file: str):
    """
    Saves the list of disabled directories to disable_nodes.json
    """
    try:
        with open(config_file, 'w', encoding='utf-8') as f:
            json.dump({"disable": disabled_dirs}, f, indent=4, ensure_ascii=False)
        print(f"Disabled directories have been saved to {config_file}")
    except Exception as e:
        print(f"Error saving disabled directories: {e}")

def process_directories(config: dict, base_path: str):
    """
    Enables or disables directories based on the configuration
    """
    if config is None:
        print("No valid configuration, unable to proceed.")
        return []

    enable_dirs = config.get("enable", [])

    enable_dirs.extend([dir + ".disabled" for dir in enable_dirs])

    
    # List all files and folders in the current directory
    items = os.listdir(base_path)
    
    # List to store the disabled directories
    disabled_dirs = []
    
    # Iterate through items in the current directory and enable/disable as needed
    for item in items:
        item_path = os.path.join(base_path, item)

        if item_path.count('__pycache__') > 0:
            continue
        print("item_path:",item_path, item)
        # If it is a directory and in the enable list, enable it
        if os.path.isdir(item_path) and item in enable_dirs:
            enable(item_path)
        # If it is a directory and not in the enable list, disable it
        elif os.path.isdir(item_path):
            disabled_dir = disable(item_path)
            if disabled_dir:
                module = get_module_name(disabled_dir)
                disabled_dirs.append(module)

    return disabled_dirs

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Enable or disable directories")
    parser.add_argument("--config", help="Path to the configuration file", default=os.path.join(os.getcwd(), 'enable_nodes.json'))
    parser.add_argument("--disable-config", help="Path to save the disabled directories list", default=os.path.join(os.getcwd(), 'disable_nodes.json'))
    parser.add_argument("--custom-nodes-dir", help="Custom nodes directory", default=os.path.join(os.getcwd(), "custom_nodes"))

    args = parser.parse_args()

    # Load the configuration file
    config = load_config(args.config)
    
    # Perform the enable/disable operations and get the list of disabled directories
    disabled_dirs = process_directories(config, args.custom_nodes_dir)
    
    # Save the list of disabled directories to the specified file
    if disabled_dirs:
        save_disabled_list(disabled_dirs, args.disable_config)


if __name__ == "__main__":
    main()

# NeoCraft

NeoCraft is a Python program designed to enhance productivity on Windows systems by providing a quick-switch mechanism between background and foreground tasks. This application allows users to streamline their workflow by automatically managing task focus.

## Features

- **Automatic Task Switching**: Switches the foreground window periodically to help manage tasks more effectively.
- **Background Task Management**: Runs specified background tasks concurrently with foreground tasks.
- **Customizable Interval**: Adjust the switching interval to suit your workflow needs.

## Requirements

- Python 3.x
- Windows operating system

## Installation

1. Clone the repository or download the `neocraft.py` file.
2. Ensure Python 3.x is installed on your Windows system.

## Usage

1. Open a command prompt or terminal.
2. Navigate to the directory containing `neocraft.py`.
3. Run the script using Python:

   ```shell
   python neocraft.py
   ```

4. The program will start managing tasks, switching between them based on the predefined interval.

## Configuration

- You can modify the `SWITCH_INTERVAL` constant in the code to change the time in seconds between automatic task switches.
- Customize the tasks within the `background_task()` and `foreground_task()` functions to suit your needs.

## Limitations

- This script is designed specifically for Windows systems.
- Ensure you have the necessary permissions to run scripts and manage windows.

## Contributing

Contributions are welcome! Feel free to submit a pull request or report issues.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
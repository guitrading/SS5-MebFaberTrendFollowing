# QuantConnect Algorithm

## Overview

This repository contains an algorithm developed for the QuantConnect platform. The algorithm aims to implement a long-term trend following strategy based on Meb Faber's method.

## Features

- Long-term trend following
- Support for multiple asset classes
- Risk management and position sizing

## Getting Started

### Prerequisites

Ensure you have the following installed on your local development environment:

- Python 3.8+
- QuantConnect Lean CLI
- [Other dependencies, if any]

## Usage

### Files

- `main.py` - The main file where the algorithm logic is implemented.
- `config.json` - Configuration file for the algorithm settings.
- `requirements.txt` - A file listing the dependencies required for the algorithm.

### Algorithm Description

The algorithm follows Meb Faber's strategy, involving these key steps:

1. **Initialize:** Sets up the algorithm parameters and data subscriptions.
2. **OnData:** Handles incoming data and makes trading decisions based on long-term trends.
3. **Risk Management:** Implements risk management strategies to control drawdowns and position sizes.
4. **Execution Model:** Describes how orders are executed to follow the strategic model.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Implement your feature or bug fix.
3. Create a pull request with a detailed description.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or issues, please file an issue in the repository or contact [gui.bertoni@gmail.com](mailto:gui.bertoni@gmail.com).
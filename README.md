# PyTM - Extended with STRIDE-ATLAS Hybrid Model

This version of PyTM includes an extension to support the STRIDE-ATLAS Hybrid Model, integrating threats specific to AI workloads and the OWASP Top Ten vulnerabilities for Web, API, and LLMs.

## New Features

- **AI Components**: Added `AIModel` and `Dataset` elements to represent AI systems.
- **Custom Threats**: Included ATLAS and OWASP Top Ten threats specific to AI and web vulnerabilities.
- **Example Script**: Provided `examples/hybrid_model.py` demonstrating how to use the new features.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- Git

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/pytm_hybrid.git
   cd pytm_hybrid
   ```

2. **Set Up a Virtual Environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Upgrade Build Tools and Install PyTM**

   ```bash
   pip install --upgrade pip setuptools wheel
   pip install -e .
   ```

### Running the Example

1. **Navigate to the Examples Directory**

   ```bash
   cd examples
   ```

2. **Run the Hybrid Model Script**

   ```bash
   python hybrid_model.py
   ```

3. **View the Output**

   The script will process the threat model and output a report in the console.

## Understanding the Extensions

- **AI Elements**

  - `AIModel`: Represents an AI or machine learning model.
  - `Dataset`: Represents a dataset used for training AI models.

- **Custom Threats**

  - **ATLAS Threats**: Defined in `pytm/threatlib/custom/atlas_threats.yaml`.
  - **OWASP Threats**: Defined in `pytm/threatlib/custom/owasp_threats.yaml`.

## Contributing

Contributions are welcome! Please open issues or pull requests for any enhancements or bug fixes.

## License

[MIT License](LICENSE)

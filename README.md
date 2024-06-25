# 🚧 Debugging `requests_html` 🚧

This repository was created to help identify and fix an issue in the `requests_html` library. Here, you will find code examples, instructions for reproducing the problem, and guidelines for contributing to the solution.

## Objective

The objectives of this project are:

- Reproduce the issue found in the `requests_html` library.
- Analyze the behavior and identify the root cause of the problem.
- Propose and test possible solutions.
- Document the debugging process and the solutions found.

## Repository Structure

- `files/`: Contains downloaded HTML pages.
- `logs/`: Logs and output files to assist in the analysis.
- `examples/`: Contains code examples that demonstrate the issue.
- `links.csv`: Links used to reproduce the error.
- `README.md`: This documentation file.

## Requirements

To reproduce and debug the problem, you will need the following (although the error has already been reproduced on various machines with different software versions):

- Python 3.8.10
- `requests_html` 0.10.0

## How to Reproduce the Issue

1. Clone this repository:

    ```bash
    git clone https://github.com/carloseduardobanjar/debug-requests-html.git
    cd debug-requests-html
    ```

2. If you wish to test multiple times, it is recommended to download the HTML pages so that you do not need to make requests repeatedly, which can be time-consuming.

    To download the HTML pages, execute the `Download HTML pages` cell in the `examples/download_and_find.ipynb` file. Then, simply run `examples/demo_problem.py`:

    ```bash
    python3 examples/demo_problem.py > logs/output.log 2>&1
    ```

3. If you want to test only once, uncomment the commented section in `examples/demo_problem.py` and comment out the section that is currently in use. This method may take longer, but both methods allow you to reproduce the error.

4. Check the logs generated in the `logs/` directory for more details on the behavior of the problem.

**Note 1:** The problem is usually identified when the code seems to hang without showing any error logs or completion.

## Contact

If you have any questions or suggestions, feel free to open an issue or get in touch.
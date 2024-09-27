# Software Engineering Project - CSC 510-001 (Fall 2024)

We are a group of three students:[**Aditya Singh**](https://github.com/adii711), [**Bahare Riahi**](https://github.com/BahareCS), and [**Monish Erode Sridhar**](https://github.com/MonishESGit) under the supervision of **Dr. Tim Menzies** for the Software Engineering course CSC 510-001 at North Carolina State University.

## Instructor Information
- **Professor**: Tim Menzies
- **Email**: timm@ieee.org
- **Department**: Computer Science, NC State University

---

### Badges
[![Python](https://img.shields.io/badge/language-Python-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-BSD--2--Clause-orange)](https://opensource.org/licenses/BSD-2-Clause)
[![Platform](https://img.shields.io/badge/platform-Linux-green)](https://www.linux.org/)
[![Pytest](https://github.com/BetaPack/Software-Engineering/actions/workflows/python-app.yml/badge.svg)](https://docs.pytest.org/en/latest/)
[![Coverage](https://img.shields.io/badge/coverage-100%25-green?label=coverage&color=green)](https://coverage.readthedocs.io/)
[![Pyflakes](https://img.shields.io/badge/lint-pyflakes-blue.svg)](https://github.com/PyCQA/pyflakes)
[![Pylint](https://img.shields.io/badge/lint-pylint-yellowgreen.svg)](https://pylint.pycqa.org/)
[![AutoPep8](https://img.shields.io/badge/format-autopep8-brightgreen.svg)](https://github.com/hhatto/autopep8)

# Homework 2 - Merge Sort Debugging and Static Analysis

## Overview
This project involves debugging a faulty implementation of the Merge Sort algorithm in `hw2_debugging.py`, using static analysis tools and automated code formatting. Follow the steps below to set up the project, run the necessary tools, and ensure proper code testing and quality checks.

## Steps

### Initial Setup
- Download and unzip the `hw2.zip` file.
- Place the unzipped contents in repository.

### Static Analysis Tools
- **AutoPep8**: Automatically formats Python code to conform to PEP 8 standards.
  ```
  bash autopep8 --in-place --aggressive --aggressive hw2_debugging.py rand.py
  ```
- **Pylint**: Static code analysis tool that checks for errors, enforces coding standards, and detects code smells.
  ```
  bash pylint hw2_debugging.py rand.py
  ```
- **Pyflakes**: Fast static analysis tool to check for errors in Python code.
  ```
  pyflakes hw2_debugging.py rand.py
  ```

### Debugging with Logger
- Ensure that the logger in hw2_debugging_logger.py is set up correctly.
- Examine the debug logs to identify the points where the code is failing.
- Code debugging is confirmed by Code splitting, Code merging, Code updation and the final sorted array

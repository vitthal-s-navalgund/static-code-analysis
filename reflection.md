

### 1. Which issues were the easiest to fix, and which were the hardest? Why?
 **Easiest:** Removing unused imports and adding missing docstrings were the simplest fixes since they required minimal code changes and had no functional impact.
**Hardest:** Replacing `eval()` and refactoring mutable default arguments were the hardest. They required understanding the function logic and ensuring that the fixes didn’t change program behavior or introduce new bugs.

### 2. Did the static analysis tools report any false positives? If so, describe one example.
 Yes, there was one **false positive** where Pylint flagged a variable as unused, even though it was indirectly used inside a nested function. The variable was actually necessary for maintaining function state, so the warning was safely ignored.

### 3. How would you integrate static analysis tools into your actual software development workflow?

 Integrate tools like **Pylint**, **Bandit**, and **Flake8** into the **CI/CD pipeline**  to automatically run checks on every commit or pull request.
 Use **pre-commit hooks** locally to catch errors early before code submission.
 Regularly review reports and maintain a low warning threshold to enforce code quality standards.

### 4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?
Code readability improved due to consistent naming and added docstrings.
 File handling became safer and more reliable using context managers.
 Security and robustness increased after removing `eval()` and using specific exception handling.
 Overall, the program became easier to maintain and less prone to runtime errors.

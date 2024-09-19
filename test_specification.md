Test Specification Document for StringCalculator
Overview
This document outlines the test specifications for the add function in the StringCalculator class. The purpose of the add function is to take a string of numbers, potentially separated by custom delimiters, and return their sum. The function should also handle specific edge cases, such as empty strings and negative numbers.

Test Objective
To validate the functionality and robustness of the add function through a series of unit tests, ensuring that it meets the specified requirements and handles edge cases appropriately.

Test Environment

Testing framework: unittest

Test Cases
1. Test Case: Expect Zero for Empty Input
Test Name: test_expectZeroForEmptyInput
Input: ""
Expected Output: 0
Description: Verify that the function returns 0 when given an empty string as input.

2. Test Case: Expect Zero for Single Zero
Test Name: test_expectZeroForSingleZero
Input: "0"
Expected Output: 0
Description: Check that the function returns 0 when the input string contains a single zero.

3. Test Case: Expect Sum for Two Numbers
Test Name: test_expectSumForTwoNumbers
Input: "1,2"
Expected Output: 3
Description: Test the addition of two positive integers separated by a comma.

4. Test Case: Ignore Numbers Greater Than 1000
Test Name: test_ignoreNumbersGreaterThan1000
Input: "1,1001"
Expected Output: 1
Description: Ensure that the function ignores numbers greater than 1000 in the input string.

5. Test Case: Expect Sum With Custom Delimiter
Test Name: test_expectSumWithCustomDelimiter
Input: "//;\n1;2"
Expected Output: 3
Description: Verify that the function correctly handles a custom delimiter (in this case, ;) and returns the sum of the numbers.

6. Test Case: Expect Sum With Newline Delimiter
Test Name: test_expectSumWithNewlineDelimiter
Input: "1\n2,3"
Expected Output: 6
Description: Test the addition of numbers separated by both newline and comma delimiters.

7. Test Case: Throw Exception for Negative Numbers
Test Name: test_throwExceptionForNegativeNumbers
Input: "1,-2"
Expected Output: Raises ValueError with message "Negatives not allowed: -2"
Description: Ensure that the function raises an appropriate exception when the input contains negative numbers.

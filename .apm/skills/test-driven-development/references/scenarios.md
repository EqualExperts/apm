# Worked scenarios

A validator should reject a blank customer name. First assert the public validation result for a blank name and observe the missing rejection. Implement that rejection, then verify blank and valid names. Extract shared validation only while those checks remain green.

If the first run fails because the test module cannot import, repair the test setup before claiming the red phase. If the user already implemented the validator, retain it and describe the new test as regression coverage rather than rewriting history.

# TROUBLE.md

This document lists difficulties encountered during the development of this project, along with their solutions.

---

### Tests Not Running as Expected
**Problem:** simply running `pytest` resulted in unexpected import issues.

**Solution:**
- Ensure `pythonpath = .` parameter is present in the `pytest.ini` configuration file. This parameter adds the root directory to the Python module search path when running tests.

---

### Travis CI Requires a Pricing Plan
**Problem:** Travis CI fails to run builds due to a required pricing plan.

**Solution:**
- Note: I have reached out via email to inquire about the pricing plan requirements, but as of now, I have not received a response.
- As a workaround, I wrote the `.travis.yml` file based on documentation and best practices, but was unable to test its validity in the Travis CI environment.
- I manually built and pushed the Docker image to my Docker Hub account instead of using automated deployment.

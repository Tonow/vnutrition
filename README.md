# V-Nutrition 🥦

[![pipeline status](https://gitlab.com/vnutrition/vnutrition-github/badges/main/pipeline.svg)](https://gitlab.com/vnutrition/vnutrition-github/-/commits/main)
[![coverage report](https://gitlab.com/vnutrition/vnutrition-github/badges/main/coverage.svg)](https://gitlab.com/vnutrition/vnutrition-github/-/commits/main)
[![Latest Release](https://gitlab.com/vnutrition/vnutrition-github/-/badges/release.svg)](https://gitlab.com/vnutrition/vnutrition-github/-/releases)

* Deployment link on [https://vnutrition.streamlit.app/](https://vnutrition.streamlit.app/)
* Main repo on [Gitlab 🦊](https://gitlab.com/vnutrition/vnutrition-github) and push mirror of [Github](https://github.com/Tonow/vnutrition)
  * Please do the Merge request on **Gitlab 🦊** 🙏

## Code quality

this project use :
* [pre-commit](https://pre-commit.com/)
  * [ruff](https://docs.astral.sh/ruff/integrations/#pre-commit)

## Parts infos

* [intake](intake/README.md)

## Run or use locally

- [ ] set virtual environment
- [ ] install requirement
    ```shell
    pip install -r requirements.txt
    ```
- [ ] run
    ```shell
    streamlit run main_apports.py
    ```

## Run tests

- [ ] set virtual environment
- [ ] run tests
    ```shell
    pip install -r requirements-dev.txt
    ```
- [ ] run tests
    ```shell
    python -m pytest  --cov --cov-report term
    ```

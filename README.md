# CICD-Project
```
This CICD project is to configure the CI/CD pipeline for the testing framework using Docker, Jenkins and GIT.
```

## Getting started
```
-> test_trn_db.py: This py file contains automated tests to run on trn db and validates the test result.

-> test_adv_works_db.py: This py file contains automated tests to run on adventure works 2012 db and validates the test result.

-> conftest.py:  This py file contains database connections for adventure works 2012 and trn databases.

-> requirements.txt: This requirements txt file contains modules and packages required by the project.

-> pytest_pipeline.jenkins: Jenkins file is a text file that contains the definition of a Jenkins pipeline and is checked into source control.
```

**Prerequisites:**
```
Setup TRN database in SQL server 
```

## Add your files
```
cd CICD-Project
git add -all
git commit -m 'updates'
git push origin main
```

**Installation:**
```
1. Download and install docker for your operating systems	https://www.docker.com/get-started
2. Find jenkins container in Docker registry https://hub.docker.com/search?q=&type=image
3. Install Python and pip - Python --version & pip -version
4. Build dockerfile
5. Run docker image
6. Setup jenkins 
7. install plugins
```

**Usage:**
```
1. Create automation project to test TRN databases using pytest
2. Create jenkins file in the repo to build the automation project
3. Push your project to git repo
4. Create pull request to master branch
5. Create a pipeline to automate the by adding git repo and branch to build and deploy the tests.
6. Click on Build Now button 
7. Build should be successful
```
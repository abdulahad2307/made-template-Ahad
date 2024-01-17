This repository contains data engineering and data science projects and exercises using open data sources as part of the MADE/SAKI course, taught by the FAU Chair for [Open-Source Software (OSS)](https://oss.cs.fau.de/) in the Winter 23/24 semester. This repo is forked from [made-template repository](https://github.com/jvalue/made-template).

# Project Work

## Project Title: Impact of weather on daily air traffic at the Paphos International Airport, Cyprus.
The Paphos International Airport plays a crucial role in connecting Cyprus to the global network of air travel. As a vital transportation hub, it is essential to understand how daily air traffic at this airport is influenced by weather conditions. This data science project focuses on analyzing the relationship between weather patterns and air traffic to provide valuable insights for airlines, passengers, and decision-makers. By examining these factors, we aim to help stakeholders better plan and manage their operations, ultimately benefiting Cyprus's economy and promoting efficient and safe air travel.

### Data Source Deatils:
    
For this project we are using two open data sources: [European Data Portal](https://data.europa.eu/data/datasets/64a4860b-e33b-4dec-9738-bbadb5c0fe8c?locale=en), which contains information on air traffic in Paphos International Airport, and [meteostat](https://meteostat.net/en/), which provides daily weather and climate data of Paphos International Airport.

### Project Structure:

The project follows a structured ETL (Extract, Transform, Load) pipeline approach, encompassing various directories and modules with specific functionalities. The "etl_main.py" serves as the entry point for running the pipeline using the command "python ./project/etl_main.py", resulting in the generation of the final dataset stored in an SQLite database named as "project.sqlite".

![ETL Pipeline Diagram](https://github.com/abdulahad2307/made-template-Ahad/assets/39805378/c4b3dbcb-1f19-4c63-855f-adb75db44b0b)

### Project Setup:

1. Clone the [repository](https://github.com/abdulahad2307/made-template-Ahad/tree/main)
2. Install [Python](https://www.python.org/downloads/), then create a [virtual environment](https://docs.python.org/3/library/venv.html) for the project.
3. Installing Dependecies using requirements.txt:
	To install the dependencies for this project, run the following command to install the dependencies specified in the requirements.txt file: 
		"pip install -r requirements.txt"
4. Run the project by running the pipeline shell script ".project/pipeline.sh"
5. To run the test will have to execute test shell script ".project/tests.sh"
6. Finally, run and explore the report at "./project/report.ipynb"
7. (Optional) Also can check the related [slides](https://github.com/abdulahad2307/made-template-Ahad/blob/main/project/slides.pdf) of the project and project [presentation video](https://drive.google.com/file/d/1FI00c-42IsGgz9RY2EDzo-Wvqsbil-9w/view?usp=drive_link)


# Exercises
During the semester you will need to complete exercises, sometimes using [Python](https://www.python.org/), sometimes using [Jayvee](https://github.com/jvalue/jayvee). You **must** place your submission in the `exercises` folder in your repository and name them according to their number from one to five: `exercise<number from 1-5>.<jv or py>`.

In regular intervalls, exercises will be given as homework to complete during the semester. We will divide you into two groups, one completing an exercise in Jayvee, the other in Python, switching each exercise. Details and deadlines will be discussed in the lecture, also see the [course schedule](https://made.uni1.de/). At the end of the semester, you will therefore have the following files in your repository:

1. `./exercises/exercise1.jv` or `./exercises/exercise1.py`
2. `./exercises/exercise2.jv` or `./exercises/exercise2.py`
3. `./exercises/exercise3.jv` or `./exercises/exercise3.py`
4. `./exercises/exercise4.jv` or `./exercises/exercise4.py`
5. `./exercises/exercise5.jv` or `./exercises/exercise5.py`

### Exercise Feedback
We provide automated exercise feedback using a GitHub action (that is defined in `.github/workflows/exercise-feedback.yml`). 

To view your exercise feedback, navigate to Actions -> Exercise Feedback in your repository.

The exercise feedback is executed whenever you make a change in files in the `exercise` folder and push your local changes to the repository on GitHub. To see the feedback, open the latest GitHub Action run, open the `exercise-feedback` job and `Exercise Feedback` step. You should see command line output that contains output like this:

```sh
Found exercises/exercise1.jv, executing model...
Found output file airports.sqlite, grading...
Grading Exercise 1
	Overall points 17 of 17
	---
	By category:
		Shape: 4 of 4
		Types: 13 of 13
```

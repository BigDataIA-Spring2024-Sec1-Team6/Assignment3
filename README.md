# Assignment3


## Problem Statement 

Develop two Python classes, URLClass and PDFClasses (MetaDataPDFClass and ContentPDFClass), to structure and validate data extracted from CFA webpages and PDFs. These classes should facilitate the creation of clean CSV files, adhering to predefined schemas. Integrate these classes into a data transformation workflow using DBT and Snowflake, focusing on building, testing, and deploying a summary table schema that captures key metrics from the data. Ensure robust testing and documentation throughout the process.

## Project Goals

1. To design and implement two Python classes (`URLClass` and `PDFClasses`) that accurately represent and validate the data structure of CFA webpages and Grobid PDF outputs.
2. To ensure these classes can process and produce "clean" CSV files, meeting specified data quality standards.
3. To integrate the developed classes with a DBT and Snowflake-based data transformation workflow, culminating in a summary table that reflects key data insights.
4. To rigorously test the data handling and schema validation processes, ensuring accuracy and reliability.
5. To document and deploy the data model effectively, establishing a robust framework for ongoing data analysis and reporting in a test and production environment.

## Technologies Used

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-0D1C2C?style=for-the-badge&logo=pydantic&logoColor=white)
![DBT](https://img.shields.io/badge/dbt-FF694B?style=for-the-badge&logo=dbt&logoColor=white)
![Snowflake](https://img.shields.io/badge/Snowflake-29B5E8?style=for-the-badge&logo=snowflake&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![pytest](https://img.shields.io/badge/pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white)


## Data Sources

1. **CFA Webpages**: HTML pages from the official CFA website, containing structured content about finance topics.
2. **PDF Documents**: These are the three PDF files given.
3. **CSV Files**: Data files generated after processing PDF documents and webpages, containing structured information ready to be loaded into Snowflake.
4. **Grobid Output**: The result of processing the three PDF files through the Grobid tool, as .txt files, representing extracted data.
5. **Snowflake Datasets**: Pre-existing datasets within Snowflake used for validation or augmentation of the extracted data.
6.  **AWS Services**: (**S3 Buckets**) Raw and processed data storage.

## Pre requisites

The prerequisites for undertaking the described project would likely include:

1. **Python Programming**: Proficiency in Python and experience with libraries such as Pydantic for data validation.
2. **Experience with SQL and Snowflake**: Familiarity with SQL queries and experience with cloud-based data warehousing solutions like Snowflake.
3. **Familiarity with DBT**: Knowledge of how to use Data Build Tool for data transformation tasks.
4. **Testing Skills**: Experience with writing and executing test cases, preferably with pytest.
5. **Knowledge of Data Extraction Tools**: Understanding of tools like Grobid for PDF data extraction.
6. **Data Preprocessing**: Skills in data cleaning and preprocessing to prepare data for analysis.

## Project Structure

```
📦 
├─ .gitignore
├─ Diagram
│  └─ diargram.txt
├─ Notebooks
│  ├─ Assignment3_Part1URLClass.ipynb
│  ├─ Assignment3_Part1_1.py
│  ├─ ContentPDFClass.ipynb
│  ├─ DBT_Assignment3_BigData.ipynb
│  ├─ Grobid_MetdataClass_new.ipynb
│  ├─ MetadataPDFClass.ipynb
│  ├─ nb.txt
│  └─ test_abc.py
├─ README.md
└─ Scripts
   └─ script.txt
```
©generated by [Project Tree Generator](https://woochanleee.github.io/project-tree-generator)

## References 
- https://grobid.readthedocs.io/en/latest/Run-Grobid/
- https://docs.getdbt.com/guides/snowflake?step=1
- https://github.com/ashrithagoramane/DAMG7245-Spring24/tree/main/repository_structure

## Learning Outcome

The learning outcome for this project would be to demonstrate the ability to design, implement, and validate data models using Python and Pydantic; to develop a transformation workflow with DBT in a Snowflake environment; and to effectively manage data through various stages of a project, from raw inputs to structured outputs in production-grade systems.

## Team Information and Contribution

WE ATTEST THAT WE HAVEN'T USED ANY OTHER STUDENT'S WORK IN OUR ASSIGNMENT AND ABIDE BY THE POLICIES LISTED IN THE STUDENT HANDBOOK

| Name               | Contribution %   | Contributions                                             |
|--------------------|------------------|-----------------------------------------------------------|
| Osborne Lopes      | 33.3%            | URLClass to represent the schema for the CFA webpages     |
| Akshita Pathania   | 33.3%            | Creation of two PDFClasses to represent the Grobid output |
| Smithi Parthiban   | 40%              | DBT with Snowflake to run transformation workflows        |
| Manimanya Reddy    | 33.3%            | Build 5+5 test cases using Pytest and Pydantic            |
 

ARCHITECTURE DIAGRAM
<img width="981" alt="Screenshot 2024-03-01 at 2 01 50 PM" src="https://github.com/BigDataIA-Spring2024-Sec1-Team6/Assignment3/assets/114605149/989a4e4b-6a06-4c06-a122-714aa88f18d1">

Links: 

CodeLabs Link :- https://codelabs-preview.appspot.com/?file_id=1ulPzcwcL_LYFQzAODiAhVDi4RdKQZm9SB5UvH9AbDUE#3

DBT - https://colab.research.google.com/drive/1hnJOytMeNpfFYNUb7wbORc3XGwEo5SQO?usp=sharing#scrollTo=H3w1JM3Y9zkd

Architectural Diagram - https://colab.research.google.com/drive/1CTw6ppHcMIPszK8kBkhjIZaAFtuFoN21?usp=sharing

#!/usr/bin/env python
# coding: utf-8

# In[119]:


#Ozzzzz

import pandas as pd
from pydantic import BaseModel, ValidationError, validator
from pydantic.networks import HttpUrl
from typing import Optional
import re

class URLClass(BaseModel):
    ID: Optional[int]
    TOPIC_NAME: Optional[str]
    YEAR: Optional[str]
    LEVEL: Optional[str]
    INTRODUCTION_SUMMARY: Optional[str]
    LEARNING_OUTCOMES: Optional[str]
    SUMMARY_PAGE_LINK: Optional[HttpUrl]
    PDF_FILE_LINK: Optional[HttpUrl]

    @validator('ID')
    def validate_id(cls, v):
        if v is not None and v < 0:
            raise ValueError('ID must be a positive integer')
        return v

    @validator('YEAR')
    def validate_year(cls, v):
        if v is not None:
            if v.strip().lower() == 'unkn':
                return None  # Treat 'Unkn' as None
            year_str = re.sub(r'\D', '', v)  # Extract digits
            if not year_str.isdigit():
                raise ValueError(f'Invalid year format: {v}. Must contain numeric characters only.')
            year_int = int(year_str)
            if year_int < 2000 or year_int > 2050:
                raise ValueError('Year must be between 2000 and 2050')
            return str(year_int)
        else:
            return None


    @validator('SUMMARY_PAGE_LINK', 'PDF_FILE_LINK')
    def validate_url(cls, v):
        if v is not None and not v.scheme.startswith('https'):
            raise ValueError('URL must start with "https://"')
        return v

    @validator('LEVEL')
    def validate_level(cls, v):
        if v is not None:
            if v.strip().lower() == 'unknown':
                return None  # Treat 'Unknown' as None
            if pd.isna(v):
                return ''
            pattern = r'^Level\s+(I|II|III|IV|V|VI|VII|VIII|IX|X+)$'
            if not re.match(pattern, v):
                raise ValueError(f'Invalid format for Level: {v}. It should be "Level" followed by a Roman numeral')
        return v

    @validator('INTRODUCTION_SUMMARY', 'TOPIC_NAME', 'LEARNING_OUTCOMES')
    def validate_string_not_empty(cls, v):
        if v is not None and not v.strip():
            return "NULL"
        return v

# Read the CSV file into a pandas DataFrame
input_file_path = 'C:\\Users\\Client\\Desktop\\updated_worksheet.csv'
output_file_path = 'C:\\Users\\Client\\Desktop\\worksheet_2.csv'

df = pd.read_csv(input_file_path)

# Validate each row of the DataFrame
validated_data = []
for index, row in df.iterrows():
    data = row.to_dict()

    # Replace NaN values with None
    for key, value in data.items():
        if pd.isna(value):
            data[key] = None

    try:
        url_instance = URLClass(**data)
        validated_data.append(data)
        print(f"Row {index + 1}: Data is valid!")
    except ValidationError as e:
        print(f"Row {index + 1}: Validation error(s): {e.errors()}")

# Create a new DataFrame from the validated data
validated_df = pd.DataFrame(validated_data)

# Append the validated data to the output CSV file
with open(output_file_path, 'a', encoding='utf-8') as f:
    validated_df.to_csv(f, index=False, header=f.tell() == 0)

print(f"Validated data has been appended to {output_file_path}")


# In[117]:





# In[120]:


# pwd


# In[ ]:





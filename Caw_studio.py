from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import json
from selenium.webdriver.common.by import By
import time
s=Service("C:\\Drivers\\Chrome\\chromedriver-win64\\chromedriver.exe")

driver = webdriver.Chrome(service=s)
driver.get("https://testpages.herokuapp.com/styled/tag/dynamic-table.html")
driver.maximize_window()

data = [
    {"name": "Bob", "age": 20, "gender": "male"},
    {"name": "George", "age": 42, "gender": "male"},
    {"name": "Sara", "age": 42, "gender": "female"},
    {"name": "Conor", "age": 40, "gender": "male"},
    {"name": "Jennifer", "age": 42, "gender": "female"}
]
data_json = json.dumps(data)

tab = driver.find_element(By.XPATH, "//summary[normalize-space()='Table Data']")
tab.click()
tab_in = driver.find_element(By.XPATH,"//textarea[@id='jsondata']")
tab_in.clear()
tab_in.send_keys(data_json)

tab_in_on = driver.find_element(By.XPATH,"//button[@id='refreshtable']")
tab_in_on.click()


# Locate the table by its ID
table = driver.find_element(By.ID,"dynamictable")

# Define the expected data as a list of lists
expected_data = [
    ["name", "age", "gender"],
    ["Bob", "20", "male"],
    ["George", "42", "male"],
    ["Sara", "42", "female"],
    ["Conor", "40", "male"],
    ["Jennifer", "42", "female"]

]

# Iterate through rows and cells, and assert the data
rows = table.find_elements(By.TAG_NAME,"tr")
for i, row in enumerate(rows):
    cells = row.find_elements(By.TAG_NAME,"td")
    for j, cell in enumerate(cells):
        actual_data = cell.text
        expected_value = expected_data[i][j]
        assert actual_data == expected_value, f"Cell ({i}, {j}) doesn't match: Expected '{expected_value}', Actual '{actual_data}'"

print("All data matched successfully!")

time.sleep(5)
driver.quit()
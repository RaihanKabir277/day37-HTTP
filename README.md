# 🚴‍♂️ Pixela Cycling Tracker

A Python script that integrates with the [Pixela API](https://pixe.la/) to track your daily cycling distance.  
This project demonstrates how to use RESTful APIs (`POST`, `PUT`, `DELETE`) in Python with the `requests` library, while maintaining a clean, reusable code structure.

---

## ✨ Features

- ✅ Create a Pixela user account programmatically  
- ✅ Create a graph to visualize cycling activity  
- ✅ Post daily cycling distance (km) to the graph  
- ✅ Update existing entries  
- ✅ Delete entries when required  
- ✅ Auto-generates today’s date in Pixela-supported format (`YYYYMMDD`)  

---

## 🛠️ Tech Stack

- **Language:** Python 3.x  
- **Libraries:** `requests`, `datetime`  
- **API Service:** [Pixela](https://pixe.la)  

---

# Create User (Step 1)
- response = requests.post(url=pixela_api, json=user_params)
---

# Create Graph (Step 2)
- graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
---

# Post Value to Graph (Step 4)
- value_response = requests.post(url=value_endpoint, json=value_config, headers=headers)

---
# Update Value
- update_response = requests.put(url=put_endpoint, json=update_data, headers=headers)

---
# Delete Value
- delete_response = requests.delete(url=delete_endpoint, headers=headers)

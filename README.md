
# **Sam media assessment**

Analyze and Visualize the provided data for users and transactions


## **Installation**

### **Development**

Python as a primary tools for development. 
See [requirements.txt](requirements.txt) for dependency packages. 

- First create the `venv` using below command (Windows)

    ```py
    python -m venv .venv
    ```

- Use below command to activate
    ```py
    .venv/scripts/activate
    ```

- Basically to reproduce environment you need to run
    ```py
    pip install -r requirements.txt
    ```

## **Implementation**

In src folder,we provide the [main.py](./src/main.py) script, which is the main file

To run the main use the below command

```py
    python ./src/main.py
```

### **Class**

Multiple Classes has been created, which are 
  -  [DataTransformation](/src/data_transformation.py) 
  -  [DBOperation](/src/db_operation.py)
  -  [DataVisualisation](/src/data_visualization.py)
  -  [SQLQuries](/src/sqlqueries.py)



# 📝 TODO API

A simple TODO application backend built using **FastAPI** and **SQLite**. This REST API allows you to create, read, update, and delete todo items.

---

## API Endpoints

### 1. Tcreate a New TODO

**Endpoint**: `POST /todos/`
**Request Body**:
```
 {
  "title": "Buy groceries",
  "description": "Milk, Bread, Eggs",
  "completed": false
}
```
**Response**:

```json
{
  "id": 1,
  "title": "Buy groceries",
  "description": "Milk, Bread, Eggs",
  "completed": false
}

```

### 2. Get All TODOs

**Endpoint**: `GET /todos/`

**Response**:

```json
[
  {
    "id": 1,
    "title": "Buy groceries",
    "description": "Milk, Bread, Eggs",
    "completed": false
  }
]

```

### 3. Get a Single TODO by ID

**Endpoint**: `GET /todos/{id}`


```json
{
  "id": 1,
  "title": "Buy groceries",
  "description": "Milk, Bread, Eggs",
  "completed": false
}

```

### 4.  Delete a TODO
**Endpoint**:`DELETE /todos/{id}`
**Request Body**:
```json
{
  "message": "TODO  deleted successfully."
}

```

### 5.  Update a TODO

**Endpoint**: `PUT /todos/{id}`

**Request Body**:
```{
  "title": "Buy groceries and fruit",
  "description": "Milk, Bread, Eggs, Apples",
  "completed": true
}
```

```json
{
  "id": 1,
  "title": "Buy groceries and fruit",
  "description": "Milk, Bread, Eggs, Apples",
  "completed": true
}
```

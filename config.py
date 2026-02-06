class Config:
    BASE_URL = "https://jsonplaceholder.typicode.com"
    
    ENDPOINTS = {
        'posts': '/posts',
        'comments': '/comments',
        'users': '/users',
        'albums': '/albums',
        'todos': '/todos'
    }
    
    HEADERS = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

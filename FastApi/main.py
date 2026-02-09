from fastapi import FastAPI

app = FastAPI()  # <-- THIS name is what Uvicorn looks for

@app.get("/")
def read_root():
    return {"message": "Hello World"}
@app.get("/about")
def about():
    return {"message":"this is about page"}
@app.get("/products")
def products():
    products_data=[{"id":1,"title":"this is title"},{"id":2,"title":"this is second title"}]
    return products_data
@app.get("/products/{id}")
def products(id:int):
     products_data=[{"id":1,"title":"this is title"},{"id":2,     "title":"this is second title"}]
     for product in products_data:
         if product["id"]==id:
             return product
     return {"message":"no product found"}
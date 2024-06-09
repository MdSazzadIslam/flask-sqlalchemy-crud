from flask import Blueprint, request
from controllers.product_controller import ProductController

products = Blueprint("products", __name__)


@products.route("/products", methods=["GET"])
def index():
    
    return  ProductController.get_products()
   
@products.route("/products/<string:product_id>", methods=["GET"])
def get(product_id):

    return ProductController.get_product(product_id)


@products.route("/products/create", methods=["POST"])
def insert():

    return ProductController.create_product(request.json)


@products.route("/products/update/<string:product_id>", methods=["PUT"])

def update(product_id):
 
    return ProductController.update_product(product_id, request.json)


@products.route("/products/delete/<string:product_id>", methods=["DELETE"])
def delete(product_id):

    return ProductController.delete_product(product_id)

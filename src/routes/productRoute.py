from flask import Blueprint, request
from controllers.productController import ProductController

products = Blueprint("products", __name__)


@products.route("/products", methods=["GET"])
async def index():
    print("all")
    return ProductController.get_products()


@products.route("/products/<string:product_id>", methods=["GET"])
async def get(product_id):
    print("single")
    return ProductController.get_product(product_id)


@products.route("/products/create", methods=["POST"])
async def insert():
    return ProductController.create_product(request.json)


@products.route("/products/update/<string:product_id>", methods=["PUT"])
async def update(product_id):
    return ProductController.update_product(product_id, request.json)


@products.route("/products/delete/<string:product_id>", methods=["DELETE"])
async def delete(product_id):
    return ProductController.delete_product(product_id)

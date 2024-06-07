from models.product import Product
from utils.db import db
from typing import Tuple
from sqlalchemy import select
import asyncio

class ProductController:
    @staticmethod
    def _commit_or_rollback():
        """
        Helper method to commit or rollback the current session.
        """
        try:
             db.session.commit()
        except:
             db.session.rollback()
             raise

    @staticmethod
    def get_products() -> Tuple[dict, int]:
        """
        Retrieve all products from the database.

        Returns:
            Tuple: A tuple containing the list of products and the HTTP status code.
        """
        try:
            products = db.session.query(Product).all()
            products_list = [
                {
                    "id": product.id,
                    "name": product.name,
                    "description": product.description,
                }
                for product in products
            ]

            return {"products": products_list}, 200
        except Exception as e:
            return {"error": str(e)}, 500

    @staticmethod
    def get_product(product_id: int) -> Tuple[dict, int]:
        """
        Retrieve a specific product by its ID.

        Args:
            product_id (int): The ID of the product to retrieve.

        Returns:
            Tuple: A tuple containing the product information and the HTTP status code.
        """
        try:
            product = db.session.query(Product).get(product_id)
            if not product:
                return {"error": "Product not found"}, 404
            return {
                "id": product.id,
                "name": product.name,
                "description": product.description,
            }, 200
        except Exception as e:
            return {"error": str(e)}, 500

    @staticmethod
    def create_product(data: dict) -> Tuple[dict, int]:
        """
        Create a new product.

        Args:
            data (dict): The data containing the product information.

        Returns:
            Tuple: A tuple containing the success message and the HTTP status code.
        """

        if not data:
            return {"error": "No data provided"}, 400

        try:
            name = data.get("name")
            description = data.get("description")

            if not name:
                return {"error": "Product name is required"}, 400

            new_product = Product(name=name, description=description)
            db.session.add(new_product)
            ProductController._commit_or_rollback()

            return {"message": "Product created successfully"}, 201

        except Exception as e:
            return {"error": str(e)}, 500

    @staticmethod
    def update_product(product_id: int, data: dict) -> Tuple[dict, int]:
        """
        Update an existing product.

        Args:
            product_id (int): The ID of the product to update.
            data (dict): The data containing the updated product information.

        Returns:
            Tuple: A tuple containing the success message and the HTTP status code.
        """
        if not product_id:
            return {"error": "No product ID provided"}, 400

        try:
            product = db.session.query(Product).get(product_id)
            if not product:
                return {"error": "Product not found"}, 404

            name = data.get("name")
            description = data.get("description")

            if name is not None:
                product.name = name

            if description is not None:
                product.description = description

            if not name and not description:
                return {"error": "At least 'name' or 'description' should be provided for update"}, 400

            ProductController._commit_or_rollback()

            return {"message": "Product updated successfully"}, 200
        except Exception as e:
            return {"error": str(e)}, 500

    @staticmethod
    def delete_product(product_id: int) -> Tuple[dict, int]:
        """
        Delete a product.

        Args:
            product_id (int): The ID of the product to delete.

        Returns:
            Tuple: A tuple containing the success message and the HTTP status code.
        """
        if not product_id:
            return {"error": "No product ID provided"}, 400

        try:
            product = db.session.query(Product).get(product_id)
            if not product:
                return {"error": "Product not found"}, 404

            db.session.delete(product)
            ProductController._commit_or_rollback()

            return {"message": "Product deleted successfully"}, 200
        except Exception as e:
            return {"error": str(e)}, 500

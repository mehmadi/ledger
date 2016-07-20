from django.shortcuts import render
from oscar.apps.basket.models import Basket
from oscar.apps.catalogue.models import Product
from rest_framework import serializers
import json
from oscar.core.loading import get_class
from django.contrib.auth import get_user_model

OrderPlacementMixin = get_class('checkout.mixins','OrderPlacementMixin')
Selector = get_class('partner.strategy', 'Selector')
selector = Selector()

def createBasket(product_list,owner):
    ''' Create a basket so that a user can check it out.
        @param product_list - [
            {
                "id": "<id of the product in oscar>",
                "quantity": "<quantity of the products to be added>"
            }
        ]
        @param - owner (user id or user object)
    '''
    try:
        old_basket = basket = None
        valid_products = []
        User = get_user_model()
        # Check if owner is of class AUTH_USER_MODEL or id
        if not isinstance(owner,User):
            owner = User.objects.get(id=owner)
            
        # Check if owner has previous baskets
        if owner.baskets.filter(status='Open'):
            old_basket = owner.baskets.get(status='Open')
            
        # Use the previously open basket if its present or create a new one    
        if old_basket:
            basket = old_basket
        else:
            basket = Basket()
            
        # Set the owner and strategy being used to create the basket    
        basket.owner = owner
        basket.strategy = selector.strategy(user=owner)
        
        # Check if there are products to be added to the cart and if they are valid products
        if not product_list:
            raise ValueError('There are no products to add to the order.')
        product_dict_list = json.loads(product_list)
        for product in product_dict_list:
            p = Product.objects.get(id=product["id"])
            valid_products.append({'product': p, 'quantity': product["quantity"]})
            
        # Add the valid products to the basket
        for p in valid_products:
            basket.add_product(p['product'],p['quantity'])
        
        # Save the basket
        basket.save()
        return basket
    except Product.DoesNotExist:
        raise
    except Exception as e:
        print str(e)
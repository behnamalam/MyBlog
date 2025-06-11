class Cart:
    def __init__(self,request):
        self.session = request.session # get all sessions of browser system

        cart = self.session.get("session_key")
        if "session_key" not in request.session:
            cart = self.session["session_key"] = {}
        
        self.cart = cart # {'session_key' : {}}

    def add(self,product):
        product_id = product.id

        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {"price" : product.price}

        self.session.modified = True # IMPORTANT
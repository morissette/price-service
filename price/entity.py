"""
Price Entity
"""
class Entity:

    def __init__(self, event):
        """
        Create Entity from Event
        :param event: Event Message
        """
        self.provider_uuid = event.provider_uuid
        self.ingredient_uuid = event.ingredient_uuid
        self.uom_uuid = event.uom_uuid
        self.unit_amount = event.unit_amount
        self.value = event.value
        self.iot_uuid = event.iot_uuid
        self.source_uuid = event.source_uuid

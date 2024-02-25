class Operation:
    def __init__(self, id_operation, date_operation, state, operation_amount, description, from_account, to_account):
        self.id_operation = id_operation
        self.date_operation = date_operation
        self.state = state
        self.operation_amount = operation_amount
        self.description = description
        self.from_account = from_account
        self.to_account = to_account

    def __str__(self):
        return f'Operation = "{self.id_operation}" | date_operation="{self.date_operation}"'

    def __repr__(self):
        return f'Operation (id_operation="{self.id_operation}", date_operation="{self.date_operation}",' \
               f' state="{self.state}"), operation_amount="{self.operation_amount}", description="{self.description}", ' \
               f' from_account="{self.from_account}", to_account="{self.to_account}"'